class BuildrPlugin(object):

    name = ""
    description = ""

    installed_apps = ()
    dependencies = ()

    def get_context(self):
        context = {
            'installed_apps': self.installed_apps,
            'dependencies': self.dependencies,
        }
        return context
