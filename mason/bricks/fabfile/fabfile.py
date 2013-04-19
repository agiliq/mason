from os.path import join, abspath, dirname

from mason.bricks.base import BaseBrick


class Fabfile(BaseBrick):

    name = "Fabfile"
    description = "Adds a fabfile to your project root"
    files = join(abspath(dirname(__file__)), 'files')
