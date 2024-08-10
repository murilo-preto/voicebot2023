
document.addEventListener('DOMContentLoaded', function () {
    const accessToken = localStorage.getItem('accessToken');

    if (accessToken) {
        const tokenPayload = JSON.parse(atob(accessToken.split('.')[1]));
        const username = tokenPayload.sub;

        console.log('User is logged in as:', username);

        const navbar = document.querySelector('.navbar');
        if (navbar) {
            appendUsernameAndLogoutButton(username, navbar);
        }
    } else {
        console.log('User is not logged in');
    }
});

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
    window.location.href = '/public/html/login.html';
}