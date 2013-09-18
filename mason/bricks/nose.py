from mason.bricks.base import BaseBrick


class Nose(BaseBrick):

    name = "Django Nose"
    description = "Configures Django Nose"

    installed_apps = ['django_nose', ]
    dependencies = ['django-nose', ]

    settings = {
        'TEST_RUNNER': 'django_nose.NoseTestSuiteRunner'
    }
