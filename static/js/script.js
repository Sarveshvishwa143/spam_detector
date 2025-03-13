let slideIndex = 0;
const slides = document.querySelectorAll('.slide');
const dots = document.querySelectorAll('.dot');

function showSlide(index) {
    slides.forEach((slide, i) => {
        slide.style.display = 'none';
        dots[i].classList.remove('active-dot');
    });
    slides[index].style.display = 'block';
    dots[index].classList.add('active-dot');
}

function changeSlide() {
    slideIndex = (slideIndex + 1) % slides.length;
    showSlide(slideIndex);
}

showSlide(slideIndex);

setInterval(changeSlide, 3000);

dots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
        slideIndex = index;
        showSlide(slideIndex);
    });
});