from mason.bricks.base import BaseBrick


class Sentry(BaseBrick):

    name = "Sentry"
    description = "Configures sentry"
    installed_apps = ['raven.contrib.django.raven_compat']
    dependencies = ['raven']

    settings = {
        'RAVEN_CONFIG': {'dsn': None}
    }

    def ask(self):
        answer = raw_input('%s :: %s | Enable? (Y/n) ' % (self.name, self.description))
        if not answer or answer.lower() == 'y':
            print "Please enter sentry details"
            print "\n"
            self.settings['RAVEN_CONFIG']['dsn'] = raw_input("Sentry DSN: ")
            return True
        return False
