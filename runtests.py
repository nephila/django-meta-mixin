import sys

try:
    from django.conf import settings

    settings.configure(
        DEBUG=True,
        USE_TZ=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        ROOT_URLCONF="example_app.urls",
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sites",
            "sekizai",
            "meta_mixin",
            "example_app",
        ],
        META_SITE_PROTOCOL='http',
        META_USE_SITES=True,
        META_USE_OG_PROPERTIES=True,
        META_USE_TWITTER_PROPERTIES=True,
        META_USE_GOOGLEPLUS_PROPERTIES=True,
        SITE_ID=1,
        NOSE_ARGS=['-s'],
        TEMPLATE_CONTEXT_PROCESSORS = [
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
            'django.core.context_processors.i18n',
            'django.core.context_processors.debug',
            'django.core.context_processors.request',
            'django.core.context_processors.media',
            'django.core.context_processors.csrf',
            'django.core.context_processors.tz',
            'django.core.context_processors.static',
            'sekizai.context_processors.sekizai',
        ],
    )

    from django_nose import NoseTestSuiteRunner
except ImportError:
    raise ImportError("To fix this error, run: pip install -r requirements-test.txt")


def run_tests(*test_args):
    if not test_args:
        test_args = ['tests']

    # Run tests
    test_runner = NoseTestSuiteRunner(verbosity=1)

    failures = test_runner.run_tests(test_args)

    if failures:
        sys.exit(failures)


if __name__ == '__main__':
    sys.path.insert(0, 'example')
    run_tests(*sys.argv[1:])