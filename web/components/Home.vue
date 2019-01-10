<template>
    <div>
        <garage-list></garage-list>
    </div>
</template>

<script>
    import GarageList from './garagelist.vue'

    export default {
        name: "Home",
        data () {
            return {
                msg: 'Welcome to Your Appengine/Vue app the garage'
            }
        }, 
        components: {
            GarageList
        }
    }
</script>

<style scoped>

</style>