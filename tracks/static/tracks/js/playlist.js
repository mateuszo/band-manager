$(document).ready(function() {
    $("#playlist tr").on("click", function() {
        //switch track
        $("#player").attr({
            "src": $(this).attr("data-audiourl"),
            "autoplay": "autoplay",
            "preload": "auto"
        });
        //change active row
        $("#playlist tr.active").removeClass('active');
        $("#playlist tr.current").removeClass('current');
        $(this).addClass('active current');
    });

    //start player with first track
    $("#player").attr({
        "src": $("#playlist tr").eq(1).attr("data-audiourl"),
    });
    $("#playlist tr").eq(1).addClass('active current');

    document.getElementById('player').onpause = function() {
        $("#playlist tr.active").removeClass('active');
    }
    document.getElementById('player').onplay = function(){
        $("#playlist tr.current").addClass('active');
    }

    document.getElementById('player').onended = function(){
        $("#player").attr({
            "src": '',
        });
        var next = $("#playlist tr.current").next()
        $("#player").attr({
            "src": next.attr("data-audiourl"),
        });
        $('tr.current').removeClass('active current')
        next.addClass('active current');
    }


    //pause/play on space
    $(window).keypress(function (e) {
      if (e.keyCode === 0 || e.keyCode === 32) {
        e.preventDefault();
        var player = $("#player")[0];
        if (player.paused) {
            player.play();
        } else {
            player.pause();
        }
      }
    });
});