from django.shortcuts import render,HttpResponse,loader,HttpResponseRedirect

# Create your views here.
def loginview(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render({},request))
def dashboard(request):
    template = loader.get_template("adminapp/Dashboard.html")
    return HttpResponse(template.render({}, request))