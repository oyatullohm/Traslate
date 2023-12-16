from django.http import JsonResponse
from googletrans import Translator
from .redis import Red
from .translator import tran
from .models import Trans
from django.db.models import Q
# from .task import add

def trans(request):
    text =  request.GET.get('text')
    text = text.lower()
    data = Red.get(text)
    if data:
        print('redis - get')
        return JsonResponse(data)

    data = Trans.objects.filter(Q(uz=text)|Q(en=text)|Q(ru=text))
    if data:
        print('db.sqlite3')
        Red.set(text,{'en':data[0].en,'uz':data[0].uz,'ru':data[0].ru})
        return JsonResponse({'en':data[0].en,'uz':data[0].uz,'ru':data[0].ru})

    data =  tran(text)
    print('trans - data' )
    Trans.objects.get_or_create(uz= data['uz'],en = data['en'],ru=data['ru'])
    Red.set(text, data)
    return JsonResponse(data)
