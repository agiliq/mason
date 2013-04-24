-------------
Django-Mason
-------------

|TravisCI|_

.. |TravisCI| image:: https://api.travis-ci.org/agiliq/mason.png?branch=master
.. _TravisCI: https://travis-ci.org/agiliq/mason

Django-Mason is a service that allows you to generate django project templates
easily.

-----
Usage
-----

Generate a project template named mytemplate:

    django-mason generate mytemplate

Now this template can be used as:

    django-admin startproject myproject --template=mytemplate


Plugins aka Bricks
---------------------

Work in progress...

* Database ✓
* South ✓
* Django Debug Toolbar ✓
* Fabric ✓
* Sentry ✓
* Parsley ✓
* Travis ✓
* Merchant
* Nose
* Piston
* Tastypie
* Rest-framework
* Userena
* Guardian
* Django-CMS
* Fein-CMS
* Mezzanine
* Disqus
* Django-Extensions
* Grapelli
* uni-form
* crispy-forms



Writing new Bricks
-------------------

To new apps, you need to create a new class which extends from
`mason.bricks.base.BaseBrick`. See the existing apps for options which can be
overriden here.
