let mediaRecorder;
let audioChunks = [];

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
        } else {
            console.error('Falha ao enviar áudio.');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

export { startRecording, stopRecording };
