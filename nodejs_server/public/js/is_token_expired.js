function isTokenExpired(token) {
    // Decode the token to access its claims
    const decodedToken = decodeToken(token);

    // Check if the "exp" claim exists
    if (decodedToken && decodedToken.exp) {
        // Get the expiration time from the token
        const expirationTime = decodedToken.exp * 1000; // Convert to milliseconds

        // Get the current time
        const currentTime = new Date().getTime();

        // Compare the current time with the expiration time
        return currentTime > expirationTime;
    }

    // If the "exp" claim is not present, consider the token as expired
    return true;
}

function decodeToken(token) {
    try {
        // Decode the token using a library or the built-in window.atob() function
        // Note: Using a library like jwt-decode is recommended for proper decoding
        const decodedPayload = JSON.parse(window.atob(token.split('.')[1]));

        return decodedPayload;
    } catch (error) {
        // Handle decoding errors
        console.error('Error decoding JWT:', error);
        return null;
    }
}

const accessToken = localStorage.getItem('accessToken');
if (accessToken){
    const isExpired = isTokenExpired(accessToken);
    
    if (isExpired) {
        console.log('The token is expired.');
        alert("Seu Token de acesso está expirado, por segurança, faça o login novamente.")
        localStorage.removeItem('accessToken');
        window.location.href = '/login';
    } else {
        console.log('The token is still valid.');
    }
}