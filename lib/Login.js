var $loginForm = $("[data-js='login_form']");

//constructor code
function Login(){

  var login = this;

  login.ajaxPOST = function(){
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


    $loginForm.on("submit", function(e){
      e.preventDefault();
      location.reload(true);

      var loginData = $loginForm.serializeObject();
      console.log(loginData);
      $.ajax({
        type: "POST",
        url: "/login",
        data: JSON.stringify(loginData),
        contentType: 'application/json',
        dataType: "json",
        success: function(response){

          // calling function again as opposed to reloading page

        }
      })
    });
  }
}
module.exports = Login;
// necessary or ability to call constructor
