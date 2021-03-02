<template>
	<v-container fluid>
		<v-row>
			<v-col cols="4">				
				<InputForm @submit="data => draw(data)" :loading="loading"/>
			</v-col>

			<v-col cols="8">
				<GMap  ref="gmap" />
			</v-col>
		</v-row>
	</v-container>
</template>

<script>
import axios from 'axios'
import GMap from "./GMap";
import InputForm from './InputForm'
export default {
	name: "IsochroneCalculator",

	components: {
		GMap,
		InputForm,
	},

	data : function(){
		return{
			loading :false
		}
	},
	
	methods: {
		draw: async function (data) {

			this.loading = true

			axios.post('http://localhost:5000/compute' , data)
			.then(response =>{
				if(response.data.status === 'success'){
					let isochrone = response.data.result
					this.$refs.gmap.draw(data.origin, isochrone)
				}				
			})
			.catch(error =>{
				console.log(error)
			})
			.finally(() =>{
				this.loading = false
			})

		}
	}
}
</script>
