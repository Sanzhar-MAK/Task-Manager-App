const hamMenu = document.querySelector('.header-ham-menu')
const offScreenMenu = document.querySelector('.header-off-screen-menu')

hamMenu.addEventListener('click', () => {
    hamMenu.classList.toggle('active');
    offScreenMenu.classList.toggle('active');
})