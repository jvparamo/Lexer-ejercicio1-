import ply.lex as lex

# resultado del analisis
resultado_lexema = []

reservada = (
    # Palabras Reservadas
    'INCLUYENTE',
    'UTILIZAR',
    'MOSTRAR',
    'LEER',
   'OPTENER',
   'CADENA',
  'DEVUELVE',
   'VACIO',
    'ENTERO',
    'SALTO',
)
tokens = reservada + (
    'IDENTIFICADOR',
    'ASIGNADOR',

    'SUMADOR',
    'RESTANDO',
    'MULTIPLICADOR',
    'DIVISOR',
    'POTENCIADOR',
    'MODULO',

    
   'SI',
    'YSINO',
    
   'MIENTRAS',
   'PARA',
  
    
    
    
)

# Reglas de Expresiones Regualres para token de Contexto simple

t_SUMADOR = r'\&'
t_RESTANDO = r'-'
t_MULTIPLICADOR = r'\*'
t_DIVISOR = r'/'
t_MODULO = r'\%'
t_POTENCIADOR = r'(\*{2} | \^)'

t_ASIGNADOR = r'='





def t_INCLUYENTE(t):
    r'incluyente'
    return t

def t_UTILIZAR(t):
    r'utilizar'
    return t

def t_MOSTRAR(t):
    r'cout'
    return t

def t_LEER(t):
    r'cin'
    return t

def t_OPTENER(t):
    r'get'
    return t

def t_SALTO(t):
    r'endl'
    return t

def t_YSINO(t):
    r'else'
    return t

def t_SI(t):
    r'if'
    return t

def t_DEVUELVE(t):
   r'return'
   return t

def t_VACIO(t):
   r'void'
   return t

def t_MIENTRAS(t):
    r'while'
    return t

def t_PARA(t):
    r'for'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t



def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'\//'
    t.lexer.lineno += t.value.count('\n+')
    print("Comentario de multiple linea")



# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        
        estado = "Linea:  {:4}   Tipo: {:16}   Valor: {:16}    Posicion: {:4}".format(str(tok.lineno),str(tok.type) ,str(tok.value), str(tok.lexpos) )
        resultado_lexema.append(estado)
    return resultado_lexema # instanciamos el analizador lexico


