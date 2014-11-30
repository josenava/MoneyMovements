from django.http import Http404, JsonResponse
import json
from django.core import serializers
from baseApp.models import Movement
from datetime import datetime
from baseApp.utils import processCsvFile, get_user_categories, create_category, update_category, delete_category

# Create your views here.
def import_file(request):
    if 'POST' == request.method and request.user.is_authenticated():
        if request.FILES is not None:
            processCsvFile(request.FILES['file'], request.user)
        return JsonResponse({'uploaded': 'ok'})

    return Http404

def add_movement(request):
    if 'POST' == request.method and request.user.is_authenticated():
        formFields = json.loads(request.body)
        # TODO create a from and validate the fields inside
        movement = Movement(
                    description=formFields['movDescription'],
                    amount=float(formFields['movAmount']),
                    balance=3,
                    date=datetime.now(),
                    user=request.user
                )
        movement.save()
        return JsonResponse({'uploaded': 'ok'}, status=200)
    return Http404

def get_movements(request, nMov):
    if 'GET' == request.method and request.user.is_authenticated():
        movements_set = Movement.objects.filter(user=request.user).order_by('amount')[:nMov]
        movements = []
        for m in movements_set:
            categories = serializers.serialize('json', m.categories.all(), fields=('name'))
            movements.append(json.dumps({'description': m.description, 'amount': m.amount, 'categories': categories}))

        print movements
        return JsonResponse({'nMov': nMov, 'movements': movements}, status=200)

def categories_api_calls(request, name=None):
    if request.user.is_authenticated():
        if 'GET' == request.method:
            categories = get_user_categories(request, name)
            return JsonResponse({'categories': categories}, status=200)
        elif 'POST' == request.method:
            (msg, statusCode) = create_category(request)
            return JsonResponse({'created': msg}, status=statusCode)
        elif 'PUT' == request.method and name is not None:
            update_category(request, name)
            return JsonResponse({'updated': 'ok'}, status=200)
        elif 'DELETE' == request.method and name is not None:
            (msg, statusCode) = delete_category(request, name)
            return JsonResponse({'updated': msg}, status=statusCode)
    return Http404