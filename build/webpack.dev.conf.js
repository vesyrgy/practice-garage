var webpack = require('webpack')
const path = require('path');

function resolve (dir) {
  return path.join(__dirname, '..', dir)
}

module.exports = {
    watch: true,
    entry: {
        home: './web/home.js'
    },
    output: {
        // Make sure to use [name] or [id] in output.filename
        //  when using multiple entry points
        filename: "[name].js",
        chunkFilename: "[name].chunk.js",
        path: resolve("/static/dist")
    },
    plugins: [
        new webpack.ProvidePlugin({
            '$': 'jquery',
            'jQuery': 'jquery'
        })
    ],
    resolve: {
      alias: {
        vue: 'vue/dist/vue.js'
      }
    },
    module: {
        rules: [
          {
            test: /\.js$/,
            use: {
                loader: 'babel-loader',
                options: {
                  presets: ['env']
                }
            }
          },
          {
            test: /\.vue$/,
            loader: 'vue-loader'
          }
        ]
    }
};