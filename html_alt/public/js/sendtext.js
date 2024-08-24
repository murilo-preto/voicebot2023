let jumbotronElement;
const accessToken = localStorage.getItem('accessToken');

// Função para decodificar Base64 e retornar um Blob
function base64toBlob(base64, mimeType) {
    const byteCharacters = atob(base64);
    const byteNumbers = Array.from(byteCharacters, char => char.charCodeAt(0));
    const byteArray = new Uint8Array(byteNumbers);
    return new Blob([byteArray], { type: mimeType });
}

// Função para reproduzir áudio a partir de um Blob de Base64
function playAudioFromBlob(audioBlob) {
    const audioElement = new Audio(URL.createObjectURL(audioBlob));
    audioElement.play()
        .then(() => console.log("Áudio reproduzido com sucesso"))
        .catch(error => console.error("Erro ao reproduzir áudio:", error));
}

// Função principal para reproduzir áudio recebido em Base64
function playReceivedAudio(audioBase64) {
    console.log("Reproduzindo áudio recebido do servidor");
    const audioBlob = base64toBlob(audioBase64, 'audio/mp3');
    playAudioFromBlob(audioBlob);
}

// Função para extrair o nome de usuário do token JWT
function extractUsernameFromToken(token) {
    const tokenPayload = JSON.parse(atob(token.split('.')[1]));
    return tokenPayload.sub;
}

// Função para configurar os cabeçalhos da requisição
function createHeaders(token) {
    const username = extractUsernameFromToken(token);
    return {
        'token': token,
        'username': username,
    };
}

// Função para criar o Jumbotron ou atualizá-lo
function updateJumbotron(text) {
    if (!jumbotronElement) {
        jumbotronElement = document.createElement('h1');
        jumbotronElement.classList.add('jumbotron');
    }

    jumbotronElement.textContent = text;

    const existingJumbotron = document.getElementById('audioData');
    if (existingJumbotron) {
        existingJumbotron.parentNode.replaceChild(jumbotronElement, existingJumbotron);
    } else {
        console.error("Elemento 'audioData' não encontrado.");
    }
}

// Função para tratar a resposta do servidor
function handleServerResponse(response) {
    response.json().then(data => {
        console.log(data);
        updateJumbotron(data.text);
        playReceivedAudio(data.audio);
    });
}

// Função para enviar texto ao servidor
function enviarTextoParaServidor(texto, endereco) {
    const headers = createHeaders(accessToken);
    const formData = new FormData();
    formData.append('texto', texto);

    fetch(endereco, {
        method: 'POST',
        body: formData,
        headers: headers
    })
        .then(response => {
            if (response.ok) {
                handleServerResponse(response);
            } else {
                console.error('Falha ao enviar texto.');
            }
        })
        .catch(error => {
            console.error('Erro:', error);
        });
}

export { enviarTextoParaServidor };
