from mason.bricks.admin import Admin


class Grappelli(Admin):

    name = "Django Grappelli"
    description = "Configures Django Grappelli"

    installed_apps = ['grappelli'] + Admin.installed_apps
    dependencies = ['django-grappelli', ]

    urls = Admin.urls + ["(r'^grappelli/', include('grappelli.urls'))"]
