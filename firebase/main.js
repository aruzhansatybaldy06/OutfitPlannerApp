// main.js
import { signUp, signIn, signOut } from './auth';
import { addCloth, getClothes, updateCloth, deleteCloth } from './database';

// Example usage
document.getElementById('sign-up-btn').addEventListener('click', () => {
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  signUp(email, password);
});

document.getElementById('sign-in-btn').addEventListener('click', () => {
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  signIn(email, password);
});

document.getElementById('sign-out-btn').addEventListener('click', () => {
  signOut();
});

document.getElementById('add-cloth-btn').addEventListener('click', () => {
  const cloth = {
    name: document.getElementById('cloth-name').value,
    category: document.getElementById('cloth-category').value,
    color: document.getElementById('cloth-color').value,
    fabric: document.getElementById('cloth-fabric').value,
    brand: document.getElementById('cloth-brand').value,
  };
  addCloth(cloth);
});

// Get and display clothes
getClothes();
