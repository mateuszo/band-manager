function playTrack(track) {
    // play track
    $("#player").attr({
        "src": track.attr("data-audiourl"),
    });
    // change row styking
    $("#playlist tr.active").removeClass('active');
    $("#playlist tr.current").removeClass('current');
    track.addClass('active current');

    // change player description
    var trackName = track.find(".track-name").html();
    var projectName = track.find(".project-name").html();
    var eventName = track.find(".event-name").html();
    $("#playing-track").html(trackName);
    $("#playing-project").html(projectName);
    $("#playing-event").html(eventName);
}

$(document).ready(function() {
    if($("#player")[0]){
        $("#playlist tr").on("click", function() {
            //switch track
            playTrack($(this));
        });

        //start player with first track
        playTrack($("#playlist tr").eq(1))

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
            playTrack($("#playlist tr.current").next())
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