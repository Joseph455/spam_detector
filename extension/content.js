chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'getEmailContent') {
      try {
        // Gmail specific selector for email content
        const emailContent = document.querySelector('.ii.gt');

        if (!emailContent) {
          sendResponse({ error: 'No email content found' });
          return;
        }
  
        // Get text content and clean it
        let cleanedContent = emailContent.innerText;
        
        // Remove URLs
        cleanedContent = cleanedContent.replace(/(?:https?|ftp):\/\/[\n\S]+/g, '');
        
        // Remove any remaining HTML tags
        cleanedContent = cleanedContent.replace(/<[^>]*>/g, '');
        
        sendResponse({ content: cleanedContent });
      } catch (error) {
        sendResponse({ error: error.message });
      }
    }
    return true; // Required for async response
});
