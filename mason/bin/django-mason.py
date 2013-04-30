#!/usr/bin/env python

"""Django Mason

Usage:
  django-mason generate <target> [--template=<default>]
  django-mason startproject <target> [--template=<default>]
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

from mason import generate, startproject

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
    templates_dir = join(abspath(dirname(generate.__file__)), 'templates', kwargs['--template'])
    kwargs['template'] = templates_dir
    kwargs['extensions'] = ['py', 'txt', 'yml']
    kwargs['plugins'] = []
    kwargs['plugin_names'] = []

    for plugin_path in PLUGINS:
        PluginClass = get_plugin_class(plugin_path)
        plugin = PluginClass()
        should_enable = plugin.ask()
        if should_enable:
            kwargs['plugins'].append(plugin)
            kwargs['plugin_names'].append(plugin.name)
            for k, v in plugin.get_context().iteritems():
                if v is not None:
                    if k in kwargs and type(v) == list:
                        kwargs[k].extend(v)
                    else:
                        kwargs[k] = v

    target = "%s_template" % kwargs['<target>']
    args = (target, )
    generate.Command().execute(*args, **kwargs)

    if 'startproject' in kwargs:
        args = kwargs['<target>']
        kwargs = {'template': target}
        startproject.Command().execute(args, **kwargs)
