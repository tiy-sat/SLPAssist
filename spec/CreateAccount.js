describe("CreateAccount", function(){
  var CreateAccount = require("../lib/createAccount");

  var createAccount;

  beforeEach(function(){
    createAccount = new CreateAccountt();
  });

  it("complete the Ajax POST", function(){
    expect(response).toHaveBeenCalled();
  });

})
