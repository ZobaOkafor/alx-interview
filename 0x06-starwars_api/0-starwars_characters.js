#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const apiEndpoint = `https://swapi-api.hbtn.io/api/films/${filmId}`;
let characterUrls = [];
const characterNames = [];

const fetchFilmData = async () => {
  await new Promise(resolve => request(apiEndpoint, (error, response, data) => {
    if (error || response.statusCode !== 200) {
      console.error('Error: ', error, '| StatusCode: ', response.statusCode);
    } else {
      const filmData = JSON.parse(data);
      characterUrls = filmData.characters;
      resolve();
    }
  }));
};

const fetchCharacterNames = async () => {
  if (characterUrls.length > 0) {
    for (const url of characterUrls) {
      await new Promise(resolve => request(url, (error, response, data) => {
        if (error || response.statusCode !== 200) {
          console.error('Error: ', error, '| StatusCode: ', response.statusCode);
        } else {
          const characterData = JSON.parse(data);
          characterNames.push(characterData.name);
          resolve();
        }
      }));
    }
  } else {
    console.error('Error: No character URLs found');
  }
};

const printCharacterNames = async () => {
  await fetchFilmData();
  await fetchCharacterNames();

  characterNames.forEach((name, index) => {
    if (index === characterNames.length - 1) {
      process.stdout.write(name);
    } else {
      process.stdout.write(name + '\n');
    }
  });
};

printCharacterNames();
