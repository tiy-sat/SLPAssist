var $ = require("jquery");
var ShowStudents = require("../lib/showStudents");
var AddStudent = require("../lib/addStudent");
var Modal = require("../lib/modal");
var CreateAccount = require("../lib/createAccount")

var $expandAddStudent = $("[data-js='dashboard_expandAddStudent']");
var $dashboardInput = $("[data-js='dashboard_input']");


$(function(){
  // Code here!

  var showStudents = new ShowStudents();

  var modal = new Modal();
  var addStudent = new AddStudent();
  var createAccount = new CreateAccount();

  addStudent.expandField();
  addStudent.ajaxPOST();
  modal.openModal();
  modal.closeModal();
  modal.updateScore();
  modal.ajaxUpdate();
  createAccount.ajaxPOST();

});
