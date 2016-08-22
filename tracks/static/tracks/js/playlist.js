$(document).ready(function() {
    if($("#player")[0]){
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

        $("#player")[0].onpause = function() {
            $("#playlist tr.active").removeClass('active');
        }
        $("#player")[0].onplay = function(){
            $("#playlist tr.current").addClass('active');
        }

        $("#player")[0].onended = function(){
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
    }
});