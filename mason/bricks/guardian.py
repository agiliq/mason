from mason.bricks.base import BaseBrick


class Guardian(BaseBrick):

    name = "Django Guardian"
    description = "Configures Django Guardian"

    installed_apps = ['guardian', ]
    dependencies = ['django-guardian', ]

    settings = {
        'ANONYMOUS_USER_ID': -1,
        'AUTHENTICATION_BACKENDS': (
            'django.contrib.auth.backends.ModelBackend', # default
            'guardian.backends.ObjectPermissionBackend',
        )
    }
