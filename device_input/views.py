from django.http import HttpResponse


def dev_input(request, dev_in_code):
    return HttpResponse(f'<h1>Device input</h1> <p> code from device: {dev_in_code} </p>')

# TODO: Decode input, for relay, endswith, temp variables
