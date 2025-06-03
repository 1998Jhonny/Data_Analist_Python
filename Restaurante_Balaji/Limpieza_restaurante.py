#Columnas:

#-order_id: identificador único para cada pedido.
#-date: fecha de la transacción.
#-item_name: nombre del alimento.
#-item_type: categoría del artículo (comida rápida o bebidas).
#-item_price: precio del artículo por unidad.
#-Quantity: cantidad que pide el cliente.
#-transaction_amount: importe total pagado por los clientes.
#-transaction_type: método de pago (efectivo, online, otros).
#-received_by: género de la persona que realiza la transacción.
#-time_of_sale: diferentes horas del día (mañana, tarde, noche, medianoche).

#importar libreria pandas
import pandas as pd
from datetime import datetime

#Importar el archivo
data = pd.read_csv('Balaji Fast Food Sales.csv')

#Revisar el número de registros y de campos
data.shape

#Información general del DataFrame
data.info()

#Estadisticas de los campos de valor cuantitativos
data.describe()

#cantidad de registros por columna
#Aquí se valida si hay valores NULL o Nan o mejor dicho si faltan valores
data.count()

#Para este caso los vamos a eliminar los valores nulos ya que aquellos que faltan son de tipo <>str
data.dropna(inplace=True)

#Nuevamente miramos el total de datos por campo
data.count()

data.describe()

#Necesito coger los nombres de las columnas
#Precisamente de los tipo <>str
data.columns

#Creamos unal lista con las columnas que son cualitativas
data_colums = ['item_name', 'item_type', 'transaction_type', 'received_by', 'time_of_sale']

#Por cada columna de data_colums necesito que imprima cuantos subniveles tiene dicha variable

for colm in data_colums:
    print(f"columna {colm}: {data[colm].nunique()} subniveles")

#Eliminar filas repetidas
print(f"filas antes de eliminar filas duplicas: {data.shape}")
data.drop_duplicates(inplace=True)
print(f"filas después de eliminar filas duplicas: {data.shape}")

data['item_name'].unique()

#Validar cuales son los valores únicos para corregir errores o duplicados
for columna in data_colums:
    valores_unicos = data[columna].unique()
    print(f"Columna: {columna}")
    print(f"Valores únicos ({len(valores_unicos)}): {valores_unicos}\n")


# Convertir la columna 'date' a datetime
def convertir_fecha(fecha_str):
    try:
        return datetime.strptime(fecha_str, '%d/%m/%Y')  # Día/Mes/Año
    except ValueError:
        try:
            return datetime.strptime(fecha_str, '%m/%d/%Y')  # Mes/Día/Año
        except ValueError:
            return pd.NaT  # Si falla, marca como fecha inválida

# Aplica la función a la columna correcta
data['fecha_datetime'] = data['date'].apply(convertir_fecha)

#Validar los cambios realizados principalmente el del tipo de fecha en la variable date
data.info()

#Exportar el archivo con la limpieza realizada
data.to_csv('Balaji_clean.csv', index=False)

