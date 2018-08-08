from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)

    # Jinja2
    config.include('pyramid_jinja2')
    config.add_jinja2_search_path('templates/')

    # Static files
    config.add_static_view(name='cache', path='cache')
    config.add_static_view(name='node_modules', path='../node_modules')

    # Routes
    config.add_route('home', '/')

    # Views
    config.scan()

    return config.make_wsgi_app()
