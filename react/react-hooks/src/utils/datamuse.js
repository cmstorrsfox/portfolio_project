//functions that make calls to datamuse API
const url = "https://api.datamuse.com/"
const noCors = "https://fast-retreat-21257.herokuapp.com/"

async function getWords(params, word, settingFunc) {
  const entries = [];
  const req = await fetch(`${noCors}${url}words?${params}=${word}`);
  const jsonReq = await req.json();

  for (let i of jsonReq.slice(0, 10)) {
    entries.push(i);
    console.log(i.tags)
  }

  settingFunc(entries);
};


export { getWords };