<template>
    <transition name="modal">
        <div class="modal-mask">
            <p>werkt dit al?</p>
            <div class="modal-wrapper">
                <div class="modal-container">
                    <form class="panel well">
                        <div class="form-group">
                                <label for="name">Name</label>
                                <input v-model='gname' type="text" class="form-control" placeholder="Enter name">
                        </div>
                        <div class="form-group">
                            <label for="brand">Brand</label>
                            <input v-model='gbrand' type="text" class="form-control" placeholder="Brand">
                        </div>
                        <button type="button" class="btn btn-default btn-primary" id="addGarage" @click='saveGarage()'>Add</button> 
                        <button type="button" class="btn btn-default btn-danger modal-default-button" @click="$emit('close')">Close</button>
                    </form>
                </div>
            </div>
        </div>
    </transition>
</template>
    

<script>
    // ...is het mogelijk/wenselijk om naar de bestaande code te refereren i.p.v. de modal hier te definieren?
    // let modal = require('../home.js')
    // import modal from '../home.js'

export default {
    name: 'modal',
    props: ['show'],
    data: function () {
        return {
            gname: '',
            gbrand: '',
            doge: ''
        };
    },
    methods: {
        saveGarage: function () {
        var self = this
        $.ajax({
            method: 'POST',
            url: '/garages',
            data: { name: this.gname, brand: this.gbrand },
            success: function() {
                    console.log('dawawdadwadw');
                    eventHub.$emit('refreshList');
                    self.$emit('close');
            }
        });
        }
    },
    mounted: function () {
        document.addEventListener('keydown', function(e) {
        if (e.keyCode == 27) {
            this.$emit('close');
        }
        });
    }
}
</script>

<style>
    .
    
</style>
