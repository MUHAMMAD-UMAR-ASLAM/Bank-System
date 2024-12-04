import time

from celery import shared_task

@shared_task
def add_numbers(x, y):
    time.sleep(10)
    return x + y