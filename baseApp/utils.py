import csv
import json
from django.utils.timezone import get_current_timezone
from datetime import datetime
from models import Movement, Category
from django.core import serializers
from baseApp.forms import CategoryForm
from django.db.models import Sum


def processCsvFile(fileName, reqUser):

    user_categories = Category.objects.filter(user=reqUser)
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
                    amount=float(row[2].replace(',', '.')),
                    date=tz.localize(datetime.strptime(row[0], '%d/%m/%Y')),
                    user=reqUser
                )
                movement.save()
                movement.tag_movement(row[1].lower(), user_categories)
                movement.save()
    return None

def get_user_categories(request, name):
    if name is None:
        try:
            return serializers.serialize(
                'json',
                Category.objects.all().filter(user=request.user),
                fields=('name', 'related_words')
            )
        except Category.DoesNotExist, c:
            return []
    else:
        pass

def get_categories_total_amount(request):
    start_date = request.GET['start_date']
    end_date = request.GET['end_date']
    return json.dumps(list(Category.objects.filter(
            user=request.user,
            movement__date__gte=start_date,
            movement__date__lte=end_date
        ).annotate(total_amount=Sum('movement__amount')).values('name', 'total_amount'))
    )

def create_category(request):
    formFields = CategoryForm(json.loads(request.body))
    if formFields.is_valid():
        try:
            c = Category.objects.get(name=formFields.cleaned_data['name'], user=request.user)
            return ("Same category already found", 400)
        except Category.DoesNotExist:
            c = Category(
                name=formFields.cleaned_data['name'],
                related_words=formFields.cleaned_data['related_words'],
                user=request.user
            )
            c.save()
            return ("Category saved", 200)
    else:
        return (formFields.errors, 400)

def update_category(request, name):
    pass

def delete_category(request, name):
    try:
        category = Category.objects.get(user=request.user, name=name)
        category.delete()
        return ("Category deleted", 200)
    except Category.DoesNotExist, c:
        return ("Couldn't find category", 404)


