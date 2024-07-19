/*****************************************************************
 *          ALL SCRIPTS
 * 
 * 
 ***********************************************************/



//Function to validate email address

function validateEmail(email){
    const regex =  /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}


function validateAll(){
    
    var name = $("#name").val();
    var phone = $("#phone").val();
    var email = $("#email").val();
    var age = $("#age").val();
    var gender = $("#gender").val();


if(name == ''){
    swal("Oops !!","Name field cannot be Empty", "error");
    return false;
}
else if(name.split(' ').length < 2 ){
    swal("Oops !!","The last name is required", "info");
    return false;
}
else if(name == name.toUpperCase()){
    swal("Oops !!","Name cannot be UpperCase", "info");
    $("#name").val("");
    return false;
}
else if(phone == ''){
    swal("Oops !!","Phone field cannot be Empty", "error");
    return false;
}
else if(email == ''){
    swal("Oops !!","Email field cannot be Empty", "error");
    return false;
}
else if(!(validateEmail(email))){
    swal("Oops !!","Put a valid Email address", "error");
    return false;
}
else if(age == ''){
    swal("Oops !!","Age field cannot be Empty", "error");
    return false;
}
/**
else if(age > 120){
    swal("Denied !!","The maximum age is 120", "error");
    $("#age").val("");
    return false;
}
**/
else if(gender == ''){
    swal("Oops !!","Gender field cannot be Empty", "error");
    return false;
}
else{
    return true;
}

}

$("#btn-add").bind("click",validateAll);


//Only letter is allowed


$(document).ready(function(){

    jQuery("input[name='name']").keyup(function(){
        var letter = jQuery(this).val();
        var allow = letter.replace(/[^a-zA-Z _]/g, '');
        jQuery(this).val(allow);
    });

    //Script to prevent starting with space
    $("input").on("keypress",function(e){
        if(e.which == 32 &&  ! this.value.length){
            e.preventDefault();
        }
    });
});


//Script to capitalize name


$("#name").keyup(function(){
    var txt = $(this).val();
    $(this).val(txt.replace(/^(.)|\s(.)/g, function($1){ return $1.toUpperCase( ); }));

});



//5) Script to lower the email 
$(document).ready(function(){
    $("#email").keyup(function(){
        this.value = this.value.toLowerCase();
    });

//6) script to only allow numbers in Age
$("#age").keyup(function(){

    if(!/^[0-9]*$/.test(this.value)){
        this.value = this.value.split(/[^0-9]/).join('');
    }
});


});



//7 Input mask for phone number

$(document).ready(function(){
    $("#phone").inputmask("(99) 9999-9999",{"onincomplete": function(){
        $("#phone").val("");
        swal("Oops!!","Incomplete phone, Review","error");
        return false;
    }});
});






// age validation

$(document).ready(function(){

$("#age").keyup(function(){
var age = $("#age").val();
if(age  > 120 ){
    $(this).val("");
    return false;
}
});

});


// prevent age field starting with zero

$("#age").on("input", function(){
    if(/^0/.test(this.value)){
        this.value = this.value.replace(/^0/,"");
    }
});

//preventing users registering fullname

$(document).ready(function(){
    $("#name").keyup(function(){
        var name = $("#name").val();
        if(name.split(' ').length == 3){
            swal("Oops!!","Put only first name and last name","info");
            $("#name").val("");
            return false;
        }


    });

});


 // time running at realtime
setInterval(function(){
    var date = new Date();
    $("#clock").html(
        (date.getHours() < 10 ? '0' : '' ) + date.getHours() +  ":" + (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() + ":" + (date.getSeconds() < 10 ? '0' :'') + date.getSeconds()
    );

},500);


//if no patient



var verify = $("#chk_td").length;
    if (verify == 0){
        $("#no-data").text("No patient found");
    } 



// email address to lowercase

$(document).ready(function(){
 $("#email").keyup(function(){
    this.value = this.value.toLowerCase();
 });

});




