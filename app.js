document.getElementById('fetchButton').addEventListener('click', fetchAIResponse);

function fetchAIResponse() {
    fetch('http://localhost:5000/api/ai-response')
        .then(response => response.json())
        .then(data => {
            document.getElementById('response').innerText = data.message;
        })
        .catch(error => console.error('Error:', error));
}
