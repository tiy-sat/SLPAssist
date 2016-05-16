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

  it("should be in DOM when page loads", function(){
    expect($("[data-js='revised_score']")).toBeInDOM()
  });

});
