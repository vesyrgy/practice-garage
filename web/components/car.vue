<template>
    <div>
        <h4>Naam: {{cname}}</h4>
        <h4>Merk: {{cbrand}}</h4>
        <h4>Kenteken: {{ckenteken}}</h4>
        <h4>Kleur: {{ckleur}}</h4>
        <p>Deze auto heeft id: {{cid}}</p>
        
        <div v-if="!edit" class="btn-group">
            <button type="button" class="btn btn-default btn-danger" id="delete" v-on:click='deleteCar()'>Verwijderen</button> 
            <button type="button" class="btn btn-default btn-primary" id="editGarage" v-on:click='edit=true'>Bewerken</button>
        </div>
    
        <form class="addCarForm" v-if="edit">
            <label for="naam">Naam</label>
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
        </form>

        <!-- <editObject></editObject> -->
    
    </div>

</template>

<script>
    export default {
        name: 'car',
        data: function() {
            return {
                edit: false,
                cname:'',
                cbrand:'',
                ckenteken:'',
                ckleur: '',
                cid: this.$route.params.id,
                gid: this.$route.params.gid
            }
        }, 
        methods: {
            getCar: function() {
                var self = this
                self.loading = true
                $.ajax({
                    method: 'GET',
                    url:'/garages/'+self.gid+'/car/'+self.cid,
                    success: function(data) {
                        console.log("car gotten")
                    }
                }).done((data) => {
                    self.cname = data.name
                    self.cbrand = data.brand
                    self.ckenteken = data.kenteken
                    self.ckleur = data.color
                }).then((data) => {
                    self.data = data
                }).always(() => {
                    self.loading = false
                })
            },
            saveCar: function() {
                var self = this
                self.loading = true
                $.ajax({
                    method: 'PUT',
                    url: '/garages/'+self.gid+'/car/'+self.cid,
                    data: { name: self.cname, brand: self.cbrand, kenteken: self.ckenteken, color: self.ckleur, garageId: self.gid },
                    timeout: 60000
                }).then((data) => {
                    self.edit = false;
                    this.data = data
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
            // editObject
        }
    }
</script>

<style>

</style>
