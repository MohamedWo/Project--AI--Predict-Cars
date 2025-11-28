import pandas as pd
import streamlit as st
import pickle

st.title('Car Price Prediction')
st.sidebar.header('Feature Selecting')
st.sidebar.info('Enter the car features to predict its price')
st.image('https://wallpapercave.com/wp/wp6404610.jpg')

# --------------------- رفع الموديل ---------------------
uploaded_file = st.file_uploader("اختر ملف الموديل (.sav)", type="sav")

if uploaded_file is not None:
    data = pickle.load(uploaded_file)
    st.success("تم تحميل الموديل بنجاح!")

    # --------------------- إدخال بيانات المستخدم ---------------------
    manu_code = st.number_input("ادخل كود المصنع (مثال: LEXUS=8, CHEVROLET=4)", min_value=0)
    model_code = st.number_input("ادخل كود الموديل", min_value=0)
    category_code = st.number_input("ادخل كود نوع العربية", min_value=0)
    leather_code = st.number_input("ادخل كود الجلد (yes=1, no=2)", min_value=1, max_value=2)
    fuel_code = st.number_input("ادخل كود نوع الوقود", min_value=0)
    mileage = st.number_input("ادخل عدد الكيلومترات", min_value=0)
    gear_code = st.number_input("ادخل كود نوع الجير", min_value=0)
    drive_code = st.number_input("ادخل كود نظام الدفع", min_value=0)
    wheel_code = st.number_input("ادخل كود نوع عجلة القيادة", min_value=0)
    color_code = st.number_input("ادخل كود اللون", min_value=0)
    levy = st.number_input("ادخل قيمة الضرائب/الرسوم", min_value=0)
    engine = st.number_input("ادخل حجم الموتور (مثال: 1.3, 2.5)", min_value=0.0, format="%.1f")
    airbags = st.number_input("ادخل عدد الوسائد الهوائية", min_value=0)
    age = st.number_input("ادخل عمر العربية بالسنين", min_value=0)
    
    # --------------------- إعداد DataFrame ---------------------
    df = pd.DataFrame({
        'Manufacturer':[manu_code],
        'Model':[model_code],
        'Category':[category_code],
        'Leather interior':[leather_code],
        'Fuel type':[fuel_code],
        'Mileage':[mileage],
        'Gear box type':[gear_code],
        'Drive wheels':[drive_code],
        'Wheel':[wheel_code],
        'Color':[color_code],
        'Levy':[levy],
        'Engine volume':[engine],
        'Cylinders':[4],
        'Airbags':[airbags],
        'Age':[age]
    })

    # --------------------- التنبؤ ---------------------
    if st.sidebar.button('Predict Price'):
        prediction = data.predict(df)
        st.sidebar.success(f"Predicted Price: {prediction[0]:,.2f} $")
