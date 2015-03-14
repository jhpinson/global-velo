(function ($) {

  var geocodeAddress = function (address, map) {

    geocoder = new google.maps.Geocoder();
    geocoder.geocode({ 'address': address}, function (results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        map.setCenter(results[0].geometry.location);
        var marker = new google.maps.Marker({
          map: map,
          position: results[0].geometry.location
        });
        console.debug(results[0].geometry.location.lat(), results[0].geometry.location.lng());
      }
    });

  };


    if ($('#map').length > 0) {

      var position = new google.maps.LatLng(43.1784004,-0.2617271999999957);

      var mapOptions = {
        center: position,
        zoom: 16
      };
      var map = new google.maps.Map(document.getElementById('map'),
        mapOptions);

      var marker = new google.maps.Marker({
          map: map,
          position: position,
          title : 'SAS Global Vélo'
        });


    }

    //geocodeAddress('1 r Pyrénées, 64800 NAY', map);




})(jQuery);