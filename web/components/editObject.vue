<template>
    <div>
        <form class="editObjectForm" v-if="edit">
            <label for="naam">Naam</label>
            <input id="naam" v-model='gname' type="text" class="form-control" v-bind:placeholder="garageData.name">
            <label for="merk">Merk</label>
            <input id="merk" v-model='gbrand' type="text" class="form-control" v-bind:placeholder="garageData.brand">
            <label for="land">Land</label>
            <input id="land" v-model='gpostal' type="text" class="form-control" v-bind:placeholder="garageData.postal_country"> 
            <div class="btn-group">
                <button type="button" class="left btn btn-default btn-secondary modal-default-button" id ="cancel" v-on:click="edit = false">Cancel</button>
                <button type="button" class="right btn btn-default btn-primary" id="save" v-on:click='saveGarage()'>Save</button> 
            </div>
        </form>
    </div>
</template>


<script>
export default {
    
}
</script>

<style>

</style>
