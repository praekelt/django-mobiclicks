from setuptools import setup, find_packages


def getcmdclass():
    try:
        from setuptest import test
        return test
    except ImportError:
        return None


setup(
    name='django-mobiclicks',
    version='0.1',
    description='Tracks MobiClicks acquisitions',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    license='BSD',
    url='http://github.com/praekelt/django-mobiclicks',
    packages = find_packages(),
    install_requires = [
        'Django>=1.4,<1.6',
        'celery>3'
    ],
    include_package_data=True,
    tests_require=[
        'django-setuptest>=0.1.2',
        'coverage',
        'pysqlite',
        'mock'
    ],
    test_suite="setuptest.setuptest.SetupTestSuite",
    cmdclass={'test': getcmdclass()},
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)