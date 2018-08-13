$(document).ready(function(){
	$("#postag").click(function(){
		$.ajax({ 
		    type: "POST", 	
			url: "http://127.0.0.1:5000/POSTagging/",
            data: JSON.stringify({
            content: $("#textcontent").val(),
            }),
			contentType: 'application/json',
			dataType: "json",
			success: function(data){
				if (data.success) { 
					$("#Result").html(data.msg);
				} else {
					$("#Result").html("出现错误：" + data.msg);
				}  
			},
			error: function(jqXHR){     
			   alert("发生错误：" + jqXHR.status);  
			},     
		});
	});
});