class BaseBrick(object):

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

    def ask(self):
        answer = raw_input('%s :: %s | Enable? (Y/n) ' % (self.name, self.description))
        if not answer:
            return True
        return True if answer.lower() == 'y' else False
