from mason.bricks.base import BaseBrick


class Extensions(BaseBrick):

    name = "Django Extensions"
    description = "Configures Django Extensions"

    installed_apps = ['django_extensions', ]
    dependencies = ['django-extensions', ]
