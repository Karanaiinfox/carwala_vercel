from flask import Flask, render_template, request, jsonify
from scraping import get_brand_names, fetch_model_data, extract_models_to_df
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_brands', methods=['POST'])
def fetch_brands():
    try:
        brand_names = get_brand_names()
        return jsonify({'success': True, 'brands': brand_names})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})


from flask import send_from_directory

@app.route('/download_file/<path:filename>', methods=['GET'])
def download_file(filename):
    static_folder = os.path.join(os.getcwd(), 'static')
    return send_from_directory(static_folder, filename, as_attachment=True)




@app.route('/fetch_models', methods=['POST'])
def fetch_models():
    data = request.json
    city_id = int(data.get('city_id'))
    selected_brands = data.get('brands', [])
    all_models_data = []

    try:
        for brand_name in selected_brands:
            brand_data = fetch_model_data(brand_name, city_id)
            if brand_data:
                df = extract_models_to_df(brand_name, brand_data, city_id)
                if df is not None:
                    all_models_data.append(df)

        if all_models_data:
            final_df = pd.concat(all_models_data, ignore_index=True)

            # Ensure the static folder exists
            static_folder = os.path.join(os.getcwd(), 'static')
            if not os.path.exists(static_folder):
                os.makedirs(static_folder)

            file_path = os.path.join(static_folder, 'all_models_with_variants.csv')
            final_df.to_csv(file_path, index=False)

            return jsonify({
                'success': True,
                'file_path': f'/download_file/all_models_with_variants.csv',
                'data': final_df.to_dict(orient='records')  # Return data for preview
            })
        else:
            return jsonify({'success': False, 'message': 'No data found for the selected brands.'})

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
