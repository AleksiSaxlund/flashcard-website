
function registerFormValidator() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var password_check = document.getElementById("password_check").value;
    
    if (username.length < 4) {
        alert("Username must be at least 4 characters long");
        return false;
    }

    if (password.length < 6) {
        alert("Password must be at least 6 characters long");
        return false;
    }

    if (!/[A-Z]/.test(password) || !/[a-z]/.test(password)) {
        alert("Password must contain both uppercase and lowercase letters");
        return false;
    }

    if (!/\d/.test(password)) {
        alert("Password must contain at least one number");
        return false;
    }

    if (!/[!@#$%^&*]/.test(password)) {
        alert("Password must contain at least one special character");
        return False
    }

    if (password !== password_check) {
        alert("Password and Confirm Password must match");
        return false;
    }

    return true;
    }