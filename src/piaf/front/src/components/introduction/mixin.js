import axios from 'axios'

export const playMixin = {
  data: () => ({
    networkIssueMessage: false,
    loading: false,
  }),
  methods: {
    async sendScore(qas,niveau) {
      try {
        let data = {
          "level": niveau,
          "score": qas
        }

        const res = await axios.post('/app/api/level/completed',data);
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
