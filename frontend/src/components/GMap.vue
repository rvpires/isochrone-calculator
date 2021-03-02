<template>
	<v-container fluid style="padding:0px">
		<v-row no-gutters>
			<v-col>
				<div id="map" ref="map" />
			</v-col>
		</v-row>
	</v-container>
</template>

<script>
export default {

	props : ['isochrone'],

	data: function () {
		return {
			map: null,
		}
	},

	mounted: function () {

		this.map = new window.google.maps.Map(this.$refs["map"], {
				center: this.isochrone.origin,
				zoom: 12,
			});

			if (this.isochrone.isochrone) {
				var poly = new window.google.maps.Polygon({
				paths: this.isochrone.isochrone,
				strokeColor: "#FF0000",
				strokeOpacity: 0.8,
				strokeWeight: 2,
				fillColor: "#FF0000",
				fillOpacity: 0.35,
				});

				poly.setMap(this.map);
			}

			if (this.isochrone.origin) {
				var origin = new window.google.maps.Marker({
				position: this.isochrone.origin,
				map: this.map,
				});

				origin.setMap(this.map);
			}
	}	
}
</script>


<style scoped>
#map {
	width: 100%;
	height: calc(100vh - 140px);
}
</style>