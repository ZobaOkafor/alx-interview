#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2] + '/';
const apiBase = 'https://swapi-api.hbtn.io/api/films/';

const fetchFilmCharacters = async () => {
  try {
    const filmUrl = apiBase + filmId;
    const filmData = await new Promise((resolve, reject) => {
      request(filmUrl, (error, response, body) => {
        if (error) return reject(error);
        resolve(JSON.parse(body));
      });
    });

    const characterEndpoints = filmData.characters;

    for (const endpoint of characterEndpoints) {
      const characterData = await new Promise((resolve, reject) => {
        request(endpoint, (error, response, body) => {
          if (error) return reject(error);
          resolve(JSON.parse(body).name);
        });
      });
      console.log(characterData);
    }
  } catch (error) {
    console.error(error);
  }
};

fetchFilmCharacters();
