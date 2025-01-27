document.addEventListener('DOMContentLoaded', function() {
    const scanButton = document.getElementById('scanButton');
    const modelSelect = document.getElementById('modelSelect');
    const resultDiv = document.getElementById('result');
  
    scanButton.addEventListener('click', async () => {
      const selectedModel = modelSelect.value;
      
      try {
        // Get active tab
        const [tab] = await chrome.tabs.query({active: true, currentWindow: true});

        console.log(tab);

        // Execute content script to get email content
        const response = await chrome.tabs.sendMessage(tab.id, { 
          action: 'getEmailContent',
          model: selectedModel 
        });
  
        if (response.error) {
          resultDiv.textContent = 'Error: ' + response.error;
          return;
        }

        resultDiv.textContent = response.content;
  
        // Send to API
        // const apiResponse = await fetch('http://127.0.0.1:8000', {
        //   method: 'POST',
        //   headers: {
        //     'Content-Type': 'application/json',
        //   },
        //   body: JSON.stringify({
        //     text: response.content,
        //     model: selectedModel
        //   })
        // });
  
        // const result = await apiResponse.json();
        
        // // Display result
        // resultDiv.textContent = result.prediction;
        // resultDiv.className = result.prediction.toLowerCase();
      } catch (error) {
        resultDiv.textContent = 'Error: ' + error.message;
      }
    });
});