from django.http import JsonResponse
from .models import MyModel


def get_data(request):
    data = MyModel.objects.all().values()
    return JsonResponse(list(data), safe=False)


