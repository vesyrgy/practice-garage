<template>
    <div id="app">
        <nav class="nav navbar navbar-header">
            <router-link to="/">Home</router-link>
            <router-link to="/garages">Garages</router-link>
            <!-- <router-link to="/cars">Cars</router-link> -->
        </nav>
        <router-view/>
    </div>
</template>

<script>
    export default {
      name: 'app'
    }
</script>

<style>
    #app {
      font-family: 'Avenir', Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-align: center;
      color: #2c3e50;
      margin-top: 60px;
      display: grid;
      grid-column-gap: 10px;
      grid-template-columns: 20% 60% 20%;
      grid-template-areas: 
        'nav nav nav'
        'left main right'
        'footer footer footer';

    }
    .left {
        grid-area: left;
    }
    .right {
        grid-area: right;
    }
</style>
