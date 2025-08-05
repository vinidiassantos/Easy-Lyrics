from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # permite acesso da sua app web

@app.route('/parse-cifra', methods=['POST'])
def parse_cifra():
    data = request.get_json()
    url = data.get('url')

    if not url or 'cifraclub.com.br' not in url:
        return jsonify({'error': 'URL inválida'}), 400

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # CifraClub usa <pre class="cifra"> para o conteúdo
        cifra_tag = soup.find('pre', class_='cifra')

        if not cifra_tag:
            return jsonify({'error': 'Cifra não encontrada'}), 404

        texto_cifra = cifra_tag.get_text()

        return jsonify({'cifra': texto_cifra})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
