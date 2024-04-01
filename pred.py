import pandas as pd
def preprocces(features):
    
    price = float(features['0 araç Fiyatı'])
    age = int(features['Araç Yaşı'])
    km_driven = int(features['Kilometre'])
    owner = int(features['Kaçıncı Kullanıcı'])
    fuel_type = features['Yakıt Türü']
    seller_type = features['Satıcı Türü']
    transmission = features['Vites Türü']
    
    if fuel_type == "Petrol":
        p = 1
        d = 0
    elif fuel_type == "Diesel":
        d = 1
        p = 0
    else:
        d = 0
        p = 0
    
    if seller_type == "Individual":
        i = 1
    else:
        i = 0
    
    if transmission == "Manual":
        m = 1
    else:
        m = 0
        
    data = {
        'Present_Price': [price/1000],
        'Kms_Driven': [km_driven],
        'Owner': [owner],
        'Age': [age],
        'Fuel_Type_Diesel': [d],
        'Fuel_Type_Petrol': [p],
        'Seller_Type_Individual' : [i],
        'Transmission_Manual' : [m]
    }
    df = pd.DataFrame(data)
    return df
    