var webpack = require('webpack')
const path = require('path');

function resolve (dir) {
  return path.join(__dirname, '..', dir)
}

module.exports = {
    context: resolve("/"),
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
    ]
};