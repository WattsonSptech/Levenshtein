from utils.emojis import EMOJIS, IMAGENS_EMOJIS

PALAVRAS_BAIXO_CALAO = [
    "merda", "porra", "caralho", "bosta", "cu", "puta", "desgraca", "viado", "corno",
    "cacete", "imundo", "imunda", "arrombado", "idiota", "bunda", "fodase", "foda-se", "fudido",
    "lixo", "buceta", "pinto", "pau", "penis", "fuder", "ovo", "energumeno", "caguei",
    "fetido", "bossal", "boboca", "safado", "safada", "vadia", "piranha", "tonto", "tanso",
    "panaca", "filho", "bolas", "punheta", "punhetacao"
]

ABREVIACOES = [
    "vc", "vcs", "pq", "blz", "mt", "td", "qq", "vlw", "flw", "tbm", "kd", "hj", "pprt", "msg",
    "msgs", "zap", "pqp", "fdp", "krl", "slk", "bct", "tmnc", "pnc", "hrs", "hs"
]

VAZIO = ['', ' ', '\t', '\r', '\n', '\v', '\f']

SIMBOLOS = [',', '.', '?', '!', ':', ';', '(', ')', '{', '}', '[', ']', '/', '\\', '+', '-', '*', '%', '&', '#', '@', '|']

NUMEROS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

PREPOSICOES = ['a', 'ante', 'apos', 'ate', 'com', 'contra', 'de', 'do', 'da', 'dos', 'das', 'desde', 'em', 'no', 'na', 'nos', 'nas', 'entre', 'para', 'perante', 'por', 'sem', 'sob', 'sobre', 'tras']

PRONOMES = [
    "eu", "tu", "ele", "ela", "nos", "vos", "eles", "elas", 
    "meu", "minha", "meus", "minhas", "teu", "tua", "teus", "tuas", "seu", "sua", "seus", "suas", "nosso", "nossa", "nossos", "nossas", "vosso", "vossa", "vossos", "vossas" 
    "este", "essa", "aquele", "aqui", "ali", "la",
    "quem", "qual", "que", "onde", "quando", "como",
    "o qual", "cujo",
    "algum", "bastante", "outro", "todo", "nenhum", "cada", "ninguem", "algo",
    "me", "te", "se",
    "vossa", "majestade", "excelencia", "senhoria"
]

ARTIGOS = ["o", "a", "os", "as", "um", "uma", "uns", "umas"]

CONECTIVOS = [
    "alem", "disso", "ademais", "outrossim",
    "exceto", "mas", "contudo", "todavia", "entretanto", "embora",
    "certamente", "indubitavelmente", "certeza", "duvida", "inegavelmente",
    "com", "fim", "intuito", "que", "e", "ja", "tem",
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

PALAVRAS_NAO_UTILIZADAS = IMAGENS_EMOJIS + PRONOMES + PALAVRAS_BAIXO_CALAO + ABREVIACOES + VAZIO + SIMBOLOS + NUMEROS + PREPOSICOES + ARTIGOS + CONECTIVOS

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
    "sim", "legal", "bom", "otimo", "otima", "excelente", "incrivel", "fantastico",
    "maravilhoso", "maravilhosa", "eficiente", "divertido", "divertida", "agradavel", "positivo",
    "impressionante", "top", "genial", "show", "confiavel", "surpreendente", "brilhante"
]

# Determinam sentimentos negativos
PALAVRAS_RUINS = [
    "ruim", "terrivel", "abominavel", "fraco", "inutil", "incompetencia",
    "horrivel", "pessimo", "pessima", "decepcionante", "lento", "mentiroso", "enganoso", 
    "insuportavel", "ridiculo", "ridicula", "desagradavel", "negativo", "negativa", "fracasso", "problematico",
    "problematica", "demorado", "demorada", "mal", "mau", "descaso", "nao", "lamentavel", "horroroso", "horrorosa", "estresse",
    "estresso", "maluco", "problema", "problemao", "problemasso", "probleminha", "precario", "precarizar", "precarizaram",
    "precarizacao", "insustentavel", "triste", "tristeza", "chato", "chata", "inferno", "odio", "prejuizo", "desastre",
    "nada", "culpa", "risco"
]