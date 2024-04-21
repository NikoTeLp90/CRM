document.addEventListener('DOMContentLoaded', function() {
    var dropdownToggle = document.getElementById('dropdown-toggle');
    var dropdownMenu = document.getElementById('dropdown-menu');

    dropdownToggle.addEventListener('click', function() {
        if (dropdownMenu.style.display === 'block') {
            dropdownMenu.style.display = 'none';
        } else {
            dropdownMenu.style.display = 'block';
        }
    });
});