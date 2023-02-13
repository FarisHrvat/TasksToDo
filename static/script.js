const form = document.querySelector('form');
const taskInput = document.querySelector('input[type="text"]');
const dateInput = document.querySelector('input[type="date"]');
const taskList = document.querySelector('ul');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const task = taskInput.value;
  const date = dateInput.value;

  const taskItem = document.createElement('li');
  taskItem.innerHTML = `<input type="checkbox"> ${task} (${date})`;

  taskList.appendChild(taskItem);
});
