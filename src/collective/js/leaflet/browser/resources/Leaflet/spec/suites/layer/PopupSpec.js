describe('Popup', function() {

	var map;

	beforeEach(function () {
		var c = document.createElement('div');
		c.style.width = '400px';
		c.style.height = '400px';
		map = new L.Map(c);
		map.setView(new L.LatLng(55.8, 37.6), 6);
	});

	it("should trigger popupopen on marker when popup opens", function() {
		var marker1 = new L.Marker(new L.LatLng(55.8, 37.6));
		var marker2 = new L.Marker(new L.LatLng(57.123076977278, 44.861962891635));

		map.addLayer(marker1);
		map.addLayer(marker2);

		marker1.bindPopup('Popup1');
		marker2.bindPopup('Popup2');

		var spy = sinon.spy();

		marker1.on('popupopen', spy);

		expect(spy.called).to.be(false);
		marker2.openPopup();
		expect(spy.called).to.be(false);
		marker1.openPopup();
		expect(spy.called).to.be(true);
	});

	it("should trigger popupclose on marker when popup closes", function() {
		var marker1 = new L.Marker(new L.LatLng(55.8, 37.6));
		var marker2 = new L.Marker(new L.LatLng(57.123076977278, 44.861962891635));

		map.addLayer(marker1);
		map.addLayer(marker2);

		marker1.bindPopup('Popup1');
		marker2.bindPopup('Popup2');

		var spy = sinon.spy();

		marker1.on('popupclose', spy);

		expect(spy.called).to.be(false);
		marker2.openPopup();
		expect(spy.called).to.be(false);
		marker1.openPopup();
		expect(spy.called).to.be(false);
		marker2.openPopup();
		expect(spy.called).to.be(true);
		marker1.openPopup();
		marker1.closePopup();
		expect(spy.callCount).to.be(2);
	});
});
