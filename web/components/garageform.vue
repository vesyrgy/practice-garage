<template>
    <div>
        <div class="row">
            <h5>{{formType}} Garage</h5>
        </div>
        <div class="row">
            <form class="GarageForm form-group">
                <div class="row">
                    <label for="naam">Naam</label>        
                    <input v-model='gDataProp.name' v-on:input="updateParent()" type="text" class="form-control" placeholder="Enter Name"><slot name="gname"></slot>
                    <label for="merk">Merk</label> 
                    <input v-model='gDataProp.brand' v-on:input="updateParent()" type="text" class="form-control" placeholder="Enter Brand"><slot name="gbrand"></slot>
                    <label for="land">Land</label> 
                    <input v-model='gDataProp.postal_country' v-on:input="updateParent()" type="text" class="form-control" placeholder="Enter Postal Country"><slot name="gpostal"></slot> 
                </div>
                <div class="row">
                    <span>  
                        <button type="button" class="btn btn-default btn-secondary modal-default-button" id ="cancel" :value="showFormProp" v-on:click="hideForm">Cancel</button>  
                    </span>
                    <span>    
                        <button v-if="formType == 'Add'" type="button" class="btn btn-default btn-primary" id="addGarage" v-on:click='addGarage()'>{{formType}}</button> 
                        <button v-if="formType == 'Save'" type="button" class="btn btn-default btn-primary" id="addGarage" v-on:click='saveGarage()'>{{formType}}</button> 
                    </span>
                </div>
            </form>
        </div>
    </div>
    
</template>

<script>

export default {
    name: 'garage-form',
    props: {
        gid: [Number, String],
        showFormProp: Boolean,
        formType: String, 
        gDataProp: {
            type: Object,
            default: function() {
                return {
                    name: '',
                    brand: '',
                    postal_country: ''
                }
            }
        }
    }, 
    data: function() {
        return {
            formVisible: false,
            formChanged: false
        }
    }, 
    unchanged: null,
    methods: {
        addGarage: function() {
            var self = this
            self.loading = true
            $.when($.ajax({
                method: 'POST',
                url: '/garages',
                data: { name: self.gDataProp.name, brand: self.gDataProp.brand, postal_country: self.gDataProp.postal_country },
                timeout: 60000,
                success: function(returned) {  
                    console.log("addGarage POST request returned garage with id: " + returned.id)
                    // self.garagelist.push(returned)
                    // self.getList()
                }
            })).done((data) => {
                this.hideForm()
            }).then((data) => {
                this.$router.go({ name: 'garages'})
                // blijkbaar werkt dit soms niet zonder even te wachten :\
                // setTimeout(function() {self.$router.push("/garages");}, 200)
            }).always(() => {
                self.loading = false
            })
                
        }, 
        saveGarage: function() {
            var self = this
            self.loading = true
            $.ajax({
                method: 'PUT',
                url: '/garages/'+self.gid,
                data: { name: self.gDataProp.name, brand: self.gDataProp.brand, postal_country: self.gDataProp.postal_country },
                timeout: 60000
            }).then((data) => {
                this.$options.unchanged = data
                // self.hideForm()
                console.log("hiding form...")
                self.hideForm()
                console.log("calling self.$parent.showGarage() with " + self.gid)
                self.$parent.showGarage(self.gid)
                
            }).always(() => {
                self.loading = false
            });   
        },
        updateParent(event) {
            this.formChanged = true
            console.log("updateParent was called. this.gDataProp is: "+JSON.stringify(this.gDataProp))
            var valObj = this.gDataProp
            this.$emit('childWasChanged', valObj)
            
        },
        hideForm(event) {
            this.formVisible = false
            this.$emit('formVisibilityChanged', this.formVisible)
            // if(formChanged == true) {

            // }
        },
        initForm: function() {
            var self = this
            console.log("formType is " + self.formType)
            if(this.formType == 'Add') {
                
            }
            else if (this.formType == 'Save') {
                console.log("formType is " + self.formType)
                this.$options.unchanged = this.gDataProp
                // self.gname = self.gDataProp.name
                // self.gbrand = self.gDataProp.brand
                // self.gpostal = self.gDataProp.postal_country
            }
        }
    },
    mounted: function() {
        console.log("garageform mounted")
        this.initForm()
    }
}
</script>

<style>
    

</style>
