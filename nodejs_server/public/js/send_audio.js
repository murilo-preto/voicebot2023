let mediaRecorder;
let audioChunks = [];

function base64toBlob(base64, mimeType) {
    var byteCharacters = atob(base64);
    var byteNumbers = new Array(byteCharacters.length);
    for (var i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
    }
    var byteArray = new Uint8Array(byteNumbers);
    return new Blob([byteArray], { type: mimeType });
}

function playReceivedAudio(audioBase64) {
    console.log("Reproduzindo áudio recebido do servidor");
    const audioBlob = base64toBlob(audioBase64, 'audio/mp3');
    const audioElement = new Audio(URL.createObjectURL(audioBlob));
    audioElement.play()
        .then(() => console.log("Áudio reproduzido com sucesso"))
        .catch(error => console.error("Erro ao reproduzir áudio:", error));
}

function startRecording() {
    console.log("Gravando áudio");
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

function sendAudioToServer(audioChunks) {
    console.log("Enviando gravação");
    const formData = new FormData();
    formData.append('audio', new Blob(audioChunks, { type: 'audio/webm' }));

    fetch('http://127.0.0.1:5000/api/upload-audio', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            console.log('Áudio enviado com sucesso.');
            audioChunks = [];

            response.json().then(data => {
                console.log(data);

                // Criar um novo elemento h1
                const newH1Element = document.createElement('h1');
                newH1Element.textContent = data.text;
                
                // Adicionar a classe "jumbotron" ao novo elemento
                newH1Element.classList.add('jumbotron');
                
                // Selecionar o elemento existente
                const jumbotronElement = document.getElementById('audioData');
                
                // Substituir o elemento existente pelo novo elemento h1
                jumbotronElement.parentNode.replaceChild(newH1Element, jumbotronElement);

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
