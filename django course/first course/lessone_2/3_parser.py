from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Encountered start tag <{tag}>')

    def handle_endtag(self, tag):
        print(f'Encountered end tag </{tag}>')

    def handle_data(self, data):
        print(f'Encountered some data "{data.strip()}"')


parser = MyHTMLParser()
parser.feed(
    '''
    <html>
    <head>
        <title>Hello, parse me!</title>
    </head>
    <body>
        <h1>BODY</h1>
    </body>
    </html>
    '''
)
