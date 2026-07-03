

const startBtn = document.getElementById("startBtn");

const hero = document.getElementById("hero");

const tasks = document.getElementById("tasks");

startBtn.addEventListener("click", function(){
/*click action*/
    tasks.scrollIntoView({
    behavior: "smooth"
});

});

// Get Elements

const addButton = document.getElementById("addBtn");

const modal = document.getElementById("taskModal");

const closeButton = document.getElementById("closeModal");

addButton.addEventListener("click", function(){

    modal.style.display = "flex";

});

closeButton.addEventListener("click", function(){

    modal.style.display = "none";

});

const themeToggle = document.getElementById("themeToggle");

// Check saved theme when page loads
if (localStorage.getItem("theme") === "dark") {

    document.body.classList.add("dark-mode");
    themeToggle.innerHTML = "☀️";

} else {

    themeToggle.innerHTML = "🌙";

}

// Toggle theme
themeToggle.addEventListener("click", function () {

    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {

        themeToggle.innerHTML = "☀️";
        localStorage.setItem("theme", "dark");

    } else {

        themeToggle.innerHTML = "🌙";
        localStorage.setItem("theme", "light");

    }

});
// Automatically open task dashboard after adding a task

const params = new URLSearchParams(window.location.search);

if (params.get("dashboard") === "true") {

    setTimeout(() => {

        tasks.scrollIntoView({
            behavior: "smooth"
        });

    }, 100);

}