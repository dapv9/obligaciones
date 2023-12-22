#importar las librerias
from flask import Flask, jsonify
import pandas as pd

# Carga los DataFrames desde los archivos pickle generados en ETL
df_olbigaciones = pd.read_pickle('df_obl_tas.pkl')
df_cliente_total = pd.read_pickle('df_total_cliente.pkl')

#se crea instancia de flask
app = Flask(__name__)

# Endpoint para obtener información del primer DataFrame
@app.route('/api/olbigaciones', methods=['GET'])
def get_olbigaciones():
    return jsonify(df_olbigaciones.to_dict(orient='records'))

# Endpoint para obtener información del segundo DataFrame
@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    return jsonify(df_cliente_total.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)