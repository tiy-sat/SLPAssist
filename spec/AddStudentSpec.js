describe("AddStudent", function(){
  var AddStudent = require("../lib/addStudent");

  var addStudent;

  beforeEach(function(){
    addStudent = new AddStudent();
  });

  it("should be hidden by default", function(){
    expect(modal.isOpen).toBe(false);
  });

})
