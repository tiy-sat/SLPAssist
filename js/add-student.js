var $ = require("jquery");

var $enterEmail = ("[data-js='parEmail']");
var $confirmEmail = ("[data-js='confEmail']");
var $emailError = ("[data-js='errorMsg']");

// confirm that confEmail matches parEmail
  $confEmail.blur(function(e){
    if ($(e.target).val() != $enterEmail.val()){
      $emailError.text = ("Please make sure caregiver email is correct");
    }
    else {
      $.ajax({

      })
    }
  })
