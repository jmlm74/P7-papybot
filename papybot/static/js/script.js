$(function(){
    $('<input type="text" class="form-control test" value="Bonjour, mon petit ! Que puis-je pour toi ?" size="32" readonly>').appendTo($('.bonjour'));
    $('form.question').on('submit', SubmitEvent);
    $('.reload').on('click',function(){
        $('.quest').val('');
        location.reload();
    });

    // init the mapstyle (OSM or Google)
    MapStyle()
    // mapstyle dropdown menu (google map or OSM map)
    $('li .osm').on('click',function(){
        console.log("Vu OSM");
        SendAjax('post',"/goosm/","OSM","text","text/plain")
        .done( function(response) {
            mapstyle = "OSM";
            MapStyle();
            location.reload(true);
        });
    });
    $('li .google').on('click',function(){
        console.log("Vu GOOGLE");
        SendAjax('post',"/goosm/","GOOGLE","text","text/plain")
        .done( function(response) {
            mapstyle = "GOOGLE"
            MapStyle()
            location.reload(true);
        });
    });

});


var SubmitEvent = function(event){
    var question;
    var data;

    if ($('.quest').val().length == 0) {
        return false;
    }
    $('.send').prop("disabled",true)
    /*
        use to call ajax to parse the question and update the page for waiting for the answer
        Ajax returns the parsed question
    */
    /* wait display */
    $('<div class="row attendrerow"><div class="col-12 col-md-1 image1"></div></div>').insertAfter($('.dialog'))
    $('.papy').clone().appendTo($('.image1'))
    $('<div class="col-12 col-md-4 attendre"></div>').appendTo($('.attendrerow'))
    $('<input type="text" class="form-control" value="Attends un peu, je réfléchis..." size="32" readonly>').appendTo($('.attendre'));
    $('.ajax-gif').clone().appendTo($('.attendrerow')).removeAttr('hidden')

    question={'question': $('.quest').val()};
    data = JSON.stringify(question);
    /* the SendAjax is a promise --> wait for the done or the fail */
    SendAjax('post','/ajax/',data)
    .done( function(response) {
        DisplayMap(response)
        DisplayWiki(response)

    })
    .fail( function(response) {
        console.error("Erreur Ajax : " + response)
        alert("Erreur acces au serveur !")
    });
    return false;
};


var SendAjax = function(type=post ,url, data, datatype='json', contenttype='application/json' ){
    /*
    Send ajax request to server 
    */
    return $.ajax({
        type: type,
        url: url,
        data: data,
        dataType: datatype,
        contentType: contenttype,
    })
}; 

var MapStyle = function(){
    /*
    The dropdown menu map-style 
    */
    if (mapstyle == 'OSM'){
        $('li .osm').addClass('active')
        $('li .google').removeClass('active')
    } else {
        $('li .osm').removeClass('active')
        $('li .google').addClass('active')
    }
}



/************************/
/*      Display Wiki    */
/************************/
var DisplayWiki = function(response_ajax){
    /*
    Display the formatted wiki result in a textarea 
    href to the wikipedia link
    and the goodbye message
    */
    var text;
    var wikilink;
    var result = response_ajax['wiki_result'];
    
    if (result['error'] == true) {
        return false
    }
    $('<section class="col-12"><div class="row wikiresp form-group"> <div class="col-sm-2 col-12 imagewiki"></div></div></section')
    .appendTo($('.wiki'))
    $('.papy:first').clone().appendTo($('.imagewiki'))
    $('<div class="papyresp col-sm-10 col-12"><textarea class="form-control rounded-0 wikitext" rows="12"></textarea></div>')
    .appendTo($('.wikiresp'))
    text = result['msg'] + "\nOui je connais l'adresse : La voici : "+ response_ajax['goo_result']['address'] 
    text = text + "\nTiens regarde le plan pour t'y rendre.\n Et tu savais que : " + result['extract'];
    $('.wikitext').text(text);
    $('<hr />').appendTo($('.wiki'));
    wikilink = "https://fr.wikipedia.org?curid=" + result['id']
    $('<a href="'+wikilink+'" target="_blank">En savoir plus sur Wikipedia</a>').appendTo($('.wiki'));
    $('<div class="row wikiresp2 col-12"> <div class="col-sm-2 col-12 imagewiki2"></div></div>').appendTo($('.wiki'))
    $('.papy:first').clone().appendTo($('.imagewiki2'))
    $('<div class="col-xs-11 wikitext2"></div>').appendTo($('.wikiresp2'))
    $('<input type="text" class="form-control" value="Si tu veux savoir autre chose, n\'hesite pas !!" size="32" readonly>').appendTo($('.wikitext2'));
}


/************************/
/*      Display Map     */
/************************/
var DisplayMap = function(response_ajax){
    /*
    display the map (OSM or Google)
    params : The ajax response
        --> get the geometry to display
        --> get the adress to catch an error --> no response for the query or other
    */
    let lat = 0;
    let lon = 0;
    let address = "";

    // hide the anim gif
    $('.ajax-gif').attr('hidden','hidden');
    result = response_ajax['goo_result'];
    address = result['address'];
    lon = result['longitude'];
    lat = result['latitude'];
    name = result['name'];

    if (address == 'None' || address == 'Error' || address == null) {
        $('<div class="row erreurrow"> <div class="col-xs-1 image2"></div></div>')
        .insertAfter($('.attendrerow'));
        $('.papy:first').clone().appendTo($('.image2'));
        $('<div class="col-xs-11 erreur"></div>').appendTo($('erreurrow'));
        $('<textarea  rows="2" cols="32" readonly>mmmhhh Ca ne me dis rien mon grand ! désolé</textarea>')
        .appendTo($('.erreurrow'));
        return false;
    };
    // the div for the map
    let line = '<section class="col-md-12"><div class="row mapwikirow">'
    line += '<div class="col-md-6 wiki" id="wikidiv"></div><div class="col-md-6" id="mapdiv"></div></div></section>'
    $(line).insertAfter($('.attendrerow'));
    // THE MAP !
    if (mapstyle == 'GOOGLE' ){
        // Google map-style
        map = new google.maps.Map(document.getElementById('mapdiv'), {
          center: {lat: lat, lng: lon},
          zoom: 14
        });
        var position = {lat: lat,lng : lon};
        var marker = new google.maps.Marker({position: position, map: map});
    } else {
        // OSM map-style
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

