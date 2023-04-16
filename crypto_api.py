import os
import pandas as pd
from alpha_vantage.timeseries import TimeSeries

def get_intraday_data(symbol, interval, api_key):
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, _ = ts.get_intraday(symbol=symbol, interval=interval)
    return data

def main():
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    if api_key is None:
        print("No se encontró la clave de API de Alpha Vantage. Asegúrate de configurar la variable de entorno ALPHA_VANTAGE_API_KEY.")
        return

    symbol = 'MSFT'
    interval = '5min'

    intraday_data = get_intraday_data(symbol, interval, api_key)
    print(f"Datos intradía para {symbol} con intervalo de {interval}:")
    print(intraday_data)

if __name__ == '__main__':
    main()
