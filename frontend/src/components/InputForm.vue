<template>
	<v-container fluid style="padding:0px">
		<v-row align="center">
			
			<v-col>
				<v-text-field
					label="Origin Address"
					hint="Origin address of isochrone"
					v-model="address"
					placeholder="Rotunda da Boavista, Porto Portugal"
					
				/>
			</v-col>			
		</v-row>
		<v-row align="center">
			
			<v-col>
				<v-select
					label="Number of isochrone points"
					v-model="nPoints"
					:items="[5 , 10 , 20 , 25]"
				/>
			</v-col>
			<v-col>
				<v-text-field
					label="Isochrone duration (minutes)"
					hint="Reachable minutes from origin"
					v-model="duration"
					:rules="[v =>  validateDuration(Number(v))]"
				/>
			</v-col>			
		</v-row>

		<v-row align="center">
			<v-col>
				<v-select
					label="Method of transportation"
					v-model="selectedTransportationMethod"
					:items="transportationMethods"
				/>
			</v-col>
			<v-col>
				<v-select
					label="Consider live traffic?"
					v-model="considerTraffic"
					:items="[{text : 'Yes' , value : true }, {text : 'No' , value : false}]"
					:disabled="selectedTransportationMethod !== 'driving'"
				/>
			</v-col>
		</v-row>
		<v-row>
			<v-col align="center">
			<v-btn 
				rounded 
				color="primary" 
				elevation="0" 
				@click="draw"
				:disabled="!validInputs || maxIsochrones"
				:loading="loading"
			>
				Compute Isochrone
			</v-btn>
			</v-col>
		</v-row>
	</v-container>

</template>

<script>
export default {

	props : ['loading' , 'maxIsochrones'],

	data: function () {
		return {			
			originCoordinates: {"lat" : 41.158167, "lng" : -8.629133 },
			nPoints : 10,
			duration : 10,
			transportationMethods : [
				{text : 'Driving (car)' , value : 'driving' }, 
				{text : 'Walking' , value : 'walking' }
			],
			selectedTransportationMethod : 'driving',
			considerTraffic : false,
			address : ''

		};
	},

	methods: {		

		draw: function () {

			let data = {
				"address": this.address,
				"n_angles": Number(this.nPoints),
				"duration" : Number(this.duration),
				"mode" : this.selectedTransportationMethod,
				"traffic" : this.selectedTransportationMethod === 'walking' ? false : this.considerTraffic
			}			

			this.$emit('submit' , data)

			
			
		},

		validateGPSLatitude(value){

			if(isNaN(Number(value))){
				return 'Enter a valid GPS Coordinate'
			}

			if(value > 90 || value < -90){
				return 'Latitude should be a value between -90 and 90'
			}

			return true			
		},

		validateGPSLongitude(value){

			if(isNaN(Number(value))){
				return 'Enter a valid GPS Coordinate'
			}

			if(value > 180 || value < -180){
				return 'Longitude should be a value between -180 and 180'
			}

			return true


			
		},

		validateDuration(value){
			if(!Number.isInteger(value)){
				return 'Enter an integer'
			}
			
			if(value > 90 || value < 5){
				return 'Isochrone duration must be between 5 and 90'

			}

			return true
		}
	},
	
	computed : {

		validInputs : function(){

			if(this.validateGPSLatitude(Number(this.originCoordinates.lat)) === true && this.validateGPSLongitude(Number(this.originCoordinates.lng)) === true && this.validateDuration(Number(this.duration)) === true){
				return true
			}

			return false

		}
	}

}
</script>

<style>

</style>