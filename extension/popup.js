document.addEventListener('DOMContentLoaded', function() {
    const scanButton = document.getElementById('scanButton');
    const modelSelect = document.getElementById('modelSelect');
    const resultDiv = document.getElementById('result');
  
    scanButton.addEventListener('click', async () => {
      const selectedModel = modelSelect.value;
      
      try {
        // Get active tab
        const [tab] = await chrome.tabs.query({active: true, currentWindow: true});

        // Execute content script to get email content
        const response = await chrome.tabs.sendMessage(tab.id, { 
          action: 'getEmailContent',
          model: selectedModel 
        });
  
        if (response.error) {
          resultDiv.textContent = 'Error: ' + response.error;
          return;
        }

        // Send to API
        const apiResponse = await fetch('https://spam-detector-h5wk.onrender.com/api/scan/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            email_content: response.content,
            model: selectedModel
          })
        });
  
        const result = await apiResponse.json();


        if (apiResponse.status === 200) {
          // Display result
          if (result.prediction === 1) {
              resultDiv.style.backgroundColor ='red';
              resultDiv.textContent = 'This email is spam';
          } else if (result.prediction === 0) {
              resultDiv.style.backgroundColor = 'green';
              resultDiv.textContent = 'This email is not spam';
          } else {
            resultDiv.style.backgroundColor = 'yellow';
              resultDiv.textContent = 'Could not classify this email. Likely a server error';
          }
        } else {
          resultDiv.style.backgroundColor ='red';
          resultDiv.textContent = 'Error: Server error';
        }

      } catch (error) {
        resultDiv.style.backgroundColor ='red';
        resultDiv.textContent = 'Error: ' + error.message;
      }
    });
});
