<template>
    <div>
        <div v-if="showCarForm==false" class="row">
            <router-link >Terug naar de garage</router-link>
            <router-link v-bind:to="{ name: 'garage', params: { id: gid }}">Terug naar de garage</router-link>
            <h4>Naam: {{cname}}</h4>
            <h4>Merk: {{cbrand}}</h4>
            <h4>Kenteken: {{ckenteken}}</h4>
            <h4>Kleur: {{ckleur}}</h4>
            <p>Deze auto heeft id: {{cid}}</p>
        </div>
        <div v-if="showCarForm==false" class="row">
            <button type="button" class="btn btn-default btn-danger" id="delete" @click='deleteCar()'>Verwijderen</button> 
            <button type="button" class="btn btn-default btn-primary" id="editGarage" @click="showCarForm=true">Bewerken</button>
        </div>

        <div class="row">
            <car-form v-bind="cData" v-if="showCarForm==true" @hideCarForm="showCarForm=false" :formType="fType"></car-form>
            <!-- <garage-form :gid="gid" :gDataProp="garageData" @childWasChanged="updateGarage($event)" :formType="fType" :showFormProp="showGarageForm" @formVisibilityChanged="showGarageForm = $event"> -->
        </div>
    </div>

</template>

<script>
    import CarForm from './carform.vue'

    export default {
        name: 'car',
        data: function() {
            return {
                showCarForm: false,
                cData: {},                
                cid: this.$route.params.id,
                cname:'',
                cbrand:'',
                ckenteken:'',
                ckleur: '',
                gid: this.$route.params.gid,
                fType: 'Save'
            }
        }, 
        methods: {
            getCar: function() {
                var self = this
                self.loading = true
                $.when($.ajax({
                    method: 'GET',
                    url:'/garages/'+self.gid+'/car/'+self.cid,
                    success: function(data) {
                        console.log("car gotten")
                    }
                })).done((data) => {
                    self.cname = data.name
                    self.cbrand = data.brand
                    self.ckenteken = data.kenteken
                    self.ckleur = data.color
                }).then((data) => {
                    self.cData = data
                }).always(() => {
                    self.loading = false
                })
            },
            saveCar: function() {
                var self = this
                self.loading = true
                $.when($.ajax({
                    method: 'PUT',
                    url: '/garages/'+self.gid+'/car/'+self.cid,
                    data: { name: self.cname, brand: self.cbrand, kenteken: self.ckenteken, color: self.ckleur, garageId: self.gid },
                    timeout: 60000
                })).done((data) => {

                }).then((data) => {
                    self.showCarForm = false;
                    // self.cData = data
                    console.log("calling getCar()")
                    self.getCar()
                }).always(() => {
                    self.loading = false
                });   
            
            },
            deleteCar: function() {
                var self = this
                self.loading = true
                $.ajax({
                    method: 'DELETE',
                    url: '/garages/'+self.gid+'/car/'+self.cid,
                    timeout: 60000
                }).done((returned) => {
                    console.log("car DELETE request returned: " + returned.id)
                }).then((data) => {
                    var id = self.gid
                    if (id == undefined) {
                        console.log("id is " + id)
                        id = self.$route.params.gid
                        console.log("id changed to " + id)
                    }
                    console.log("calling 'cars' with id: " + id)
                    // self.$router.push({ name: 'cars', params: {id} })
                    setTimeout(function() {self.$router.push("/garages/"+id);}, 100)
                }).always(() => {
                    self.loading = false
                });
            }
        },
        beforeMount() {
            this.getCar()
        },
        mounted() {
            console.log("car mounted")
        },
        components: {
            'car-form': CarForm
            // editObject
        }
    }
</script>

<style>

</style>
