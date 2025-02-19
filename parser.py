import ply.yacc as yacc
from lexer import tokens  # Importando tokens do analisador léxico

# Regras da gramática

def p_program(p):
    '''program : statement_list'''
    print("Análise sintática concluída sem erros!")

def p_statement_list(p):
    '''statement_list : statement statement_list
                      | statement'''
    
# Declaração de variáveis
def p_statement_declaration(p):
    '''statement : INT ID EQUALS expression SEMICOLON
                 | FLOAT ID EQUALS expression SEMICOLON'''
    print(f"Declaração válida: {p[1]} {p[2]} = {p[4]}")

# Atribuições e expressões matemáticas
def p_statement_assignment(p):
    '''statement : ID EQUALS expression SEMICOLON'''
    print(f"Atribuição válida: {p[1]} = {p[3]}")

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''

def p_factor(p):
    '''factor : NUMBER
              | ID
              | LPAREN expression RPAREN'''

# Estruturas condicionais
def p_statement_if(p):
    '''statement : IF LPAREN condition RPAREN LBRACE statement_list RBRACE'''
    print("Estrutura condicional válida.")

def p_condition(p):
    '''condition : expression GREATER expression
                 | expression LESS expression
                 | expression EQUALS expression'''

# Erros de sintaxe
def p_error(p):
    if p:
        print(f"Erro de sintaxe perto de '{p.value}' na linha {p.lineno}")
    else:
        print("Erro de sintaxe: final inesperado do código.")

# Construindo o parser
parser = yacc.yacc()

#Teste do analisador sintático Com erros
codigo_teste_invalido = """
int 3xa;
float 1y;
int @ 10;
y = 3.a;
if (x > y) x = x + * y;
"""

#Teste do analisador sintático Sem erros
codigo_teste_valido = """
int x = 10;
float y = 5.5;
y = x + 2;
if (x > 0){ y = y -  1; }
"""

print("\nAnalisando código:")
parser.parse(codigo_teste_valido)
