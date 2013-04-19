from mason.bricks.base import BaseBrick


class South(BaseBrick):

    name = "South"
    description = "Enables south"

    installed_apps = ['south', ]
    dependencies = ['south==0.7.6', ]
