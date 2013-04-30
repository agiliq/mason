from mason.tests.bricks.foobar import FooBarBrick


class TestBaseBrick:

    def setup_method(self, method):
        self.brick = FooBarBrick()

    def test_context(self):
        assert self.brick.get_context() == {
            'dependencies': ['foobar'],
            'installed_apps': ['foobar'],
            'middleware_classes': ['foobar.middleware.FooBar'],
            'settings': {'FOO': 'bar'},
            'urls': ["url(r'^admin/', include(admin.site.urls))"]
        }

    def test_files_path(self):
        assert self.brick.get_files_path().endswith('foobar_files')
