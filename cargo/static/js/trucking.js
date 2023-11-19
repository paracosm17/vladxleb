// JavaScript for Login Form

document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.querySelector('.login');
    
    loginForm.addEventListener('submit', function(event) {
        const emailInput = document.getElementById('id_login');
        const passwordInput = document.getElementById('id_password');
        
        if (emailInput.value === '' || passwordInput.value === '') {
            event.preventDefault(); // Prevent form submission
            alert('Please fill in both email and password.');
        }
    });
});