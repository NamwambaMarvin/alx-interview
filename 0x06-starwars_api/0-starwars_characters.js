#!/usr/bin/node
/* Use the requests modeule to get stars wars API */
const request = require('request');
const urlApi = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];

// Get from the API
request(urlApi + movieId, (error, response, body) => {
    if (error) throw error;
    const characters = JSON.parse(body).characters;
    showNames(characters);
});
// Display results
const showNames = (names, i = 0) => {
    if (i === names.length) return;
    request(names[i], (error, response, body) => {
	if (error) throw error;
	console.log(JSON.parse(body).name);
	showNames(names, i + 1);
    });
};
