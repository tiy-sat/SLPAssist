describe("AddStudent", function(){
  var AddStudent = require("../lib/addStudent");
  var jsdom = require("jsdom");

  var $dashboardInput = $("[data-js='dashboard_input']");

  var addStudent;

  beforeEach(function(){
    addStudent = new AddStudent();
    document = jsdom.jsdom('<body></body>');
    window = document.defaultView;
    $ = require('jquery');
  });

  it("should be hidden by default", function(){
    expect($dashboardInput).toBeHidden();
  });
})
