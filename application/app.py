import sys
import os, sys
from flask import Flask, request, jsonify

app = Flask(__name__)

sys.path.append(os.path.join(os.path.dirname(__file__), "."))
from model.calculate_tax import calculate_tax


@app.route("/tax/<salary>", methods=['GET'])
def handle_calculate_tax_req(salary):
    if request.method == 'GET':
        tax_amount = calculate_tax(float(salary))
        return str(tax_amount)

if __name__ == "__main__":
    app.run()