from trains.models import Train


def dfs_paths(graph: dict, start, goal):
    """
    Функция поиска всех возможных маршрутов
    из одной вершины графа в другой. Вариант
    посещения одной и той же вершины не рассматривается.

    :param graph:
    :param start:
    :param goal:
    :return:
    """

    stack = [(start, [start])]
    while stack:
        vertex, path = stack.pop()

        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))


def get_graph(qs):
    graph = {}

    for q in qs:
        graph.setdefault(q.from_city_id, set())
        graph[q.from_city_id].add(q.to_city_id)

    return graph


def get_route(request, form) -> dict:
    context = {'from': form}

    qs = Train.objects.all()
    graph = get_graph(qs)

    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    cities = data['cities']
    travelling_time = data['travelling_time']

    all_ways = list(dfs_paths(graph, from_city.id, to_city.id))

    if not len(all_ways):
        raise ValueError('Маршрута, удовлетворящего условиям, не существует')

    if cities:
        _cities = [city.id for city in cities]
        right_ways = []

        for route in all_ways:
            if all(city in route for city in _cities):
                right_ways.append(route)

        if not right_ways:
            raise ValueError('Маршрута, проходящий через указанные города, не существует')

    return context

