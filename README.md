# 📚 Atividade Django - Matéria Full Stack

Projeto desenvolvido em **Django** para a disciplina de **Full Stack**, com foco na gestão, categorização e pesquisa de um acervo bibliográfico.

## Funcionalidades da Atividade

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
