import axios from 'axios'

export async function getNewParagraph(theme) {
  let t = (['Religion', 'Géographie', 'Histoire', 'Sport', 'Arts', 'Société', 'Sciences'].indexOf(theme) !== -1)
  ? '?theme='+theme
  : ''
  try {
    const res = await axios.get('/app/api/paragraph'+t);
    console.log(res);
    if (res && res.data && typeof res.data.text === 'string') {
      return res.data
    }else {
      return false
    }
  } catch (error) {
    return false
  }
}

export async function sendQA(qas) {
  try {
    const res = await axios.post('/app/api/paragraph',qas);
    console.log(res);
    if (res && res.data) {
      return res
    }else {
      return false
    }
  } catch (error) {
    console.error(error);
    return false
  }
}

export async function getUserDetails() {
  try {
    const res = await axios.get('/app/me');
    console.log(res);
    if (res && res.data && typeof res.data.email === 'string') {
      return res.data
    }else {
      return false
    }
  } catch (error) {
    return false
  }
}
