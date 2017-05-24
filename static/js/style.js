$(document).ready(function(){
    $(".nav-tabs a").click(function(){
        $(this).tab('show');
    });
    var n = currenttime(); 
    tabcurrent(n);
    clicktab();
    chooseDanish();
});


function currenttime(){
	var today = new Date();
	var n = today.getHours();

	if (n < 12){
		return 0;
	}
	else if (n < 18){
		return 1;
	}
	else{
		return 2;
	}
}
function tabcurrent(n){
	if (n == 0){
		$("#sche-day-moorning").addClass("in active");
		$(".sche-job-day-moorning").addClass("in active");
	}else if (n==1){
		$("#sche-day-afternoon").addClass("in active");
		$(".sche-job-day-afternoon").addClass("in active");
	}else{
		$("#sche-day-everning").addClass("in active");
		$(".sche-job-day-everning").addClass("in active");
	} 
}
function clicktab(){	
	$("li").click(function(){
		var n = currenttime();
		var target = this.id;
		var type = target.split("-");
		$(".sche-work-"+type[0]).removeClass("in active");
		$(".sche-job-"+type[0]).removeClass("in active");
 
		if (target == "day-current"){
			tabcurrent(n);
		}else{
			$("#sche-"+target).addClass("in active");
			$(".sche-job-"+target).addClass("in active");
			

		}
	});
	
}
// chon nha sy theo danh dach ngay
function chooseDanish(){
	$(".sche-day-dn").click(function() {

    	var id =$(this).parent().attr("id");
    	var d = id.split("-");

    	$(".sche-"+d[0]+"-dn").removeClass('sche-dn-'+d[0]+'-active');
    	$(".sche-show-"+d[0]).removeClass('sche-axis-active');

    	$("#"+id).children(".sche-"+d[0]+"-dn").addClass("sche-dn-"+d[0]+"-active");
    	$("#"+id).children(".sche-show-"+d[0]).addClass("sche-axis-active");
    });
    $(".sche-week-dn").click(function() {

    	var id =$(this).parent().attr("id");
    	var d = id.split("-");

    	$(".sche-"+d[0]+"-dn").removeClass('sche-dn-'+d[0]+'-active');
    	$(".sche-show-"+d[0]).removeClass('sche-axis-active');

    	$("#"+id).children(".sche-"+d[0]+"-dn").addClass("sche-dn-"+d[0]+"-active");
    	$("#"+id).children(".sche-show-"+d[0]).addClass("sche-axis-active");
    });
}
