from enum import Enum


class Aritmetica(Enum):
    MAS = 1
    MENOS = 2
    POR = 3
    DIVIDIDO = 4
    MODULO = 5
    POTENCIA = 6


class Relacionales(Enum):
    MAYOR_QUE = 1
    MENOR_QUE = 2
    IGUAL = 3
    DIFERENTE = 4
    MAYORIGUAL_QUE = 5
    MENORIGUAL_QUE = 6


class Logicas(Enum):
    AND = 1
    OR = 2
    NOT = 3


class Expresion(Enum):
    ID = 1
    BOOLEAN = 2
    DECIMAL = 3
    ENTERO = 4
    CADENA = 5
    TABATT = 6
    NEGATIVO = 7


class TipoDato(Enum):
    NUMERICO = 1
    CHAR = 2
    FECHA = 3
    FIELDS = 4
    BOOLEAN = 5


class TipoAlterColumn(Enum):
    NOTNULL = 1
    CAMBIOTIPO = 2


class TipoAlterDrop(Enum):
    CONSTRAINT = 1
    COLUMN = 2


class TipoOpcionales(Enum):
    PRIMARYKEY = 1
    DEFAULT = 2
    NOTNULL = 3
    NULL = 4
    UNIQUE = 5
    CHECK = 6


class Sentencia:
    '''clase abstracta'''


class SCrearBase(Sentencia):
    def __init__(self, owner, mode, replace, exists, id):
        self.id = id
        self.owner = owner
        self.mode = mode
        self.replace = replace
        self.exists = exists


class SShowBase(Sentencia):
    def __init__(self, like, cadena):
        self.like = like
        self.cadena = cadena


class SAlterBase(Sentencia):
    def __init__(self, id, rename, owner, idnuevo):
        self.id = id
        self.rename = rename
        self.owner = owner
        self.idnuevo = idnuevo


class SDropBase(Sentencia):
    def __init__(self, exists, id):
        self.exists = exists
        self.id = id


class STypeEnum(Sentencia):
    def __init__(self, id, lista=[]):
        self.id = id
        self.lista = lista


class SExpresion(Sentencia):
    def __init__(self, valor, tipo):
        self.valor = valor
        self.tipo = tipo


class SOperacion(Sentencia):
    def __init__(self, opIzq, opDer, operador):
        self.opIzq = opIzq
        self.opDer = opDer
        self.operador = operador


class SUpdateBase(Sentencia):
    def __init__(self, id, listaSet=[], listaWhere=[]):
        self.id = id
        self.listaSet = listaSet
        self.listaWhere = listaWhere


class SValSet(Sentencia):
    def __init__(self, columna, valor):
        self.columna = columna
        self.valor = valor


class SDeleteBase(Sentencia):
    def __init__(self, id, listaWhere=[]):
        self.id = id
        self.listaWhere = listaWhere


class STruncateBase(Sentencia):
    def __init__(self, listaIds=[]):
        self.listaIds = listaIds


class SInsertBase(Sentencia):
    def __init__(self, id, listValores=[]):
        self.id = id
        self.listValores = listValores


class SCrearTabla(Sentencia):
    def __init__(self, id, herencia, nodopadre, columnas=[]):
        self.id = id
        self.columnas = columnas
        self.herencia = herencia
        self.nodopadre = nodopadre


class SUse(Sentencia):
    def __init__(self, id):
        self.id = id


class STipoDato(Sentencia):
    def __init__(self, dato, tipo, cantidad):
        self.dato = dato
        self.tipo = tipo
        self.cantidad = cantidad


class SShowTable(Sentencia):
    ''' Show table'''


class SDropTable(Sentencia):
    def __init__(self, id):
        self.id = id


class SAlterTableRenameColumn(Sentencia):
    def __init__(self, idtabla, idcolumna, idnuevo):
        self.idtabla = idtabla
        self.idcolumna = idcolumna
        self.idnuevo = idnuevo


class SAlterTableCheck(Sentencia):
    def __init__(self, idtabla, expresion, idcons):
        self.idtabla = idtabla
        self.expresion = expresion
        self.idcons = idcons


class SAlterTable_AlterColumn(Sentencia):
    def __init__(self, idtabla, columnas=[]):
        self.idtabla = idtabla
        self.columnas = columnas


class SAlterColumn(Sentencia):
    def __init__(self, idcolumna, tipo, valcambio):
        self.idcolumna = idcolumna
        self.tipo = tipo
        self.valcambio = valcambio


class SAlterTableAddColumn(Sentencia):
    def __init__(self, idtabla, ListaColumnas=[]):
        self.idtabla = idtabla
        self.listaColumnas = ListaColumnas


class SNAlterAdd(Sentencia):
    def __init__(self, idcolumna, tipo):
        self.idcolumna = idcolumna
        self.tipo = tipo


class SAlterTableAddUnique(Sentencia):
    def __init__(self, idtabla, idconstraint, idcolumna):
        self.idtabla = idtabla
        self.idconstraint = idconstraint
        self.idcolumna = idcolumna


class SAlterTableAddFK(Sentencia):
    def __init__(self, idtabla, idtablafk,idlocal=[], idfk=[]):
        self.idtabla = idtabla
        self.idtablafk=idtablafk
        self.idlocal = idlocal
        self.idfk = idfk


class SAlterTableDrop(Sentencia):
    def __init__(self, idtabla, tipo, listaColumnas=[]):
        self.idtabla = idtabla
        self.tipo = tipo
        self.listaColumnas = listaColumnas


class SAlterRenameTable(Sentencia):
    def __init__(self, idactual, idnuevo):
        self.idactual = idactual
        self.idnuevo = idnuevo


class SNAlterDrop(Sentencia):
    def __init__(self, idcolumna):
        self.idcolumna = idcolumna


class SColumna(Sentencia):
    def __init__(self, id, tipo, opcionales=[]):
        self.id = id
        self.tipo = tipo
        self.opcionales = opcionales


class SColumnaCheck(Sentencia):
    def __init__(self, id, condicion):
        self.id = id
        self.condicion = condicion


class SColumnaUnique(Sentencia):
    def __init__(self, id=[]):
        self.id = id


class SColumnaPk(Sentencia):
    def __init__(self, id=[]):
        self.id = id


class SColumnaFk(Sentencia):
    def __init__(self, id, idlocal=[], idfk=[]):
        self.id = id
        self.idlocal = idlocal
        self.idfk = idfk


class SOpcionales(Sentencia):
    def __init__(self, tipo, valor, id):
        self.tipo = tipo
        self.valor = valor
        self.id = id


class Squeries(Sentencia):
    def __init__(self, query1, ope, query2):
        self.query1 = query1
        self.ope = ope
        self.query2 = query2


class SQuery(Sentencia):
    def __init__(self, select, ffrom, where, groupby, having, orderby, limit):
        self.select = select
        self.ffrom = ffrom
        self.where = where
        self.groupby = groupby
        self.having = having
        self.orderby = orderby
        self.limit = limit


class SSelectCols(Sentencia):
    def __init__(self, distinct, cols=[]):
        self.distinct = distinct
        self.cols = cols


class SSelectFunc(Sentencia):
    def __init__(self, id):
        self.id = id


class SColumnasAsSelect(Sentencia):
    def __init__(self, id, cols=[]):
        self.id = id
        self.cols = cols


class SColumnasSubstr(Sentencia):
    def __init__(self, st, st2, st3, id):
        self.st = st
        self.st2 = st2
        self.st3 = st3
        self.id = id


class SColumnasGreatest(Sentencia):
    def __init__(self, id, cols=[]):
        self.id = id
        self.cols = cols


class SColumnasLeast(Sentencia):
    def __init__(self, id, cols=[]):
        self.cols = cols
        self.id = id


class SExtract(Sentencia):
    def __init__(self, field, timestampstr):
        self.field = field
        self.timestampstr = timestampstr


class SExtract2(Sentencia):
    def __init__(self, field, dtype, timestampstr):
        self.field = field
        self.dtype = dtype
        self.timestampstr = timestampstr


class SFuncAgregacion(Sentencia):
    def __init__(self, funcion, param):
        self.funcion = funcion
        self.param = param


# 1 parametro
class SFuncMath(Sentencia):
    def __init__(self, funcion, param):
        self.funcion = funcion
        self.param = param


# 2 parametros
class SFuncMath2(Sentencia):
    def __init__(self, funcion, param, param2):
        self.funcion = funcion
        self.param = param
        self.param2 = param2


# sin parametros
class SFuncMathSimple(Sentencia):
    def __init__(self, funcion):
        self.funcion = funcion


# Lista params
class SFuncMathLista(Sentencia):
    def __init__(self, funcion, params=[]):
        self.funcion = funcion
        self.params = params

    # 1 parametro


class SFuncTrig(Sentencia):
    def __init__(self, funcion, param):
        self.funcion = funcion
        self.param = param


# 2 parametros
class SFuncTrig2(Sentencia):
    def __init__(self, funcion, param, param2):
        self.funcion = funcion
        self.param = param
        self.param2 = param2


class SFuncBinary(Sentencia):
    def __init__(self, funcion, param):
        self.funcion = funcion
        self.param = param


class SFuncBinary2(Sentencia):
    def __init__(self, funcion, param, param2):
        self.funcion = funcion
        self.param = param
        self.param2 = param2


class SFuncBinary3(Sentencia):
    def __init__(self, funcion, param, det, param2):
        self.funcion = funcion
        self.param = param
        self.det = det
        self.param2 = param2


class SFuncBinary4(Sentencia):
    def __init__(self, funcion, param, param2, param3):
        self.funcion = funcion
        self.param = param
        self.param2 = param2
        self.param3 = param3


class SFechaFunc(Sentencia):
    def __init__(self, param, param2):
        self.param = param
        self.param2 = param2


class SFechaFunc2(Sentencia):
    def __init__(self, id, param, tipo, param2):
        self.id = id
        self.param = param
        self.tipo = tipo
        self.param2 = param2


class SCase(Sentencia):
    def __init__(self, casos):
        self.casos = casos


class SCaseElse(Sentencia):
    def __init__(self, casos, casoelse):
        self.casos = casos
        self.casoelse = casoelse


class SCaseList(Sentencia):
    def __init__(self, param, param2, clist=[]):
        self.param = param
        self.param2 = param2
        self.clist = clist


class SFrom(Sentencia):
    def __init__(self, clist=[]):
        self.clist = clist


class SFrom2(Sentencia):
    def __init__(self, id, clist=[]):
        self.id = id
        self.clist = clist


class SWhere(Sentencia):
    def __init__(self, clist=[]):
        self.clist = clist


class SGroupBy(Sentencia):
    def __init__(self, slist=[]):
        self.slist = slist


class SLimit(Sentencia):
    def __init__(self, limit, offset):
        self.limit = limit
        self.offset = offset


class SListOrderBy(Sentencia):
    def __init__(self, ascdesc, firstlast, listorder=[]):
        self.ascdesc = ascdesc
        self.firstlast = firstlast
        self.listorder = listorder


class sOrderBy(Sentencia):
    def __init__(self, slist=[]):
        self.slist = slist


class SAlias(Sentencia):
    def __init__(self, id, alias):
        self.id = id
        self.alias = alias


class SWhereCond1(Sentencia):
    def __init__(self, conds=[]):
        self.conds = conds


class SWhereCond2(Sentencia):
    def __init__(self, isnotNull, conds=[]):
        self.isnotNull = isnotNull
        self.conds = conds


class SWhereCond3(Sentencia):
    def __init__(self, tIs, tNot, directiva, conds=[]):
        self.tIs = tIs
        self.tNot = tNot
        self.directiva = directiva
        self.conds = conds


class SWhereCond4(Sentencia):
    def __init__(self, tIs, tNot, distinct, conds=[], ffrom=[]):
        self.tIs = tIs
        self.tNot = tNot
        self.distinct = distinct
        self.conds = conds
        self.ffrom = ffrom


class SWhereCond5(Sentencia):
    def __init__(self, substr, c1=[], c2=[], c3=[]):
        self.substr = substr
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3


class SWhereCond6(Sentencia):
    def __init__(self, tNot, exists, cols=[]):
        self.tNot = tNot
        self.exists = exists
        self.cols = cols


class SWhereCond7(Sentencia):
    def __init__(self, operador, anyallsome, efunc=[], qcols=[]):
        self.operador = operador
        self.anyallsome = anyallsome
        self.efunc = efunc
        self.qcols = qcols


class SWhereCond8(Sentencia):
    def __init__(self, tNot, tIn, efunc=[], qcols=[]):
        self.tNot = tNot
        self.tIn = tIn
        self.efunc = efunc
        self.qcols = qcols


class SWhereCond9(Sentencia):
    def __init__(self, tNot, between, efunc=[], efunc2=[]):
        self.tNot = tNot
        self.between = between
        self.efunc = efunc
        self.efunc2 = efunc2


class SHaving(Sentencia):
    def __init__(self, efunc=[]):
        self.efunc = efunc
