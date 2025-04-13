$(document).ready(function () {

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },

    });

    // Siri configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
      });

    // Siri message animation
    $('.siri-msg').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },

    });

    // mic button click event

    $("#Micbtn").click(function () {
        eel.playAssistantSound()
        $("#Oval").hide();
        $("#SiriWave").show();
        eel.allCommands()()

    });
    


    function doc_keyUp(e) {
        // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time

        if (e.key === 'j' && e.metaKey) {
            eel.playAssistantSound()
            $("#Oval").hide();
            $("#SiriWave").show();
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    // to play assisatnt 
    function PlayAssistant(message) {

        if (message != "") {

            $("#Oval").hide();
            $("#SiriWave").show();
            eel.allCommands(message);
            $("#chatbox").val("")
            $("#MicBtn").show();
            $("#SendBtn").hide();
            

        }

    }

    // toogle fucntion to hide and display mic and send button 
    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").show();
            $("#SendBtn").hide();
             
        }
        else {
            $("#MicBtn").hide();
            $("#SendBtn").show();
        }
    }

    // key up event handler on text box
    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        ShowHideButton(message)
    
    });
    
    // send button event handler
    $("#SendBtn").click(function () {
    
        let message = $("#chatbox").val()
        PlayAssistant(message)
    
    });
    

    // enter press event handler on chat box
    $("#chatbox").keypress(function (e) {
        key = e.which;
        if (key == 13) {
            let message = $("#chatbox").val()
            PlayAssistant(message)
        }
    });




});
// siriwave
document.addEventListener("DOMContentLoaded", function () {
    const micBtn = document.getElementById("Micbtn");
    const ovalSection = document.getElementById("Oval");
    const siriWaveSection = document.getElementById("SiriWave");
    const siriContainer = document.getElementById("siri-container");
  
    micBtn.addEventListener("click", function () {
      // Hide Oval, Show SiriWave
      ovalSection.style.display = "none";
      siriWaveSection.hidden = false; // or siriWaveSection.style.display = "block";
  
      // Clear any previous SiriWave
      siriContainer.innerHTML = "";
  
      // Init SiriWave
      const siriWave = new SiriWave({
        container: siriContainer,
        width: 600,
        height: 200,
        style: 'ios9',
        speed: 0.2,
        amplitude: 1,
        autostart: true
      });
    });
  });
  