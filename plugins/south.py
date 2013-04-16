class BuildrPlugin(object):

    def get_context(self):
        return  {'INSTALLED_APPS': (
            'south',
        )}
