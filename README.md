Django CiteIt
=================

[![Build Status](https://github.com/unt-libraries/django-citeit/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/unt-libraries/django-citeit/actions)

This app displays an annotated bibliography and allows the viewer to sort by
different criteria such as scope, author, year, etc.


Requirements
------------

* Django 4.2
* Python 3.8 - 3.10


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
	urlpatterns = [
            path('admin/', admin.site.urls),
            path('withers/', include('citeIt.urls'))
        ]
    ```

4.  Migrate/sync the database
    ```sh
	$ python manage.py migrate
    ```


Developing
----------

1. Clone the git repository:
   ```sh
       $ git clone https://github.com/unt-libraries/django-citeit.git
   ```

2. Navigate into the cloned repository:
   ```sh
       $ cd django-citeit
   ```

3. Install the requirements (preferably in a virtual environment):
   ```sh
       $ pip install -r requirements-dev.txt
   ```

4. Run the migrations:
   ```sh
       $ ./manage.py migrate
   ```

5. Create a superuser so you can log into the admin interface   
   ```sh
       $ ./manage.py createsuperuser
   ```

6. Start the test server:
   ```sh
       $ ./manage.py runserver
   ```

   The test server can be viewed from a browser by navigating to the default location: `http://localhost:8000/withers`


Testing
-------

1. Run the tests using tox
   ```sh
       $ pip install tox

       $ tox
   ```


License
-------

See LICENSE


Contributors
------------

* [Mark Phillips](https://github.com/vphill)
* [Gio Gottardi](https://github.com/somexpert)
* [Madhulika Bayyavarapu](https://github.com/madhulika95b)
