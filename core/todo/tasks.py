from celery import shared_task
from .models import Task


@shared_task
def delete_all_tasks():
    Task.objects.all().delete()
