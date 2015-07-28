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

1.  Download source code from Github.
    ```sh
	$ git clone https://github.com/unt-libraries/citeIt
    ```

2.  Navigate into citeIt/ and create tarball.
    ```sh
	$ python setup.py sdist
    ```	

3.  Install the tarball.
    ```sh
	$ pip install name_of_tarball
    ```

4.  Add app to INSTALLED_APPS.
    ```python
	INSTALLED_APPS = (
            'citeIt',
        )
    ```

5.  Include the URLs.
    ```python
	urlpatterns = [
            url(r'^admin/', include(admin.site.urls)),
            url(r'^withers/', include('citeIt.urls',
                namespace='citeIt'))
        ]
    ```

6.  Migrate/sync the database
    ```sh
	$ python manage.py migrate
    ```


License
-------

See LICENSE
