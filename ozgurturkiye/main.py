from flask import Flask, jsonify
import parse_tcmb
import tcmb_parsed
import dolar
import euro
import generic_manipulate


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "This web API is about the exchange rate currency"


@app.route('/start_parse')
def get_all_exchange_rate():
    exchange_rates = parse_tcmb.get_tcmb_exchange_rates()
    return jsonify(exchange_rates)


@app.route('/exchange_rates')
def get_exchange_rates():
    parsed = tcmb_parsed.get_json_file()
    return jsonify(parsed)


@app.route('/dolar')
def get_dolar_rate():
    parsed = dolar.manipulate_dolar()
    return jsonify(parsed)


@app.route('/euro')
def get_euro_rate():
    parsed = euro.manipulate_euro()
    return jsonify(parsed)


@app.route('/<exchange_code>')
def get_generic_rate(exchange_code):
    parsed = generic_manipulate.get_generic(exchange_code)
    return jsonify(parsed)


if __name__ == "__main__":
    app.run(debug=True)