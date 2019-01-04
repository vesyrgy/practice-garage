<template>
	
    <div>
		<h1>Garages</h1>
        <!-- <button class="btn btn-default btn-primary" v-on:click="showModal">Add Garage (via modal)</button> -->
        <!-- <modal v-if="show" v-on:close="show = false"></modal> -->
        <!-- <modal></modal> -->

        <button v-if="!showForm" class="btn btn-default btn-primary" v-on:click="showForm = true">Add Garage</button>
        <form v-if="showForm">
            <input v-model='gname' type="text" class="form-control" placeholder="Enter name"> 
            <button type="button" class="btn btn-default btn-secondary modal-default-button" v-on:click="showForm = false">Close</button>
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
            gname: '',
            showForm: false,
            garagelist: []
        }
      },
      methods: {
        getList: function() {
            var self = this
            $.ajax({url:'/garages',
                success: function(data) {
                    self.garagelist = data
                }
            });
        },
        getGarage: function(id) {
            this.$router.push({ name: 'garage', params: {id} });
        },
        addGarage: function() {
            var self = this
            $.ajax({
                method: 'POST',
                url: '/garages',
                data: { name: this.gname },
                success: function(data) {
                    self.getList()
                }
            });
        },
        showModal: function() {
            
        }
      },
      created: function() {
        this.getList();
				//  eventHub.$on('refreshList', this.getList);
      },
      components: {
          Modal
      }
    }


</script>

<style>
    /* .btn-secondary {

    } */
	.col-1 { 
        width: 25%;
        float: left;
    }
    .col-2 {
        width: 75%;
        float: left;
    }
</style>
