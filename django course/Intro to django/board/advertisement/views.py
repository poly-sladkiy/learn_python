from django.shortcuts import render
from django.http import HttpResponse


def advertisement_list(request, *args, **kwargs):
	return HttpResponse(
			'''
				<ul>
					<li>Мастер на час</li>
					<li>Ремонт техники</li>
					<li>Услуги грузчика</li>
				</ul>
			'''
		)