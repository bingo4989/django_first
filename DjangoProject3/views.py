from django.http import HttpResponse
from django.shortcuts import render
def index(requests):
   html = "<html><body>hello with function </body></html>"
   return HttpResponse(html)


def index2(requests):
   return render(requests, 'test.html')