import pymysql
import pytest

# Configurações de conexão com o banco de dados
db_config = {
    'user': 'root',          # Usuário do banco de dados
    'password': '',        # Senha do banco de dados
    'host': '127.0.0.1',            # Host do banco de dados
    'database': 'bitnami_wordpress',    # Nome do banco de dados do WordPress
    'port': 3307,  # Porta padrão do MySQL
    
}

@pytest.fixture(scope='module')
def db_connection():
    connection = pymysql.connect(**db_config)
    yield connection
    connection.close()

def test_users_table_exists(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("SHOW TABLES LIKE 'wp_users'")
        result = cursor.fetchone()
        assert result is not None, "Tabela 'wp_users' não existe no banco de dados"

def test_users_table_not_empty(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM wp_users")
        result = cursor.fetchone()
        assert result[0] > 0, "Tabela 'wp_users' está vazia"

def test_post_table_exists(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("SHOW TABLES LIKE 'wp_posts'")
        result = cursor.fetchone()
        assert result is not None, "Tabela 'wp_posts' não existe no banco de dados"

def test_post_table_not_empty(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM wp_posts")
        result = cursor.fetchone()
        assert result[0] > 0, "Tabela 'wp_posts' está vazia"

def test_comments_table_exists(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("SHOW TABLES LIKE 'wp_comments'")
        result = cursor.fetchone()
        assert result is not None, "Tabela 'wp_comments' não existe no banco de dados"

def test_comments_table_not_empty(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM wp_comments")
        result = cursor.fetchone()
        assert result[0] > 0, "Tabela 'wp_comments' está vazia"


def test_terms_table_exists(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("SHOW TABLES LIKE 'wp_terms'")
        result = cursor.fetchone()
        assert result is not None, "Tabela 'wp_terms' não existe no banco de dados"

def test_terms_table_not_empty(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM wp_terms")
        result = cursor.fetchone()
        assert result[0] > 0, "Tabela 'wp_terms' está vazia"

#insercao
    def test_insert_post(db_connection):
     cursor = db_connection.cursor()
    
     # Dados para inserção
     insert_query = "INSERT INTO wp_posts (ID,post_author, post_title) VALUES (%s, %s)"
     data = ('35','1', 'Test no Banco')
    
     # Executa inserção
     cursor.execute(insert_query, data)
     db_connection.commit()
    
     # Verifica se o dado foi inserido
     cursor.execute("SELECT * FROM wp_posts WHERE post_author = %s AND post_title = %s", data)
     result = cursor.fetchone()

    def test_insert_terms(db_connection):
     cursor = db_connection.cursor()
    
     # Dados para inserção
     insert_query = "INSERT INTO wp_terms (term_id, name, slug, term_group) VALUES (%s, %s,%s,%s)"
     data = ('27', 'Test2_name','test2_slug','test2_term_group')
    
     # Executa inserção
     cursor.execute(insert_query, data)
     db_connection.commit()
    
     # Verifica se o dado foi inserido
     cursor.execute("SELECT * FROM wp_terms WHERE term_id = %s AND name = %s AND slug = %s AND term_group= %s", data)
     result = cursor.fetchone()

    def test_insert_user(db_connection):
     cursor = db_connection.cursor()
    
     # Dados para inserção
     insert_query = "INSERT INTO wp_users (ID, user_login, user_email) VALUES (%s, %s,%s)"
     data = ('7', 'Test1_login','test@gmail.com')
    
     # Executa inserção
     cursor.execute(insert_query, data)
     db_connection.commit()
    
     # Verifica se o dado foi inserido
     cursor.execute("SELECT * FROM wp_users WHERE ID = %s AND user_login = %s AND user_email = %s", data)
     result = cursor.fetchone()

    def test_insert_comments(db_connection):
     cursor = db_connection.cursor()
    
     # Dados para inserção
     insert_query = "INSERT INTO wp_comments (comment_ID, comment_post_ID, comment_author, comment_content) VALUES (%s, %s,%s,%s)"
     data = ('4', '125','Julia Hille','Muito legal')
    
     # Executa inserção
     cursor.execute(insert_query, data)
     db_connection.commit()
    
     # Verifica se o dado foi inserido
     cursor.execute("SELECT * FROM wp_comments WHERE comment_ID = %s AND comment_post_ID = %s AND comment_author = %s AND comment_content= %s", data)
     result = cursor.fetchone()
def test_delete_users(db_connection):
    cursor = db_connection.cursor()
    
    # Dados para exclusão
    delete_query = "DELETE FROM wp_users WHERE ID = %s"
    condition_value = '7'
    
    # Executa exclusão
    cursor.execute(delete_query, (condition_value,))
    db_connection.commit()
    
    # Verifica se o dado foi excluído
    cursor.execute("SELECT * FROM wp_users WHERE ID = %s", (condition_value,))
    result = cursor.fetchone()
    
    assert result is None

def test_delete_post(db_connection):
    cursor = db_connection.cursor()
    
    # Dados para exclusão
    delete_query = "DELETE FROM wp_posts WHERE ID = %s"
    condition_value = '35'
    
    # Executa exclusão
    cursor.execute(delete_query, (condition_value,))
    db_connection.commit()
    
    # Verifica se o dado foi excluído
    cursor.execute("SELECT * FROM wp_posts WHERE ID = %s", (condition_value,))
    result = cursor.fetchone()
    
    assert result is None

def test_delete_terms(db_connection):
    cursor = db_connection.cursor()
    
    # Dados para exclusão
    delete_query = "DELETE FROM wp_terms WHERE term_id = %s"
    condition_value = '27'
    
    # Executa exclusão
    cursor.execute(delete_query, (condition_value,))
    db_connection.commit()
    
    # Verifica se o dado foi excluído
    cursor.execute("SELECT * FROM wp_terms WHERE term_id = %s", (condition_value,))
    result = cursor.fetchone()
    
    assert result is None

def test_delete_comments(db_connection):
    cursor = db_connection.cursor()
    
    # Dados para exclusão
    delete_query = "DELETE FROM wp_comments WHERE comment_id = %s"
    condition_value = '4'
    
    # Executa exclusão
    cursor.execute(delete_query, (condition_value,))
    db_connection.commit()
    
    # Verifica se o dado foi excluído
    cursor.execute("SELECT * FROM wp_comments WHERE comment_id = %s", (condition_value,))
    result = cursor.fetchone()
    
    assert result is None

def test_update_user(db_connection):
    cursor = db_connection.cursor()
    
    # Dados para atualização
    update_query = "UPDATE wp_users SET user_nicename = %s WHERE ID = %s"
    new_value = 'breno_werlang'
    condition_value = '3'
    
    # Executa atualização
    cursor.execute(update_query, (new_value, condition_value))
    db_connection.commit()
    
    # Verifica se o dado foi atualizado
    cursor.execute("SELECT user_nicename FROM wp_users WHERE ID = %s", (condition_value,))
    result = cursor.fetchone()

def test_update_term(db_connection):
    cursor = db_connection.cursor()
    
    # Dados para atualização
    update_query = "UPDATE wp_terms SET name = %s WHERE term_id = %s"
    new_value = 'Acelerar'
    condition_value = '14'
    
    # Executa atualização
    cursor.execute(update_query, (new_value, condition_value))
    db_connection.commit()
    
    # Verifica se o dado foi atualizado
    cursor.execute("SELECT name FROM wp_terms WHERE term_id = %s", (condition_value,))
    result = cursor.fetchone()
    
    assert result is not None
    assert result[0] == new_value

@pytest.mark.failx
def test_update_post(db_connection):
    cursor = db_connection.cursor()
    
    # Dados para atualização
    update_query = "UPDATE wp_posts SET post_status = %s WHERE ID = %s"
    new_value = 'public'
    condition_value = '1'
    
    # Executa atualização
    cursor.execute(update_query, (new_value, condition_value))
    db_connection.commit()
    
    # Verifica se o dado foi atualizado
    cursor.execute("SELECT post_author FROM wp_posts WHERE ID = %s", (condition_value,))
    result = cursor.fetchone()
    
    assert result is not None
    assert result[0] == new_value

def test_update_comments(db_connection):
    cursor = db_connection.cursor()
    
    # Dados para atualização
    update_query = "UPDATE wp_comments SET comment_author = %s WHERE comment_ID = %s"
    new_value = 'Breno Werlang'
    condition_value = '1'
    
    # Executa atualização
    cursor.execute(update_query, (new_value, condition_value))
    db_connection.commit()
    
    # Verifica se o dado foi atualizado
    cursor.execute("SELECT comment_author FROM wp_comments WHERE comment_ID = %s", (condition_value,))
    result = cursor.fetchone()
    
    assert result is not None
    assert result[0] == new_value