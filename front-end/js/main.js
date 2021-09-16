// OPEN/CLOSE MODAL

const buttonModal = document.querySelectorAll('.open-modal');
const modal = document.querySelectorAll('.modal');
const closed = document.querySelectorAll('.close')

buttonModal.forEach((i) => {
    i.addEventListener('click', () => {
      modal[0].classList.add('modal-active');
    });
     });

closed.forEach((i) => {
i.addEventListener('click', () => {
modal[0].classList.remove('modal-active');
});
});     

