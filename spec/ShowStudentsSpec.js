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

  it("should produce an array of objects", function(){
    expect($results).toBe(true);
  });

});
