<template>
  <div id="map" ref="map" />
</template>

<script>
export default {

  data: function () {
    return {
      map: null,
    };
  },

  mounted: function () {
    this.map = new window.google.maps.Map(this.$refs["map"], {
      center: {lat : 41.158167, lng : -8.629133 },
      zoom: 12,
    });
  },

  methods: {
    draw: function (originCoordinates,polygonCoordinates ) {

		console.log(originCoordinates , polygonCoordinates)
      this.map = new window.google.maps.Map(this.$refs["map"], {
        center: originCoordinates,
        zoom: 12,
      });

      if (polygonCoordinates) {
        var poly = new window.google.maps.Polygon({
          paths: polygonCoordinates,
          strokeColor: "#FF0000",
          strokeOpacity: 0.8,
          strokeWeight: 2,
          fillColor: "#FF0000",
          fillOpacity: 0.35,
        });

        poly.setMap(this.map);
      }

      if (originCoordinates) {
        var origin = new window.google.maps.Marker({
          position: originCoordinates,
          map: this.map,
        });

        origin.setMap(this.map);
      }
    },
  },
};
</script>


<style scoped>
#map {
  width: 100%;
  height: calc(100vh - 100px);
}
</style>