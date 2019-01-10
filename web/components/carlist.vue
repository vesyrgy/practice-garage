<template>
    <div v-bind:addCar="addCar">
        <h4>Auto's</h4>
        <div id="car-list" class="panel well col-xs-12">
            <ul>
            <li class="car-item" v-for="(c, index) in carList" :key="index">
                <span class="col-1">
                    <!-- {{c.id}}:  -->
                </span>
                <span class="col-2">
                    <a v-on:click="getCar(gid,c.id)">{{ c.name }}</a>
                </span>
            </li>
            </ul>
        </div>

        <form class="addCarForm" v-if="showCarForm">
            <label for="naam">Naam</label>
            <input id="naam" v-model='cname' type="text" class="form-control" placeholder="Naam">
            <label for="merk">Merk</label>
            <input id="merk" v-model='cbrand' type="text" class="form-control" placeholder="Merk">
            <label for="kenteken">Kenteken</label>
            <input id="kenteken" v-model='ckenteken' type="text" class="form-control" placeholder="Kenteken">
            <label for="color">Kleur</label>
            <input id="color" v-model='ccolor' type="text" class="form-control" placeholder="Kleur"> 
            <div class="btn-group">
                <button type="button" class="left btn btn-default btn-secondary modal-default-button" id ="cancel" @click="hideForm">Cancel</button>
                <button type="button" class="right btn btn-default btn-primary" id="save" v-on:click='addCar()'>Voeg Auto Toe aan {{gname}}</button> 
            </div>
        </form>

    </div>
</template>

<script>
export default {
    name: 'car-list',
    props: ['showCarForm', 'gname', 'gid'],
    data: function() {
        return {
            carList: {},
            carData: {},
            showForm: false,
            cname: '',
            cbrand: '',
            ckenteken: '',
            ccolor: ''
        }
    },
    methods: {
        getList: function() {
            var self = this
            var id = self.gid
            self.loading = true
            if (id == undefined) {
                console.log("id is " + id)
                id = self.$route.params.id
                console.log("id changed to " + id)
            }
            $.when($.ajax({
                method: 'GET',
                url:'/garages/'+id+'/cars',
                success: function(returned) {
                    console.log("carlist gotten")
                    console.log("data on success: " + JSON.stringify(returned))
                }
            })).done((returned) => {
                console.log("data on done: " + returned)
                self.carList = returned
            }).then((returned) => {
                console.log("data on then: " + returned)
                self.carList = returned
            }).always(() => {
                self.loading = false
            })
        },
        hideForm(event) {
            this.showForm = false
            this.$emit('hideForm', this.showForm)
        }, 
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
            }).then(
                setTimeout(function() {self.getList()}, 100)
            ).always(() => {
                self.loading = false
            })
        }, 
        getCar: function(gid, id) {
            if( gid == undefined) {
                gid = this.$route.params.gid
            }
            console.log("this.gid: " + gid)
            this.$router.push({ name: 'car', params: {gid,id} });
        }
    },
    beforeMount: function() {
        this.getList()
        console.log("beforeMount of carlist")
        console.log("carlist is: " + JSON.stringify(this.carlist))
    },
    mounted: function() {
        console.log("carlist mounted")
        setTimeout(function() {this.getList()}, 100)
    },

}
</script>

<style>

</style>
