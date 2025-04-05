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

const addParticipant = (event) => {
    // Step 2: Write your code to manipulate the DOM here
    event.preventDefault();

    let user = document.getElementById("user").value;
    let classType = document.getElementById("class").value;
    let level = document.getElementById("level").value;

    let participantsList = document.querySelector("#rsvp-participants");


    let newMember = document.createElement("p");
    newMember.innerHTML = user + "(" + classType + ") has joined the party! "
    participantsList.appendChild(newMember);
}

// Step 3: Add a click event listener to the submit RSVP button here
submitButton.addEventListener("click", addParticipant);



/*** Form Handling [PLACEHOLDER] [ADDED IN UNIT 6] ***/
/*** Form Validation [PLACEHOLDER] [ADDED IN UNIT 7] ***/
/*** Animations [PLACEHOLDER] [ADDED IN UNIT 8] ***/
/*** Success Modal [PLACEHOLDER] [ADDED IN UNIT 9] ***/
