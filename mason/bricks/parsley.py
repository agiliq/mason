from mason.bricks.base import BaseBrick


class Parsley(BaseBrick):

    name = "Parsley"
    description = "Enables Parsley"

    installed_apps = ['parsley', ]
    dependencies = ['django-parsley', ]
