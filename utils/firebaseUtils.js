// src/utils/firebaseUtils.js
import { db } from "../firebase";
import { doc, setDoc, getDoc } from "firebase/firestore";

export async function salvarCifra(uid, cifra) {
  const ref = doc(db, "cifras", uid);
  await setDoc(ref, { texto: cifra });
}

export async function carregarCifra(uid) {
  const ref = doc(db, "cifras", uid);
  const snap = await getDoc(ref);
  return snap.exists() ? snap.data().texto : "";
}
