document.getElementById('dataForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission
    // Get form data
    const formData = new FormData(this);
    // Convert form data to JSON
    const jsonData = {};
    for (const [key, value] of formData.entries()) {
        jsonData[key] = parseFloat(value);
    }
    // Send data to API endpoint
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
    .then(response => {
        if (response.ok) {
            return response.json(); // Parse response JSON
        } else {
            throw new Error('Failed to send data');
        }
    })
    .then(data => {
        console.log(data);
        if (data.predicted_crop) {
            // Display result on the webpage
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = `<p>Suitable Crop for Cultivation: ${data.predicted_crop}</p>`;

            // Display suggestion on the webpage
            const suggestionDiv = document.getElementById('suggestion');
            suggestionDiv.innerHTML = `<p>Suggestion: ${data.suggestion}</p>`;
        } else {
            throw new Error('Invalid response from API');
        }
    })

});
