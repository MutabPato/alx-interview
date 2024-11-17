#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Fetch movie details
request(apiUrl, { json: true }, (err, res, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  if (res.statusCode !== 200) {
    console.error(`Error: Unable to fetch data (Status code: ${res.statusCode})`);
    return;
  }

  // Ensure "characters" list exists in the response
  if (!body.characters || !Array.isArray(body.characters)) {
    console.error('Error: No character data found for this movie.');
    return;
  }

  const characterUrls = body.characters;
  const characterNames = new Array(characterUrls.length); // Placeholder for names
  let completedRequests = 0;

  characterUrls.forEach((url, index) => {
    request(url, { json: true }, (charErr, charRes, charBody) => {
      if (charErr) {
        console.error('Error fetching character data:', charErr);
      } else if (charRes.statusCode === 200) {
        characterNames[index] = charBody.name; // Ensure order
      } else {
        console.error(`Error fetching character (Status Code:; ${charRes.statusCode})`);
      }
      completedRequests++;

      // Print all character once all requests are completed
      if (completedRequests === characterUrls.length) {
        characterNames.forEach((name) => {
          if (name) console.log(name);
        });
      }
    });
  });
});
