$(document).ready(function() {
    $('.agregar-a-carrito').on('click', function() {

      var talla = document.querySelector("#elegir-talla select")[document.querySelector("#elegir-talla select").selectedIndex].innerHTML;
      console.log(talla);

      document.getElementById("talla").value = talla;


    });
    
  });
