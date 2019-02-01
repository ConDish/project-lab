$(document).ready(function(){
    
   
   
   
});


function envio(){
    
    var user = $("#user").val();
    var password = $("#password").val();
   
   
   $.ajax({
       url : "/prueba",
       type : "POST",
       data : {
           "user" : user,
           "password" : password,
       },
       success : function(dato){
           
           window.location.href = "prueba"
       }
   });
}