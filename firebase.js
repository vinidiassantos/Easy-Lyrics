// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCABDdasnNb0kCHyvW-X2g-Vct5w3TbTIk",
  authDomain: "vini-easy-lyrics.firebaseapp.com",
  projectId: "vini-easy-lyrics",
  storageBucket: "vini-easy-lyrics.firebasestorage.app",
  messagingSenderId: "856758043115",
  appId: "1:856758043115:web:6acb55c36b7d632a1499ae",
  measurementId: "G-E4705R7GFC"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);