from django.http import HttpResponse
import requests


def dev_output(request):
    return HttpResponse('Device output')

def send_command_to_pico(request):
    pico_url = 'http://192.168.31.40:81/?relay1=on'

    try:
        response = requests.get(pico_url)
        if response.status_code == 200:
            return HttpResponse('Command successfully sent to Raspberry Pi Pico')
        else:
            return HttpResponse('Error sending the command to Raspberry Pi Pico', status=500)
    except requests.exceptions.RequestException as e:
        return HttpResponse(f'Error sending the request: {str(e)}', status=500)
