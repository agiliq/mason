from mason.bricks.base import BaseBrick


class CrispyForms(BaseBrick):

    name = "Django Crispy Forms"
    description = "Configures Django Crispy Forms"

    installed_apps = ['crispy_forms', ]
    dependencies = ['django-crispy-forms', ]
