<template>
    <div id="app" class="container-fluid">
        <div class="row">
            <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2"></div>
            <nav class="nav navbar navbar-header col-xs-8 col-sm-8 col-md-8 col-lg-8">
                <router-link to="/">Home</router-link>
                <!-- <router-link to="/garages">Garages</router-link> -->
                <!-- <router-link to="/cars">Cars</router-link> -->
            </nav>
            <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2"></div>
        </div>
        <div class="row">
            <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2"></div>
            <router-view class="col-xs-8 col-sm-8 col-md-8 col-lg-8"/>
            <div class="col-xs-2 col-sm-2 col-md-2 col-lg-2"></div>
        </div>  
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
      /* text-align: center; */
      color: #2c2e50;
      margin-top: 80px;
      display: grid;
      /* grid-column-gap: 10px;
      grid-template-columns: 20% 80% 20%;
      grid-template-areas: 
        'nav nav nav'
        'left main right'
        'footer footer footer'; */
        

    }
    .btn-primary {
        float: right;
    }
    .btn-seconday {
        float: left;
    }
    ul {
        list-style-type: none;
        padding: 0;
        margin: 0;
    }
    #cancel {
        float: left;
        clear: both;
    }
    #delete {
        float: left;
        clear: both;
    }

    /* .left {
        grid-area: left;
    }
    .right {
        grid-area: right;
    } */
    

</style>
