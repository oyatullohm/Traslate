
# from core.celery import app

# @app.task(bind=True, ignore_result=True)
# def add(x):
#     for i in range(x):
#         print( i)



# from demoapp.models import Trans
from .models import Trans
from celery import shared_task


# @shared_task
# def add(x, y):
#     return x + y


# @shared_task
# def mul(x, y):
#     return x * y


# @shared_task
# def xsum(numbers):
#     return sum(numbers)


# @shared_task
# def count_Transs():
#     return Trans.objects.count()


# @shared_task
# def rename_Trans(Trans_id, uz):
#     w = Trans.objects.get(id=Trans_id)
#     w.uz = ux
#     w.save()