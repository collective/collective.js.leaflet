L.Icon.Default.imagePath = (function () {
	var scripts = document.getElementsByTagName('script'),
	    leafletRe = /[\/]\+\+plone\+\+static[\/]\+\+unique\+\+([\w\-\.\%]*)[\/]leaflet[\-\._]?([\w\-\._]*)\.js\??/;

	var i, len, src, matches, path;

	for (i = 0, len = scripts.length; i < len; i++) {
		src = scripts[i].src;
		matches = src.match(leafletRe);

		if (matches) {
			path = src.split(leafletRe)[0];
      console.log(path)
			return (path ? path + '/++resource++collective.js.leaflet/' : '') + 'images';
		}
	}
}());
