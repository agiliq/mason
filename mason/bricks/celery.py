from mason.bricks.base import BaseBrick


class Celery(BaseBrick):

    name = "Celery"
    description = "Configures django-celery"
    installed_apps = ['djcelery', ]
    dependencies = ['django-celery==3.0.17', ]

    settings = {
        'BROKER_URL':  '"django://"',
        '_RAW': "import djcelery\ndjcelery.setup_loader()"
    }

    def ask(self):
        answer = raw_input('%s :: %s | Enable? (Y/n) ' % (self.name, self.description))
        if not answer or answer.lower() == 'y':
            print "Please enter celery details"
            print "\n"
            broker_url = raw_input("Celery Broker URL [django://]: ")
            if broker_url:
                self.settings['BROKER_URL'] = '"%s"' % broker_url
            return True
        return False
