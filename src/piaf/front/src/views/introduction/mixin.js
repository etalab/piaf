import axios from 'axios'

export const playMixin = {
  created: function () {
    this.hello()
  },
  methods: {
    hello: function () {
      console.log('hello from mixin!')
    },
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
