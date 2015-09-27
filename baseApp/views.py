from django.shortcuts import render, redirect
from django.http import Http404
from .models import Movement
from django.db.models import Max
from .forms import UploadFileForm


def index(request):

    if 'GET' == request.method:
        if not request.user.is_authenticated():
            return render(request, 'login.html')
        else:
            max_date = Movement.objects.all().filter(user=request.user).aggregate(Max('date'))
            return render(request, 'index.html',
                          {
                              'user': request.user,
                              'last_movement_date': str(max_date['date__max'])
                          }
                    )
    return Http404
