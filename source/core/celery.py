from celery import Celery

celery_app = Celery(__name__)

celery_app.config_from_object("source.core.settings:settings")
celery_app.conf.broker_connection_retry_on_startup = True
celery_app.autodiscover_tasks(["source.app.export.tasks"])
