# Controle de Luminosidade para Pacientes com Fotosensibilidade

Este projeto implementa a **parte do servidor**, desenvolvida em Python, de um sistema de controle de luminosidade voltado a pacientes com fotosensibilidade. A comunicação entre cliente e servidor é feita via **sockets TCP**, permitindo o envio e recebimento de dados pela rede de forma simples e eficiente.

## 🧠 Contexto do Projeto

O sistema completo é composto por duas partes:

- **Cliente**: responsável por ler os dados de luminosidade (via sensor LDR) e enviá-los ao servidor.
- **Servidor**: recebe esses dados e, com base em uma lógica de controle, aciona dispositivos de alerta (LEDs e buzzer).

Este projeto se destina a ajudar pacientes com **fotosensibilidade** a evitar ambientes com luminosidade excessiva.

