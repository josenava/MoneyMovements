from django.shortcuts import render
from django.http import Http404, JsonResponse
import json
import csv
from baseApp.models import Movement
from django.utils.timezone import get_current_timezone
from datetime import datetime

def processCsvFile(fileName, reqUser):
    newFileName = '/tmp/test'+datetime.now().strftime('%Y%m%d%H%M%S')+'.csv'
    with open(newFileName, 'wb+') as fDest:
        for chunk in fileName.chunks():
            fDest.write(chunk)
    with open(newFileName, 'rU') as f:
        reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        tz = get_current_timezone()
        for i, row in enumerate(reader):
            if 0 != i:
                movement = Movement(
                    description=row[1],
                    amount=float(row[2]),
                    balance=float(row[3]),
                    date=tz.localize(datetime.strptime(row[0], '%d/%m/%y')),
                    user=reqUser
                )
                movement.save()
    return None
# Create your views here.
def importFile(request):
    if 'POST' == request.method and request.user.is_authenticated():
        if request.FILES is not None:
            processCsvFile(request.FILES['file'], request.user)
        return JsonResponse({'uploaded': 'ok'})

    return Http404

def addMovement(request):
    if 'POST' == request.method and request.user.is_authenticated():
        formFields = json.loads(request.body)
        movement = Movement(
                    description=formFields['movDescription'],
                    amount=float(formFields['movAmount']),
                    balance=3,
                    date=datetime.now(),
                    user=request.user
                )
        movement.save()
        return JsonResponse({'uploaded': 'ok'})
    return Http404