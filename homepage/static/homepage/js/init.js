
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

    //create the slider
    $('.cd-testimonials-wrapper').flexslider({
        selector: ".cd-testimonials > li",
        animation: "slide",
        controlNav: true,
        slideshow: true,
        smoothHeight: true,
        start: function() {
            $('.cd-testimonials').children('li').css({
                'opacity': 1,
                'position': 'relative'
            });
        }
    });

    function getTimeRemaining(endtime){
        var t = Date.parse(endtime) - Date.parse(new Date());
        var seconds = Math.floor( (t/1000) % 60 );
        var minutes = Math.floor( (t/1000/60) % 60 );
        var hours = Math.floor( (t/(1000*60*60)) % 24 );
        var days = Math.floor( t/(1000*60*60*24) );
        return {
            'total': t,
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        };
    }

    function initializeClock(id, endtime){
        var clock = document.getElementById(id);
        var daysSpan = clock.querySelector('.days');
        var hoursSpan = clock.querySelector('.hours');
        var minutesSpan = clock.querySelector('.minutes');
        var secondsSpan = clock.querySelector('.seconds');

        function updateClock(){
            var t = getTimeRemaining(endtime);
            daysSpan.innerHTML = t.days;
            hoursSpan.innerHTML = ('0' + t.hours).slice(-2);
            minutesSpan.innerHTML = ('0' + t.minutes).slice(-2);
            secondsSpan.innerHTML = ('0' + t.seconds).slice(-2);

            if(t.total<=0){
                clearInterval(timeinterval);
            }
        }

        updateClock();
        var timeinterval = setInterval(updateClock,1000);
    }
    // LAUNCH DATE
    // USE CHRISTMAS DAY so countdown is not a negative value for foreseeable future
    var deadline = 'December 01 2017 00:00:00 UTC';
    initializeClock('countdown', deadline);
});
