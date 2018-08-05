(function() {
  var stamenWatercolor = L.tileLayer(
    'https://stamen-tiles-{s}.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.{ext}',
    {
      attribution:
        'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
      subdomains: 'abcd',
      minZoom: 1,
      maxZoom: 18,
      ext: 'png'
    }
  );

  var stamenTonerLabels = L.tileLayer(
    'https://stamen-tiles-{s}.a.ssl.fastly.net/toner-labels/{z}/{x}/{y}{r}.{ext}',
    {
      attribution:
        'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
      subdomains: 'abcd',
      minZoom: 0,
      maxZoom: 18,
      ext: 'png'
    }
  );

  var mapLocation = L.Permalink.getMapLocation(6, [-29, 23]);

  var map = L.map('map', {
    center: mapLocation.center,
    zoom: mapLocation.zoom,
    layers: [stamenWatercolor, stamenTonerLabels]
  });

  L.Permalink.setup(map);

  var markers = L.markerClusterGroup();

  points.forEach(function(point) {
    var lat = Number(point[0]);
    var lon = Number(point[1]);

    var marker = L.marker(new L.LatLng(lat, lon), {
      title: point[2]
    });
    marker.bindPopup(point[2] + '<br/>' + point[0] + '<br/>' + point[1]);
    markers.addLayer(marker);
  });

  map.addLayer(markers);
})();
