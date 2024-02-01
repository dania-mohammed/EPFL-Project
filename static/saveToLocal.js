// Function to display the task list from local storage
function showTask(){
    listContainer.innerHTML = localStorage.getItem("data");
}

showTask();
