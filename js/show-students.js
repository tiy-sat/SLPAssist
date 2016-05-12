var $ = require("jquery");

var $students = $("[data-js='studentListWrapper']");

$(function(){
  $.getJSON("/students", function (dataArray){
    dataArray.forEach(function(results){
          $("[data-js='studentListWrapper']").prepend(`
            <article class="dashboard__student--overview" data-js="studentOverview">
              <h3 class="dashboard__student--name" data-js="student_name">${results.stuName}</h3>
              <div class="dashboard__edit--score">&#9997;</div>
                <p class="dashboard__student--scoreStatic">
                  <span class="dashboard__student--scoreDynamic" data-js="student_score">${results.score}</span>/10
                </p>
            </article>
            `)

    var $score = $("[data-js='student_score']").html();

      if($score > 5){
         $("[data-js='student_score']").toggleClass("dashboard__student--scoreDynamicGreen");
      };

    });
  });
});
