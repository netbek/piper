from pyramid.response import Response
from pyramid.view import view_config
from .helpers.views import render_home_view


class HomeViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    def index(self):
        return Response(render_home_view(base_url='/'))
