const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Usage: node fetch_and_save.js <URL> <file_path>');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching the URL:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to retrieve content. Status code:', response.statusCode);
    return;
  }

  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error('Error writing to file:', err);
      return;
    }
    console.log(`Content successfully saved to ${filePath}`);
  });
});
