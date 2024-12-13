// auth.js
import firebase from 'firebase/app';
import 'firebase/auth';

// Sign up a new user
const signUp = (email, password) => {
  firebase.auth().createUserWithEmailAndPassword(email, password)
    .then((userCredential) => {
      // Signed up
      const user = userCredential.user;
      console.log('User signed up:', user);
    })
    .catch((error) => {
      console.error('Error signing up:', error);
    });
};

// Sign in an existing user
const signIn = (email, password) => {
  firebase.auth().signInWithEmailAndPassword(email, password)
    .then((userCredential) => {
      // Signed in
      const user = userCredential.user;
      console.log('User signed in:', user);
    })
    .catch((error) => {
      console.error('Error signing in:', error);
    });
};

// Sign out the current user
const signOut = () => {
  firebase.auth().signOut()
    .then(() => {
      console.log('User signed out');
    })
    .catch((error) => {
      console.error('Error signing out:', error);
    });
};

export { signUp, signIn, signOut };
