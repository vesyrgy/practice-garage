<template>
	<div>
        <div class="row">
            
            <h1>Garages</h1>
        </div>
        <div class="row">
            <!-- <button class="btn btn-default btn-primary" v-on:click="showModal = true">Add Garage (via modal)</button>
            <modal v-if="showModal" v-on:close="showModal = false"></modal> -->
            <button v-if="!showGarageForm" class="btn btn-default btn-primary" v-on:click="showGarageForm = true">Add Garage</button>
        </div>
        <div class="row">   
            <garage-form v-bind:formType="fType" v-if="showGarageForm" @formVisibilityChanged="showGarageForm = $event"></garage-form>
        </div>
        <div id="garages" class="row" v-if="!showGarageForm">  
            <ul class="list-group">
                <li class="garage-item" v-for="(g, index) in garagelist" :key="index">
                    <span class="col-2">
                        <router-link class="list-group-item" v-bind:to="{ name: 'garage', params: { id: g.id }}">{{ g.name }}</router-link>
                    </span>
                </li>
            </ul>  
        </div>
    </div>
</template>

<script>
    import Modal from './modal.vue'
    import GarageForm from './garageform.vue'

	//  import eventHub from './eventHub.vue'
    export default {
      name: 'garage-list',
      data: function () {
        return {
            // showModal: false,
            hover: false,
            showGarageForm: false,
            fType: 'Add',
            garagelist: []
        }
      },
      methods: {
        getList: function() {
            var self = this
            self.loading = true
            $.ajax({
                method: 'GET',
                url:'/garages',
                success: function(data) {
                    console.log("garagelist gotten")
                }
            }).done((data) => {
                self.garagelist = data
                // console.log("data; " + data)
            }).then((data) => {
                // self.garagelist = data
            }).always(() => {
                self.loading = false
            })
        },
        showModal: function() {
            
        }
      },
      beforeMount: function() {
        this.getList();
      },
      mounted: function() {
        console.log("garagelist mounted")
        this.getList();
				//  eventHub.$on('refreshList', this.getList);
      },

      components: {
          'garage-form': GarageForm
      }
    }


</script>

<style>
    /* #cancel {
        color: gray;
        float: left;
    }
    #addGarage {
        float: right;
    }
    .addGarageForm {
        grid-column: 2 / span 3;
    } */
</style>
