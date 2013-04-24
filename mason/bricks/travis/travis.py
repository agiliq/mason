from os.path import join, abspath, dirname

from mason.bricks.base import BaseBrick


class Travis(BaseBrick):

    name = "Travis"
    description = "Configure travis CI integration"
    files = join(abspath(dirname(__file__)), 'files')

    def ask(self):
        self.travis = {
            'script': 'python manage.py test',
            'install': 'pip install -r requirements.txt'
        }
        answer = raw_input('%s :: %s | Enable? (Y/n) ' % (self.name, self.description))
        if not answer or answer.lower() == 'y':
            print "Please enter travis CI details"
            print "\n"
            self.travis['script'] = raw_input("script - Command to run the tests [python manage.py test]: ")
            self.travis['install'] = raw_input("install - Command to install dependencies [pip install -r requirements]: ")
            return True
        return False

    def get_context(self):
        context = super(Travis, self).get_context()
        context['travis'] = self.travis
        return context
