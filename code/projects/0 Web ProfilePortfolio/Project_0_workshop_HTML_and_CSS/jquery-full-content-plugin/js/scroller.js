    $(document).ready(function (){
		
		$('#container').fullContent({ 
		  stages: 'div', 
		  mapPosition: [{v: 1, h: 1}, {v: 1, h: 2}, {v: 1, h: 3}], 
		  stageStart: 1, 
		  speedTransition: 800, 
		  idComplement: 'page_' 
		});
			
	});