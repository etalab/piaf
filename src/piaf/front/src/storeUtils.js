export async function getNewParagraph() {
  try {
    const res = await axios.get('/app/api/paragraph');
    console.log(res);
    if (res && res.data && res.data.text) {
      return res
    }else {
      return false
    }
  } catch (error) {
    console.error(error);
    return false
  }
}

export async function sendQA(data) {
  try {
    const res = await axios.post('/app/api/paragraph',data);
    console.log(res);
    if (res && res.data && res.data.text) {
      return res
    }else {
      return false
    }
  } catch (error) {
    console.error(error);
    return false
  }
}
