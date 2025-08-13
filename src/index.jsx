import React, { useEffect, useState } from "react";

function App() {
  const [root, setMensagem] = useState("");

  useEffect(() => {
    fetch("/api/main/root") // rota da sua API no Vercel
      .then((res) => res.json())
      .then((data) => setMensagem(data.texto));
  }, []);

function myButton(){
    return(
        <button>
            Clique Aqui
        </button>
    );
}


function MyApp() {
    return(
        <div>
            <h1>
                Bem vindo à pagina
            </h1>
            <myButton />
        </div>
    );

}
}