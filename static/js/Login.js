function showFlashMessage() {
    setTimeout(function() {
        const msg = document.getElementById('alert');
        if (msg) {
            msg.style.display = 'none';
        }
    }, 2000); 
};

window.addEventListener('load',showFlashMessage);