describe("Login", function(){
  var Login = require("../lib/login");
  var jsdom = require("jsdom");

  var login;

  beforeEach(function(){
    login = new Login();
    document = jsdom.jsdom('<body></body>');
    window = document.defaultView;
    $ = require('jquery');
  });

  it("should handle form submission", function(){
    expect($loginForm).toHandle("submit")
  });

})
