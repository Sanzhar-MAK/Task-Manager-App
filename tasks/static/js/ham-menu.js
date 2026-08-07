const hamMenu = document.querySelector('.header-ham-menu')
const offScreenMenu = document.querySelector('.header-off-screen-menu')
// const addNewTask = document.querySelector('.add-new-task')

hamMenu.addEventListener('click', () => {
    hamMenu.classList.toggle('active');
    offScreenMenu.classList.toggle('active');
})

// addNewTask.addEventListener('click', () => {
//     this.remove();
// })