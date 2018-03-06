from tkinter import *
from tkinter import ttk

import ply.lex as lex


resultado_lexema = []

reservada = (
   
    'INCLUIR',
    'MOSTRAR',
    'LEER',
    'NUMERICO',
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
    'MAYOROIGUAL',
    'IGUAL',
    'DESIGUAL',
    
    'PARENIZQ',
    'PARENDER',
    'LLAVEIZQ',
    'LLAVEDER',
    'FINDESENTENCIA',
  
)



t_SUMADOR = r'\&'
t_RESTANDO = r'-'
t_MULTIPLICADOR = r'\*'
t_DIVISOR = r'/'
t_MODULO = r'\%'
t_POTENCIADOR = r'(\*{2} | \^)'
t_ASIGNADOR = r'='

t_Y= r'\&\&'
t_O = r'\|{2}'
t_NEGACION= r'\!'
t_ELMENOR = r'<'
t_ELMAYOR = r'>'
t_FINDESENTENCIA = ';'
t_PARENIZQ = r'\('
t_PARENDER = r'\)'
t_LLAVEIZQ = r'{'
t_LLAVEDER = r'}'
t_ignore =' \t'



def t_INCLUIR(t):
    r'incl'
    return t

def t_MOSTRAR(t):
    r'msg'
    return t

def t_LEER(t):
    r'rec'
    return t

def t_NUMERICO(t):
    r'num'
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

def t_MENOROIGUAL(t):
    r'<='
    return t

def t_MAYOROIGUAL(t):
    r'>='
    return t

def t_IGUAL(t):
    r'=='
    return t

def t_DESIGUAL(t):
    r'!='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'\$.*'
    pass

def t_error(t):
    global resultado_lexema
    estado = "Token no valido en la Linea: {:4}     Valor: {:16}    Posicion: {:4}".format(str(t.lineno), str(t.value[0]),str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

class AnalizadorLexico:
    def __init__(self,tokens):
        self.tokens=tokens
    
    def getTokens(self):
        return self.tokens
    
    def prueba(self,data):
        global resultado_lexema
        analizador.input(data)
        resultado_lexema.clear()
        i=1
        print('progreso |', end='')
        while True:
            tok=analizador.token()
            if not tok:
                break
            estado="Linea:  {:4}   Tipo: {:16}   Valor: {:16}    Posicion: {:4}".format(str(tok.lineno),str(tok.type) ,str(tok.value), str(tok.lexpos) )
            resultado_lexema.append(estado)
            if i<=10:
                print('*'*i, end='')
                i=i+1
        print('|')  
        print('*ANALIZIS FINALIZADO*')
        return resultado_lexema
        
analizador = lex.lex()
a=AnalizadorLexico(tokens)

arc=open('holamundo.arc','r')
data=arc.read()
        
a.prueba(data)

ventana=Tk()
ventana.title('Analizador lexico')
ventana.minsize(width=600,height=500)

scrollbar = Scrollbar(ventana)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(ventana)
listbox.pack()
listbox.place(relwidth=0.98, relheight=1)

listbox.insert(END, '                                                                                *ANALIZIS FINALIZADO*')
for toke in resultado_lexema:
    listbox.insert(END, toke)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
 
ventana.mainloop()
     




