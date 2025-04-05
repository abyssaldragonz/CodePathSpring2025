/*** Dark Mode ***
  
  Purpose:
  - Use this starter code to add a dark mode feature to your website.

  When To Modify:
  - [X] Project 5 (REQUIRED FEATURE) 
  - [ ] Any time after
***/

// Step 1: Select the theme button
let themeButton = document.getElementById("theme-button");

// Step 2: Write the callback function
const toggleDarkMode = () => {
    // Write your code here
    // This section will run whenever the button is clicked
    document.body.classList.toggle("dark-mode");
}

// Step 3: Register a 'click' event listener for the theme button,
//             and tell it to use toggleDarkMode as its callback function
themeButton.addEventListener("click", toggleDarkMode);



/*** Form Handling ***
  
  Purpose:
  - When the user submits the RSVP form, the name and state they 
    entered should be added to the list of participants.

  When To Modify:
  - [ ] Project 6 (REQUIRED FEATURE)
  - [ ] Project 6 (STRETCH FEATURE) 
  - [ ] Project 7 (REQUIRED FEATURE)
  - [ ] Project 9 (REQUIRED FEATURE)
  - [ ] Any time between / after
***/

// Step 1: Add your query for the submit RSVP button here
let submitButton = document.getElementById("rsvp-button");
let count = 5;

const addParticipant = (event) => {
    // Step 2: Write your code to manipulate the DOM here
    event.preventDefault();

    let user = document.getElementById("user").value;
    let classType = document.getElementById("class").value;
    let level = document.getElementById("level").value;

    let participantsList = document.querySelector(".rsvp-participants");

    let newMember = document.createElement("p");
    newMember.innerHTML = user + " (" + classType + ") has joined the party! ";
    participantsList.appendChild(newMember);

    // Suggested Solution !! Updates it below the participants list !!
    // let countDiv = document.querySelector("#rsvp-count");
    // countDiv.remove();
    // count++;
    // let newCounter = document.createElement("p");
    // newCounter.id = "rsvp-count";
    // newCounter.innerHTML = "🔥" + count + " people have joined the party!🔥";
    // participantsList.appendChild(newCounter);

    // Using span !! Updates it at the top under RSVP title !!!
    let countSpan = document.querySelector("#count");
    count++;
    countSpan.innerHTML = count;
}

// Step 3: Add a click event listener to the submit RSVP button here
submitButton.addEventListener("click", addParticipant);



/*** Form Validation ***
  
  Purpose:
  - Prevents invalid form submissions from being added to the list of participants.

  When To Modify:
  - [ ] Project 7 (REQUIRED FEATURE)
  - [ ] Project 7 (STRETCH FEATURE)
  - [ ] Project 9 (REQUIRED FEATURE)
  - [ ] Any time between / after
***/

// Step 1: We actually don't need to select the form button again -- we already did it in the RSVP code above.

// Step 2: Write the callback function
const validateForm = () => {

  let containsErrors = false;

  var rsvpInputs = document.getElementById("rsvp-form").elements;
  // TODO: Loop through all inputs

  // TODO: Inside loop, validate the value of each input

  // TODO: If no errors, call addParticipant() and clear fields

}

// Step 3: Replace the form button's event listener with a new one that calls validateForm()



/*** Animations [PLACEHOLDER] [ADDED IN UNIT 8] ***/
document.getElementById("joinBattle").onclick = function () {
    window.location.hash = "#rsvp";
};



/*** Success Modal [PLACEHOLDER] [ADDED IN UNIT 9] ***/
