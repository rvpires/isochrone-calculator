<template>
	<v-app>
		<v-app-bar app color="primary" dark flat>
			<v-spacer/>
			<span class="appTitle"> Isochrone Calculator </span>
			<v-spacer/>
		</v-app-bar>
		<v-main>
			<IsochroneCalculator/>
		</v-main>
	</v-app>
</template>

<script>
import IsochroneCalculator from './components/IsochroneCalculator';

export default {
	name: 'App',

	components: {
		IsochroneCalculator,
	}
	
};
</script>

<style>

* {
	font-family: 'Inter';
}

.appTitle{
	font-size: 20px;
}

</style>
