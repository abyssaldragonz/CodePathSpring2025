/*** Dark Mode ***
  
    Purpose:
    - Use this starter code to add a dark mode feature to your website.

    When To Modify:
    - [X] Project 5 (REQUIRED FEATURE) 
    - [X] Any time after
***/

// Step 1: Select the theme button
let themeButton = document.getElementById("theme-button");
let darkMode = false;

// Step 2: Write the callback function
const toggleDarkMode = () => {
	// Write your code here
	// This section will run whenever the button is clicked
	document.body.classList.toggle("dark-mode");
    if (!darkMode){
        themeButton.style.backgroundColor = "#231942";
    }
    else {
        themeButton.style.backgroundColor = "#684fb5";
    }
    darkMode = !darkMode;
};

// Step 3: Register a 'click' event listener for the theme button,
//          and tell it to use toggleDarkMode as its callback function
themeButton.addEventListener("click", toggleDarkMode);


/*** Form Handling ***

    Purpose:
    - When the user submits the RSVP form, the name and state they 
        entered should be added to the list of participants.

    When To Modify:
    - [X] Project 6 (REQUIRED FEATURE)
    - [X] Project 6 (STRETCH FEATURE) 
    - [X] Project 7 (REQUIRED FEATURE)
    - [X] Project 9 (REQUIRED FEATURE)
    - [X] Any time between / after
***/

// Step 1: Add your query for the submit RSVP button here
let submitButton = document.getElementById("rsvp-button");
let count = 5;

const addParticipant = (person, event) => {
	// Step 2: Write your code to manipulate the DOM here
	event.preventDefault();

	// let user = document.getElementById("user").value;
	// let classType = document.getElementById("class").value;
	// let level = document.getElementById("level").value;
	// let contact = document.getElementById("contact").value;

	let participantsList = document.querySelector(".rsvp-participants");

	let newMember = document.createElement("p");
	newMember.innerHTML = `${person.user.value} (${person.class.value}) has joined the party!`;
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
};

// Step 3: Add a click event listener to the submit RSVP button here
// submitButton.addEventListener("click", addParticipant);


/*** Form Validation ***
  
    Purpose:
    - Prevents invalid form submissions from being added to the list of participants.

    When To Modify:
    - [X] Project 7 (REQUIRED FEATURE)
    - [X] Project 7 (STRETCH FEATURE)
    - [X] Project 9 (REQUIRED FEATURE)
    - [X] Any time between / after
***/

// Step 1: We actually don't need to select the form button again -- we already did it in the RSVP code above.

// Step 2: Write the callback function
const validateForm = (event) => {
	const person = {
		user: document.getElementById("user"),
		class: document.getElementById("class"),
		level: document.getElementById("level"),
		contact: document.getElementById("contact"),
	};
    
	let containsErrors = false;
	var rsvpInputs = document.getElementById("rsvp-form").elements;
	// Loop through all inputs
	for (let i = 0; i < rsvpInputs.length; i++) {
		// Inside loop, validate the value of each input
		rsvpInputs[i].classList.remove("error");

		if (rsvpInputs[i].id != "level" && rsvpInputs[i].value.length < 2) {
			// length of inputs is less than 2
			containsErrors = true;
			rsvpInputs[i].classList.add("error");
		}
	}

	if (person.level.value.length == "") {
		// blank level
		containsErrors = true;
		person.level.classList.add("error");
	}

	if (!person.contact.value.includes("@") || !person.contact.value.includes(".net")) {
		// invalid email
		containsErrors = true;
		person.contact.classList.add("error");
	}

	// If no errors, call addParticipant() and clear fields
	if (containsErrors == false) {
		addParticipant(person, event);
		toggleModal(person);
		for (let i = 0; i < rsvpInputs.length; i++) {
			rsvpInputs[i].classList.remove("error");
			rsvpInputs[i].value = "";
		}
	}
};

// Step 3: Replace the form button's event listener with a new one that calls validateForm()
submitButton.addEventListener("click", validateForm);


/*** Animations ***/
document.getElementById("joinBattle").onclick = function () {
	window.location.hash = "#rsvp";
};

document.getElementById("noticeBoard").onclick = function () {
	window.location.hash = "#about";
};


/*** Modal ***
  
    Purpose:
    - Use this starter code to add a pop-up modal to your website.

    When To Modify:
    - [X] Project 9 (REQUIRED FEATURE)
    - [X] Project 9 (STRETCH FEATURE)
    - [X] Any time after
***/

// Toggle reduce motion
let reduceMotion = false;
let motionButton = document.getElementById("reduce-motion-button");
let headerImage = document.getElementById("header-img");
let navImage = document.getElementById("navbar-img");

const toggleMotion = () => {
    if (!reduceMotion){
        motionButton.style.backgroundColor = "#451D0F";
        motionButton.style.color = "#8F592C";
		motionButton.innerText = "REDUCE MOTION: ON"
        headerImage.style.animation = `none`;
        navImage.style.animation = `none`;
    }
    else {
        motionButton.style.backgroundColor = "#8F592C";
        motionButton.style.color = "#451D0F";
		motionButton.innerText = "REDUCE MOTION: OFF"
        headerImage.style.animation = `myAnim 2s steps(1, end) 0s infinite normal forwards`;
        navImage.style.animation = `myAnim 2s steps(2, end) 0s infinite reverse forwards`;
    }
    reduceMotion = !reduceMotion;
};

motionButton.addEventListener("click", toggleMotion);

// Toggle modal
const toggleModal = (person) => {
	// Select the elements
	let modal = document.getElementById("success-modal");
	let modalContent = document.getElementById("modal-text");

	// Update modal display to flex
	modal.style.display = "flex";

	// Update modal text to personalized message
	modalContent.innerHTML = `Dungeon run mission accepted! <br><br> Welcome to the party <span class="warning">${person.user.value}</span>! <br><br> Your class is: <span class="warning">${person.class.value}</span>! <br><br> Prepare your weapons, your armor, and your inventory for battle! <br><br> It will be a tough journey ahead into the Catacombs!`;

	// Set modal timeout to 5 seconds
	setTimeout(() => {
		modal.style.display = "none";
	}, 5000);

	// Add custom button to exit out of the modal early
	closeModalButton = document.getElementById("close-modal");
	closeModalButton.addEventListener("click", () => {
		modal.style.display = "none";
	});

    // Animate image
    if (!reduceMotion) {
        let intervalId = setInterval(animateImage, 500);
        setTimeout(() => {
            modal.style.display = "none";
            clearInterval(intervalId);
        }, 5000);   
    }
};

// Animation variables and animateImage() function
let rotateFactor = 10;
let modalImage = document.getElementById("modal-image");
const animateImage = (imageElement = modalImage) => {
	if (rotateFactor == 10) {
		rotateFactor = -10;
	} else {
		rotateFactor = 10;
	}
    imageElement.style.transform = `rotate(${rotateFactor}deg)`;
};