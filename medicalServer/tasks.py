from celery import shared_task
import time
#test for django 1.11 and python 2.7
@shared_task
def add(x, y):
    print("start")
    time.sleep(5)
    print("end")
    return x + y

