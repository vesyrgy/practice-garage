<template>
    <div class="contact col-xs-12 col-sm-12 col-md-12 col-lg-12">
        
        <div v-if="contact_id" class="row">
            Contact: <router-link v-bind:to="{ name: 'contact', params: {key: contact_id}}">{{contact_id}}</router-link>
        </div>
        <div v-else class="row">
            Deze auto heeft nog geen contact.
            <button v-if="showContactForm==false" type="button" class="btn btn-default btn-primary" @click="showContactForm=true">Contact Toevoegen</button>
        </div>
        <div class="row form-group">
            <contact-form v-if="showContactForm==true" :car_id="car_id" :c-data-prop="contactData" :form-type="fType" @hideForm="showContactForm=false" @changeData="updateFrom(new_data)"></contact-form>
        </div>
    </div>
</template>

<script>
    import ContactForm from './contactform.vue'

    export default {
        name: 'contact',
        props: {
            car_id: [String, Number],
            contact_id: [String, Number]
        },
        data: function() {
            return {
                fType: "Add",
                showContactForm: false,
                contactData: {
                    naam: '',
                    straat: '',
                    huisnummer: '',
                    postcode: '',
                    plaats: '',
                    id: ''
                }
            }
        },
        methods: {
            getContact: function(id) {
                var self = this
                self.loading = true
                $.when($.ajax({
                    method: 'GET',
                    //  TODO: decide which url to use
                    url:`/contacts/${self.gid}`,
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
            updateFrom: function(cData) {
                this.contactData = cData
            }

        },
        components: {
            'contact-form': ContactForm
        }

    }
</script>

<style>

</style>

