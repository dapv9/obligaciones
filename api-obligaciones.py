#importar las librerias
from flask import Flask, jsonify
import pandas as pd

# Carga los DataFrames desde los archivos pickle generados en ETL
df_olbigaciones = pd.read_pickle('df_obl_tas.pkl')
df_cliente_total = pd.read_pickle('df_total_cliente.pkl')

#se crea instancia de flask
app = Flask(__name__)

# Ruta por defecto
@app.route('/', methods=['GET'])
def inicio():
    return 'api para consultar obligaciones y clientes \n Obligaciones: /api/olbigaciones \n Clientes: /api/clientes'

# ruta para obtener información del DataFrame con las obligaciones de los clientes
@app.route('/api/olbigaciones', methods=['GET'])
def get_olbigaciones():
    return jsonify(df_olbigaciones.to_dict(orient='records'))

# ruta para obtener información del DataFrame de los clientes con el valor total de sus obligaciones
@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    return jsonify(df_cliente_total.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)