from django.shortcuts import render

from type.api import get_all_types


# Create your views here.
def see_all_types(request):
    types = get_all_types()
    return render(request, 'types/pages/index.html', {"types":types})