function display(){
    var name=document.getElementsByName('name')[0].value;
    var father=document.getElementsByName('father')[0].value;
    var surname=document.getElementsByName('surname')[0].value;
    var mother=document.getElementsByName('mother')[0].value;
    var dob=document.getElementsByName('dob')[0].value;
    var registration=document.getElementsByName('registration')[0].value;
    var year=document.getElementsByName('year')[0].value;
    var branch=document.getElementsByName('branch')[0].value;
    var start=document.getElementsByName('start')[0].value;
    var end=document.getElementsByName('end')[0].value;
    var clas=document.getElementsByName('clas')[0].value;
    

if(name==='' || father==='' || surname==='' || mother==='' || dob==='' || registration==='' || year==='' || branch==='' || start==='' || clas==='' || end===''){


    alert("Fill all Fields");
}
else{
    alert("Your form is succesfully submitted")
};

registration_no_validate();
validation();


}


function email_validate(email){
const re = /\S+@\S+\.\S+/;

return re.test(email);
}


function validation(){
var email=document.getElementsByClassName('email').value;

if(!email_validate(email)){
    confirm("Enter Proper Email Format");
}
}


function registration_no_validate(){
    var r_no=document.getElementById('registration').value;

    if((r_no.length)!=9){
        alert("Enter Valid Registration No");
    }
    


}