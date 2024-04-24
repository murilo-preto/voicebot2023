const accessToken = localStorage.getItem('accessToken');
let mediaRecorder;
let audioChunks = [];

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

function startRecording() {
    console.log("Gravando áudio");
    // Reinicializar audioChunks para uma matriz vazia
    audioChunks = [];

    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(stream => {
            mediaRecorder = new MediaRecorder(stream, { mimeType: 'audio/webm' });
            mediaRecorder.ondataavailable = event => audioChunks.push(event.data);
            mediaRecorder.start();
        })
        .catch(error => console.error('Erro ao acessar o microfone:', error));
}


function stopRecording() {
    console.log("Parando gravação");
    mediaRecorder.stop();

    mediaRecorder.addEventListener('stop', () => {
        // Parar a gravação do microfone
        if (mediaRecorder.stream) {
            mediaRecorder.stream.getTracks().forEach(track => {
                track.stop();
            });
        }

        console.log("Gravação finalizada");
        sendAudioToServer(audioChunks);
    });
}

let jumbotronElement;

function sendAudioToServer(audioChunks) {
    console.log("Enviando gravação");
    let formData = new FormData();
    formData.append('audio', new Blob(audioChunks, { type: 'audio/webm' }));

    const tokenPayload = JSON.parse(atob(accessToken.split('.')[1]));
    const username = tokenPayload.sub;

    const headers = {
        'token': accessToken,
        'username': username,
    };

    fetch('http://voicebot.fernandoteubl.com:5000/api/upload-audio', {
        method: 'POST',
        body: formData,
        headers : headers
    })
    .then(response => {
        if (response.ok) {
            audioChunks = [];
            console.log('Áudio enviado com sucesso.');

            response.json().then(data => {
                console.log(data);
                
                // Se jumbotronElement já foi definido, atualizar seu conteúdo; caso contrário, criar um novo elemento
                if (jumbotronElement) {
                    // Atualizar o conteúdo do elemento existente
                    jumbotronElement.textContent = data.text;
                } else {
                    // Criar um novo elemento h1
                    jumbotronElement = document.createElement('h1');
                    jumbotronElement.textContent = data.text;
                    jumbotronElement.classList.add('jumbotron');
                    
                    // Selecionar o elemento existente para substituição futura
                    let existingJumbotron = document.getElementById('audioData');
                    if (existingJumbotron) {
                        // Substituir o elemento existente pelo novo elemento h1
                        existingJumbotron.parentNode.replaceChild(jumbotronElement, existingJumbotron);
                    } else {
                        console.error("Element 'audioData' not found.");
                    }
                }
                
                playReceivedAudio(data.audio);
            });
        } else {
            console.error('Falha ao enviar áudio.');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

export { startRecording, stopRecording };
