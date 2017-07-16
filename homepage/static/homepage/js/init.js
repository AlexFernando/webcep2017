$( document ).ready(function(){
    $('.parallax').parallax();

    $('.button-collapse').sideNav({
        menuWidth: 200, // Default is 300
        edge: 'left', // Choose the horizontal origin
        closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
        draggable: true // Choose whether you can drag to open on touch screens
    });

    /*slider fotos cep*/
    $('.slider').slider({interval:10000});

    /*slider carousel sponsor*/
    $('.carousel').carousel();
    $('select').material_select();
    $('.tooltipped').tooltip({delay: 50});

    $('#textarea1').val('New Text');
    $('#textarea1').trigger('autoresize');

});




