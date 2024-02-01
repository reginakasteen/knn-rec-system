let text = document.getElementById('text')
let clouds = document.getElementById('clouds')
let houses1 = document.getElementById('houses1')
let houses2 = document.getElementById('houses2')
let houses3 = document.getElementById('houses3')
let trees = document.getElementById('trees')

clouds.style.marginTop = 0;

window.addEventListener('scroll', () => {
    let value = window.scrollY;
    //text.style.marginTop = value * 2.5 + 'px';
    clouds.style.marginLeft = value * 0.1 + 'vh';
    houses1.style.marginTop = value * 0.15 + 'vh';
    houses2.style.marginTop = value * 0.1 + 'vh';
    houses3.style.marginTop = value * 0.25 + 'vh';

});
