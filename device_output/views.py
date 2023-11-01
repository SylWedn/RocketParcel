from django.http import HttpResponse


def dev_output(request):
    return HttpResponse('Device output')
