var $ = require("jquery");

var $enterEmail = ("[data-js='parEmail']");
var $confirmEmail = ("[data-js='confEmail']");
var $emailError = ("[data-js='errorMsg']");


// confirm that confEmail matches parEmail
  $("[data-js='confEmail']").change(function(e){
    console.log($(e.target).val());
    if ($(e.target).val() != $enterEmail.val()){
      console.log($enterEmail.val());
      // $emailError.text = ("Please make sure caregiver email is correct");
    }
  //   // else {
  //   //   $.ajax({
  //   //
  //   //   })
  //   }
  })
