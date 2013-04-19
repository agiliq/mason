#!/usr/bin/env python

"""Django Mason

Usage:
  django-mason generate <target> [--template=<default>]
  django-mason (-h | --help)
  django-mason --version

Options:
  --template=<default>  Project template [default: default].
  -h --help             Show this screen.
  --version             Show version.
"""
from importlib import import_module
from os.path import join, abspath, dirname
from docopt import docopt

from mason.generate import Command

from mason.conf import PLUGINS


def get_plugin_class(plugin_path):
    try:
        module, classname = plugin_path.rsplit('.', 1)
    except ValueError:
        raise Exception('%s isn\'t a middleware module' % plugin_path)
    try:
        mod = import_module(module)
    except ImportError as e:
        raise Exception('Error importing middleware %s: "%s"' % (module, e))
    try:
        klass = getattr(mod, classname)
    except AttributeError:
        raise Exception('Middleware module "%s" does not define a "%s" class' % (module, classname))
    return klass


if __name__ == '__main__':

    kwargs = docopt(__doc__, version='Django Mason 0.1')
    templates_dir = join(abspath(dirname(__file__)), '..', 'templates', kwargs['--template'])
    kwargs['template'] = templates_dir
    kwargs['extensions'] = ['py', 'txt']
    kwargs['plugins'] = []

    for plugin_path in PLUGINS:
        PluginClass = get_plugin_class(plugin_path)
        plugin = PluginClass()
        should_enable = plugin.ask()
        if should_enable:
            kwargs['plugins'].append(plugin)
            for k, v in plugin.get_context().iteritems():
                if v is not None:
                    if k in kwargs and type(v) == list:
                        kwargs[k].extend(v)
                    else:
                        kwargs[k] = v

    args = (kwargs['<target>'], )

    Command().execute(*args, **kwargs)
