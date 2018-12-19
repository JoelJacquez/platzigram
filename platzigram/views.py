
from django.http import HttpResponse
from datetime import datetime

def hello_word(request):
    return HttpResponse('Oh, hi!! Current server time is {now}'.format(
        now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def hi(request):

    # return HttpResponse(str(numbers))
    from django.http import JsonResponse
    numbers = sorted(request.GET['numbers'].split(','))


    return JsonResponse(numbers, safe=False)
    