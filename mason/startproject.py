from optparse import NO_DEFAULT

from django.core.management.commands.startproject import Command as StartProjectCommand


class Command(StartProjectCommand):

    def handle(self, target=None, *args, **options):
        defaults = {}
        for opt in self.option_list:
            if opt.default is NO_DEFAULT:
                defaults[opt.dest] = None
            else:
                defaults[opt.dest] = opt.default
        defaults.update(options)
        super(Command, self).handle(project_name=target, **defaults)
