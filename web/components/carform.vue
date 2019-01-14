<template>
    <div>
        <div class="row">
            <h5>{{formType}} Car</h5>
        </div>
        <form class="addCarForm form-group">
            <div class="row">
                <label for="naam">Naam</label>
                <input id="naam" v-model='name' type="text" class="form-control" placeholder="Naam">
                <label for="merk">Merk</label>
                <input id="merk" v-model='brand' type="text" class="form-control" placeholder="Merk">
                <label for="kenteken">Kenteken</label>
                <input id="kenteken" v-model='kenteken' type="text" class="form-control" placeholder="Kenteken">
                <label for="color">Kleur</label>
                <input id="color" v-model='color' type="text" class="form-control" placeholder="Kleur"> 
            </div>
            <div class="row">
                <span>
                    <button type="button" class="left btn btn-default btn-secondary" id="cancel" @click="$emit('hideCarForm')">Cancel</button>
                </span>
                <span>
                    <button v-if="formType == 'Add'" type="button" class="btn btn-default btn-primary" id="addCar" @click='addCar()'>{{formType}}</button> 
                    <button v-if="formType == 'Save'" type="button" class="btn btn-default btn-primary" id="saveGarage" @click='saveCar()'>{{formType}}</button> 
                </span>
            </div>
        </form>

        <!-- <form class="editCarForm" v-if="edit">
            <label for="naam">Naam Label</label>
            <input id="naam" v-model='cname' type="text" class="form-control" v-bind:placeholder="cname">
            <label for="merk">Merk</label>
            <input id="merk" v-model='cbrand' type="text" class="form-control" v-bind:placeholder="cbrand">
            <label for="kenteken">Kenteken</label>
            <input id="kenteken" v-model='ckenteken' type="text" class="form-control" v-bind:placeholder="ckenteken">
            <label for="color">Kleur</label>
            <input id="color" v-model='ckleur' type="text" class="form-control" v-bind:placeholder="ckleur"> 
            <div class="btn-group">
                <button type="button" class="left btn btn-default btn-secondary modal-default-button" id ="cancel" v-on:click='edit=false'>Cancel</button>
                <button type="button" class="right btn btn-default btn-primary" id="save" v-on:click='saveCar()'>Opslaan</button> 
            </div>
        </form> -->

    </div>
</template>


<script>
    export default {
        name: 'car-form',
        props: {
            formType: String, 
            id: [Number, String],
            name: String,
            brand: String,
            kenteken: String,
            color: String,
            garage: [Number, String],
            gname: String
        },
        data: {
            
        },
        methods: {
            addCar: function() {
                var self = this
                self.hideForm()
                self.loading = true
                $.when($.ajax({
                    method: 'POST',
                    url: '/garages/'+self.gid+'/cars',
                    data: { name: self.cname, brand: self.cbrand, kenteken: self.ckenteken, color: self.ccolor, garageId: self.gid },
                    timeout: 60000,
                    success: function(data) {
                        self.data = data
                    }
                })).done((data) => {
                    self.data = data
                    console.log("id of new car: " + data.id)
                }).then((data) => {
                    self.getlist();
                    // setTimeout(function() {self.getList()}, 200)
                }).always(() => {
                    self.loading = false
                })
            }
            
        }
        
    }
</script>

<style>

</style>
