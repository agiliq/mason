from mason.bricks.base import BaseBrick


class Grappelli(BaseBrick):

    name = "Django Grappelli"
    description = "Configures Django Grappelli"

    installed_apps = ['grappelli', 'django.contrib.admin',]
    dependencies = ['django-grappelli', ]

    urls = ["(r'^grappelli/', include('grappelli.urls'))"]
