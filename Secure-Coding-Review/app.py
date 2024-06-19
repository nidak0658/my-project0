from flask import Flask, request, redirect, jsonify
import string
import random

app = Flask(__name__)

# Dictionary to store mappings of short codes to original URLs
url_map = {}

def generate_short_code():
    """Generate a random short code for URL"""
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))
    return short_code

@app.route('/shorten', methods=['POST'])
def shorten_url():
    """Endpoint to shorten a URL"""
    req_data = request.get_json()
    if 'url' not in req_data:
        return jsonify({'error': 'Missing URL in request body'}), 400

    original_url = req_data['url']
    short_code = generate_short_code()
    url_map[short_code] = original_url

    short_url = request.host_url + short_code
    return jsonify({'short_url': short_url}), 200

@app.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    """Endpoint to redirect to original URL"""
    if short_code not in url_map:
        return jsonify({'error': 'Short URL not found'}), 404

    original_url = url_map[short_code]
    return redirect(original_url, code=302)

if __name__ == '__main__':
    app.run(debug=True)
