import requests
import time
def extract_engine():
    model_name="City Hybrid eHEV"
    if " " in model_name:
        model_name= model_name.replace(" ","-")
        model_name=model_name.lower()
   
    print(model_name, "model_name-----------------")
    params = {
        "makeMaskingName": 'maruti-suzuki',
        "modelMaskingName": 'ciaz',
        "cityId": -1,
        "areaId": -1,
        "showOfferUpfront": "false",
        "platformId": 1
    }
    

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    attempt = 0
    while attempt < 3:
        try:
            BASE_URL_Model = "https://www.carwale.com/api/modelpagedata/"
            # Send GET request
            response = requests.get(BASE_URL_Model, headers=headers, params=params)
            response.raise_for_status() 
            responses = response.json()
            print("*****response*******",responses)
        
            print("Keyspec!!!!!!!!!!!!!!!!!",responses.get('keySpecs'))
            responses1=responses.get('keySpecs')[3]['keySpecsValue'][0]['text']
           
            # responses1=responses.get('keySpecs')[2]['keySpecsValue'][0]['text']  Rs. 4668
                    
            
            print("@@@@@@@",responses1)
            return response.json()

        except requests.exceptions.RequestException as e:
            attempt += 1
            # print(f"Attempt {attempt} failed for brand '{brand_name}' and model '{model_name}': {e}")
            if attempt < 3:
                wait_time =  3
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"Failed to fetch data after {3} attempts.")
                return None
extract_engine()



aa={'offerDetails': {'IsOfferAvailable': False, 'Url': '/honda-cars/amaze/?showOfferUpfront=true', 'ModelName': 'Amaze', 'MakeName': 'Honda', 'PageName': 'MakePage', 'Offertext': 'Offers Available', 'ParentWidgetName': 'NewCarModel'}, 'dealerAd': {'campaign': {'id': 25887, 'dealerId': 30385, 'clientId': 29, 'contactName': 'Nexa', 'contactNumber': '08068441441', 'contactEmail': '', 'type': 1, 'actionText': '', 'isEmailRequired': False, 'leadPanel': 0, 'cvlDetails': {'isCvl': False}, 'mutualLeads': False, 'dealerAdminId': 0, 'isTestDriveCampaign': False, 'isTurboMla': False, 'maskingNumberEnabled': False, 'linkText': '', 'ctaLinkText': 'Get EMI Assistance', 'showWhatsappLink': False, 'dealerWhatsappNumber': '', 'targetType': 2, 'isOtpRequired': False, 'isSoftOtpRequired': False, 'hideRecoScreen': False, 'isMultiSelectDealer': False, 'isTurboCrossSell': False, 'brandingType': 1, 'leadHoldingType': 0, 'campaignType': 1, 'shouldShowPreferredLanguageDropdown': False, 'shouldAskBuyingSpan': False, 'isOtpOptional': False, 'isPincodeRequired': False, 'isDealerRequired': False, 'isEmailOptional': False}, 'dealerDetails': {'id': 30385, 'name': 'Carwale Dealer', 'maskingName': 'carwaledealer', 'city': 'Mumbai', 'areaId': 0, 'mobile': '9999999999', 'distance': 0, 'address': 'Automotive Exchange Pvt Ltd, 12th floor, Vishwaroop IT Park,Sector 30A, Vashi', 'latitude': 20.2422, 'longitude': 72.5234, 'categoryType': 5, 'isFinancial': False, 'shouldShowMissedCallText': False, 'uspList': [], 'pincode': '400705', 'dealerDistance': 0.0, 'isFeatured': False, 'cityName': 'Mumbai', 'stateName': 'Maharashtra', 'isPremium': 0, 'cityId': 1, 'stateId': 1, 'isSignatureDealer': False, 'isBackupCampaignDealer': False, 'dealerContactDetails': []}, 'pageProperty': [], 'featuredCarData': {'makeName': 'Honda', 'modelName': 'Amaze', 'originalImgPath': 'https://imgd.aeplcdn.com/664x374/n/cw/ec/184377/amaze-exterior-right-front-three-quarter-3.jpeg?isig=0&q=80', 'makeId': 7, 'modelId': 2959, 'versionId': 18995}, 'location': {'cityId': 244, 'areaId': 0, 'stateId': 0}, 'campaignType': 1}, 'mileageRangeText': '18-19 kmpl', 'maxPowerRangeText': '89 bhp', 'keySpecs': [], 'colors': [], 'isMostPopular': False, 'IsLaunchingSoon': False, 'isSponsored': False, 'versionId': 0, 'basicSpecs': [], 'differentSpecs': [], 'specsSummary': [], 'isSpecialVersion': False, 'trimId': 0, 'sortOrder': 0, 'colorPhotos': [], 'is360Available': False, 'makeId': 7, 'makeName': 'Honda', 'subMakeId': 7, 'subMakeName': 'Honda', 'makeMaskingName': 'honda', 'modelId': 2959, 'modelName': 'Amaze', 'modelMaskingName': 'amaze', 'imagePath': 'https://imgd.aeplcdn.com/664x374/n/cw/ec/184377/amaze-exterior-right-front-three-quarter-3.jpeg?isig=0&q=80', 'status': 2, 'fuelTypeId': 0, 'priceOverview': {'formattedPrice': 'Rs. 8.87 Lakh', 'priceLabel': 'On-Road Price, Chandigarh', 'priceSuffix': 'onwards', 'pricePrefix': '', 'labelColor': 'price-label-text--grey text-light-grey ', 'priceStatus': 1, 'price': 886741, 'exShowRoomPrice': 799900, 'colorType': 0, 'nearByCityId': 0}, 'defaultVariant': 18995, 'confidence': 5, 'launchedOn': '12/04/2024 00:00:00', 'discontinuedOn': '', 'unveiledOn': '', 'modelAggregateRating': 4.7, 'modelReviewCount': 26, 'bodyStyleId': 10, 'rootMaskingName': 'amaze', 'rootName': 'Amaze', 'rootId': 36, 'seoName': 'Amaze', 'brochurePath': 'f/brochure/7/2959/k63fkf8.pdf', 'segmentId': 3, 'makeSeoName': 'Honda', 'isElectricVehicle': False, 'showFullDate': True, 'isBS6Phase2BadgeValid': False, 'subStatus': 1, 'isBookingCampaignAvailable': False}

[{'title': 'Price', 'identifier': 'price', 'keySpecsValue': 
    [{'text': 'Rs. 9.40 Lakh onwards'}], 'itemMasterId': 0}, 
{'title': 'Mileage', 'identifier': '12', 'keySpecsValue': 
    [{'text': '20.04 to 20.65 kmpl'}], 'itemMasterId': 0}, 
{'title': 'Service Cost per Year', 'identifier': 'servicecost', 'keySpecsValue': 
    [{'text': 'Rs. 4668'}], 'tooltipText': "Service Cost/Year calculation: Average of 'Service Cost' for the initial five years.", 'itemMasterId': 0}, 
{'title': 'Engine', 'identifier': '14', 'keySpecsValue': [{'text': '1462 cc'}], 'itemMasterId': 0}, 
{'title': 'Safety', 'identifier': '703', 'keySpecsValue': [{'text': '4 Star (ASEAN NCAP)'}], 'itemMasterId': 0}, 
{'title': 'Fuel Type', 'identifier': '26', 'keySpecsValue': [{'text': 'Petrol'}], 'itemMasterId': 0}, 
{'title': 'Transmission', 'identifier': '29', 'keySpecsValue': [{'text': 'Manual'}, {'text': 'Automatic'}], 'itemMasterId': 0}, 
{'title': 'Seating Capacity', 'identifier': '9', 'keySpecsValue': [{'text': '5'}], 'itemMasterId': 0}]

# print(aa.keys)


