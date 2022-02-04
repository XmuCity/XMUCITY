from django.http import HttpResponse

def index(request):
    title = '<h1 style = "text-align: center">XMUCITY</h1>'
    return HttpResponse(title)




