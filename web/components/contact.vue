<template>
    <div class="contact col-xs-12 col-sm-12 col-md-12 col-lg-12">
        
        <div v-if="contact" class="row">
            Contact: <router-link>{{contact.naam}}</router-link>
        </div>
        <div v-else class="row">
            <button type="button" class="btn btn-default btn-primary">Contact Toevoegen</button>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'contact',
        props: ['contact'],
        data: function() {
            return {
            }
        },
        methods: {
            getContact: function(id) {
                
            }
        }

    }
</script>

<style>

</style>

