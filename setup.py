from setuptools import setup, find_packages

setup(
    name='django-citeit',
    version='2.0.0',
    packages=find_packages(exclude=['tests*']),
    description='A Django app for the creation of an annotated bibliography.',
    long_description=('Visit https://github.com/unt-libraries/django-citeit '
                      'for the latest documentation.'),
    include_package_data=True,
    url='https://github.com/unt-libraries/django-citeit',
    author='University of North Texas Libraries',
    author_email='mark.phillips@unt.edu',
    license='BSD',
    keywords=['django', 'annotated', 'bibliography'],
    classifiers=[
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
        'Programming Language :: Python :: 3.6'
        'Programming Language :: Python :: 3.7'
    ]
)
