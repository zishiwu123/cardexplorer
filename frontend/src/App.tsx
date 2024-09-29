import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

const LORCANA_NUM_SETS = 5;

// NOTE: this varies by set but we will use the largest number for now
const LORCANA_MAX_NUM_CARDS_IN_SET = 225;

function padZeroes(n: string, maxLength: number): string {
  if (n.length >= maxLength) {
    return n;
  }
  const diffLength = maxLength - n.length;
  let result = n;
  for (let i = 0; i < diffLength; i++) {
    result = "0" + result;
  }
  return result;
}

function extractSetNumber(n: string | null): string {
  let setNumber = 0;
  if (!n) {
    return "";
  }
  try {
    setNumber = parseInt(n);
  } catch {
    console.error(`setNumber must be a number: ${n}`);
    return "";
  }
  if (setNumber < 1 || setNumber > LORCANA_MAX_NUM_CARDS_IN_SET) {
    console.error(`cardNumber must be between 1 and ${LORCANA_MAX_NUM_CARDS_IN_SET}`);
    return "";
  }
  // The set number needs to be 3 digits long for request to dreamborn
  //   1 -> 001
  //  11 -> 111
  // 111 -> 111
  return padZeroes(setNumber.toString(), 3);
}

function extractCardNumber(n: string | null): string {
  let cardNumber = 0;
  if (!n) {
    return "";
  }
  try {
    cardNumber = parseInt(n);
  } catch {
    console.error(`cardNumber must be a number: ${n}`);
    return "";
  }
  if (cardNumber < 1 || cardNumber > LORCANA_NUM_SETS) {
    console.error(`cardNumber must be between 1 and ${LORCANA_NUM_SETS}`);
    return "";
  }
  return padZeroes(cardNumber.toString(), 3);
}

/***
 * Return Dreamborn CDN url for image to corresponding Lorcana card,
 * if the setNumber and cardNumber are valid. Otherwise return empty string.
 * Example: https://cdn.dreamborn.ink/static/images/en/cards/001-001.jpg
 */
function getDreambornCdnImageUrl(setNumber: string | undefined, cardNumber: string | undefined): string {
  if (!setNumber || !cardNumber) {
    return "";
  }
  const baseUrl = "https://cdn.dreamborn.ink/static/images/en/cards";
  return `${baseUrl}/${setNumber}-${cardNumber}.jpg`
}

function getDreambornCdnImageUrlFromQueryParams(): string {
  const queryParams = new URLSearchParams(window.location.search);
  const setNumber = extractSetNumber(queryParams.get("setNumber"));
  const cardNumber = extractCardNumber(queryParams.get("cardNumber"));
  const imageUrl = getDreambornCdnImageUrl(setNumber, cardNumber);
  console.log(`** imageUrl: ${imageUrl}`);
  return imageUrl;
}

function App() {
  // TODO: learn how to use React state to update the card being shown. Not sure if submitting forms
  // is in line with responsive stateful Single Page Application (SPA) though. This form feels more
  // like server side rendering static HTML templates.
  // const [imageUrl, setImageUrl] = useState("https://cdn.dreamborn.ink/static/images/en/cards/001-002.jpg");
  const defaultImageUrl = "https://cdn.dreamborn.ink/static/images/en/cards/001-002.jpg";
  const imageUrl = getDreambornCdnImageUrlFromQueryParams() ?? defaultImageUrl;

  return (
    <>
      <div>
        {/* TODO: store urls to TCGPlayer links for the card. These are not searchable by url query params
         so we have to store these internally in backend and have frontend fetch the info. */}
        <a href="https://www.tcgplayer.com/product/504451" target="_blank">
          <img src={imageUrl} className="logo" alt="Ariel - Spectacular Singer" />
        </a>
        <a href="https://vitejs.dev/" target="_blank">
          <img src={viteLogo} className="logo vite" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Lorcana + Vite + React</h1>
      <form>
        <label>
          Set Number:   <input name="setNumber" />
        </label>
        <br>
        </br>
        <label>
          Card Number:   <input name="cardNumber" />
        </label>
        <br>
        </br>
        <input type="submit" value="Submit" />
      </form>
      <p className="read-the-docs">
        Click on the Lorcana Card, and Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
