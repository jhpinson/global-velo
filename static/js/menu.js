(function ($) {

    $('#menu_toggle').on('click', function (event) {
        event.preventDefault();
        $('#header nav').toggleClass('visible');

    })


    ////////////////////////////////////////// home page
    
    if($('body').hasClass('home')){

        $('#dot').addClass('landed');
        var scrolled = false;

        $(window).on('scroll', function(){
            if(!scrolled) {
                $('#dot').addClass('hidden');
                scrolled = true
            }
        })
        
        $('#slideshow').addClass('loading');
        var images_to_preload = []
        var img = new Image();
        img.src = $('.slide').first().css('background-image').replace('url(','').replace(')','').replace('"', '').replace('"', '');
        console.log($('.slide').first().css('background-image').replace('url(','').replace(')','').replace('"', '').replace('"', ''))
        img.onload = function(){
            
            var $home_owl = $('#slideshow .owl-carousel').owlCarousel({
                
                margin:0,
                items:1,
                slideBy:1,
                dots:true,
                nav:false,
                autoplay:true,
                autoplayTimeout:6000,
                smartSpeed:600,
                autoplaySpeed:true,
                animation:'fadeout',
                onTranslated:function(e){     
                    //$('#slideshow bikes').get( idx ).addClass('translated');
                },
                onChanged:function(event){
                    $('#slideshow bikes').removeClass('translated');
                },     
                onInitialized:function(){
                    var s = setTimeout(function(){
                        $('#slideshow').removeClass('loading');
                    }, 600)
                }
                
            });
        }
    }
    ////////////////////////////////////////// all pages

    if($(window).width() > 850)
        $(".subnav").stick_in_parent();

    var s = setTimeout(function(){
        $('.page .splash').addClass('active');
    }, 800)

    ////////////////////////////////////////// bike page

    var carousel_options = {
        loop:false,
        margin:50,
        responsiveClass:true,
        nav:true,
        dots:false,
        responsive:{
            0:{
                items:1,
                nav:true,
                slideBy:1,
                margin:0
            },
            500:{
                margin:50,
                items:1,
                nav:true,
                slideBy:1
            },
            700:{
                items:2,
                nav:true,
                slideBy:2
            },
            850:{
                items:3,
                nav:true,
                slideBy:3
            },
            1280:{
                items:4,
                nav:true,
                slideBy:4
            }
        }
    }

    var carousel_alt_options = {
        loop:false,
        nav:true,
        dots:false,
        items:1,
        nav:true,
        slideBy:1,
        margin:50
    }


    // Owl Carousel !

    var $bikes = $('#bikes'),
        $owl = null;

    pleaseOwl = function(current){
        
        $bikes.addClass('loading');

        var was_alt = $bikes.hasClass('alt'),
            options = was_alt ? carousel_options : carousel_alt_options;

        if( $owl != null ){
            // destroy old owl
            destroyOwl($owl);           
        } 
        
        $owl = $('#bikes .owl-carousel').owlCarousel(options);

        $bikes.toggleClass('alt');

        $('#andmore').css('height', $('#andmore').parent().prev().height() );

        setTimeout(function(){
            $bikes.removeClass('loading'); 
        }, 500)
        
    }

    // owl()!
    pleaseOwl();

    $owl.on('click', '.owl-item a', function(e) {
        e.preventDefault();
        pleaseOwl();
        $owl.trigger('to.owl.carousel', [$(this).closest('.owl-item').index(), 500]);        
    });
    

    var destroyOwl = function($owl, reset){
        $owl.trigger('destroy.owl.carousel');
        $owl.find('.owl-stage-outer').children().unwrap(); 
    }


    ////////////////////////////////////////// filtering */

    // prepare bin
    var $devnull = $('<div id="devnull" style="display:none"></div>');
    $devnull.appendTo('body');

    $('#filtres a').on('click', function(e){

        e.preventDefault();

        var filter = $(this).data('filter');
        if(filter === undefined) return;

        $bikes.addClass('loading');

        // cls on menu
        $('#filtres a').removeClass('selected');
        $(this).addClass('selected')

        // carousel destroy
        $owl.trigger('destroy.owl.carousel').removeClass().addClass('owl-carousel');
        $owl.find('.owl-stage-outer').children().unwrap();
        
        // sort bikes (false -> dev/null)
        $('.bike').appendTo('#bikes .owl-carousel');
        $('.bike').not( filter ).appendTo($devnull);

        // carousel reset
        $owl = $('#bikes .owl-carousel').owlCarousel(carousel_options)

        if($bikes.hasClass('alt')){
            pleaseOwl();
        } else {
            $bikes.removeClass('loading'); 
        }
        var s = setTimeout(function(){
            
        }, 25000)
    })

})(jQuery);