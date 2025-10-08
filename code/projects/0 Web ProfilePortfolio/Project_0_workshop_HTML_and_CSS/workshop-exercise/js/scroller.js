    $(document).ready(function (){
		// first down button
		$("#clickDown1").click(function (){
        // scroll the page to the top of div2
            $('html, body').animate({
                scrollTop: $("#div2").offset().top
            }, 500);
        
   	 	});

		// second down button
    	$("#clickDown2").click(function (){
        // scroll the page to the top of div3
            $('html, body').animate({
                scrollTop: $("#div3").offset().top
            }, 500);
        
    	});
		
		// second up button
    	$("#clickUp2").click(function (){
        // scroll the page to the top of div3
            $('html, body').animate({
                scrollTop: $("#div1").offset().top
            }, 500);
			
    	});
		// third up button
    	$("#clickUp3").click(function (){
        // scroll the page to the top of div3
            $('html, body').animate({
                scrollTop: $("#div2").offset().top
            }, 500);
			
		});
			
	});