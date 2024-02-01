// Get references to HTML elements
const inputBox = document.getElementById("input-box");
const listContainer = document.getElementById("list-container");
const addItem = document.getElementById("addItem"); // Reference to add item button element

// Function to add a task
function addTask(){
    if(inputBox.value === ''){
         alert("You must write something!"); // Display an alert if the input box is empty
    }
    else{
        let li = document.createElement("li"); // Create a new list item
        li.innerHTML = inputBox.value;
        listContainer.appendChild(li); 
        let span = document.createElement("span"); // Create a new span element
        span.innerHTML="\u00d7"; // Set the innerHTML of the span to the '×' symbol
        li.appendChild(span); 
    }
    inputBox.value= ""; 
    saveData(); 
}

// Add event listener to the add item button
addItem.addEventListener("click", addTask);

// Add event listener to the list container
listContainer.addEventListener("click", function(e){
    if(e.target.tagName === "LI"){
        e.target.classList.toggle("checked"); // Toggle the "checked" class on the clicked item
        saveData(); // Save the updated task list
    }
    else if(e.target.tagName === "SPAN"){ // If the span within a list item is clicked
        e.target.parentElement.remove(); 
        saveData(); 
    }
}, false);

// Function to save the task list to local storage
function saveData(){
    localStorage.setItem("data", listContainer.innerHTML);
}

