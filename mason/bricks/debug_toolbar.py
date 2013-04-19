from .base import BaseBrick


class DebugToolbar(BaseBrick):

    name = "Django Debug Toolbar"
    description = "Configures Django Debug Toolbar"

    installed_apps = ['debug_toolbar', ]
    dependencies = ['django-debug-toolbar==0.9.4', ]
    middleware_classes = ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

    settings = {
        'INTERNAL_IPS': ('127.0.0.1', )
    }
