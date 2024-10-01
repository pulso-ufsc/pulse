# Projeto Pulso - LabTec-UFSC

## Título

Desenvolvimento de um sistema de gerenciamento e monitoramento em tempo real do estado de pacientes idosos cardíacos utilizando dados provenientes de pulseiras inteligentes.

## Objetivo

O objetivo desse projeto é desenvolver uma plataforma web que permita o gerenciamento e monitoramento em tempo real da saúde de pacientes idosos cardíacos. A plataforma utilizará dados de sinais vitais coletados de dispositivos vestíveis (wearables), como pulseiras inteligentes, integrados via API (Garmin Health API). O sistema permitirá o cadastro e gerenciamento de pacientes, a coleta contínua de sinais vitais, análise automatizada dos dados e a exibição de informações de forma clara e acessível para médicos, enfermeiros e outros profissionais de saúde. Além disso, o sistema deverá emitir alertas em tempo real para situações críticas, auxiliando na tomada de decisões clínicas e no acompanhamento do estado de saúde dos pacientes. O projeto será desenvolvido utilizando o framework Django, garantindo a criação de uma interface web responsiva e escalável.

## Atividades

1. Levantamento de requisitos:
   - Entendimento das necessidades dos usuários finais (médicos, enfermeiros, pacientes e administradores).
   - Definição dos tipos de dados a serem coletados (batimentos cardíacos, pressão arterial, oxigenação, etc.).
2. Projeto de interfaces:
   - Criação de wireframes e protótipos das interfaces de usuário para o sistema web.
   - Desenvolvimento de interfaces responsivas com Bootstrap, permitindo a visualização em diferentes dispositivos.
3. Integração com a Garmin Health API:
   - Estudo e compreensão da documentação da API da Garmin Health.
   - Implementação de endpoints para coletar e armazenar dados dos dispositivos vestíveis no banco de dados.
4. Desenvolvimento do backend:
   - Implementação do backend utilizando Django.
   - Criação de modelos de dados para armazenar informações dos pacientes, médicos, sinais vitais, alertas, etc.
   - Implementação de lógica para análise automática dos dados recebidos e geração de alertas.
5. Segurança e autenticação:
   - Implementação de autenticação e autorização de usuários (Allauth).
   - Definição de permissões de acesso baseadas no tipo de usuário (administrador, médico, enfermeiro, paciente).
6. Monitoramento em tempo real:
   - Implementação de funcionalidades em tempo real usando WebSockets.
   - Exibição de dashboards com visualização dos gráficos e dados em tempo real.
7. Testes e validação:
   - Testes unitários e de integração para garantir o funcionamento correto do sistema.
   - Realização de testes de desempenho e segurança.
8. Manutenção e documentação:
   - Criação de documentação técnica para facilitar a manutenção do sistema.

## Observações

- O sistema deve ser intuitivo e de fácil utilização, visando atender às necessidades dos profissionais de saúde e pacientes.
- A segurança dos dados dos pacientes é fundamental, garantindo o sigilo e a integridade das informações coletadas.
- A integração com a API da Garmin Health permitirá a coleta de dados precisos e confiáveis dos dispositivos vestíveis.
- A análise automática dos dados e a geração de alertas contribuirão para a identificação precoce de situações críticas e o acompanhamento contínuo dos pacientes.
- A visualização em tempo real dos sinais vitais dos pacientes facilitará a tomada de decisões clínicas e o monitoramento eficaz do estado de saúde.
- O sistema será desenvolvido de forma modular e escalável, permitindo a adição de novas funcionalidades e integrações futuras.
- A documentação técnica e o treinamento dos usuários serão essenciais para garantir o uso adequado e eficiente do sistema.
