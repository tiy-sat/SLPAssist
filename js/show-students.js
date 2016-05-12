var $ = require("jquery");

var $students = $("[data-js='studentListWrapper']");

$(function(){

  $.getJSON("/students", function (dataArray){
    dataArray.forEach(function(results){
          $("[data-js='studentListWrapper']").prepend(`
            <article class="dashboard__student--overview">
              <h3 class="dashboard__student--name" data-js="student_name">${results.stuName}</h3>
              <span class="dashboard__edit--score">&#9997;</span>
                <p class="dashboard__student--scoreStatic">
                  <span class="dashboard__student--scoreDynamic" data-js="student_score">${results.score}</span>/10
                </p>
            </article>
            `)
    });
  });

});
