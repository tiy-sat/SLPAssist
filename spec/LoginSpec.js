describe("Login", function(){
  var Login = require("../lib/login");

  var login;

  beforeEach(function(){
    login = new Login();
  });

  it("should be hidden by default", function(){
    expect(modal.isOpen).toBe(false);
  });

})
