from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Home Page</h1>")

def page_not_found(request,exception):
    return render(request,template_name='404.html',status=404)

