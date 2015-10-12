Django CiteIt
=================

[![Build Status](https://travis-ci.org/unt-libraries/django-citeit.svg?branch=master)](https://travis-ci.org/unt-libraries/django-citeit)

This app displays an annotated bibliography and allows the viewer to sort by
different criteria such as scope, author, year, etc.


Requirements
------------

* Django >= 1.8
* Python >= 2.7


Installation
------------

1.  Download and install from source code.
    ```sh
	$ pip install git+git://github.com/unt-libraries/django-citeit.git
    ```

2.  Add app to INSTALLED_APPS.
    ```python
	INSTALLED_APPS = (
            'citeIt',
        )
    ```

3.  Include the URLs.
    ```python
    from citeIt.site_views import main_admin

	urlpatterns = [
            url(r'^admin/', include(main_admin.urls)),
            url(r'^withers/', include('citeIt.urls', namespace='citeIt'))
        ]
    ```

4.  Migrate/sync the database
    ```sh
	$ python manage.py migrate
    ```


License
-------

See LICENSE


Contributors
------------

* [Mark Phillips](https://github.com/vphill)
* [Gio Gottardi](https://github.com/somexpert)
