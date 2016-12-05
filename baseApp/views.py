from django.shortcuts import render
from django.http import Http404
from django.template import loader
from .models import Movement
from django.db.models import Max


def index(request):
    if 'GET' == request.method:
        if not request.user.is_authenticated():
            # template = loader.get_template('userApp/login.html')
            return render(request, 'user/login.html')
        else:
            max_date = Movement.objects.all().filter(
                user=request.user).aggregate(Max('date'))
            return render(request, 'base/index.html',
                          {
                              'user': request.user,
                              'last_movement_date': str(max_date['date__max'])
                          }
                          )
    return Http404
