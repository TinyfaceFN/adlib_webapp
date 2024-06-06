const storyButtons = document.querySelectorAll('.storyselect')
const body = document.querySelector('body')
// This was just for testing some ideas please disregard no js functionality is being used in this page

function createAdlibForm(){

}

document.addEventListener('DOMContentLoaded', function() {
    storyButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        console.log('WORKING');

      });
    });
  });