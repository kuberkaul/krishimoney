from django.shortcuts import render
from krishimoney.models import *


def adminForm(request):
    return render(request, 'template/adminForm.html', context)
