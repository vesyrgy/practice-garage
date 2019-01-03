<template>
	<div>
		<h1>Garages</h1>
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
</template>

<script>
	//  import eventHub from './eventHub.vue'
    export default {
      name: 'garage-list',
      data: function () {
        return {
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
        }
      },
      created: function() {
        this.getList();
				//  eventHub.$on('refreshList', this.getList);
      }
    }


</script>

<style>
	.col-1 { 
        width: 25%;
        float: left;
    }
    .col-2 {
        width: 75%;
        float: left;
    }
</style>
