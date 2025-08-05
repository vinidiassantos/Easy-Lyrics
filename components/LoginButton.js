// src/components/LoginButton.js
import { signInWithPopup } from 'firebase/auth';
import { auth, provider } from '../firebase';

export default function LoginButton({ onLogin }) {
  const handleLogin = async () => {
    const result = await signInWithPopup(auth, provider);
    onLogin(result.user);
  };

  return <button onClick={handleLogin}>Login com Google</button>;
}
