
    function validtionform(){
    	$('span').hide();
	var pswd = $('#id_password').val();
	var cpswd = $('#id_confirmpassword').val();
	if (pswd!=cpswd){
		msg="password not match";
		$('#span_password').text(msg);
		$('#span_password').show();
		
		return false;
	}

	var mo = $('#id_mobileno').val();
	if (mo.length!=10){
		msg = "Eneter valid mobile no";
		$('#span_mobileno').text(msg);
		$('#span_mobileno').show();
		return false;
	}
	return true;
}


$('.down').click(function () {
				var product_value = $(".myNumber" + this.parentElement.id).val();
				if (product_value >1 )
				{
					var csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
	                var product_id= $(this).parent().attr('id')
	                $.ajax({
	                  url: "/User/quantity/",
	                  type: "POST",
	                  data: {'csrfmiddlewaretoken': csrf_token, 'cartitem_id':product_id, 'operation': 'down'},
	                }).then(function (result){
	                    if (result.status == "success") {
	                    console.log(result.status); 
							   var new_value=parseInt($('.myNumber'+result.id).val());
							   console.log("old Value:"+new_value);

							   if(new_value <= 1)
							   {
							    // $('.down').css({
							    // "cursor": "wait","pointer-events": "none"});
							   }

							   else{
							    $('.myNumber'+result.id).val(new_value-1);
							    console.log("New Value:"+$('.myNumber'+result.id).val());
							$('#total').html('&#8377;'+result.total);}
							    
	                    }
	                    else {
	                        console.log(result.status);
	                    }

	                    
	                });
				}
                
            });
$('.up').click(function () {
				// $('.down').css({
				// 		    "cursor": "auto","pointer-events": "auto"});
                var csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
                $.ajax({
                  url: "/User/quantity/",
                  type: "POST",
                  data: {'csrfmiddlewaretoken': csrf_token, 'cartitem_id': $(this).parent().attr('id'), 'operation': 'up'},
                }).then(function (result){
                    if (result.status == "success") {
						      
						  console.log("success");
						  $('.myNumber'+result.id).val(parseInt($('.myNumber'+result.id).val())+1);
						  console.log(parseInt($('.myNumber'+result.id).val()));
						  console.log("Total:"+result.total);
						  $('#total').html('&#8377;'+result.total);
                    }
                    else {
                        console.log(result);
                    }
   
                });
            });

$('.remove').click(function () {
				
                var csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
                var item = $(this).attr('id').split('_')[1];
                var elem = $(this);
                $.ajax({
                  url: "/User/remove/",
                  type: "POST",
                  data: {'csrfmiddlewaretoken': csrf_token, 'cartitem_id': item }
                }).then(function (result){
                    if (result.status == "success") {
						      elem.parents('.remove_id').hide();
						      $('#total').html('&#8377;'+result.total);
						      if (result.total == 0)
						      {
						      	$('.checkout_colorp').hide();
						      	var total_zero = $('#total').html('&#8377;'+result.total);
						      	total_zero.hide();
						      	$(".empty").html("Your cart is empty!");
						      }
                    }
                    else {
                        console.log(result);
                    }
                });
            });


        