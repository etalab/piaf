module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],
  "filenameHashing": false,
  css: {
    extract: {
      filename: '[name].css',
      chunkFilename: '[name].css',
      ignoreOrder: true,
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
    : (process.env.NODE_ENV === 'development')
      ? '/'
      : '/static/front/',
}
