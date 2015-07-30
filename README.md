CiteIt Django app
=================

This app displays an annotated bibliography and allows the viewer to sort by
different criteria such as scope, author, year, etc.


Requirements
------------

* Django == 1.8
* Python >= 2.7


Additional Testing Requirements
-------------------------------

* factory-boy >= 2.5


Installation
------------

1.  Download and install from source code.
    ```sh
	$ pip install https://github.com/unt-libraries/django-citeit
    ```

2.  Add app to INSTALLED_APPS.
    ```python
	INSTALLED_APPS = (
            'citeIt',
        )
    ```

3.  Include the URLs.
    ```python
	urlpatterns = [
            url(r'^admin/', include(admin.site.urls)),
            url(r'^withers/', include('citeIt.urls',
                namespace='citeIt'))
        ]
    ```

4.  Migrate/sync the database
    ```sh
	$ python manage.py migrate
    ```


License
-------

See LICENSE
