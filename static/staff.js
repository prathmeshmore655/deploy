function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}


const search = () => {
    let key = document.getElementById('query').value.trim().toLowerCase();
    let table = document.querySelector('.table');
    let rows = table.getElementsByTagName('tr');

    for (let i = 1; i < rows.length; i++) {
        let cells = rows[i].getElementsByTagName('td');
        let found = false;

        for (let j = 0; j < cells.length; j++) {
            let cellContent = cells[j].textContent || cells[j].innerHTML;

            if (cellContent.toLowerCase().indexOf(key) > -1) {
                found = true;
                break;
            }
        }

        rows[i].style.display = found ? "" : "none";
    }
};


const debouncedSearch = debounce(search, 300);


function showDetails(studentId) {
    let popups = document.querySelectorAll('.popup');
    popups.forEach(popup => {
        popup.style.opacity = '0';
        popup.style.display = 'none';
    });

        let popupId = 'details_' + studentId;
    let popup = document.getElementById(popupId);
    if (popup) {
        popup.style.display = 'block';
        setTimeout(() => {
            popup.style.opacity = '1';
        }, 100);
    }
}


function closepopup(){
location.reload();
}

print_receipt()
