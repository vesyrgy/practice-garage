<template>
    <div class="garage col-xs-12 col-sm-12 col-md-12 col-lg-12">
        <div class="row">
            <router-link class="row" v-bind:to="{ name: 'garages'}">Terug naar de garages</router-link>
        </div>
        <div v-if="showGarageForm==false" class="row">
                <h3>Garage: {{gname}}</h3>
                <p>Id: {{gid}}</p>
                <h4>Merk: {{garageData.brand}}</h4>
                <h4>Land: {{gpostal}}</h4>
                <car-list :carlist="carList" :gid="gid" :gname="gname" :showCarForm="showCarForm" @showCarForm="showCarForm = $event" @hideForm="showCarForm = false"></car-list>
        </div>
        <div v-if="showGarageForm==false && showCarForm==false" class="row">
                
            <button type="button" class="btn btn-default btn-danger" id="delete" @click='deleteGarage()'>Garage Verwijderen</button> 
            <button type="button" class="btn btn-default btn-primary" id="editGarage" @click='showGarageForm=true'>Garage Bewerken</button>
        </div>
        <div v-if="showGarageForm">
            <garage-form :gid="gid" :gDataProp="garageData" @childWasChanged="updateGarage($event)" :formType="fType" :showFormProp="showGarageForm" @formVisibilityChanged="showGarageForm = $event">
            </garage-form>
        </div>
    </div>
</template>

<script>
    import carList from './carlist.vue'
    import GarageForm from './garageform.vue'

    export default {
        name: 'garage',
        data: function() {
            return {
                gid: this.$route.params.id,
                gname: '',
                gbrand: '',
                gpostal: '',
                garageData: {},
                carList: [], 
                showCarForm: false,
                showGarageForm: false,
                fType: 'Save'
            }
        },
        methods: {
            showGarage: function(id) {
                console.log("showGarage called")
                var self = this
                $.when($.ajax({
                    method: 'GET',
                    url:'/garages/'+id,
                    success: function(data) {
                        console.log("success")
                        self.updateGarage(data)
                        self.carList = data.cars
                        // self.gname = data.name
                        // self.gbrand = data.brand
                        // self.gpostal = data.postal_country
                    }
                })).done((data) => {
                    
                });

            },
            deleteGarage: function() {
                var self = this
                self.loading = true
                $.when($.ajax({
                    method: 'DELETE',
                    url: '/garages/'+self.gid,
                    timeout: 60000,
                    success: function(data) {
                        console.log("DELETE was successful.")
                    }
                })).done((returned) => {
                    console.log("garages DELETE request returned: " + returned.id)
                }).then((data) => {
                    self.gid = ''
                    console.log("calling this.$router.go({ name: 'garages'})")
                    // self.$router.push({ name: 'garages' })

                    // blijkbaar gaat het soms mis met de update als je niet even wacht :\
                    setTimeout(function() {self.$router.push("/garages")}, 200)
                }).always(() => {
                    self.loading = false
                });
            },
            updateGarage: function(event) {
                console.log("update garage called")
                this.garageData = event
                
                this.gname = event.name
                this.gbrand = event.brand
                this.gpostal = event.postal_country
                // console.log("garageData.name: " + this.gname)
            }
            
        }, 
        created() {
            // console.log("garage created")
            this.gid = this.$route.params.id
            this.showGarage(this.gid)
        }, 
        components: {
            carList,
            'garage-form': GarageForm
        }  

    }
</script>

<style>
    /* .garageView {
        grid-area: main;
    } */
</style>

