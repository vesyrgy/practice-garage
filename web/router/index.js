import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home'
import Garages from '../components/garagelist'
import Garage from '../components/garage'
import Cars from '../components/carlist'
import Car from '../components/car'

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
            meta: {linkText: "Garage"},
            component: Garage
        },
        {
            path: '/garages/:id/cars',
            name: 'cars',
            component: Cars
        },
        {
            path: '/garages/:gid/car/:id',
            name: 'car',
            component: Car
        }
    ]
})
