// Method 1: Using document.createElement
function createHeader() {
    // Create a new h1 element
    const header = document.createElement('h1');
    
    // Set the text content of the header
    header.textContent = 'Hello world';
    
    // Append the header to the body of the document
    document.body.appendChild(header);
  }
  // Choose one of the methods above to execute
  createHeader(); // Using Method 1