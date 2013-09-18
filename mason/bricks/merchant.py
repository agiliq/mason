from mason.bricks.base import BaseBrick


class Merchant(BaseBrick):

    name = "Django Merchant"
    description = "Configures Django Merchant"

    installed_apps = ['billing', ]
    dependencies = ['django-merchant', ]
