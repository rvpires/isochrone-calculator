<template>
  <div id="map" ref="map"/>
</template>

<script>
export default {

  props : ['originCoordinates' , 'polygonCoordinates'],

  data : function(){
    return{
      map : null
    }
  },

  mounted : function(){
    this.map = new window.google.maps.Map(this.$refs["map"] , {
      center: {lat: 41.184679, lng: -8.681554},
      zoom: 12    
    })      
  },

  methods : {
    draw : function(){

      this.map = new window.google.maps.Map(this.$refs["map"] , {
        center: {lat: 41.184679, lng: -8.681554},
        zoom: 12    
      })   
      
      if(this.polygonCoordinates){
        var poly = new window.google.maps.Polygon({
                   paths: this.polygonCoordinates,
                   strokeColor: '#FF0000',
                   strokeOpacity: 0.8,
                   strokeWeight: 2,
                   fillColor: '#FF0000',
                   fillOpacity: 0.35});

        poly.setMap(this.map);
      }

      if(this.originCoordinates){
          var origin = new window.google.maps.Marker({
          position: this.originCoordinates,
          map: this.map
        });

        origin.setMap(this.map); 
      }      
    }
  }  
};
</script>


<style scoped>
#map {
  width: 100%;
  height: calc(100vh - 100px);
}
</style>