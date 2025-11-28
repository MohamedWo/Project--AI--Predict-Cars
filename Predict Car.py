# import pandas as pd
# import streamlit as st
# import pickle

# st.title('Car Price Prediction')
# st.sidebar.header('Feature Selecting')
# st.sidebar.info('أدخل بيانات السيارة للتنبؤ بالسعر')
# st.image('https://wallpapercave.com/wp/wp6404610.jpg')

# # --------------------- تحميل الموديل من ملف محلي ---------------------
# with open("Car_Predict.sav", "rb") as f:
#     model = pickle.load(f)

# # --------------------- إدخال بيانات المستخدم ---------------------
# # يمكنك تغيير القوائم هنا لتكون باللغة العربية حسب الحاجة
# manufacturers = ['LEXUS', 'CHEVROLET', 'HONDA', 'FORD', 'HYUNDAI', 'TOYOTA']
# models = ['RX 450', 'Equinox', 'FIT', 'E 230 124', 'RX 450 F SPORT', 'Prius C aqua']
# categories = ['Jeep', 'Hatchback', 'Sedan', 'Microbus', 'Goods wagon']
# leathers = ['yes', 'no']
# fuels = ['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG', 'Hydrogen']
# gear_boxes = ['Automatic', 'Tiptronic', 'Variator', 'Manual']
# drives = ['4x4', 'Front', 'Rear']
# wheels = ['Left wheel', 'Right-hand drive']
# colors = ['Silver', 'Black', 'White', 'Grey', 'Blue']

# manu = st.selectbox('المصنع', manufacturers)
# model_sel = st.selectbox('الموديل', models)
# category = st.selectbox('نوع العربية', categories)
# leather = st.selectbox('الجلد', leathers)
# fuel = st.selectbox('نوع الوقود', fuels)
# mileage = st.number_input('عدد الكيلومترات', min_value=0)
# gear = st.selectbox('نوع الجير', gear_boxes)
# drive = st.selectbox('نظام الدفع', drives)
# wheel = st.selectbox('عجلة القيادة', wheels)
# color = st.selectbox('اللون', colors)
# levy = st.number_input('قيمة الضرائب/الرسوم', min_value=0)
# engine = st.number_input('حجم الموتور', min_value=0.0, format="%.1f")
# airbags = st.number_input('عدد الوسائد الهوائية', min_value=0)
# age = st.number_input('عمر العربية بالسنين', min_value=0)

# # --------------------- تحويل البيانات إلى أكواد (إن أردت) ---------------------
# # هذه القيم يجب أن تكون متوافقة مع ما تدرب عليه الموديل
# manu_map = {'LEXUS':8, 'CHEVROLET':4, 'HONDA':9, 'FORD':38, 'HYUNDAI':20, 'TOYOTA':40}
# model_map = {'RX 450':276, 'Equinox':262, 'FIT':649, 'E 230 124':575, 'RX 450 F SPORT':664, 'Prius C aqua':106}
# category_map = {'Jeep':3, 'Hatchback':4, 'Sedan':8, 'Microbus':9, 'Goods wagon':6}
# leather_map = {'yes':1, 'no':2}
# fuel_map = {'Hybrid':4, 'Petrol':2, 'Diesel':1, 'CNG':5, 'Plug-in Hybrid':3, 'LPG':0, 'Hydrogen':0}
# gear_map = {'Automatic':3, 'Tiptronic':0, 'Variator':2, 'Manual':1}
# drive_map = {'4x4':1, 'Front':0, 'Rear':2}
# wheel_map = {'Left wheel':0, 'Right-hand drive':1}
# color_map = {'Silver':1, 'Black':6, 'White':4, 'Grey':13, 'Blue':8}

# # --------------------- إنشاء DataFrame ---------------------
# df = pd.DataFrame({
#     'Manufacturer':[manu_map[manu]],
#     'Model':[model_map[model_sel]],
#     'Category':[category_map[category]],
#     'Leather interior':[leather_map[leather]],
#     'Fuel type':[fuel_map[fuel]],
#     'Mileage':[mileage],
#     'Gear box type':[gear_map[gear]],
#     'Drive wheels':[drive_map[drive]],
#     'Wheel':[wheel_map[wheel]],
#     'Color':[color_map[color]],
#     'Levy':[levy],
#     'Engine volume':[engine],
#     'Cylinders':[4],  # يمكنك إضافة إدخال من المستخدم إذا أردت
#     'Airbags':[airbags],
#     'Age':[age]
# })

# # --------------------- التنبؤ ---------------------
# if st.sidebar.button('تنبؤ بالسعر'):
#     price = model.predict(df)
#     st.success(f"سعر السيارة المتوقع: {price[0]:,.2f} $")







import pandas as pd
import streamlit as st

st.title('Car Price Prediction (Demo)')
st.sidebar.header('Feature Selecting')
st.sidebar.info('ادخل مواصفات السيارة لتقدير السعر تقريبيًا')

st.image('https://wallpapercave.com/wp/wp6404610.jpg')

# --------------------- إدخال بيانات المستخدم ---------------------
manu = st.selectbox("اختر الشركة المصنعة", ["LEXUS", "HONDA", "TOYOTA", "BMW", "MERCEDES"])
model = st.text_input("ادخل موديل السيارة")
category = st.selectbox("اختر نوع السيارة", ["Sedan", "SUV", "Hatchback", "Pickup"])
leather = st.radio("جلد داخلي؟", ["Yes", "No"])
fuel = st.selectbox("نوع الوقود", ["Petrol", "Diesel", "Hybrid"])
mileage = st.number_input("عدد الكيلومترات", min_value=0)
gear = st.selectbox("نوع الجير", ["Automatic", "Manual"])
drive = st.selectbox("نظام الدفع", ["4x4", "Front", "Rear"])
wheel = st.selectbox("نوع عجلة القيادة", ["Left", "Right"])
color = st.selectbox("لون السيارة", ["White", "Black", "Silver", "Red", "Blue"])
levy = st.number_input("الضرائب/الرسوم", min_value=0)
engine = st.number_input("حجم المحرك (مثال 1.6, 2.0)", min_value=0.0, format="%.1f")
airbags = st.number_input("عدد الوسائد الهوائية", min_value=0)
age = st.number_input("عمر السيارة بالسنين", min_value=0)

# --------------------- حساب السعر التجريبي ---------------------
def demo_price_prediction(df):
    # قاعدة مبسطة: سعر أساسي + زيادة حسب المحرك والموديل والنوع
    base_price = 5000
    base_price += engine * 3000           # تأثير حجم المحرك
    base_price += airbags * 200           # تأثير عدد الوسائد
    base_price += 1000 if leather=="Yes" else 0
    base_price += levy
    base_price -= age * 500                # انخفاض السعر مع العمر
    base_price -= mileage * 0.1            # انخفاض السعر حسب المسافة
    return round(base_price, 2)

# --------------------- إعداد DataFrame ---------------------
df = pd.DataFrame({
    'Manufacturer':[manu],
    'Model':[model],
    'Category':[category],
    'Leather interior':[leather],
    'Fuel type':[fuel],
    'Mileage':[mileage],
    'Gear box type':[gear],
    'Drive wheels':[drive],
    'Wheel':[wheel],
    'Color':[color],
    'Levy':[levy],
    'Engine volume':[engine],
    'Cylinders':[4],
    'Airbags':[airbags],
    'Age':[age]
})

# --------------------- زر التنبؤ ---------------------
if st.sidebar.button('Predict Price'):
    price = demo_price_prediction(df)
    st.sidebar.success(f"Estimated Price: ${price:,}")
