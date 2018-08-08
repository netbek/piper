import os
import shutil

from app.views.helpers.views import render_home_view


def copy(src, dst):
    shutil.rmtree(dst, ignore_errors=True)
    shutil.copytree(src, dst)


DIR = os.path.dirname(__file__)
GHPAGES_DIR = 'ghpages'

# Empty and make static pages directory
shutil.rmtree(os.path.join(DIR, GHPAGES_DIR), ignore_errors=True)
os.mkdir(os.path.join(DIR, GHPAGES_DIR))

# Write static pages
data = render_home_view(base_url='https://netbek.github.io/piper/')
file = open(os.path.join(DIR, GHPAGES_DIR, 'index.html'), 'w')
file.write(data)
file.close()

# Copy vendor files
for path in [
    'node_modules/leaflet',
    'node_modules/leaflet.markercluster',
    'node_modules/leaflet.Permalink'
]:
    copy(os.path.join(DIR, path),
         os.path.join(DIR, GHPAGES_DIR, path))
