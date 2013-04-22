-------------
Django-Mason
-------------

Django-Mason is a service that allows you to generate django project templates easily.

-----
Usage
-----

Generate a project template named basic:

    django-mason generate mytemplate

Use the django-skel template

    django-mason generate mytemplate --template=django-skel


Now this template can be used as:

    django-admin startproject myproject --template=mytemplate


Plugins
-------

Work in progress...

* Database ✓
* South ✓
* Django Debug Toolbar ✓
* Fabric ✓
* Sentry ✓
* Travis
* Merchant
* Parsley
* Nose
