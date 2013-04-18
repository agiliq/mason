from .base import BuildrPlugin


class SouthPlugin(BuildrPlugin):

    name = "South"
    description = "Enables south"

    installed_apps = ['south', ]
    dependencies = ['south==0.7.6', ]
