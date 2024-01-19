document.addEventListener('DOMContentLoaded', function () {
    const accessToken = localStorage.getItem('accessToken');

    if (accessToken) {
        const headers = {
            'Authorization': `Bearer ${accessToken}`,
        };

        const tokenPayload = JSON.parse(atob(accessToken.split('.')[1]));
        const username = tokenPayload.sub;

        console.log('User is logged in as:', username);

        const navbar = document.querySelector('.navbar');

        if (navbar) {
            appendUsernameAndLogoutButton(username, navbar);
        }

        const voicebotLink = document.querySelector('.voicebot-link');

        if (voicebotLink) {
            voicebotLink.addEventListener('click', function (event) {
                event.preventDefault();
                handleVoicebotLinkClick('/voicebot', headers);
            });
        }

    } else {
        console.log('User is not logged in');
    }
});

function appendUsernameAndLogoutButton(username, navbar) {
    const usernameContainer = createContainer('span', `Bem vindo, ${username}`, ['navbar-text', 'mr-2']);
    const logoutButton = createContainer('button', 'Desconectar', ['btn', 'btn-outline-secondary']);
    
    logoutButton.addEventListener('click', function () {
        localStorage.removeItem('accessToken');
        console.log('User logged out');
        window.location.href = '/login';
    });

    navbar.appendChild(usernameContainer);
    navbar.appendChild(logoutButton);
}

function createContainer(elementType, textContent, classes) {
    const container = document.createElement(elementType);
    container.textContent = textContent;
    container.classList.add(...classes);
    return container;
}

function handleVoicebotLinkClick(url, headers) {
    fetch(url, {
        method: 'GET',
        headers: headers,
    })
    .then(response => response.text())
    .then(html => {
        const newPage = document.implementation.createHTMLDocument('Voicebot Page');
        newPage.body.innerHTML = html;

        document.body.innerHTML = newPage.documentElement.outerHTML;
    })
    .catch(error => console.error('Error:', error));
}
