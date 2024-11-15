# Sistema de Agenda de Atividades Acadêmicas

Este repositório contém a especificação do software para um sistema de agenda de atividades acadêmicas voltado para alunos de cursos de graduação da área de Tecnologia da Informação da Universidade São Judas Tadeu. O sistema permitirá que os alunos gerenciem suas atividades acadêmicas de forma eficiente, com funcionalidades para adicionar, editar, listar e deletar atividades.

## 1. Introdução

O sistema foi desenvolvido para atender às necessidades dos alunos, proporcionando uma interface amigável e funcionalidades que facilitam o gerenciamento de atividades acadêmicas.

## 2. Requisitos

### 2.1 Requisitos Funcionais

1. **Cadastro de Usuário**:
   - O sistema deve permitir que novos alunos se cadastrem, fornecendo informações como nome, matrícula, e-mail, usuário e senha.
   
2. **Login de Usuário**:
   - O sistema deve permitir que usuários registrados façam login usando suas credenciais.
   
3. **Gerenciamento de Atividades**:
   - O sistema deve permitir que os usuários adicionem novas atividades, especificando título, descrição, data de início, data de término, tipo e status.
   - O sistema deve permitir que os usuários listem todas as suas atividades.
   - O sistema deve permitir que os usuários editem atividades existentes.
   - O sistema deve permitir que os usuários deletam atividades que não são mais necessárias.
   
4. **Visualização de Atividades**:
   - O sistema deve permitir que os usuários vejam os detalhes de cada atividade, incluindo título, descrição, datas e status.

5. **Sistema de Notificações**:
   - O sistema deve enviar notificações sobre atividades próximas ao prazo de término.

### 2.2 Requisitos Não Funcionais

1. **Desempenho**:
   - O sistema deve ser capaz de suportar pelo menos 100 usuários simultâneos sem degradação de desempenho.

2. **Segurança**:
   - As senhas dos usuários devem ser armazenadas de forma criptografada.
   - O sistema deve implementar medidas de segurança para proteger as informações pessoais dos usuários.

3. **Usabilidade**:
   - A interface do usuário deve ser intuitiva e fácil de navegar, com um design responsivo que funcione em diferentes dispositivos.

4. **Manutenibilidade**:
   - O código do sistema deve ser modular e bem documentado, facilitando a manutenção e a adição de novas funcionalidades.

5. **Compatibilidade**:
   - O sistema deve ser compatível com os navegadores mais populares, como Chrome, Firefox e Safari.

## 3. Protótipos Não Funcionais das Telas

Os protótipos das telas podem ser representados em ferramentas como Figma ou Adobe XD. Aqui estão descrições das principais telas:

1. **Tela de Login**:
   - Campos para usuário e senha.
   - Botão de "Login" e link para "Cadastrar".

2. **Tela de Cadastro**:
   - Campos para nome, matrícula, e-mail, usuário, senha e curso.
   - Botão de "Cadastrar" e link para "Voltar".

3. **Tela Principal**:
   - Botões para adicionar, listar, editar e deletar atividades.
   - Exibição de um resumo das atividades.

4. **Tela de Adição de Atividade**:
   - Campos para título, descrição, data de início, data de término, tipo e status.
   - Botão de "Salvar" e "Voltar".

5. **Tela de Listagem de Atividades**:
   - Lista de atividades com opções para editar ou deletar cada uma.

6. **Tela de Edição de Atividade**:
   - Campos preenchidos com os dados da atividade selecionada.
   - Botões para "Salvar" e "Voltar".

## 4. Modelo Entidade-Relacionamento (ER)

### Entidades

- **Usuário**: 
  - id (PK)
  - nome
  - matricula
  - email
  - usuario
  - senha
  - curso

- **Atividade**: 
  - id (PK)
  - titulo
  - descricao
  - data_inicio
  - data_termino
  - tipo
  - status
  - usuario_id (FK)

### Relacionamentos

- Um usuário pode ter várias atividades (1:N).

## 5. Modelo Lógico de Banco de Dados

```sql
CREATE TABLE Usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    matricula VARCHAR(20) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL,
    curso VARCHAR(100) NOT NULL
);

CREATE TABLE Atividade (
    id SERIAL