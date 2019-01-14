<template>
    <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
        <div v-if="showCarForm == false" class="row">
            <!-- <garage-form v-bind:formType="fType" v-bind:showFormProp="showGarageForm" @formVisibilityChanged="showGarageForm = $event"></garage-form>     -->
            <button type="button" class="btn btn-default btn-primary" id="addCar" @click="showCarForm=true; $emit('showCarForm')">Auto Toevoegen</button>
            <h4>Auto's ({{carList.length}}):</h4>
        </div>
        <div v-if="showCarForm == false" id="car-list" class="row">
            <ul class="list-group">
                <li class="car-item" v-for="(c, index) in carList" :key="index">
                    
                        <router-link class="list-group-item" v-bind:to="{ name: 'car', params: { gid: gid, id: c.id }}">{{ c.name }}</router-link>
                    
                </li>
            </ul>
        </div>
        <div v-if="showCarForm == true" class="row">
            <car-form @hideForm="showCarForm=false; $emit('hideForm')" :formType="fType" :gname="gname" :garage="gid"></car-form>
        </div>
    </div>
</template>

<script>
    import CarForm from './carform.vue'

    export default {
        name: 'car-list',
        props: ['gname', 'gid'],
        data: function() {
            return {
                carList: {},
                carData: {},
                showCarForm: false,
                fType: 'Add'
            }
        },
        methods: {
            getList: function() {
                var self = this
                var id = self.gid
                self.loading = true
                if (id == undefined) {
                    console.log("id is " + id)
                    id = self.$route.params.id
                    console.log("id changed to " + id)
                }
                $.when($.ajax({
                    method: 'GET',
                    url:'/garages/'+id+'/cars',
                    success: function(returned) {
                        // console.log("carlist gotten")
                        // console.log("data on success: " + JSON.stringify(returned))
                    }
                })).done((returned) => {
                    // console.log("data on done: " + JSON.stringify(returned))
                    // self.carList = returned
                }).then((returned) => {
                    // console.log("data on then: " + JSON.stringify(returned))
                    self.carList = returned
                }).always(() => {
                    self.loading = false
                })
            }
        },
        beforeMount: function() {
            this.getList()
            // console.log("beforeMount of carlist")
            // console.log("carlist is: " + JSON.stringify(this.carlist))
        },
        mounted: function() {
            // console.log("carlist mounted")
            // setTimeout(function() {this.getList()}, 100)
        },
        components: {
            'car-form': CarForm
        }
    }
</script>

<style>
    
</style>
