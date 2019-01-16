<template>
    <div class="car col-xs-12 col-sm-12 col-md-12 col-lg-12">
        <div class="row">
            <router-link v-bind:to="{ name: 'garage', params: { id: gid }}">Terug naar de Garage</router-link>
        </div>
        <div v-if="showCarForm==false" class="row">
            <h4>Naam: {{cname}}</h4>
            <h4>Merk: {{cbrand}}</h4>
            <h4>Kenteken: {{ckenteken}}</h4>
            <h4>Kleur: {{ckleur}}</h4>
            <p>Deze auto heeft id: {{cid}}</p>
        </div>
        <div v-if="contact" class="row" >
            Contact id: <router-link v-bind:to="{ name: 'contact', params: { key: contact, car_id: cid, gid: gid, ftype: 'Save' }}">{{ contact }}</router-link>
        </div>
        <div v-else class="row">
            Deze auto heeft nog geen contact. <router-link v-bind:to="{ name: 'contact', params: { key: contact, car_id: cid, gid: gid, ftype: 'Add' }}">Contact toevoegen?</router-link>
        </div>
        
        <div class="row form-group">
            <contact v-if="showContact" :contact_id="contact" :car_id="cid" :showForm="true"></contact>
        </div>
        <div v-if="showCarForm==false" class="row form-group">
            <button type="button" class="btn btn-default btn-danger" id="delete" @click='deleteCar()'>Auto Verwijderen</button> 
            <button type="button" class="btn btn-default btn-primary" id="editGarage" @click="showCarForm=true">Auto Bewerken</button>
        </div>

        <div class="row form-group">
            <car-form v-if="showCarForm" v-bind="cData" @hideForm="showCarForm=false" :formType="fType"></car-form>
        </div>
    </div>

</template>

<script>
    import CarForm from './carform.vue'
    import Contact from './contact.vue'

    export default {
        name: 'car',
        data: function() {
            return {
                showCarForm: false,
                showContact: false,
                cData: {},                
                cid: this.$route.params.id,
                cname:'',
                cbrand:'',
                ckenteken:'',
                ckleur: '',
                contact: '',
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
                    url:`/garages/${self.gid}/car/${self.cid}`,
                    success: function(data) {
                        console.log("car gotten")
                    }
                })).done((data) => {
                    self.cname = data.name
                    self.cbrand = data.brand
                    self.ckenteken = data.kenteken
                    self.ckleur = data.color
                    self.contact = data.contact
                }).then((data) => {
                    self.cData = data
                }).always(() => {
                    self.loading = false
                })
            },
            deleteCar: function() {
                var self = this
                self.loading = true
                $.when($.ajax({
                    method: 'DELETE',
                    url: `/garages/${self.gid}/car/${self.cid}`,
                    timeout: 60000
                })).done((returned) => {
                    console.log(`car DELETE request returned: ${returned.id}`)
                }).then((data) => {
                    var id = self.gid
                    if (id == undefined) {
                        console.log(`id is ${id}`)
                        id = self.$route.params.gid
                        console.log(`is is not ${id}`)
                    }
                    console.log(`calling 'cars' with id: ${id}`)
                    // self.$router.go({ name: 'cars', params: {id} })
                    // blijkbaar werkt dit niet goed zonder eventjes te wachten
                    setTimeout(function() {self.$router.push(`/garages/${id}`)}, 200)
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
            'car-form': CarForm,
            'contact': Contact
        }
    }
</script>

<style>

</style>
