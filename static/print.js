
function print_receipt(){

    var button=document.querySelector('.print');
    var send_email=document.querySelector('.send_email');
    
    button.style.display='none';
    send_email.style.display='none';
    window.print();

    button.style.display='block';
    send_email.style.display='block';
}


var today = new Date();

var formattedDate = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();


document.getElementById('date').innerText = formattedDate;



