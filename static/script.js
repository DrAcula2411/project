// Hover text is added with the help of ChatGPT.
document.querySelectorAll('.image-container').forEach(container => {
    const image = container.querySelector('img');
    const hoverText = container.querySelector('.hover-text');

    image.addEventListener('mouseenter', () => {
        hoverText.textContent = image.getAttribute('data-text');
        hoverText.style.display = 'inline';
    });

    image.addEventListener('mouseleave', () => {
        hoverText.style.display = 'none';
    });
    image.addEventListener('click', () => {
        window.location.href = "/buy";
    });
});