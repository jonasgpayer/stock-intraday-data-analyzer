import os
import argparse
import pandas as pd
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from alpha_vantage.foreignexchange import ForeignExchange

def parse_arguments():
    parser = argparse.ArgumentParser(description='Obtener datos de criptomonedas y tasas de cambio')
    parser.add_argument('symbol', type=str, help='Símbolo de la criptomoneda')
    parser.add_argument('market', type=str, help='Moneda en la que se cotiza la criptomoneda')
    return parser.parse_args()

def get_crypto_data(symbol, market, api_key):
    cc = CryptoCurrencies(key=api_key, output_format='pandas')
    data, _ = cc.get_digital_currency_daily(symbol=symbol, market=market)
    return data

def get_exchange_rates(api_key):
    fx = ForeignExchange(key=api_key, output_format='pandas')
    usd_to_eur, _ = fx.get_currency_exchange_rate(from_currency='USD', to_currency='EUR')
    return float(usd_to_eur['5. Exchange Rate'])

def main():
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    if api_key is None:
        print("No se encontró la clave de API de Alpha Vantage. Asegúrate de configurar la variable de entorno ALPHA_VANTAGE_API_KEY.")
        return

    args = parse_arguments()
    symbol = args.symbol
    market = args.market

    crypto_data = get_crypto_data(symbol, market, api_key)
    usd_to_eur_rate = get_exchange_rates(api_key)

    print(f"Datos diarios de la criptomoneda {symbol} en el mercado {market}:")
    print(crypto_data)
    print(f"Tasa de cambio actual de USD a EUR: {usd_to_eur_rate}")

if __name__ == '__main__':
    main()

