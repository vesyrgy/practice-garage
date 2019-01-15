<template>
    <div class="col-xs-12 col-sm-12 col-md-12 col-lg-12">
        <div class="row">
            <h5>{{formType}} Car</h5>
        </div>
        <form class="addCarForm form-group">
            <div class="row">
                <label for="naam">Naam</label>
                <input id="naam" v-model='cname' type="text" class="form-control" placeholder="Naam">
                <label for="merk">Merk</label>
                <input id="merk" v-model='cbrand' type="text" class="form-control" placeholder="Merk">
                <label for="kenteken">Kenteken</label>
                <input id="kenteken" v-model='ckenteken' type="text" class="form-control" placeholder="Kenteken">
                <label for="color">Kleur</label>
                <input id="color" v-model='ccolor' type="text" class="form-control" placeholder="Kleur"> 
            </div>
            <div class="row">
                <span>
                    <button type="button" class="left btn btn-default btn-secondary" id="cancel" @click="$emit('hideForm')">Cancel</button>
                </span>
                <span>
                    <button v-if="formType == 'Add'" type="button" class="btn btn-default btn-primary" id="addCar" @click='addCar()'>{{formType}}</button> 
                    <button v-if="formType == 'Save'" type="button" class="btn btn-default btn-primary" id="saveGarage" @click='saveCar()'>{{formType}}</button> 
                </span>
            </div>
        </form>
    </div>
</template>


<script>
    export default {
        name: 'car-form',
        props: {
            formType: String, 
            id: [Number, String],
            name: { type: String, default: '' },
            brand: { type: String, default: '' },
            kenteken: { type: String, default: '' },
            color: { type: String, default: '' },
            garage: [Number, String],
            gname: String,
        },
        data: function() {
            return {
                cname: this.name,
                cbrand: this.brand,
                ckenteken: this.kenteken,
                ccolor: this.color,

            }
        },
        methods: {
            addCar: function() {
                var self = this
                self.$emit('hideForm')
                self.loading = true
                $.when($.ajax({
                    method: 'POST',
                    url: '/garages/'+self.gid+'/cars',
                    data: { name: self.cname, brand: self.cbrand, kenteken: self.ckenteken, color: self.ccolor, garageId: self.garage },
                    timeout: 60000,
                    success: function(data) {
                        self.data = data
                    }
                })).done((data) => {
                    console.log("id of new car: " + data.id)
                }).then((data) => {
                    self.$router.go({ name: 'garage', params: { id: self.garage }})
                    // setTimeout(function() {self.$router.push({ name: 'garage', params: { id: self.garage }}), 200)
                }).always(() => {
                    self.loading = false
                })
            },
            saveCar: function() {
                var self = this
                self.loading = true
                $.when($.ajax({
                    method: 'PUT',
                    url: '/garages/'+self.gid+'/car/'+self.id,
                    data: { name: self.cname, brand: self.cbrand, kenteken: self.ckenteken, color: self.ckleur, garageId: self.garage },
                    timeout: 60000
                })).done((data) => {
                    console.log("car with id " + data.id + " was modified.")
                }).then((data) => {
                    // FIXME: get rid of call to $parent
                    self.$parent.getCar()
                    console.log("calling getCar()")
                    self.$emit('hideForm')
                }).always(() => {
                    self.loading = false
                });   
            
            }
            
        }
        
    }
</script>

<style>

</style>
