from config.database import get_connection

def crear_Tablas():
    conexion = get_connection()
    cursor = conexion.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS clientes (
        dni VARCHAR(8) PRIMARY KEY,
        nombres VARCHAR(100) NOT NULL,
        apellido_paterno VARCHAR(100) NOT NULL,
        apellido_materno VARCHAR(100) NOT NULL,
        direccion VARCHAR(150),
        telefono VARCHAR(20)
    );

    CREATE TABLE IF NOT EXISTS empleados (
        dni VARCHAR(8) PRIMARY KEY,
        nombres VARCHAR(100) NOT NULL,
        apellido_paterno VARCHAR(100) NOT NULL,
        apellido_materno VARCHAR(100) NOT NULL,
        direccion VARCHAR(150),
        telefono VARCHAR(20)
    );

    CREATE TABLE IF NOT EXISTS productos (
        codigo CHAR(4) PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        descripcion VARCHAR(150) NOT NULL,
        stock_minimo int NOT NULL,
        stock_actual int NOT NULL,
        precio_costo NUMERIC(10,2) NOT NULL,
        precio_venta NUMERIC(10,2) NOT NULL,
        proveedor VARCHAR(50),
        almacen VARCHAR(50)
    );

    CREATE TABLE IF NOT EXISTS comprobantes (
        id_comprobante CHAR(5) PRIMARY KEY,
        tipo VARCHAR(20) NOT NULL,
        fecha DATE NOT NULL,
        total NUMERIC(10,2) NOT NULL
    );
    """

    cursor.execute(sql)
    conexion.commit()

    cursor.close()
    conexion.close()

    print("Tablas creadas correctamente")