from __future__ import absolute_import, unicode_literals
from celery import Celery
import os

# ----------------- uncomment this section if you use to create your periodic task function  in this file  -------------
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
# import django
# django.setup()
# from todo.tasks import delete_all_tasks
# ----------------------------------------------------------------------------------------------------------------------


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls delete_all_tasks() every 10 seconds.
#     sender.add_periodic_task(10.0, delete_all_tasks.s(), name='delete every 10')
