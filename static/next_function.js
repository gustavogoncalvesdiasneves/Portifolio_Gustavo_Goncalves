document.addEventListener("DOMContentLoaded", function() {
  var currentIndex = 0;
  var projectsContainer = document.getElementById("projects");
  var nextButton = document.getElementById("nextButton");

  function showNextProjects() {
      // Fazer uma solicitação AJAX para buscar mais projetos
      var xhr = new XMLHttpRequest();
      xhr.open("GET", `/get_additional_projects/${currentIndex}`, true);

      xhr.onreadystatechange = function() {
          if (xhr.readyState === 4 && xhr.status === 200) {
              var additionalProjects = JSON.parse(xhr.responseText);

              if (additionalProjects.length === 0) {
                  nextButton.style.display = "none";
              } else {
                  additionalProjects.forEach(function(project) {
                      var projectHTML = `
                        <a href="${project.link}" style="text-decoration:none" target="_blank"
                          <div class="card-container">
                          <div class="card-${project.card_id}" style="background-image: url(${project.image});">
                            <div class="card-wrapper">
                              <h2>${project.title}</h2>
                              <p>${project.p}</p>
                            </div>
                          </div>
                          <div class="card-text">
                            <p>${project.description}</p>
                          </div>
                          </div>
                        </a>
                        `;
                      projectsContainer.innerHTML += projectHTML;
                  });

                  currentIndex += additionalProjects.length;
              }
          }
      };

      xhr.send();
  }

  nextButton.addEventListener("click", showNextProjects);
});
