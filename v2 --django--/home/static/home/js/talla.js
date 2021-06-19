$(document).ready(function() {
    $('#aBtnGroup button').on('click', function() {
      var thisBtn = $(this);
      
      thisBtn.addClass('active').siblings().removeClass('active');
      var btnText = thisBtn.text();
      var btnValue = thisBtn.val();
      $('#talla').val(btnValue);
      console.log(btnText,btnValue)
      $('#talla').attr('data-id',btnText);

    });
    
  });
