from django.shortcuts import render
from rest_framework.response import Response
from .translator import tran
from . serialazers import *
from .models import Trans
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from .redis import Red
from django.db.models import Q

def index(request):
    return render(request,'index.html')

@api_view(['GET','POST'])
@permission_classes((AllowAny,))
def transApi(request):
    shablon = " {'uz':'salom dp yozin'}"
    if request.method == 'GET':
        return Response({'masalan salom dep yozin ':f' yoki :{shablon}'})
    text = request.data
    text_ = str()
    if type(text) == dict:
        for i in text:
            text_ += text[i]
    else:
        text_ = text
        if text_:
            data =  Red.get(text_)
            if data:
                print('redis - get')
                return Response(data)
    data = Trans.objects.filter(Q(uz=text_)|Q(en=text_)|Q(ru=text_))
    if data:
        print('db.sqlite3')
        Red.set(text,{'en':data[0].en,'uz':data[0].uz,'ru':data[0].ru})
        serializer = TransSerializer(data[0], many=False)
        return Response(serializer.data)


    data =  tran(text_)
    print('trans - data' )
    Trans.objects.get_or_create(uz= data['uz'],en = data['en'],ru=data['ru'])
    Red.set(text_,data)
    if data:
        return Response(data)
    return Response({'status':f'masalan  salom deb yozin  yoki {shablon} 1111'})
