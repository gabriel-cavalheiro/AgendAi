// OPEN/CLOSE MODAL

const buttonLogin = document.querySelector('.open-modal')
const modal = document.getElementById('mymodal');
const close = document.querySelector('.close');

buttonLogin.addEventListener('click', () => {
    modal.classList.add('modal-active');
})

close.addEventListener('click', () => {
    modal.classList.remove('modal-active');
})

const buttonHero = document.querySelector('#open-modal')
const modalHero = document.getElementById('mymodal');
const closeModal = document.querySelector('.close');

buttonHero.addEventListener('click', () => {
    modal.classList.add('modal-active');
})

close.addEventListener('click', () => {
    modal.classList.remove('modal-active');
})
