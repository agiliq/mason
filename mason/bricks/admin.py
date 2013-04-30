from mason.bricks.base import BaseBrick


class Admin(BaseBrick):

    name = "Admin"
    description = "Enables Django Admin"
    installed_apps = ['django.contrib.admin']
    urls = ["url(r'^admin/', include(admin.site.urls))"]
