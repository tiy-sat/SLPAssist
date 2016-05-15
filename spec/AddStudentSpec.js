describe("AddStudent", function(){
  var AddStudent = require("../lib/addStudent");

  var $dashboardInput = $("[data-js='dashboard_input']");

  var addStudent;

  beforeEach(function(){
    addStudent = new AddStudent();
  });

  it("should be hidden by default", function(){
    expect($dashboardInput).toBeHidden();
  });
})
