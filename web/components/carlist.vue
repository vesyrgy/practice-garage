<template>
    <div v-bind:addCar="addCar">
        <div v-if="showCarForm == false" class="row">
            <h4>Auto's</h4>
        </div>
        <div v-if="showCarForm == false" class="row">
            <!-- <garage-form v-bind:formType="fType" v-bind:showFormProp="showGarageForm" @formVisibilityChanged="showGarageForm = $event"></garage-form>     -->
            <button type="button" class="btn btn-default btn-primary" id="addCar" @click='showCarForm=true'>Auto Toevoegen</button>
        </div>
        <div v-if="showCarForm == false" id="car-list" class="row">
            <ul class="list-group">
            <li class="car-item" v-for="(c, index) in carList" :key="index">
                <span class="col-1">
                    <!-- {{c.id}}:  -->
                </span>
                <span class="col-2">
                    <router-link class="list-group-item" v-bind:to="{ name: 'car', params: { gid: gid, id: c.id }}">{{ c.name }}</router-link>
                </span>
            </li>
            </ul>
        </div>
        <div v-if="showCarForm == true" class="row">
            <car-form @hideCarForm="showCarForm=false" :formType="fType"></car-form>
        </div>
    </div>
</template>

<script>
    import CarForm from './carform.vue'

    export default {
        name: 'car-list',
        props: ['showCarForm', 'gname', 'gid'],
        data: function() {
            return {
                hover: true,
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
                        console.log("carlist gotten")
                        console.log("data on success: " + JSON.stringify(returned))
                    }
                })).done((returned) => {
                    console.log("data on done: " + JSON.stringify(returned))
                    // self.carList = returned
                }).then((returned) => {
                    console.log("data on then: " + JSON.stringify(returned))
                    self.carList = returned
                }).always(() => {
                    self.loading = false
                })
            }, 
            addCar: function() {
                var self = this
                self.hideForm()
                self.loading = true
                $.when($.ajax({
                    method: 'POST',
                    url: '/garages/'+self.gid+'/cars',
                    data: { name: self.cname, brand: self.cbrand, kenteken: self.ckenteken, color: self.ccolor, garageId: self.gid },
                    timeout: 60000,
                    success: function(data) {
                        self.data = data
                    }
                })).done((data) => {
                    self.data = data
                    console.log("id of new car: " + data.id)
                }).then(
                    setTimeout(function() {self.getList()}, 200)
                ).always(() => {
                    self.loading = false
                })
            }
        },
        beforeMount: function() {
            this.getList()
            console.log("beforeMount of carlist")
            console.log("carlist is: " + JSON.stringify(this.carlist))
        },
        mounted: function() {
            console.log("carlist mounted")
            // setTimeout(function() {this.getList()}, 100)
        },
        components: {
            'car-form': CarForm
        }
    }
</script>

<style>
    /* .car-item:hover{
        color: white;
        background-color: gray;
    } */
    
</style>
