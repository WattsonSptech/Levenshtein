from emojis import EMOJIS

PALAVRAS_BAIXO_CALAO = [
    "merda", "porra", "caralho", "bosta", "cu", "puta", "desgraca", "viado", "corno",
    "cacete", "imundo", "arrombado", "idiota", "bunda", "fodase", "foda-se", "fudido",
    "lixo", "buceta", "pinto", "pau", "penis", "fuder"
]

ABREVIACOES = [
    "vc", "pq", "blz", "mt", "td", "qq", "vlw", "flw", "tbm", "kd", "hj", "pprt", "msg",
    "zap", "pqp", "fdp", "krl", "slk", "bct", "tmnc", "pnc"
]

VAZIO = [' ', '\t', '\r', '\n', '\v', '\f']

SIMBOLOS = [',', '.', '?', '!', ':', ';', '(', ')', '{', '}', '[', ']', '/', '\\', '+', '-', '*', '%', '&', '#', '@', '|']

NUMEROS = ['0123456789']

PREPOSICOES = ['a', 'ante', 'apos', 'ate', 'com', 'contra', 'de', 'desde', 'em', 'entre', 'para', 'perante', 'por', 'sem', 'sob', 'sobre', 'tras']

ARTIGOS = ["o", "a", "os", "as", "um", "uma", "uns", "umas"]

CONECTIVOS = [
    "alem", "disso", "ademais", "outrossim",
    "exceto", "mas", "contudo", "todavia", "entretanto", "embora",
    "certamente", "indubitavelmente", "certeza", "duvida", "inegavelmente",
    "com", "fim", "intuito",
    "suma", "portanto", "assim", "logo", "desse", "modo",
    "porque", "pois", "visto", "portanto",
    "principio", "priori", "sobretudo", "primeiramente",
    "seguida", "frequentemente", "eventualmente", "vezes", "enquanto",
    "segundo", "conforme",
    "se", "caso",
    "talvez", "possivelmente", "provavelmente", "provavel",
    "inesperadamente", "subito", "subitamente", "repente", "surpreendentemente",
    "exemplo", "isto", "seja", "alias",
    "proximo", "aqui", "adiante", "perto", "acola",
    "ou", "quer", "ora"
]

PALAVRAS_NAO_UTILIZADAS = [(EMOJIS[i]['emoji'] for i in range(len(EMOJIS))), PALAVRAS_BAIXO_CALAO, ABREVIACOES, VAZIO, SIMBOLOS, NUMEROS, PREPOSICOES, ARTIGOS, CONECTIVOS]

# Caso a palavra seja um intensificador, deve aumentar o valor da variável 'multiplicador' do arquivo main em +1
# exemplos:
# "muito bom" -> multiplicador = 2x

INTENSIFICADORES_POSITIVOS = [
    "muito", "bastante", "extremamente", "totalmente", "completamente",
    "super", "demais", "intensamente", "altamente", "notavelmente", "bem" 
]

INTENSIFICADORES_NEGATIVOS = [
    "pouco", "minimamente", "raramente", "quase", "levemente", "insuficientemente", 
    "moderadamente", "vagamente", "apenas", "parcialmente", "limitadamente"
]

# Determinam sentimentos positivos
PALAVRAS_BOAS = [
    "legal", "bom", "otimo", "excelente", "incrivel", "fantastico",
    "maravilhoso", "eficiente", "divertido", "agradavel", "positivo",
    "impressionante", "top", "genial", "show", "confiavel", "surpreendente",
    "brilhante"
]

# Determinam sentimentos negativos
PALAVRAS_RUINS = [
    "ruim", "terrivel", "abominavel", "fraco", "inutil", "incompetencia",
    "horrivel", "pessimo", "decepcionante", "lento", "mentiroso", "enganoso", 
    "insuportavel", "ridiculo", "desagradavel", "negativo", "fracasso", "problematico",
    "demorado", "mal", "mau"
]