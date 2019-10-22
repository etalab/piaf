module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],
  "filenameHashing": false,
  css: {
    extract: {
      filename: '[name].css',
      chunkFilename: '[name].css',
    },
  },
  configureWebpack: {
    output: {
      filename: '[name].js',
      chunkFilename: '[name].js',
    }
  },
  publicPath: process.env.WEBPACK_ENVIRONMENT_PRODUCTION === 'True'
    ? '/static/front/'
    : '/static/front/',
}
