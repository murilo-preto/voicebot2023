
function appendUsernameAndLogoutButton(username, navbar) {
    const usernameContainer = createContainer('span', `Bem vindo, ${username}`, ['navbar-text', 'mr-2']);
    const logoutButton = createContainer('button', 'Desconectar', ['btn', 'btn-outline-secondary']);

    logoutButton.addEventListener('click', handleLogout);

    navbar.appendChild(usernameContainer);
    navbar.appendChild(logoutButton);
}

function createContainer(elementType, textContent, classes) {
    const container = document.createElement(elementType);
    container.textContent = textContent;
    container.classList.add(...classes);
    return container;
}

function handleLogout() {
    localStorage.removeItem('accessToken');
    console.log('User logged out');
    window.location.href = '/login';
}

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

function handleNavbarLinkClick(event, accessToken, url) {
    event.preventDefault();
    const headers = {
        'Authorization': `Bearer ${accessToken}`,
    };
    fetch(url, { method: 'GET', headers: headers })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(html => {
            document.write(html);
            document.close();
        })
        .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function () {
    const accessToken = localStorage.getItem('accessToken');

    if (accessToken) {
        const tokenPayload = JSON.parse(atob(accessToken.split('.')[1]));
        const username = tokenPayload.sub;

        const isExpired = isTokenExpired(accessToken);

        if (isExpired) {
            console.log('The token is expired.');
            alert("Seu Token de acesso está expirado, por segurança, faça o login novamente.")
            localStorage.removeItem('accessToken');
            window.location.href = '/login';
        } else {
            console.log('The token is still valid.');
        }

        console.log('User is logged in as:', username);

        const navbarLinks = document.querySelectorAll('.navbar-nav .nav-link');

        navbarLinks.forEach(link => {
            link.addEventListener('click', function (event) {
                handleNavbarLinkClick(event, accessToken, link.getAttribute('href'));
            });
        });

        const navbar = document.querySelector('.navbar');
        if (navbar) {
            appendUsernameAndLogoutButton(username, navbar);
        }
    } else {
        console.log('User is not logged in');
    }
})