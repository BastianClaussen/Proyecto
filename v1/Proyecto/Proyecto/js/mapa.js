function iniciarMap(){
    var coord = {lat:-33.4179935 ,lng: -70.6063901};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 15,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}