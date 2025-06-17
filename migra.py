import oracledb
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

# Oracle Client
oracledb.init_oracle_client(lib_dir=r"C:\\Users\\edson.neto\\Documents\\Projetos\\ITRIAD\\migrador d banco\\instantclient-basiclite-windows")

# Configuração de conexão
DB_CONFIG = {
    "user": "usr",
    "password": "psw",
    "dsn": "dsn"
}

# Lê o conteúdo do arquivo
with open("script.sql", "r", encoding="utf-8") as f:
    conteudo_sql = f.read()

# Divide comandos usando o delimitador real de fim de comando: ');
comandos_raw = conteudo_sql.split("');")
comandos = [comando.strip() + "');" for comando in comandos_raw if comando.strip()]

print(f"🚀 Executando {len(comandos)} comandos com threads...\n") !

# Função para validar aspas simples balanceadas
def aspas_balanceadas(comando: str) -> bool:
    return comando.count("'") % 2 == 0

# Função executada por thread
def executar_comando(index, comando):
    if not aspas_balanceadas(comando):
        return (index, False, comando, "Aspas simples desbalanceadas (')")

    try:
        conn = oracledb.connect(**DB_CONFIG)
        with conn.cursor() as cursor:
            cursor.execute(comando.rstrip(';'))
            conn.commit()
        conn.close()
        return (index, True, None)
    except Exception as e:
        return (index, False, comando, str(e))

# Execução paralela
comandos_falhos = []

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [
        executor.submit(executar_comando, i, comando)
        for i, comando in enumerate(comandos, 1)
    ]

    for future in as_completed(futures):
        result = future.result()
        if result[1]:
            print(f"[{result[0]}] ✅ OK")
        else:
            print(f"[{result[0]}] ❌ Erro: {result[3]}")
            comandos_falhos.append(result[2])

# Salva falhas
if comandos_falhos:
    with open("falhas_migracao.sql", "w", encoding="utf-8") as f:
        f.write('\n\n'.join(comandos_falhos) + '\n')
    print(f"\n⚠️ {len(comandos_falhos)} comandos falharam e foram salvos em falhas_migracao.sql")
else:
    print("\n✅ Todos os comandos executados com sucesso.")