document.addEventListener("DOMContentLoaded", () => {
    // const loginForm = document.querySelector("#loginForm");
    const registerForm = document.querySelector("#registerForm");
    const reserveForm = document.querySelector("#reserveForm");

    // if (loginForm) {
    //     loginForm.addEventListener("submit", (e) => {
    //         e.preventDefault();
    //         alert("Login submitted!");
    //         // Add AJAX logic for backend communication
    //     });
    // }

    if (registerForm) {
        registerForm.addEventListener("submit", (e) => {
            e.preventDefault();
            alert("Registration submitted!");
            // Add AJAX logic for backend communication
        });
    }

    if (reserveForm) {
        reserveForm.addEventListener("submit", (e) => {
            e.preventDefault();
            alert("Reservation submitted!");
            // Add AJAX logic for backend communication
        });
    }
});
