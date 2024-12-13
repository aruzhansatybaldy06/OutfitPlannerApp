// database.js
import firebase from 'firebase/app';
import 'firebase/database';

// Reference to the clothes data
const clothesRef = firebase.database().ref('clothes');

// Add a new cloth item
const addCloth = (cloth) => {
  clothesRef.push(cloth)
    .then(() => {
      console.log('Cloth added successfully');
    })
    .catch((error) => {
      console.error('Error adding cloth:', error);
    });
};

// Get cloth items
const getClothes = () => {
  clothesRef.on('value', (snapshot) => {
    const clothes = snapshot.val();
    console.log('Clothes:', clothes);
  });
};

// Update a cloth item
const updateCloth = (id, cloth) => {
  clothesRef.child(id).update(cloth)
    .then(() => {
      console.log('Cloth updated successfully');
    })
    .catch((error) => {
      console.error('Error updating cloth:', error);
    });
};

// Delete a cloth item
const deleteCloth = (id) => {
  clothesRef.child(id).remove()
    .then(() => {
      console.log('Cloth deleted successfully');
    })
    .catch((error) => {
      console.error('Error deleting cloth:', error);
    });
};

export { addCloth, getClothes, updateCloth, deleteCloth };
