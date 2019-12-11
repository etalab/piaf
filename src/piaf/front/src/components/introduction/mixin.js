import axios from 'axios'

export const playMixin = {
  methods: {
    async sendScore(qas,niveau) {
      try {
        const res = await axios.post('/app/api/scoreupdate',qas,niveau);
        if (res && res.status === 201) {
          return true
        }else {
          return false
        }
      } catch (error) {
        // eslint-disable-next-line
        console.error(error);
        return false
      }
    },
  }
}
