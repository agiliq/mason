from mason.bricks.base import BaseBrick


class FooBarBrick(BaseBrick):

    name = "FooBar"
    description = "Configures FooBar"

    installed_apps = ["foobar"]
    dependencies = ["foobar"]
    middleware_classes = ["foobar.middleware.FooBar"]
    settings = {"FOO": "bar"}
    files = "foobar_files"
    urls = ["url(r'^admin/', include(admin.site.urls))"]
