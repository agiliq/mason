from mason.bricks.base import BaseBrick


class Celery(BaseBrick):

    name = "Celery"
    description = "Configures django-celery"
    installed_apps = ['djcelery', ]
    dependencies = ['django-celery==3.0.17', ]
