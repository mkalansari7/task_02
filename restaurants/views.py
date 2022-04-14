from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    context = {
		'msg':"Hello World!",
	}
    return render(request, 'hello.html', context)
 