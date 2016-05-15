describe("Modal", function(){
  var Modal = require("../lib/modal");
  var jsdom = require("jsdom");

  var modal;

  beforeEach(function(){
    modal = new Modal();
    document = jsdom.jsdom('<body></body>');
    window = document.defaultView;
    $ = require('jquery');
  });

  it("should produce an array of objects", function(){
    expect($results).toBe(true);
  });

});
