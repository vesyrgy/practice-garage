import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home'
import Garages from '../components/garagelist'
import Garage from '../components/garage'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/garages/',
            name: 'garages',
            component: Garages
        },
        {
            path: '/garages/:id',
            name: 'garage',
            component: Garage
        }
    ]
})
