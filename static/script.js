document.getElementById('questionForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent page reload on form submission

    const question = document.getElementById('questionInput').value;
    const responseBox = document.getElementById('responseBox');
    
    // Clear any previous content and show a "processing" message
    responseBox.innerHTML = '<p>Processing...</p>';

    try {
        const response = await fetch('/api/ask', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question })
        });

        const data = await response.json(); // Parse the response as JSON

        // Check if the response has an error
        if (data.error) {
            responseBox.innerHTML = `<p class="error">Error: ${data.error}</p>`;
        } else {
            responseBox.innerHTML = `<p class="answer">${data.answer}</p>`;
        }
    } catch (error) {
        responseBox.innerHTML = '<p class="error">An error occurred. Please try again.</p>';
    }
});
