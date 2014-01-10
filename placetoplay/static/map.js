function initialize()
{
	var eudo = new google.maps.LatLng(37.871997,-122.267013);
	var tourn = new google.maps.LatLng(37.371235,-122.048579);
	var chess = new google.maps.LatLng(37.788747,-122.403034);
	
	
	var mapOptions =
	{
		zoom: 10,
		center: new google.maps.LatLng(37.724208, -122.296371),
		mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	
	var map = new google.maps.Map(document.getElementById("mapsAPI"), mapOptions);
	
	var sample1 = new google.maps.Marker
	({
		position: eudo,
		map: map,
		title: "Magic Tournament"
	});
	
	var sample2 = new google.maps.Marker
	({
		position: tourn,
		map: map,
		title: "League of Legends Tournament"
	});
	
	var sample3 = new google.maps.Marker
	({
		position: chess,
		map: map,
		title: "Chess pick-up"
	});
}

google.maps.event.addDomListener(window, 'load', initialize);