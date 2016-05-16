var $students = $("[data-js='studentListWrapper']");

//constructor code
function ShowStudents(){
  var showStudents = this;

    $.getJSON("/students", function (dataArray){
      dataArray.forEach(function(results){
            $("[data-js='studentListWrapper']").prepend(`
              <article class="dashboard__student--overview" data-js="studentOverview">
                <h3 class="dashboard__student--name" data-js="student_name">${results.stuName}</h3>
                <div class="dashboard__score--wrapper">
                  <i class="dashboard__edit--score" data-id="${results.id}">&#9997;</i>
                  <br></br>
                    <p class="dashboard__student--scoreStatic">
                      <span class="dashboard__student--scoreDynamic" data-js="student_score">${results.score}</span>/10
                    </p>
                  </div>
                </article>
              `).find("[data-js='student_score']:first").toggleClass("dashboard__student--scoreDynamicGreen", results.score > 5)
              var $results = results

      });

    });

}
module.exports = ShowStudents;
// necessary for ability to call constructor
