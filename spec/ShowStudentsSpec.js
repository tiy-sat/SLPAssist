describe("ShowStudents", function(){
  // var ShowStudents = require("../lib/ShowStudents");
  var ShowStudents = require("../lib/showStudents");

  var showStudents;

  beforeEach(function(){
    showStudents = new ShowStudents();
  });

  it("should produce an array of objects", function(){
    expect($results).toBe(true);
  });

});
