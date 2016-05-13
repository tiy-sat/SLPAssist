var $ = require("jquery");
var showStudents = require("showStudents");
var addStudent = require("addStudent");
var modal = require("modal");

var $expandAddStudent = $("[data-js='dashboard_expandAddStudent']");
var $dashboardInput = $("[data-js='dashboard_input']");


$(function(){
  // Code here!
  addStudent.expandField();
  addStudent.ajaxPOST();
  showStudents.addToStudents();
  modal.openModal();
  modal.closeModal();
  modal.updateScore();
  modal.ajaxUpdate();

});
