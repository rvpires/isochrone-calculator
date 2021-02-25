<template>
	<v-container fluid>
		<v-row>
			<v-col cols="4">
				
				
				Isochrone Center
					
				<v-row v-if="false">
					<v-col>
						<v-text-field
						label="Latitude"
						hint="Origin latitude in decimal degrees"
						v-model="lat"
						/>
					</v-col>
					<v-col>
						<v-text-field
							label="Longitude"
							hint="Origin longitude in decimal degrees"
							v-model="lat"
						/>
					</v-col>
				</v-row>

				<v-btn @click="draw">Draw</v-btn>
			</v-col>

			<v-col cols="8">
				<GMap :polygonCoordinates="polygonCoordinates" :originCoordinates="originCoordinates" ref="gmap" />
			</v-col>
		</v-row>
	</v-container>
</template>

<script>
//import axios from 'axios'
import GMap from "./GMap";
export default {
	name: "IsochroneCalculator",

	components: {
		GMap,
	},

	data: function () {
		return {
			polygonCoordinates: [],
			originCoordinates: { lat: 41.184679, lng: -8.681554 },
			n_points : 12,
			duration : 5

		};
	},

	methods: {
		draw: function () {
			this.$refs.gmap.draw();
		},

		computeIsochrone : function(){

		},

		radians: function(degrees){
			var pi = Math.PI;
			return degrees * (pi/180);
		},

		degrees: function(radians){
			var pi = Math.PI;
			return radians * 180/ pi;
		},

		initialPlotting : function(originGeocode , angle , radius){

			/*Harvsines are used to consider earth curvature
			origin_geocode is the GPS coordinates of origin
			angle is the angle from it's going to be calculated
			radius is how long the arch is going to be*/

			let r = 6371.0  //Radius of the Earth in  km
			let bearing = this.radians(angle)  //Bearing in radians converted from angle in degrees
			let lat1 = this.radians(originGeocode.lat)
			let lng1 = this.radians(originGeocode.lng)

			let lat2 = Math.asin(Math.sin(lat1) * Math.cos(radius / r) + Math.cos(lat1) * Math.sin(radius / r) * Math.cos(bearing))
			let lng2 = lng1 + Math.atan2(Math.sin(bearing) * Math.sin(radius / r) * Math.cos(lat1), Math.cos(radius / r) - Math.sin(lat1) * Math.sin(lat2))

			lat2 = this.degrees(lat2)
			lng2 = this.degrees(lng2)

			return {lat : lat2, lng : lng2}

		}
	},

	created : function(){		
		
		for(let i = 0 ; i < this.n_points; i++ ){

			let initialRadius = this.duration / 6
			let angle =  i * 360 / this.n_points

			this.polygonCoordinates = this.polygonCoordinates.concat(this.initialPlotting(this.originCoordinates , angle , initialRadius))
			
		}
	}
};
</script>
