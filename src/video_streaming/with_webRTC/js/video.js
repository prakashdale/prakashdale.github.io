(function() {
    console.log('self executing function')
    var video = document.getElementById("video");
    //var vendorURL = window.URL || window.webkitURL;
    
    
    navigator.getMedia = navigator.getUserMedia || 
                         navigator.webkitGetUserMedia ||
                         navigator.mozGetUserMedia ||
                         navigator.msGetUserMedia;

    console.log(navigator.geolocation);

    //Capture video
    navigator.getMedia({
        video: true,
        audio: false
    }, function(stream){
        const mediaStream = new MediaStream(stream);
        video.srcObject = mediaStream;
        video.play();
    }, function(error) {
        alert('webrtc not supported');
    });


})();