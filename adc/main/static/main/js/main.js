// получаем элементы
const header = document.querySelector('.header__container');
const burger = document.querySelector('.menu__burger');
const menu = document.querySelector('.header__menu');

// добавляем обработчик события на клик по бургер-меню
burger.addEventListener('click', () => {
  // добавляем класс "active" элементам меню и бургер-меню
  burger.classList.toggle('active');
  menu.classList.toggle('active');
  header.classList.toggle('active');
});
