from .base import BaseBrick


class DebugToolbar(BaseBrick):

    name = "Django Debug Toolbar"
    description = "Configures Django Debug Toolbar"

    installed_apps = ['debug_toolbar', ]
    dependencies = ['django-debug-toolbar==0.9.4', ]
