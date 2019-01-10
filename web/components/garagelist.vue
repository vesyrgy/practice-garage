<template>
	
    <div>
		<h1>Garages</h1>
        <!-- <button class="btn btn-default btn-primary" v-on:click="showModal = true">Add Garage (via modal)</button>
        <modal v-if="showModal" v-on:close="showModal = false"></modal> -->

        <button v-if="!showForm" class="btn btn-default btn-primary" v-on:click="showForm = true">Add Garage</button>
        <form class="addGarageForm" v-if="showForm">
            <input v-model='gname' type="text" class="form-control" placeholder="Enter name"> 
            <input v-model='gbrand' type="text" class="form-control" placeholder="Enter brand"> 
            <input v-model='gpostal' type="text" class="form-control" placeholder="Enter postal country"> 
            <button type="button" class="btn btn-default btn-secondary modal-default-button" id ="cancel" v-on:click="showForm = false">Cancel</button>
            <button type="button" class="btn btn-default btn-primary" id="addGarage" v-on:click='addGarage()'>Add</button> 
        </form>
        <div id="garages" class="panel well col-xs-12">    
            <ul>
                <li class="garage-item" v-for="(g, index) in garagelist" :key="index">
                    <span class="col-1">
                        <!-- {{g.id}}:  -->
                    </span>
                    <span class="col-2">
                        <a v-on:click="getGarage(g.id)">{{ g.name }}</a>
                    </span>
                </li>
            </ul>
        </div>    
	</div>
</template>

<script>
    import Modal from './modal.vue'

	//  import eventHub from './eventHub.vue'
    export default {
      name: 'garage-list',
      data: function () {
        return {
            // showModal: false,
            gname: '',
            gbrand: '',
            gpostal: '',
            showForm: false,
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
                console.log("data; " + data)
            }).then((data) => {
                self.garagelist = data
            }).always(() => {
                self.loading = false
            })
        },
        getGarage: function(id) {
            this.$router.push({ name: 'garage', params: {id} });
        },
        addGarage: function() {
            var self = this
            self.showForm = false
            self.loading = true
            $.when($.ajax({
                method: 'POST',
                url: '/garages',
                data: { name: self.gname, brand: self.gbrand, postal_country: self.gpostal },
                timeout: 60000,
                success: function(returned) {  
                    console.log("addGarage POST request returned garage with id: " + returned.id)
                    // self.garagelist.push(returned)
                    // self.getList()
                }
            })).done((data) => {
                self.garagelist.push(data)
            }).then(
                self.getList()
            ).always(() => {
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
          Modal
      }
    }


</script>

<style>
    ul {
        list-style-type: none;
        padding: 0;
        margin: 0;
    }
    #cancel {
        color: gray;
        float: left;
    }
    #addGarage {
        float: right;
    }
    .addGarageForm {
        grid-column: 2 / span 3;
    }
</style>
