document.addEventListener('DOMContentLoaded', function () {
    const accessToken = localStorage.getItem('accessToken');

    if (accessToken) {
        const tokenPayload = JSON.parse(atob(accessToken.split('.')[1]));
        const username = tokenPayload.sub;

        console.log('User is logged in as:', username);

        const userContainer = document.querySelector('#user-container');
        if (userContainer) {
            appendUsernameAndLogoutButton(username, userContainer);
        }
    } else {
        console.log('User is not logged in');
    }
});

function appendUsernameAndLogoutButton(username, container) {
    const usernameContainer = createContainer('span', `Bem-vindo, ${username}`, ['navbar-text', 'mr-3']);
    const logoutButton = createContainer('button', 'Desconectar', ['btn', 'btn-outline-secondary']);

    logoutButton.addEventListener('click', handleLogout);

    container.appendChild(usernameContainer);
    container.appendChild(logoutButton);
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
