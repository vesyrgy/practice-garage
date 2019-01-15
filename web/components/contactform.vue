<template>
    <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
        <div class="row">
            <h5>{{formType}} Contact</h5>
        </div>
        <form class="addContactForm form-group">
            <div class="row">
                <label for="naam">Naam</label>
                <input id="naam" v-model='c_naam' type="text" class="form-control" placeholder="Naam">
                <label for="straat">Straat</label>
                <input id="straat" v-model='c_straat' type="text" class="form-control" placeholder="straat">
                <label for="huisnummer">Huisnummer</label>
                <input id="huisnummer" v-model='c_huisnummer' type="text" class="form-control" placeholder="Huisnummer">
                <label for="postcode">Kleur</label>
                <input id="postcode" v-model='c_postcode' type="text" class="form-control" placeholder="Postcode"> 
                <label for="plaats">Plaats</label>
                <input id="plaats" v-model='c_plaats' type="text" class="form-control" placeholder="Plaats"> 
            </div>
            <div class="row">
                <span>
                    <button type="button" class="left btn btn-default btn-secondary" id="cancel" @click="$emit('hideForm')">Cancel</button>
                </span>
                <span>
                    <button v-if="formType == 'Add'" type="button" class="btn btn-default btn-primary" id="addContact" @click='addContact()'>{{formType}}</button> 
                    <button v-if="formType == 'Save'" type="button" class="btn btn-default btn-primary" id="saveContact" @click='saveContact()'>{{formType}}</button> 
                </span>
            </div>
        </form>
    </div>
    
</template>

<script>
    export default {
        name: 'contact-form',
        props: {
            formType: String,
            cDataProp: {
                type: Object,
                default: function() {
                    return {
                        naam: '',
                        straat: '',
                        huisnummer: '',
                        postcode: '',
                        plaats: '',
                        id: ''
                    }
                }
            },
            car_id: [String,Number]
        },
        data: function() {
            return {
                c_naam: this.cDataProp.naam,
                c_straat: this.cDataProp.straat,
                c_huisnummer: this.cDataProp.huisnummer,
                c_postcode: this.cDataProp.postcode,
                c_plaats: this.cDataProp.plaats,
                c_id: this.cDataProp.id
            }
        },
        watch: {
            contactDataProp: function() {
                console.log("contactDataProp changed")
            },
            c_naam: function() {
                console.log("c_naam changed")
            }
        },
        methods: {
            addContact: function() {
                var self = this
                self.loading = true
                $.when($.ajax({
                    method: 'POST',
                    url: `/contacts/${self.c_id}/${self.car_id}`,
                    data: { naam: self.c_naam, straat: self.c_straat, huisnummer: self.c_huisnummer, postcode: self.c_postcode },
                    timeout: 60000
                })).done((data) => {
                    console.log(`car with id ${self.car_id} was modified.`)
                }).then((data) => {
                    // FIXME: get rid of call to $parent
                    self.$parent.getContact()
                    console.log("calling getContact() from parent")
                    self.$emit('hideForm')
                }).always(() => {
                    self.loading = false
                });
                
            },
            saveContact: function() {
                var self = this
                self.loading = true
                $.when($.ajax({
                    method: 'PUT',
                    // TODO: decide which URL to use for this
                    // url: '/garages/'+self.gid+'/car/'+self.id,
                    data: { naam: self.c_naam, straat: self.c_straat, huisnummer: self.c_huisnummer, postcode: self.c_postcode, id: self.c_id },
                    timeout: 60000
                })).done((data) => {
                    console.log(`contact with id ${data.id} was modified.`)
                }).then((data) => {
                    // FIXME: get rid of call to $parent
                    self.$parent.getContact()
                    self.$emit('hideForm')
                    self.update(data)
                }).always(() => {
                    self.loading = false
                });   
            },
            update: function(cData) {
                console.log("updating contact data")
                // var cDataKopie = $.extend(true, {}, this.cDataProp)
                // $emit('changeData', cDataKopie)
            }
            
        }
    }
</script>

<style>

</style>
