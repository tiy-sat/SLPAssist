var $ = require("jquery");
var ShowStudents = require("../lib/showStudents");
var AddStudent = require("../lib/addStudent");
var Modal = require("../lib/modal");

var $expandAddStudent = $("[data-js='dashboard_expandAddStudent']");
var $dashboardInput = $("[data-js='dashboard_input']");


$(function(){
  // Code here!

  var showStudents = new ShowStudents();
  var modal = new Modal(showStudents);
  var addStudent = new AddStudent(showStudents);

  addStudent.expandField();
  addStudent.ajaxPOST();
  modal.openModal();
  modal.closeModal();
  modal.updateScore();
  modal.ajaxUpdate();

});
