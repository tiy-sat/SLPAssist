var $ = require("jquery");

var $signUp = $("[data-js='create-account-form']");

// constructor code
function CreateAccount(){

  var createAccount = this;



  createAccount.ajaxPOST = function(){
    $.fn.serializeObject = function(){
        var o = {};
        var a = this.serializeArray();
        $.each(a, function() {
            if (o[this.name] !== undefined) {
                if (!o[this.name].push) {
                    o[this.name] = [o[this.name]];
                }
                o[this.name].push(this.value || '');
            } else {
                o[this.name] = this.value || '';
            }
        });
        return o;
    };


    $signUp.on("submit", function(e){
      e.preventDefault();

      var newAccountData = $signUp.serializeObject();
      console.log(newAccountData);
      $.ajax({
        type: "POST",
        url: "/users",
        data: JSON.stringify(newAccountData),
        contentType: 'application/json',
        dataType: "json",
        success: function(response){
          console.log(response)


        }
      })

    });
  }
}
module.exports = CreateAccount;
// necessary or ability to call constructor
