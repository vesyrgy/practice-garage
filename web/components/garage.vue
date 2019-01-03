<template>
    <div class="garage">
        <h3>Garage: {{garageData.name}}</h3>
        <p>Deze garage heeft id: {{ garageData.id }}</p>
    </div>
</template>

<script>
    export default {
        name: 'garage',
        data: function() {
            return {
                garageData: {}
            }
        },
        methods: {
            showGarage: function(id) {
                console.log(this.$route.params.id)
                console.log("clicked")
                var self = this
                console.log(id)
                
                $.ajax({url:'/garages/'+this.$route.params.id,
                    success: function(data) {
                        console.log("sucess")
                        self.garageData = data
                    }
                });
            }
        }, 
        beforeMount(){
            this.showGarage(this.$route.params.id)
        }  
    }
</script>

<style>
    
</style>

