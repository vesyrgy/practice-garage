<template>
    <div class="contact col-xs-12 col-sm-12 col-md-12 col-lg-12">
        <div class="row"> 
            <router-link v-if="gid" v-bind:to="{ name: 'garage', params: { id: gid }}">Terug naar de Garage</router-link> 
            <span v-if="car_id">/</span> 
            <router-link v-if="car_id" v-bind:to="{ name: 'car', params: { gid: gid, id: car_id}}">Terug naar de Auto</router-link>
        </div>
        
        <div class="row form-group">
            <h4>{{contactData.naam}}</h4>
            <h4>{{contactData.straat}} {{contactData.huisnummer}}</h4>
            <h4>{{contactData.postcode}} {{contactData.plaats}}</h4>        
        </div>
        <div class="row form-group">
            <contact-form v-if="showContactForm" :car_id="car_id" :c-data-prop="contactData" @hideForm="showContactForm=false" @changeData="updateFrom(new_data)"></contact-form>
        </div>
        <div v-if="showContactForm==false" class="row form-group">
            <button type="button" class="btn btn-default btn-danger" id="deleteContact" @click='deleteContact()'>Contact Verwijderen</button> 
            <button type="button" class="btn btn-default btn-primary" id="editContact" @click="showContactForm=true">Contact Bewerken</button>
        </div>
        <div class="row ">
            <!-- TODO: auto's van de contact weergeven -->
            <!-- <carlist></carlist> -->
        </div>
    </div>
</template>

<script>
    import ContactForm from './contactform.vue'
    import CarList from './carlist.vue'

    export default {
        name: 'contact',
        props: {
            showForm: Boolean
        },
        data: function() {
            return {
                fType: this.$route.params.ftype,
                showContactForm: false,
                expandContact: false,
                contactData: {
                    naam: '',
                    straat: '',
                    huisnummer: '',
                    postcode: '',
                    plaats: '',
                    id: ''
                }, 
                car_id: this.$route.params.car_id,
                gid: this.$route.params.gid,
                contact_id: this.$route.params.key
            }
        },
        methods: {
            getContact: function() {
                console.log(`getContact called with key: ${this.contact_id}`)
                var self = this
                self.loading = true
                $.when($.ajax({
                    method: 'GET',
                    //  TODO: decide which url to use
                    url:`/contacts/${self.$route.params.key}`,
                    success: function(data) {
                        console.log(`contact with id: ${data.id} gotten`)
                    }
                })).done((data) => {
                    // self.naam = data.naam
                    // self.cbrand = data.brand
                    // self.ckenteken = data.kenteken
                    // self.ckleur = data.color
                    self.contactData = data
                }).then((data) => {
                    // self.contactData = data

                }).always(() => {
                    self.loading = false
                })
            },
            deleteContact: function() {
                
                var self = this
                self.loading = true
                $.when($.ajax({
                    method: 'DELETE',
                    url: `/contacts/${self.contact_id}`,
                    timeout: 60000
                })).done((returned) => {
                    console.log(`contact DELETE request returned: ${returned}`)
                }).then((data) => {
                    
                    console.log(`Going back to Garage ${self.gid}`)
                    self.$router.go({ name: 'garage', params: {gid: self.gid} })
                    // blijkbaar werkt dit niet goed zonder eventjes te wachten
                    // setTimeout(function() {self.$router.push(`/garages/${id}`)}, 200)
                }).always(() => {
                    self.loading = false
                });
            },
            toggleContact: function() {
                console.log("toggling Contact")
                if (this.expandContact == false)
                    this.expandContact = true
                else {
                    this.expandContact = false
                }
            },
            updateFrom: function(cData) {
                this.contactData = cData
            }

        },
        created() {
            if (this.$route.params.fType == "Save")
                this.getContact()
            else
                this.showContactForm = true
        },
        mounted() {
            
        },
        components: {
            'contact-form': ContactForm,
            'carlist': CarList
        }

    }
</script>

<style>

</style>

