from django.shortcuts import render, redirect
from django.http import Http404
from .forms import UploadFileForm
# Create your views here.
def index(request):
    if 'GET' == request.method:
        if not request.user.is_authenticated():
            return render(request, 'login.html')
        else:
            return render(request, 'index.html', {'user': request.user})
    return Http404