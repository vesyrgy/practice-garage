<template>
    <div class="garage">
        <h3>Garage: {{gname}}</h3>
        <p>Deze garage heeft id: {{gid}}</p>

        <div class="garageView" v-if="!edit">
            <h4>Merk: {{gbrand}}</h4>
            <h4>Land: {{gpostal}}</h4>
            <car-list :carlist="carList" :gid="gid" :gname="gname" :showCarForm="showCarForm" @hideForm="showCarForm = $event"></car-list>
            <div class="btn-group">
                <button type="button" class="btn btn-default btn-secondary" id="addCar" v-on:click='showCarForm=true'>Auto Toevoegen</button>
                <button type="button" class="btn btn-default btn-primary" id="editGarage" v-on:click='edit=true'>Bewerken</button>
                <button type="button" class="btn btn-default btn-danger" id="delete" v-on:click='deleteGarage()'>Verwijderen</button> 
            </div>

        </div>

        <form class="editGarageForm" v-if="edit">
            <label for="naam">Naam</label>
            <input id="naam" v-model='gname' type="text" class="form-control" v-bind:placeholder="garageData.name">
            <label for="merk">Merk</label>
            <input id="merk" v-model='gbrand' type="text" class="form-control" v-bind:placeholder="garageData.brand">
            <label for="land">Land</label>
            <input id="land" v-model='gpostal' type="text" class="form-control" v-bind:placeholder="garageData.postal_country"> 
            <div class="btn-group">
                <button type="button" class="left btn btn-default btn-secondary modal-default-button" id ="cancel" v-on:click="edit = false">Cancel</button>
                <button type="button" class="right btn btn-default btn-primary" id="save" v-on:click='saveGarage()'>Save</button> 
            </div>
        </form>


    </div>
</template>

<script>
    import carList from './carlist.vue'

    export default {
        name: 'garage',
        data: function() {
            return {
                gid: this.$route.params.id,
                edit: false,
                gname: '',
                gbrand: '',
                gpostal: '',
                garageData: {},
                carList: [], 
                showCarForm: false
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
                        self.garageData = data,
                        self.gname = data.name,
                        self.gbrand = data.brand,
                        self.gpostal = data.postal_country,
                        self.carList = data.cars
                    }
                });
            },
            saveGarage: function() {
                var self = this
                self.loading = true
                $.ajax({
                    method: 'PUT',
                    url: '/garages/'+self.gid,
                    data: { name: self.gname, brand: self.gbrand, postal_country: self.gpostal },
                    timeout: 60000
                }).then((data) => {
                    self.edit = false;
                    this.data = data
                    console.log("calling showGarage with " + self.gid)
                    self.showGarage(self.gid)
                }).always(() => {
                    self.loading = false
                });   
            },
            deleteGarage: function() {
                var self = this
                self.loading = true
                $.ajax({
                    method: 'DELETE',
                    url: '/garages/'+self.gid,
                    timeout: 60000
                }).then((data) => {
                    this.data = data
                    setTimeout(function() {self.$router.push("/garages");}, 100)
                }).always(() => {
                    self.loading = false
                });
            }
            
        }, 
        beforeMount(){
            this.gid = this.$route.params.id
            this.showGarage(this.gid)
        }, 
        components: {
            carList
        }  

    }
</script>

<style>
    .garageView {
        grid-area: main;
    }
</style>

