// src/App.js
import { useState, useEffect } from "react";
import LoginButton from "./components/LoginButton";
import { salvarCifra, carregarCifra } from "./utils/firebaseUtils";

function App() {
  const [user, setUser] = useState(null);
  const [cifra, setCifra] = useState("");

  useEffect(() => {
    if (user) {
      carregarCifra(user.uid).then(setCifra);
    }
  }, [user]);

  const handleSave = () => {
    if (user) salvarCifra(user.uid, cifra);
  };

  return user ? (
    <>
      <textarea value={cifra} onChange={e => setCifra(e.target.value)} />
      <button onClick={handleSave}>Salvar Cifra</button>
    </>
  ) : (
    <LoginButton onLogin={setUser} />
  );
}

export default App;
