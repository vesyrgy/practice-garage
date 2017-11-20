import 'bootstrap';
import Vue from 'vue'
import GarageList from './components/garagelist.vue'

window.eventHub = new Vue();

Vue.component('modal', {
  template: '#modal-template',
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
    document.addEventListener('keydown', (e) => {
      if (e.keyCode == 27) {
        this.$emit('close');
      }
    });
  }
});

new Vue({
    el: "#garages",
    data: {
      showModal: false
    },
    components: {
      GarageList
    }
});

$('body').on('click', '.edit-garage', function() {
  alert('dwadawadw');
  //eventHub.$emit('refreshList');
});
