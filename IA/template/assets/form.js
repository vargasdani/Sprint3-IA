document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('formAgricola');
    const resultadoDiv = document.getElementById("resultado");
    const predictionElement = document.getElementById("prediction");

    // Submeter o forms via AJAX
    form.addEventListener('submit', function (event) {
        event.preventDefault(); 
        fetch('/predict', {
            method: 'POST',
            body: new FormData(form),
        })
        .then(response => response.json())  // resposta como JSON, temos que mudar depois
        .then(data => {
            predictionElement.textContent = data.previsao;

            resultadoDiv.classList.remove("invisivel");
        })
        .catch(error => {
            console.error('Erro ao enviar a requisição:', error);
            alert('Ocorreu um erro ao tentar prever. Por favor, tente novamente.');
        });
    });
});
