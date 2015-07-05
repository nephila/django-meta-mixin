HELPER_SETTINGS = dict(
    ROOT_URLCONF='example_app.urls',
    INSTALLED_APPS=[
        'sekizai',
        'meta_mixin',
        'example_app',
    ],
    META_SITE_PROTOCOL='http',
    META_USE_SITES=True,
    META_USE_OG_PROPERTIES=True,
    META_USE_TWITTER_PROPERTIES=True,
    META_USE_GOOGLEPLUS_PROPERTIES=True,
    NOSE_ARGS=['-s'],
    TEMPLATE_CONTEXT_PROCESSORS=[
        'sekizai.context_processors.sekizai',
    ],
)


def run():
    import sys
    from djangocms_helper import runner
    sys.path.insert(0, 'example')
    runner.run('meta_mixin')


if __name__ == '__main__':
    run()
