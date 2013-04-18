from .base import BaseBrick


class Database(BaseBrick):

    name = "Database"
    description = "Configure the database"

    def ask(self):
        self.databases = {'default': {
            'ENGINE': '',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }}
        answer = raw_input('%s :: %s | Enable? (Y/n) ' % (self.name, self.description))
        if not answer or answer.lower() == 'y':
            print "Please enter database details"
            print "\n"
            self.databases['default']['ENGINE'] = raw_input("ENGINE, enter any one: 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle': ")
            self.databases['default']['NAME'] = raw_input("NAME (path to database file if using sqlite): ")
            if self.databases['default']['ENGINE'] != 'sqlite3':
                self.databases['default']['USER'] = raw_input("USER: ")
                self.databases['default']['PASSWORD'] = raw_input("PASSWORD: ")
                self.databases['default']['HOST'] = raw_input("HOST: ")
                self.databases['default']['PORT'] = raw_input("PORT: ")
            return True
        return False

    def get_context(self):
        context = super(Database, self).get_context()
        context['databases'] = self.databases
        return context
