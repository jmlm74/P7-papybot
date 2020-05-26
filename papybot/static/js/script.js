$(function(){
    console.log("loaded")
    $('<input type="text" value="Bonjour, mon petit ! Que puis-je pour toi ?" size="32" readonly>').appendTo($('.bonjour'));
    $('form.question').on('submit', submit_event);
    
    // init the mapstyle (OSM or Google)
    map_style()
    // mapstyle dropdown menu
    $('li .osm').on('click',function(){
        console.log("Vu OSM");
        Send_ajax('post',"/goosm/","OSM","text","text/plain");
        mapstyle = "OSM"
        map_style()
    });
    $('li .google').on('click',function(){
        console.log("Vu GOOGLE");
        Send_ajax('post',"/goosm/","GOOGLE","text","text/plain");
        mapstyle = "GOOGLE"
        map_style()
    });

});


var submit_event = function(event){
    var question;
    var data;
    /*
        use to call ajax to parse the question and update the page for waiting for the answer
        Ajax returns the parsed question
    */
    /* wait display */
    $('<div class="row attendrerow"> <div class="col-xs-1 image1"></div></div>').insertAfter($('.dialog'))
    $('.papy').clone().appendTo($('.image1'))
    $('<div class="col-xs-11 attendre"></div>').appendTo($('attendrerow'))
    $('<input type="text" value="Attends un peu, je réfléchis..." size="32" readonly>').appendTo($('.attendrerow'));
    $('.ajax-gif').clone().appendTo($('.attendrerow')).removeAttr('hidden')

    question={'question': $('.quest').val()};
    data = JSON.stringify(question);
    /* the send_ajax is a promise --> wait for the done or the fail */
    Send_ajax('post','/ajax/',data)
    .done( function(response) {
        affiche_map(response)

    })
    .fail( function(response) {
        console.error("Erreur Ajax : " + response)
        alert("Erreur acces au serveur !")
    });
    return false;
};


var Send_ajax = function(type=post ,url, data, datatype='json', contenttype='application/json' ){
    return $.ajax({
        type: type,
        url: url,
        data: data,
        dataType: datatype,
        contentType: contenttype,
    })
};


var affiche_map = function(response_ajax){
    let lat = 0;
    let lon = 0;
    let address = "";
    result_map = response_ajax['map'];

    response_ajax['tab_result'].forEach(function(result){
        address = result['address'];
        lon = result['longitude'];
        lat = result['latitude'];
    });
    $('.ajax-gif').attr('hidden','hidden');
    $('<div class="row map"> <div class="col-md-6 map" id="mapdiv"></div></div>')
    .insertAfter($('.attendrerow'));

    if (mapstyle == 'GOOGLE' ){
        map = new google.maps.Map(document.getElementById('mapdiv'), {
          center: {lat: lat, lng: lon},
          zoom: 14
        });
        var position = {lat: lat,lng : lon};
        var marker = new google.maps.Marker({position: position, map: map});
    } else {
        map = new OpenLayers.Map("mapdiv");
        map.addLayer(new OpenLayers.Layer.OSM());
        var lonLat = new OpenLayers.LonLat(lon ,lat)
            .transform(
                new OpenLayers.Projection("EPSG:4326"), // transform from WGS 1984
                map.getProjectionObject() // to Spherical Mercator Projection
            );
        var zoom=16;
        var markers = new OpenLayers.Layer.Markers( "Markers" );
        map.addLayer(markers);
        markers.addMarker(new OpenLayers.Marker(lonLat));
        map.setCenter (lonLat, zoom);
    }
}


let map_style = function(){
    if (mapstyle == 'OSM'){
        $('li .osm').addClass('active')
        $('li .google').removeClass('active')
    } else {
        $('li .osm').removeClass('active')
        $('li .google').addClass('active')
    }
}