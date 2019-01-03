<template>
    <div class="garage">
        <h3>hier moet garage data komen te staan</h3>
        {{ garageData }} {{ $route.params.id}}
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
            getGarage: function() {
                console.log($route.params.id)
                console.log("clicked")
                var self = this
                console.log(id)
                
                $.ajax({url:'/garages/'+$route.params.id,
                    success: function(data) {
                        console.log("sucess")
                        self.garageData = data
                    }
                });
                
            }

        }  
    }
</script>

<style>
    
</style>

