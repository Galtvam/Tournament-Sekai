$(window).on('ready', function(event, user) {
    disableLoader();
    
    refreshFrontData('user-login', user.login);
    refreshFrontData('user-name', user.name);
    
    $('.tournament-carousel').each(function(index, el){
        $(this).slick({
            dots: false,
            infinite: false,
            arrows: false,
            focusOnSelect: false,
            initialSlide: Math.floor($(this).children().length / 2),  
            speed: 300,
            slidesToShow: 1,
            centerMode: true,
            variableWidth: true,
            autoplay: false,
            autoplaySpeed: (index + 1) * 2500,
        });
    });
});