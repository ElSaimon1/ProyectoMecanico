$(document).ready(function () {
    $("#panel-oculto").hide(); 
    let isPanelVisible = false; 

    $("#boton-toggle").click(function (event) {
        event.preventDefault(); 

        if (!isPanelVisible) {
            $("#panel-oculto").slideDown(); 
            isPanelVisible = true; 
        } else {
            $("#panel-oculto").slideUp(); 
            isPanelVisible = false; 
        }
    });
});



