from mason.bricks.base import BaseBrick


class Guardian(BaseBrick):

    name = "Django Guardian"
    description = "Configures Django Guardian"

    installed_apps = ['guardian', ]
    dependencies = ['django-guardian', ]

    settings = {
        'AUTHENTICATION_BACKENDS': (
            'django.contrib.auth.backends.ModelBackend', # default
            'guardian.backends.ObjectPermissionBackend',
        )
    }
