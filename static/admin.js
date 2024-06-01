
show_password();

function login_admin(){

    var a=document.getElementById('a').value;
    var b=document.getElementById('b').value;

    if(a === 'admin' && b === 'admin@123'){
        window.location.href='adminPanel';
    }
    else if(a=== 'staff' && b=== 'hod@123'){
        window.location.href='staff';
        }
        
    else{
            alert('Incorrect Password or Username');
        }
    }
  


function show_password(){
    var b=document.getElementById('b');
    var a=document.querySelector('#show_password');

    a.addEventListener('click',function () {

        if(a.checked){
            b.type ="text";
        }
        else{
            b.type ="password";
        }
    })

}