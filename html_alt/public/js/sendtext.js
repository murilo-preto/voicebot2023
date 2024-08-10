let jumbotronElement;
const accessToken = localStorage.getItem('accessToken');


function base64toBlob(base64, mimeType) {
    let byteCharacters = atob(base64);
    let byteNumbers = new Array(byteCharacters.length);
    for (let i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
    }
    let byteArray = new Uint8Array(byteNumbers);
    return new Blob([byteArray], { type: mimeType });
}

function playReceivedAudio(audioBase64) {
    console.log("Reproduzindo áudio recebido do servidor");
    let audioBlob = base64toBlob(audioBase64, 'audio/mp3');
    let audioElement = new Audio(URL.createObjectURL(audioBlob));
    audioElement.play()
        .then(() => console.log("Áudio reproduzido com sucesso"))
        .catch(error => console.error("Erro ao reproduzir áudio:", error));
}

function enviarTextoParaServidor(texto) {
    const tokenPayload = JSON.parse(atob(accessToken.split('.')[1]));
    const username = tokenPayload.sub;

    const headers = {
        'token': accessToken,
        'username': username,
    };

    const formData = new FormData();
    formData.append('texto', texto);

    fetch('https://voicebot.fernandoteubl.com:5000/api/chatbot', {
        method: 'POST',
        body: formData,
        headers: headers
    })
        .then(response => {
            if (response.ok) {
                response.json().then(data => {
                    console.log(data);

                    if (jumbotronElement) {
                        jumbotronElement.textContent = data.text;
                    } else {
                        jumbotronElement = document.createElement('h1');
                        jumbotronElement.textContent = data.text;
                        jumbotronElement.classList.add('jumbotron');

                        let existingJumbotron = document.getElementById('audioData');
                        if (existingJumbotron) {
                            existingJumbotron.parentNode.replaceChild(jumbotronElement, existingJumbotron);
                        } else {
                            console.error("Element 'audioData' not found.");
                        }
                    }
                    
                    // lerTexto(data.text);
                    playReceivedAudio(data.audio);
                });
            } else {
                console.error('Falha ao enviar texto.');
            }
        })
        .catch(error => {
            console.error('Erro:', error);
        });
}

// function lerTexto(texto) { 
//     var discurso = new SpeechSynthesisUtterance(texto);
//     discurso.voice = speechSynthesis.getVoices()[0];
//     speechSynthesis.speak(discurso);
// }

export { enviarTextoParaServidor };