import { getManuscriptsApiUrl } from "./urls";
import { loadManuscripts } from "../actions/manuscripts";
export function createManuscriptPayload(manuscript) {
  console.log(manuscript.voter_guide_alternatives);
  return JSON.stringify({
    pk: manuscript.pk,
    type: manuscript.type,
    name: manuscript.name,
    items: manuscript.items.map(item => {
      return {
        type: item.type,
        order: item.order,
        text: item.text,
        reply_action_1: item.reply_action_1,
        reply_action_2: item.reply_action_2,
        reply_action_3: item.reply_action_3,
        reply_text_1: item.reply_text_1,
        reply_text_2: item.reply_text_2,
        reply_text_3: item.reply_text_3
      };
    }),
    voter_guide_alternatives: manuscript.voter_guide_alternatives
  });
}

export function loadAndDispatchManuscripts(dispatch) {
  dispatch(loadManuscripts());
  return fetch(getManuscriptsApiUrl())
    .then(response => response.json())
    .then(manuscripts => dispatch(loadManuscripts(manuscripts)))
    .catch(error => dispatch(loadManuscripts(error)));
}

export function sendManuscriptToApi(manuscript, url, method) {
  return fetch(url, {
    method: method,
    body: createManuscriptPayload(manuscript),
    headers: new Headers({
      'Content-Type': 'application/json'
    })
  })
    .then(response => response.json());
}