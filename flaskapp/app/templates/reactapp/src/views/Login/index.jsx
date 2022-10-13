import Container from "./styles";

import Button from "../../components/Button";
import Input from "../../components/Input";

import React from "react";

function Login() {
  return (
    <Container>
      <h2>Realizar Login</h2>
      <Input placeholder="Login" />
      <Input placeholder="Senha" />
      <Button>Entrar</Button>
    </Container>
  );
}

export default Login;