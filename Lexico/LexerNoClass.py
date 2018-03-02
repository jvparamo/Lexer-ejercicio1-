import ply.lex as lex

# resultado del analisis
resultado_lexema = []

reservada = (
    # Palabras Reservadas
    'INCLUYENTE',
    'MOSTRAR',
    'LEER',
    'OPTENER',
    'DEVUELVE',
    'VACIO',
    'ENTERO',
    'BOOL',
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
    'Y',
    'O',
    'NEGACION',
    'ELMENOR',
    'MENOROIGUAL',
    'ELMAYOR',
    'MAYOR0IGUAL',
    'IGUAL',
    'DESIGUAL',
    
    'PARENIZQ',
    'PARENDER',
    'LLAVEIZQ',
    'LLAVEDER',
    'FINALDESENTENCIA',
  
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
    r'incl'
    return t

def t_MOSTRAR(t):
    r'msg'
    return t

def t_LEER(t):
    r'rec'
    return t

def t_OPTENER(t):
    r'opt'
    return t

def t_BOOL(t):
    r'bool'
    return t

def t_YSINO(t):
    r'sino'
    return t

def t_SI(t):
    r'si'
    return t

def t_DEVUELVE(t):
   r'retorna'
   return t

def t_VACIO(t):
   r'vac'
   return t

def t_MIENTRAS(t):
    r'mtras'
    return t

def t_PARA(t):
    r'para'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'\$.*'
    pass

def t_error(t):
    global resultado_lexema
    estado = "Token no valido en la Linea: {:4}     Valor: {:16}    Posicion: {:4}".format(str(t.lineno), str(t.value),str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)






