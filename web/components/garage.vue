<template>
    <div class="garage">
        <div v-if="!showGarageForm" class="row">
                <h3>Garage: {{gname}}</h3>
                <p>Deze garage heeft id: {{gid}}</p>
                <h4>Merk: {{garageData.name}}</h4>
                <h4>Land: {{gpostal}}</h4>
                <car-list :carlist="carList" :gid="gid" :gname="gname" :showCarForm="showCarForm" @hideForm="showCarForm = $event"></car-list>
        </div>
        <div class="row">
                
            <button type="button" class="btn btn-default btn-danger" id="delete" @click='deleteGarage()'>Verwijderen</button> 
                
            <button type="button" class="btn btn-default btn-primary" id="editGarage" @click='showGarageForm=true'>Bewerken</button>
                
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
                var self = this
                $.ajax({
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
                }).done((data) => {

                });

            },
            deleteGarage: function() {
                var self = this
                self.loading = true
                $.ajax({
                    method: 'DELETE',
                    url: '/garages/'+self.gid,
                    timeout: 60000
                }).done((returned) => {
                    console.log("garages DELETE request returned: " + returned.id)
                }).then((data) => {
                    // self.$router.push("/garages")
                    // blijkbaar gaat het mis met de update als je niet even wacht :\
                    setTimeout(function() {self.$router.push("/garages");}, 200)
                }).always(() => {
                    self.loading = false
                });
            },
            updateGarage: function(event) {
                console.log("update garage called")
                this.garageData = event
                console.log("event.name: " + event.name)
                this.gname = event.name
                this.gbrand = event.brand
                this.gpostal = event.postal_country
            }
            
        }, 
        mounted(){
            console.log("garage mounted")
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

