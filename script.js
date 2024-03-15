// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAoJ0HHLxRubJ_XdRsSb6sAE0MOIYBJpH0",
  authDomain: "exceed-pay.firebaseapp.com",
  projectId: "exceed-pay",
  storageBucket: "exceed-pay.appspot.com",
  messagingSenderId: "184767791915",
  appId: "1:184767791915:web:159a3e61b6ec8e7be8fb6e",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

const checkoutBut = document.getElementById("button");
