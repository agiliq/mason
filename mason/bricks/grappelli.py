from mason.bricks.base import BaseBrick


class Grappelli(BaseBrick):

    name = "Django Grappelli"
    description = "Configures Django Grappelli"

    installed_apps = ['grappelli', 'django.contrib.admin',]
    dependencies = ['django-grappelli', ]

    #Still need to add url patterns 
    # (r'^grappelli/', include('grappelli.urls')),

