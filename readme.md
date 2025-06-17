Claro! Abaixo estão:

1. ✅ Um **README.md** com instruções para rodar seu projeto Python que executa scripts SQL em Oracle usando o pacote `oracledb` (modo thin, **sem precisar instalar Oracle Instant Client**).
2. ✅ O comando para exportar o `requirements.txt`.

---

## ✅ `README.md`

````markdown
# Oracle SQL Runner

Este projeto executa comandos SQL em um banco de dados Oracle diretamente a partir de um arquivo `.sql` usando Python.

### 📦 Requisitos

- Python 3.8+
- Conexão com banco Oracle (local ou remoto)

### 🚀 Como rodar

1. Clone o repositório ou baixe os arquivos.
2. Crie e ative o ambiente virtual:

```bash
python -m venv venv
# source venv/bin/activate  # Linux/macOS
source venv\Scripts\activate   # Windows
````

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure as variáveis de conexão no script `run_sql_oracle.py`:

```python
user="seu_usuario"
password="sua_senha"
dsn="host:porta/servico"  # Exemplo: localhost:1521/xe
```

5. Certifique-se de que seu arquivo `script.sql` está na raiz do projeto e contém os comandos SQL que deseja executar.

6. Execute o script:

```bash
python run_sql_oracle.py
```

---

### 💡 Observações

* Este projeto usa o pacote `oracledb` no modo `thin`, ou seja, **não é necessário instalar o Oracle Instant Client**.
* Os comandos no arquivo `.sql` devem estar separados por ponto e vírgula `;`.

---

### 📁 Exemplo de `script.sql`

```sql
INSERT INTO employees (id, name) VALUES (1, 'João');
INSERT INTO employees (id, name) VALUES (2, 'Maria');
```

---

### 🔒 Segurança

**Nunca** versionar ou compartilhar senhas ou credenciais de banco. Use variáveis de ambiente ou arquivos `.env` em produção.

