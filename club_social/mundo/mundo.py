from club_social.mundo.errores import SocioNoExistenteError, SocioExistenteError


class Factura:

    def __init__(self, concepto: str, valor: float, autorizado: str = ""):
        """
        Inicializa una factura de un socio

        Args:
            concepto: un str que describe el concepto del consumo
            valor: un float indica el valor del consumo
            autorizado: Opcional. Un str que indica el nombre del autorizado que hizo el consumo
        """

        self.concepto: str = concepto
        self.valor: float = valor
        self.autorizado: str = autorizado

    def __str__(self):
        return f"{self.concepto} - valor: {self.valor} - autorizado: {self.autorizado}"

class Socio:
    """
    Clase que representa un socio del club social

    Attributes:
        cedula: un str que indica la identificación del socio
        nombre: un str que indica el nombre del socio
        autorizados: una lista de str que contiene los nombres de los autorizados del socio
        facturas: una lista de objetos de la clase Factura que contiene los consumos del socio y sus autorizados
    """

    def __init__(self, cedula: str, nombre: str):
        self.cedula: str = cedula
        self.nombre: str = nombre
        self.autorizados = list()
        self.facturas = list()

    def agregar_autorizado(self, autorizado: str):
        """
        Agrega un autorizado a la lista de autorizados del socio

        Args:
            autorizado: un str con el nombre del autorizado que se quiere agregar
        """
        self.autorizados.append(autorizado)

    def eliminar_factura(self, factura: Factura):
        self.facturas.remove(factura)

    def agregar_factura(self, concepto: str, valor: float, autorizado: str = ""):
        factura = Factura(concepto, valor, autorizado)
        self.facturas.append(factura)
        return  factura

    def __str__(self):
        return f"({self.cedula}) {self.nombre}"


class Club:
    """
    Clase que representa el club social

    Attributes:
        socios: Un diccionario que contiene la lista de socios, donde la cédula es la clave.
    """

    def __init__(self):
        self.socios = dict()

    def registrar_autorizado_por_socio(self, cedula_socio: str, nombre_autorizado: str):
        """

        :param cedula_socio:
        :param nombre_autorizado:
        :return:
        """
        socio = self.buscar_socio(cedula_socio)
        if socio is not None:
            socio.agregar_autorizado(nombre_autorizado)
        else:
            raise SocioNoExistenteError(cedula_socio, f"No existe un socio con la cédula {cedula_socio}")


    def buscar_socio(self, cedula: str) -> Socio:
        """
        Busca un socio dada una cédula

        Args:
            cedula: un str con la cédula del socio que se quiere buscar

        Returns:
            Un objeto de la clase Socio o None si no existe ningún socio con la cédula dada
        """
        if cedula in self.socios.keys():
            return self.socios[cedula]
        else:
            return None

    def pagar_factura(self, cedula_socio: str, factura: Factura):
        socio = self.buscar_socio(cedula_socio)
        if socio is not None:
            socio.eliminar_factura(factura)
        else:
            raise SocioNoExistenteError(cedula_socio, f"No existe un socio con la cédula {cedula_socio}")

    def afiliar_socio_al_club(self, cedula_socio: str, nombre_socio: str):
        socio = self.buscar_socio(cedula_socio)
        if socio is None:
            socio = Socio(cedula_socio, nombre_socio)
            self.socios[cedula_socio] = socio
            return socio
        else:
            raise SocioExistenteError(cedula_socio, f"Ya existe un socio con la cédula {cedula_socio}")

    def registrar_consumo_a_socio(self, cedula_socio: str, concepto: str, valor: float, autorizado: str = ""):
        socio = self.buscar_socio(cedula_socio)
        if socio is not None:
            socio.agregar_factura(concepto, valor, autorizado)
        else:
            raise SocioNoExistenteError(cedula_socio, f"No existe un socio con la cédula {cedula_socio}")
