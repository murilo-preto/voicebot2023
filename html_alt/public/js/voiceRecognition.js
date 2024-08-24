
function voiceRecognition(callback) {
    if (!('webkitSpeechRecognition' in window)) {
        alert("Seu navegador não suporta a Web Speech API.");
    } else {
        var recognition = new webkitSpeechRecognition();
        recognition.lang = "pt-BR";
        recognition.continuous = false;
        recognition.interimResults = false;

        recognition.onresult = function (event) {
            var resultado = event.results[0][0].transcript;
            console.log("Você disse: " + resultado);
            callback(resultado);
        };

        recognition.onerror = function (event) {
            console.error("Ocorreu um erro: " + event.error);
        };

        recognition.start();
    }
}

export { voiceRecognition };
