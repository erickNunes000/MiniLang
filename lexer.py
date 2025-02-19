import ply.lex as lex

# Lista de palavras reservadas
reserved = {
   'if': 'IF',
   'then': 'THEN',
   'else': 'ELSE',
   'int': 'INT',
   'float': 'FLOAT',
   'while': 'WHILE',
}

# Lista de tokens
tokens = [
    'ID',
    'NUMBER',      # Identificador de Numeros como (5.5 e 2)
    'PLUS',         # Operador soma "+"
    'MINUS',        # Operador subtracao "-"
    'TIMES',       # Operador multiplicacao "*"
    'DIVIDE',      # Operador divisao "/"
    'LPAREN',     #Parentese esquerdo "("
    'RPAREN',     #Parentese direito ")"
    'SEMICOLON',  # Ponto e vírgula (;)
    'EQUALS',     # Operador de atribuição (=)
    'GREATER',    # Operador maior que (>)
    'LESS',       # Operador menor que (<)
    'INVALID_ID',  # Identificadores malformados como "1y 3ax"
    'LBRACE',   # Chave esquerda "{"
    'RBRACE'    #Chave direita "}"
] + list(reserved.values())

# Expressões regulares para tokens simples
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_SEMICOLON = r';'
t_EQUALS    = r'='
t_GREATER   = r'>'
t_LESS      = r'<'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

# Expressão para capturar identificadores inválidos ANTES de capturar números
def t_INVALID_ID(t):
    r'\d+[a-zA-Z_]+'
    print(f"Erro léxico: Identificador inválido '{t.value}' na linha {t.lineno}")
    return t

# Expressão para números
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Expressão para identificadores (variáveis e palavras reservadas)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica se é palavra reservada
    return t

# Ignorar espaços e tabulações
t_ignore = ' \t'

# Atualiza a contagem de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regra para capturar caracteres ilegais
def t_error(t):
    print(f"Erro léxico: Caractere ilegal '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

# Construção do lexer
lexer = lex.lex()

# Teste do analisador léxico (❌Invalido) codigo com erros
codigo_teste_invalido = """
int 3xa;
float 1y;
int @ 10;
y = 3.a;
if (x > y) x = x + * y;
"""
# Teste do analisador léxico (✅Valido) codigo sem erros
codigo_teste_valido = """
int x = 10;
float y = 5.5;
y = x + 2;
if (x > 0){ y = y - 1; }
"""

#lexer.input(data)
lexer.input(codigo_teste_valido)

print("Tokens reconhecidos:")
while True:
    tok = lexer.token()
    if not tok:
        break
    print(f"{tok.type}: {tok.value}")
