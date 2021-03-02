<template>
	<v-container fluid>
		<v-row>
			<v-col cols="4" align="">				
				<InputForm @submit="data => draw(data)" :loading="loading" :maxIsochrones="maxIsochrones"/>
			</v-col>

			<v-col cols="8">
				<v-row v-if="isochrones.length > 0">
					<v-col v-for="(isochrone,i) in isochrones" :key="isochrone.id" align="center">
						Isochrone {{i + 1}}						
						<v-btn icon @click="removeIsochrone(isochrone.id)">
							<v-icon>mdi-close</v-icon>
						</v-btn>
						<GMap :isochrone="isochrone" />
					</v-col>					
				</v-row>
				<v-row v-else>
					<v-col>
						<v-row style="width:100%; height: calc(100vh - 100px); background:#e5e5e5" no-gutters align="center" justify="center">
							<v-col align="center">
							<div v-if="loading">
								<v-progress-circular
									indeterminate
									color="black"
								/>
							</div>
							<span v-else class="initMessage">Provide information to compute isochrone..</span>


							</v-col>
						</v-row>						
					</v-col>
				</v-row>
			</v-col>
		</v-row>
	</v-container>
</template>

<script>
import axios from 'axios'
import GMap from "./GMap";
import InputForm from './InputForm'
import { v4 as uuidv4 } from 'uuid'

export default {
	name: "IsochroneCalculator",

	components: {
		GMap,
		InputForm,
	},

	data : function(){
		return{
			loading :false,
			isochrones: [],
		}
	},

	computed : {
		maxIsochrones : function(){
			if(this.isochrones.length > 2){
				return true
			}

			return false
		}
	},
	
	methods: {
		draw: function (data) {


			if(this.maxIsochrones){
				return;
			}

			this.loading = true		
			

			axios.post('http://localhost:5000/compute' , data)
			.then(response =>{
				if(response.data.status === 'success'){
					let isochrone = response.data.result
					let origin = response.data.origin
					this.isochrones = this.isochrones.concat({id : uuidv4() , origin, isochrone})
				}				
			})
			.catch(error =>{
				console.log(error)
			})
			.finally(() =>{
				this.loading = false
			})

		},

		removeIsochrone: function(id){
			this.isochrones = this.isochrones.filter(element => element.id !== id)
		} 
	}
}
</script>

<style scoped>
.initMessage{
	color:grey;
	font-size: 15px;

}
</style>
