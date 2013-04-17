class BuildrPlugin(object):

    installed_apps = ('south', )
    dependencies = ('south==0.7.6', )

    def get_context(self):
        context = {
            'installed_apps': self.installed_apps,
            'dependencies': self.dependencies,
        }
        return context
