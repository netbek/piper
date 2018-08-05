import pandas as pd
import pprint

from pyramid.view import view_config
from sqlalchemy import create_engine


APP_DIR = 'app'
PLOTS_DIR = 'app/cache/plots'
CACHE = False


def to_url(filename):
    if filename.startswith(APP_DIR + '/'):
        return filename[len(APP_DIR):]
    return filename


class HomeViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='home.jinja2')
    def index(self):
        source = 'data/schools/operational-ordinary-school.db'
        engine = create_engine('sqlite:///' + source)

        df = pd.read_sql_table('schools', engine)

        # Remove rows with invalid longitude and/or latitude
        df = df[pd.to_numeric(df.gis_longitude, errors='coerce').notnull()]
        df = df[pd.to_numeric(df.gis_latitude, errors='coerce').notnull()]

        points = df[['gis_latitude', 'gis_longitude', 'institution_name']]

        points_json = points.to_json(orient='values')

        return {
            'points_json': points_json
        }
