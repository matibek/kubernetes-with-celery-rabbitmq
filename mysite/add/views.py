import random

from django.http import HttpResponse

from worker.tasks import add


def index(request):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    add.delay(x, y)

    return HttpResponse("Task created to add {} and {}!".format(x, y))
