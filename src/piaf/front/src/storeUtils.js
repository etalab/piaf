import axios from 'axios'

export async function getNewParagraph() {
  try {
    const res = await axios.get('/app/api/paragraph');
    console.log(res);
    if (res && res.data && typeof res.data.name === 'string') {
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
