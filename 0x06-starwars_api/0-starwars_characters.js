#!/usr/bin/node

const rp = require('request-promise');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Movie ID is required');
  process.exit(1);
}

const filmsUrl = `https://swapi.dev/api/films/${movieId}/`;

/**
 * Fetch data from a URL and return parsed JSON.
 * @param {string} url - The URL to fetch data from.
 * @returns {Promise<Object>} - A promise that resolves to the parsed JSON data.
 */
const fetchData = async (url) => {
  try {
    const data = await rp({ uri: url, json: true });
    return data;
  } catch (error) {
    console.error('Error fetching data:', error.message);
    process.exit(1);
  }
};

const fetchCharacterNames = async (urls) => {
  for (const url of urls) {
    const character = await fetchData(url);
    console.log(character.name);
  }
};

const fetchMovieData = async () => {
  const movieData = await fetchData(filmsUrl);
  if (!movieData.characters) {
    console.error('No characters found in the movie data');
    process.exit(1);
  }
  await fetchCharacterNames(movieData.characters);
};

fetchMovieData();
