<template>
	<v-app>
		<v-app-bar app color="primary" dark flat>
			<v-container fluid style="padding:0px">
				<v-row no-gutters>
					<v-spacer />
					<v-col align="center">
						<span class="appTitle"> Isochrone Calculator </span>
					</v-col>
					<v-col align="end">
						<v-btn text color="white" href="https://github.com/rvpires">
							<span style="color:white">More about author</span>
						</v-btn>
					</v-col>
				</v-row>
			</v-container>
			
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
	font-weight: 300;
}

</style>
