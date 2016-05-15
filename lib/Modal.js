var $ = require("jquery");

var $editScore = $("[data-js='edit_score']");
var $students = $("[data-js='studentListWrapper']");
var $cancelModal = $("[data-js='modal_close']");
var $modal = $("[data-js='modal']");
var $studentID = $("[data-id='${results.id}']");
var $modalHeading = $("[data-js='modal_heading']");
var $revisedScore = $("[data-js='revised_score']");
var $insertScore = $("[data-js='insert_score']");
var $dataID = $();
var $newScore = $();

// constructor code
function Modal(){
  var modal = this;
  modal.selector = "[data-js='modal']";
  
  modal.openModal = function(){
    $students.on("click", $("[data-id='${results.id}']"), function(e){
      $modal.toggleClass("modal__hide");
      // $modal.html("set " + results.name + "'s score");
      $dataID = $(e.target).attr("data-id");
      console.log($dataID);

    })
  }

  modal.closeModal = function(){

    $cancelModal.on("click", function(e){
      $modal.toggleClass("modal__hide");

    })
  }

  modal.updateScore = function(){
    $modal.on("click", $("[data-js='revised_score']"), function(e){
      $newScore = $(e.target).attr("data-counter");
      console.log($newScore);
    })
  }

  modal.ajaxUpdate = function(){

    $insertScore.on("click", function(e){
      e.preventDefault();
      $modal.toggleClass("modal__hide");
      var newScoreData = {id:$dataID, score:$newScore};

          $.ajax({
            type: "POST",
            url: "/students/" + $dataID,
            data: JSON.stringify(newScoreData),
            contentType: 'application/json',
            dataType: "json",
            success: function(response){
              //update score
              console.log(response);
            }
          });
      })

  }
}

module.exports = Modal;
// necessary or ability to call constructor
