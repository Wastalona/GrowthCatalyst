let btn = document.querySelector("#btn");
let slider = document.querySelector(".slidebar");

if (btn && slider) {
    btn.addEventListener('click', function() {
        alert("message");
        slider.classList.toggle('active');
    });
} else {
    console.error("Button or slider not found");
}
