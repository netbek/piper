import pandas as pd

from jinja2 import Environment, PackageLoader
from sqlalchemy import create_engine

env = Environment(
    loader=PackageLoader('app', 'templates')
)


def render_home_view(base_url='/'):
    source = 'data/schools/operational-ordinary-school.db'
    engine = create_engine('sqlite:///' + source)

    df = pd.read_sql_table('schools', engine)

    # Remove rows with invalid longitude and/or latitude
    df = df[pd.to_numeric(df.gis_longitude, errors='coerce').notnull()]
    df = df[pd.to_numeric(df.gis_latitude, errors='coerce').notnull()]

    points = df[['gis_latitude', 'gis_longitude', 'institution_name']]
    points_json = points.to_json(orient='values')

    return env.get_template('home.jinja2').render({
        'base_url': base_url,
        'points': points_json
    })
