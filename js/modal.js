var $ = require("jquery");

var $editScore = $("[data-js='edit_score']");
var $students = $("[data-js='studentListWrapper']");
var $cancelModal = $("[data-js='modal_close']");
var $modal = $("[data-js='modal']");

this.openModal = function(){

  $students.on("click", $("[data-js='edit_score']"), function(e){
    $modal.toggleClass("modal__hide");

  })
}

this.closeModal = function(){

  $cancelModal.on("click", function(e){
    $modal.toggleClass("modal__hide");

  })
}
