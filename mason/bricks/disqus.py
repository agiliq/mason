from mason.bricks.base import BaseBrick


class Disqus(BaseBrick):

    name = "Django Disqus"
    description = "Configures Django Disqus"
    installed_apps = ['disqus', ]
    dependencies = ['django-disqus', ]

    settings = {
        'DISQUS_API_KEY': None,
        'DISQUS_WEBSITE_SHORTNAME': None,
    }

    def ask(self):
        answer = raw_input('%s :: %s | Enable? (Y/n) ' % (self.name, self.description))
        if not answer or answer.lower() == 'y':
            print "Please enter Disqus API key\n"
            self.settings['DISQUS_API_KEY'] = raw_input("API KEY: ")

            print "Please enter Disqus website shortname\n"
            self.settings['DISQUS_WEBSITE_SHORTNAME'] = raw_input("Short Name: ")
            return True
        return False

