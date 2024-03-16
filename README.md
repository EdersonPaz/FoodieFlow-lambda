# Repositório de Funções Lambda para Interação com Cognito

Este repositório contém várias funções Lambda que interagem com o serviço Cognito da AWS. Cada função está contida em sua própria pasta e tem um propósito específico.

## Funções Lambda

- `create-auth-challenge-9c5f29cd-001c-4fb3-b71a-9ef9037004ee`: Esta função é responsável por criar autenticação.
- `define-auth-challenge-c59f32d6-215c-45fc-8613-3dfb836d627b`: Esta função é responsável por definir  autenticação.
- `jwt-validator-3b16b3a5-cce1-4a6e-87c0-b833260b8fad`: Esta função é responsável por validar tokens JWT.
- `pre-signup-new-42ae4e8d-270e-4ccd-bf8c-0bbdf3119675`: Esta função é responsável por lidar com novos eventos de pré-inscrição (recebimento CPF).
- `verify-auth-challenge-f524a303-99f2-49a2-a576-5f3bdc727364`: Esta função é responsável por verificar autenticação.

## GitHub Actions

Este repositório utiliza GitHub Actions para automatizar o processo de implantação das funções Lambda. O fluxo de trabalho é ativado em cada push para a branch main.

O fluxo de trabalho realiza as seguintes etapas:
1. Configura o ambiente de execução.
2. Instala as dependências necessárias.
3. Empacota as funções Lambda.
4. Faz upload das funções Lambda para um bucket S3 na AWS.
5. Esses usados  no serviço Cognito usando os artefatos do bucket S3.
