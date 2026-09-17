# 📚 Atividade Django - Matéria Full Stack

Projeto desenvolvido em **Django** para a disciplina de **Full Stack**, com foco na gestão, categorização e pesquisa de um acervo bibliográfico.

---

## 📌 Preservação das Aulas 4 e 5

O estado original desenvolvido nas **Aulas 4 e 5** foi devidamente salvo e preservado:
- **Branch:** `aula-original`
- **Tag:** `v1.0-aula-original`

### 🔄 Como alternar entre as versões
- **Para voltar exatamente ao código original das Aulas 4 e 5:**
  ```bash
  git checkout aula-original
  ```
- **Para retornar à versão final com as atualizações da atividade:**
  ```bash
  git checkout main
  ```

---

## 🚀 Funcionalidades da Atividade

1. **Tipo de Acervo**:
   - Exemplares classificados como `Físico` ou `Digital`.
2. **Categorias CDD (Classificação Decimal de Dewey)**:
   - `000` – Generalidades e Informação: Obras gerais, enciclopédias, jornais e biblioteconomia.
   - `100` – Filosofia e Psicologia: Ética, lógica e investigações sobre a mente humana.
   - `200` – Religião e Teologia: Mitologia, teologia e estudos sobre crenças e religiões.
   - `300` – Ciências Sociais e Direito: Política, economia, sociologia, educação e leis.
   - `400` – Linguística e Idiomas: Gramáticas, dicionários e estudos de línguas.
   - `500` – Ciências Puras (Exatas e Naturais): Matemática, física, química, biologia e astronomia.
   - `600` – Ciências Aplicadas (Tecnologia): Medicina, engenharia, agricultura e administração.
   - `700` – Artes e Recreação: Pintura, música, arquitetura, esportes e lazer.
   - `800` – Literatura: Poesia, romances, contos, crônicas e crítica literária.
   - `900` – História e Geografia: Biografias, viagens e acontecimentos históricos.
3. **Pesquisa e Filtros**:
   - Busca por nome (título ou autor).
   - Filtro por tipo de acervo (Físico ou Digital).
   - Filtro por categoria Dewey.
   - Suporte a filtros combinados e opção de limpar filtros.

---

## 🛠️ Como Executar o Projeto

1. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate
   ```
2. Configure o banco no arquivo `.env` (baseie-se no `.env.example`).
3. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```
4. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```
5. Acesse em: [http://127.0.0.1:8000/livros/](http://127.0.0.1:8000/livros/)

---

## 📜 Histórico dos 10 Commits da Atividade

1. `chore: configurar .gitignore e .env.example para ignorar venv, pycache e arquivos locais`
2. `feat: salvar estado original consolidado das aulas 4 e 5 (biblioteca e acervo)`
3. `feat(models): adicionar campo tipo de acervo (Físico ou Digital) no modelo Livro`
4. `feat(models): adicionar as 10 categorias de Dewey (CDD 000 a 900) ao modelo Livro`
5. `feat(migrations): gerar migration com os novos campos de tipo e categoria`
6. `feat(forms): atualizar LivroForm com campos de tipo e categoria`
7. `feat(views): implementar pesquisa e filtros por nome, tipo e categoria`
8. `feat(templates): atualizar formulario de cadastro de livro`
9. `feat(templates): implementar tela de listagem com pesquisa por nome, tipo e categoria`
10. `docs: adicionar README com documentacao da atividade django de full stack`
