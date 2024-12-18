from flask import Flask, render_template, request, jsonify
# from scraping import get_brand_names, fetch_model_data, extract_models_to_df
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd
import time
from random import randint

BASE_URL = "https://www.carwale.com/api/makepagedata/"
BASE_URL_Model = "https://www.carwale.com/api/modelpagedata/"
VERSION_URL = "https://www.carwale.com/api/v3/versions/"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib.parse


def get_brand_names():
    # Set up Chrome options
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')

    # # Set up the WebDriver
    # service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service, options=chrome_options)
    # print(driver,'driver')
    # if True:
    #     # Navigate to the website
    #     url = 'https://www.carwale.com/' 

    #     # Wait for the page to load
    #     driver.implicitly_wait(10)

    #     # Locate and click "View More Brands" button (retry logic included)
    #     retries = 3
    #     for _ in range(retries):
    #         try:
    #             view_more_button = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="View More Brands"]')
    #             view_more_button.click()
    #             time.sleep(2)  # Wait for expanded content to load
    #             break
    #         except Exception:
    #             time.sleep(2)

    #     # Extract brand names
    #     brand_list = driver.find_elements(By.CSS_SELECTOR, "div.o-bqHweY > div > ul > li")
    #     brand_names = [brand.text.strip() for brand in brand_list if brand.text.strip()]
        brand_names = ['Maruti Suzuki', 'Mahindra', 'Tata', 'Toyota', 'BMW', 'Hyundai', 'Mercedes-Benz', 'Kia', 'Audi', 'Skoda', 'MG', 'Land Rover', 'Porsche', 'Lamborghini', 'Volvo', 'Honda', 'Citroen', 'Volkswagen', 'Ferrari', 'Renault', 'Lexus', 'Maserati', 'Jeep', 'Jaguar', 'Rolls-Royce', 'BYD', 'MINI', 'Nissan', 'Aston Martin', 'McLaren', 'Isuzu', 'VinFast', 'Force Motors', 'Bentley', 'Tesla', 'Lotus', 'Fisker', 'Pravaig', 'OLA', 'Leapmotor']
        return brand_names
    # except:
    # finally:
    #     driver.quit()


def extract_engine(brand_name, model_name, city_id, platform_id=1, retries=3):
    print("Initial Brand Name:", brand_name)
    if " " in brand_name:   
        brand_name= brand_name.replace(" ","-")
    print("Model Masking Name:", model_name)
    if " " in model_name:   
        model_name= model_name.replace(" ","-")
    brand_name=brand_name.lower()
    model_name=model_name.lower()
    

    
    params = {
        "makeMaskingName": brand_name,
        "modelMaskingName": model_name,
        "cityId": city_id,
        "areaId": -1,
        "showOfferUpfront": "false",
        "platformId": platform_id
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    attempt = 0
    while attempt < retries:
        try:
            # Send GET request
            response = requests.get(BASE_URL_Model, headers=headers, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors

            # Print the response JSON
            responses = response.json()
            # print ("aaaaaaaaaaaa",responses)
            # print(responses.get('keySpecs'))
            result = responses.get('keySpecs')[1]['keySpecsValue'][0]['text']
            # print(responses.get('keySpecs')[1]['keySpecsValue'][0]['text'])
            if 'cc' not in result:
                result=responses.get('keySpecs')[2]['keySpecsValue'][0]['text']
            if 'cc' not in result:
                result=responses.get('keySpecs')[3]['keySpecsValue'][0]['text']
            if 'cc' not in result:
                result='N/A'
            return result

        except requests.exceptions.RequestException as e:
            attempt += 1
            # print(f"Attempt {attempt} failed for brand '{brand_name}' and model '{modelMaskingName}': {e}")
            if attempt < retries:
                wait_time = randint(1, 3)
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"Failed to fetch data after {retries} attempts.")
                return None


def fetch_model_data(brand_name, city_id, platform_id=1, retries=3):
    print("Initial Brand Name:", brand_name)

    params = {
        "maskingName": brand_name,
        "cityId": city_id,
        "areaId": -1,
        "platformId": platform_id
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(BASE_URL, headers=headers, params=params)
            response.raise_for_status()
            print("response_of_fetching_model_makepagedata",response.json())
            return response.json()
        except requests.exceptions.RequestException as e:
            attempt += 1
            # print(f"Attempt {attempt} failed for brand '{brand_name}': {e}")
            if attempt < retries:
                wait_time = randint(1, 3)
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                # Modify brand_name on failure
                print("Retry failed, adjusting brand_name...")
                brand_name = brand_name.lower().replace(" ", "-")
                print("Adjusted Brand Name:", brand_name)

                # Retry with adjusted brand_name
                params["maskingName"] = brand_name
                attempt = 0  # Reset attempt counter for retrying with the new brand_name
                
                # Optionally, you could add another retry loop or handle differently here
                continue

    print(f"Failed to fetch data after {retries} attempts.")
    return None

def fetch_variant_data(model_id, city_id, retries=5):
    params = {
        "modelId": model_id,
        "type": "new",  # Assuming you're looking for new versions
        "itemIds": "29,26",  # Example itemIds; modify as needed
        "cityId": city_id,
        "application": 1
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(VERSION_URL, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            attempt += 1
            print(f"Attempt {attempt} failed for model ID '{model_id}': {e}")
            if attempt < retries:
                wait_time = randint(1, 3)
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"Failed to fetch variant data after {retries} attempts for model ID '{model_id}'.")
                return None




def extract_models_to_df(brand_name, brand_data, city_id):
    city_mapping = {
        1: "Mumbai",
        105: "Bangalore"
    }
    city_name = city_mapping.get(city_id, f"{city_id}")  # Default to City ID if no mapping is found
    # print("brand_name",brand_name)
    # print("brand_data",brand_data)

    if 'models' in brand_data:
        models = []
        for model in brand_data['models']:
            # print("wwwwwwwwwwwwwwwwwwwww",model)
            model_name = model.get('offerDetails', {}).get('ModelName', None)
            # print("dddddddddddddd",model_name)
            model_masking_name=model.get('modelMaskingName')
            # print("kfjdelkf",model_masking_name)
            model_id = model.get('modelId', None)
            model_price = model.get('offerDetails', {}).get('formattedPrice', None)
            model_features = model.get('offerDetails', {}).get('priceLabel', None)
            if model_name and model_id:
                # Fetch variants for the current model
                variant_data = fetch_variant_data(model_id, city_id)
                variants = []
                
                for variant in variant_data.get('variants', []):
                    engine_data= extract_engine(brand_name,model_masking_name,city_id)
                    version_name = variant.get('versionName', None)
                    version_id = variant.get('versionId', None)
                    transmission = next((spec['value'] for spec in variant.get('specsSummary', []) if spec['itemName'] == 'Transmission Type'), None)
                    fuel_type = next((spec['value'] for spec in variant.get('specsSummary', []) if spec['itemName'] == 'Fuel Type'), None)
                    price = variant.get('priceOverview', {}).get('formattedPrice', None)  # Example price field
                    exshowroomprice = variant.get('priceOverview', {}).get('exShowRoomPrice', None)  # Example price field
                    features = variant.get('features', None)
                    if version_name and version_id:
                        variants.append({
                            'Brand Name': brand_name,
                            'Model Name': model_name,
                            'Model ID': model_id,
                            'City': city_name,
                            'Variant Name': version_name,
                            'Version ID': version_id,
                            'Transmission Type': transmission,
                            'Fuel Type': fuel_type,
                            'Ex-Showroom Price':exshowroomprice,
                            'On-Road Price': price,
                            'cc':engine_data
                        })

                if variants:
                    models.extend(variants)

        df = pd.DataFrame(models)
        print("___**",df)
        return df
    else:
        print(f"No models data found for brand '{brand_name}'.")
        return None


def main():
    print("Fetching brand names...")
    brand_names = get_brand_names()
    print(f"Fetched brand names: {brand_names}")

    all_models_data = []

    city_id = input("Enter City ID :")

    for brand_name in brand_names:
        print(f"Fetching data for brand: {brand_name}")
        brand_data = fetch_model_data(brand_name, city_id=int(city_id))
        #Loop 
        print(f"Data fetched for {brand_name}: {brand_data}")
        if brand_data:
            df = extract_models_to_df(brand_name, brand_data, city_id=int(city_id))

            if df is not None:
                all_models_data.append(df)
            else:
                print(f"No models found for brand: {brand_name}")
        else:
            print(f"Failed to fetch data for brand: {brand_name}")

    if all_models_data:
        final_df = pd.concat(all_models_data, ignore_index=True)
        print(final_df)

      
    else:
        print("No data to save.")



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_brands', methods=['POST'])
def fetch_brands():
    if True:
        brand_names = get_brand_names()
        return jsonify({'success': True, 'brands': brand_names})
    else: # Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/fetch_models', methods=['POST'])
def fetch_models():
    data = request.json
    city_id = int(data.get('city_id'))
    selected_brands = data.get('brands', [])
    all_models_data = []

    if True:
        for brand_name in selected_brands:
            brand_data = fetch_model_data(brand_name, city_id)
            if brand_data:
                df = extract_models_to_df(brand_name, brand_data, city_id)
                if df is not None:
                    all_models_data.append(df)

        if all_models_data:
            final_df = pd.concat(all_models_data, ignore_index=True)

            # Ensure the static folder exists
            # static_folder = os.path.join(os.getcwd(), 'static')
            # if not os.path.exists(static_folder):
            #     os.makedirs(static_folder)

            # file_path = os.path.join(static_folder, 'all_models_with_variants.csv')
            # final_df.to_csv(file_path, index=False)
            print({
                'success': True,
                'file_path': f'',
                'data': final_df.to_dict(orient='records')  # Return data for preview
            })

            return jsonify({
                'success': True,
                'file_path': f'',
                'data': final_df.to_dict(orient='records')  # Return data for preview
            })
        else:
            return jsonify({'success': False, 'message': 'No data found for the selected brands.'})

    else: #Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)









