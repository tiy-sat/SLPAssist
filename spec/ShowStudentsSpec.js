describe("ShowStudents", function(){
  // var ShowStudents = require("../lib/ShowStudents");
  var ShowStudents = require("../lib/showStudents");
  var jsdom = require("jsdom");

  var showStudents;

  beforeEach(function(){
    showStudents = new ShowStudents();
    document = jsdom.jsdom('<body></body>');
    window = document.defaultView;
    $ = require('jquery');
  });

  it("should show green if score is greater than 5", function(){
    expect($("[data-js='student_score']"), results.score > 5).toHaveClass("dashboard__student--scoreDynamicGreen");

  });

});
