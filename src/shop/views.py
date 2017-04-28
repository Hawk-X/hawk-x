from django.shortcuts import render, render_to_response


def index(request):
	template_name = 'index.html'
	return render_to_response(template_name)