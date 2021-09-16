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
    modalHero.classList.add('modal-active');
})

close.addEventListener('click', () => {
    modal.classList.remove('modal-active');
})

const buttonMeet = document.getElementById('open-modal-m')
const modalMeet = document.getElementById('mymodal-m');
const closeModalMeet = document.querySelector('.close');

buttonMeet.addEventListener('click', () => {
    modal.classList.add('modal-active');
})

close.addEventListener('click', () => {
    modal.classList.remove('modal-active');
})
