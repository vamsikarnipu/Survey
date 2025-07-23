// static/script.js
 
function updateSubSkills() {
    var mainSkill = document.getElementById("main_skill").value;
    var subSkillSelect = document.getElementById("sub_skill");
    subSkillSelect.innerHTML = ""; // Clear previous options
  
    var skills = {
      'Cooking': ['Indian', 'Chinese', 'Japanese', 'Thai', 'Italian', 'Continental', 'Baking', 'Vegan', 'Grilling & BBQ'],
      'Dancing': ['Classical (Bharatanatyam, Kathak)', 'Western', 'Hip Hop', 'Contemporary', 'Ballet', 'Robotic', 'Jazz', 'Salsa'],
      'Coding': ['Web Dev (HTML, CSS, JS)', 'App Dev (Flutter, Kotlin)', 'Data Science', 'AI/ML', 'Cybersecurity', 'DevOps'],
      'Music': ['Vocal', 'Guitar', 'Piano', 'Violin', 'Indian Classical', 'Western Classical', 'Music Production', 'DJing'],
      'Art & Design': ['Sketching', 'Digital Art', 'Graphic Design', 'UI/UX', 'Animation', 'Fashion Design', '3D Modelling'],
      'Fitness & Health': ['Yoga', 'Zumba', 'Weightlifting', 'CrossFit', 'Pilates', 'Martial Arts', 'Nutrition', 'Physiotherapy Basics'],
      'Language Learning': ['English', 'French', 'Spanish', 'Japanese', 'German', 'Korean', 'Hindi', 'Sign Language'],
      'Soft Skills': ['Public Speaking', 'Communication', 'Leadership', 'Teamwork', 'Time Management', 'Emotional Intelligence'],
      'Teaching': ['School Subjects (Maths, Science, English)', 'Online Tutoring', 'Curriculum Planning', 'Special Ed', 'EdTech Tools'],
      'Business & Marketing': ['Digital Marketing', 'Social Media', 'SEO', 'Branding', 'Business Strategy', 'Entrepreneurship', 'Sales']
    };
  
    if (skills[mainSkill]) {
      skills[mainSkill].forEach(function(sub) {
        var option = document.createElement("option");
        option.text = sub;
        option.value = sub;
        subSkillSelect.appendChild(option);
      });
    }
  }
   


function showFlashMessage() {
    setTimeout(function() {
        const msg = document.getElementById('alert');
        if (msg) {
            msg.style.display = 'none';
        }
    }, 2000); 
};


window.addEventListener('load', updateSubSkills);
window.addEventListener('load', showFlashMessage);

 