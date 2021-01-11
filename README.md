Django CiteIt
=================

[![Build Status](https://travis-ci.org/unt-libraries/django-citeit.svg?branch=master)](https://travis-ci.org/unt-libraries/django-citeit)

This app displays an annotated bibliography and allows the viewer to sort by
different criteria such as scope, author, year, etc.


Requirements
------------

* Django 2.2
* Python 3.5- 3.7


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

4. Navigate to the root of the project directory and run the migrations:
   ```sh
       $ ./manage.py migrate
   ```

5. Create a superuser so you can log into the admin interface and add/remove/modify subjects:
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

1. Run the tests using tox.
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
