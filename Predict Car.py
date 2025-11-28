# import pandas as pd 
# import streamlit as st
# import pickle

# # python -m streamlit run "Predict Car.py"  To let python work


# # data = pickle.load(open(r"C:\Users\jddkd\Downloads\Car_Predict.sav", "rb"))

# import pickle

# with open("Car_Predict.sav", "rb") as f:
#     data = pickle.load(f)


# st.title('Car price Prediction')
# st.sidebar.header('Feature selecting')

# st.sidebar.info('Easy Application For Predicting Cares_Price')



# st.image('https://wallpapercave.com/wp/wp6404610.jpg')


# #__________________-_____________________________________________________


# m1=['LEXUS', 'CHEVROLET', 'HONDA', 'FORD', 'HYUNDAI', 'TOYOTA',
#        'MERCEDES-BENZ', 'OPEL', 'PORSCHE', 'BMW', 'JEEP', 'VOLKSWAGEN',
#        'AUDI', 'RENAULT', 'NISSAN', 'SUBARU', 'DAEWOO', 'KIA',
#        'MITSUBISHI', 'SSANGYONG', 'MAZDA', 'GMC', 'FIAT', 'INFINITI',
#        'ALFA ROMEO', 'SUZUKI', 'ACURA', 'LINCOLN', 'VAZ', 'GAZ',
#        'CITROEN', 'LAND ROVER', 'MINI', 'DODGE', 'CHRYSLER', 'JAGUAR',
#        'ISUZU', 'SKODA', 'DAIHATSU', 'BUICK', 'TESLA', 'CADILLAC',
#        'PEUGEOT', 'BENTLEY', 'VOLVO', 'სხვა', 'HAVAL', 'HUMMER', 'SCION',
#        'UAZ', 'MERCURY', 'ZAZ', 'ROVER', 'SEAT', 'LANCIA', 'MOSKVICH',
#        'MASERATI', 'FERRARI', 'SAAB', 'LAMBORGHINI', 'ROLLS-ROYCE',
#        'PONTIAC', 'SATURN', 'ASTON MARTIN', 'GREATWALL']


# m2=[ 8,  4,  9, 38, 20, 40, 29, 25, 44, 36, 47, 23, 14, 24, 35, 19,  6,
#         3, 37, 17, 26, 12, 46, 22,  2, 16, 13,  0, 39, 11, 33, 45, 18, 34,
#        27, 42,  7, 43, 32, 10, 28, 15, 21, 30, 41,  1, 31,  5]





# manu_maping=dict(zip(m1,m2))

# manu1=st.selectbox("Manufacturer",m1)
# manu2=manu_maping[manu1]
# #_________________________________



# #_________________________________

# mm1 = ['RX 450', 'Equinox', 'FIT', 'E 230 124', 'RX 450 F SPORT', 'Prius C aqua']

# mm2 = [276, 262, 649, 575, 664, 106]

# Model_maping = dict(zip(mm1, mm2))

# Model1 = st.selectbox("Model", mm1)

# Model = Model_maping[Model1]  

# #______________________________________

# c1=['Jeep', 'Hatchback', 'Sedan', 'Microbus', 'Goods wagon',
#        'Universal', 'Coupe', 'Minivan', 'Cabriolet', 'Limousine',
#        'Pickup']

# c2=[3, 4, 8, 9, 6, 0, 1, 5, 2, 7]

# category_Mapping=dict(zip(c1,c2))
# category1=st.selectbox('category',c1)
# category=category_Mapping[category1]

# #_____________________________________________
# l1=['yes','no']
# l2=[1,2]
# leather_Mapping=dict(zip(l1,l2))
# leather1=st.selectbox('leather',l1)
# leather=leather_Mapping[leather1]
# #________________

# f1=['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG',
#        'Hydrogen']
# f2=[4, 2, 1, 5, 3, 0]
# Fuel_Mapping=dict(zip(f1,f2))
# Fuel1=st.selectbox('Fuel type',f1)
# Fuel=Fuel_Mapping[Fuel1]
# #___________________
# a1=['Automatic', 'Tiptronic', 'Variator', 'Manual']
# a2=[3, 0, 2, 1]
# Auto_Mapping=dict(zip(a1,a2))
# Auto1=st.selectbox('Fuel type',a1)
# Auto=Auto_Mapping[Auto1]

# #_________________

# d1=['4x4', 'Front', 'Rear']
# d2=[1, 0, 2]
# Drive_Mapping=dict(zip(d1,d2))
# Drive1=st.selectbox('Drive Wheels',d1)
# Drive=Drive_Mapping[Drive1]
# #___________________
# w1=['Left wheel', 'Right-hand drive']
# w2=[0,1]
# wheel_Mapping=dict(zip(w1,w2))
# wheel1=st.selectbox('Wheel',w1)
# wheel=wheel_Mapping[wheel1]
# #___________---------
# cc1=['Silver', 'Black', 'White', 'Grey', 'Blue', 'Green', 'Red',
#        'Sky blue', 'Orange', 'Yellow', 'Brown', 'Golden', 'Beige',
#        'Carnelian red', 'Purple', 'Pink']
# cc2=[ 1,  6,  4, 13,  8,  5,  3, 14, 12,  7,  9, 11,  0, 10,  2, 15]
# color_Mapping=dict(zip(cc1,cc2))
# color1=st.selectbox('color',cc1)
# color=color_Mapping[color1]
# #___________________
# Engine=st.selectbox('Engine volume',[1.3, 2.5, 2. , 1.8, 2.4, 1.6, 2.2, 1.5, 1.4, 2.3, 1.2, 1.7, 2.9,
#        1.9, 2.7, 3.5, 2.1, 1. , 0.8, 3. , 3.3, 2.8, 3.2, 1.1])
# #______________________
# Airbag=st.selectbox('AirBage',[ 2,  0,  4, 12,  8, 10,  6,  1, 16,  7,  9,  5, 11,  3, 14, 15, 13])

# #____________________________________

# Age=st.number_input('Age')
# #______________________________
# mileags=st.number_input('mileags')
# #______________________________-
# Levy=st.number_input('Levy')
# #______________________________

# # pd.DataFrame({'Manufacturer':manu2,'Model':Model,'category':category,'leather':leather
# #               ,'Fuel type':Fuel,'Mileage':mileags,'Gear box type':Auto,
# #               'Drive Wheels':Drive,'Wheel':wheel,'Color':color,'Levy':Levy
# #               ,'Engine volume':Engine,'Airbags':Airbag,'Age':Age},index=0)
# #____________
# # df=pd.DataFrame({
# #     'Manufacturer': manu2,
# #     'Model': Model,
# #     'category': category,
# #     'leather': leather,
# #     'Fuel type': Fuel,
# #     'Mileage': mileags,
# #     'Gear box type': Auto,
# #     'Drive Wheels': Drive,
# #     'Wheel': wheel,
# #     'Color': color,
# #     'Levy': Levy,
# #     'Engine volume': Engine,
# #     'Airbags': Airbag,
# #     'Age': Age
# # }, index=[0])

# #_____________
# df = pd.DataFrame({
#     'Manufacturer': [manu2],
#     'Model': [Model],
#     'Category': [category],              # صح بدل category
#     'Leather interior': [leather],       # صح بدل leather
#     'Fuel type': [Fuel],
#     'Mileage': [mileags],
#     'Gear box type': [Auto],
#     'Drive wheels': [Drive],             # صح بدل Drive Wheels
#     'Wheel': [wheel],
#     'Color': [color],
#     'Levy': [Levy],
#     'Engine volume': [Engine],
#     'Cylinders': [4],                    # أضف عمود Cylinders (قيمة افتراضية أو اختياره من المستخدم)
#     'Airbags': [Airbag],
#     'Age': [Age]
# }, index=[0])

# p=st.sidebar.button('Predict Price')


# if p:
#     pre=data.predict(df)
#     st.sidebar.write("price is :", pre)
    

# ------------------------------------------------------------------------


# import pandas as pd
# import streamlit as st
# import pickle

# st.title('Car Price Prediction')
# st.sidebar.header('Feature Selecting')
# st.sidebar.info('Easy Application For Predicting Car Prices')

# st.image('https://wallpapercave.com/wp/wp6404610.jpg')

# # --------------------- رفع الموديل ---------------------
# uploaded_file = st.file_uploader("اختر ملف الموديل (.sav)", type="sav")

# if uploaded_file is not None:
#     data = pickle.load(uploaded_file)
#     st.success("تم تحميل الموديل بنجاح!")

#     # --------------------- إعداد البيانات ---------------------
#     m1 = ['LEXUS', 'CHEVROLET', 'HONDA', 'FORD', 'HYUNDAI', 'TOYOTA',
#           'MERCEDES-BENZ', 'OPEL', 'PORSCHE', 'BMW', 'JEEP', 'VOLKSWAGEN',
#           'AUDI', 'RENAULT', 'NISSAN', 'SUBARU', 'DAEWOO', 'KIA',
#           'MITSUBISHI', 'SSANGYONG', 'MAZDA', 'GMC', 'FIAT', 'INFINITI',
#           'ALFA ROMEO', 'SUZUKI', 'ACURA', 'LINCOLN', 'VAZ', 'GAZ',
#           'CITROEN', 'LAND ROVER', 'MINI', 'DODGE', 'CHRYSLER', 'JAGUAR',
#           'ISUZU', 'SKODA', 'DAIHATSU', 'BUICK', 'TESLA', 'CADILLAC',
#           'PEUGEOT', 'BENTLEY', 'VOLVO', 'სხვა', 'HAVAL', 'HUMMER', 'SCION',
#           'UAZ', 'MERCURY', 'ZAZ', 'ROVER', 'SEAT', 'LANCIA', 'MOSKVICH',
#           'MASERATI', 'FERRARI', 'SAAB', 'LAMBORGHINI', 'ROLLS-ROYCE',
#           'PONTIAC', 'SATURN', 'ASTON MARTIN', 'GREATWALL']

#     m2 = [8, 4, 9, 38, 20, 40, 29, 25, 44, 36, 47, 23, 14, 24, 35, 19, 6,
#           3, 37, 17, 26, 12, 46, 22, 2, 16, 13, 0, 39, 11, 33, 45, 18, 34,
#           27, 42, 7, 43, 32, 10, 28, 15, 21, 30, 41, 1, 31, 5]

#     manu_mapping = dict(zip(m1, m2))
#     manu1 = st.selectbox("Manufacturer", m1)
#     manu2 = manu_mapping[manu1]

#     mm1 = ['RX 450', 'Equinox', 'FIT', 'E 230 124', 'RX 450 F SPORT', 'Prius C aqua']
#     mm2 = [276, 262, 649, 575, 664, 106]
#     model_mapping = dict(zip(mm1, mm2))
#     Model1 = st.selectbox("Model", mm1)
#     Model = model_mapping[Model1]

#     c1 = ['Jeep', 'Hatchback', 'Sedan', 'Microbus', 'Goods wagon',
#           'Universal', 'Coupe', 'Minivan', 'Cabriolet', 'Limousine',
#           'Pickup']
#     c2 = [3, 4, 8, 9, 6, 0, 1, 5, 2, 7]
#     category_mapping = dict(zip(c1, c2))
#     category1 = st.selectbox('Category', c1)
#     category = category_mapping[category1]

#     l1 = ['yes', 'no']
#     l2 = [1, 2]
#     leather_mapping = dict(zip(l1, l2))
#     leather1 = st.selectbox('Leather interior', l1)
#     leather = leather_mapping[leather1]

#     f1 = ['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG', 'Hydrogen']
#     f2 = [4, 2, 1, 5, 3, 0, 6]
#     fuel_mapping = dict(zip(f1, f2))
#     Fuel1 = st.selectbox('Fuel type', f1)
#     Fuel = fuel_mapping[Fuel1]

#     a1 = ['Automatic', 'Tiptronic', 'Variator', 'Manual']
#     a2 = [3, 0, 2, 1]
#     auto_mapping = dict(zip(a1, a2))
#     Auto1 = st.selectbox('Gear box type', a1)
#     Auto = auto_mapping[Auto1]

#     d1 = ['4x4', 'Front', 'Rear']
#     d2 = [1, 0, 2]
#     drive_mapping = dict(zip(d1, d2))
#     Drive1 = st.selectbox('Drive wheels', d1)
#     Drive = drive_mapping[Drive1]

#     w1 = ['Left wheel', 'Right-hand drive']
#     w2 = [0, 1]
#     wheel_mapping = dict(zip(w1, w2))
#     wheel1 = st.selectbox('Wheel', w1)
#     wheel = wheel_mapping[wheel1]

#     cc1 = ['Silver', 'Black', 'White', 'Grey', 'Blue', 'Green', 'Red',
#            'Sky blue', 'Orange', 'Yellow', 'Brown', 'Golden', 'Beige',
#            'Carnelian red', 'Purple', 'Pink']
#     cc2 = [1, 6, 4, 13, 8, 5, 3, 14, 12, 7, 9, 11, 0, 10, 2, 15]
#     color_mapping = dict(zip(cc1, cc2))
#     color1 = st.selectbox('Color', cc1)
#     color = color_mapping[color1]

#     Engine = st.selectbox('Engine volume', [1.3, 2.5, 2., 1.8, 2.4, 1.6, 2.2, 1.5, 1.4, 2.3, 1.2, 1.7, 2.9,
#                                            1.9, 2.7, 3.5, 2.1, 1., 0.8, 3., 3.3, 2.8, 3.2, 1.1])

#     Airbag = st.selectbox('Airbags', [2, 0, 4, 12, 8, 10, 6, 1, 16, 7, 9, 5, 11, 3, 14, 15, 13])
#     Age = st.number_input('Age')
#     mileags = st.number_input('Mileage')
#     Levy = st.number_input('Levy')

#     # --------------------- إنشاء DataFrame ---------------------
#     df = pd.DataFrame({
#         'Manufacturer': [manu2],
#         'Model': [Model],
#         'Category': [category],
#         'Leather interior': [leather],
#         'Fuel type': [Fuel],
#         'Mileage': [mileags],
#         'Gear box type': [Auto],
#         'Drive wheels': [Drive],
#         'Wheel': [wheel],
#         'Color': [color],
#         'Levy': [Levy],
#         'Engine volume': [Engine],
#         'Cylinders': [4],
#         'Airbags': [Airbag],
#         'Age': [Age]
#     }, index=[0])

#     # --------------------- التنبؤ ---------------------
#     p = st.sidebar.button('Predict Price')

#     if p:
#         pre = data.predict(df)
#         st.sidebar.write("Predicted Price:", pre)

# import pandas as pd
# import streamlit as st
# import pickle

# st.title('Car Price Prediction')
# st.sidebar.header('Feature Selecting')
# st.sidebar.info('Enter the car features to predict its price')

# st.image('https://wallpapercave.com/wp/wp6404610.jpg')

# # --------------------- رفع الموديل ---------------------
# uploaded_file = st.file_uploader("اختر ملف الموديل (.sav)", type="sav")

# if uploaded_file is not None:
#     data = pickle.load(uploaded_file)
#     st.success("تم تحميل الموديل بنجاح!")

#     # --------------------- إدخال بيانات المستخدم ---------------------
#     manu_code = st.number_input("ادخل كود المصنع (مثال: LEXUS=8, CHEVROLET=4)", min_value=0)
#     model_code = st.number_input("ادخل كود الموديل", min_value=0)
#     category_code = st.number_input("ادخل كود نوع العربية", min_value=0)
#     leather_code = st.number_input("ادخل كود الجلد (yes=1, no=2)", min_value=1, max_value=2)
#     fuel_code = st.number_input("ادخل كود نوع الوقود", min_value=0)
#     mileage = st.number_input("ادخل عدد الكيلومترات", min_value=0)
#     gear_code = st.number_input("ادخل كود نوع الجير", min_value=0)
#     drive_code = st.number_input("ادخل كود نظام الدفع", min_value=0)
#     wheel_code = st.number_input("ادخل كود نوع عجلة القيادة", min_value=0)
#     color_code = st.number_input("ادخل كود اللون", min_value=0)
#     levy = st.number_input("ادخل قيمة الضرائب/الرسوم", min_value=0)
#     engine = st.number_input("ادخل حجم الموتور (مثال: 1.3, 2.5)", min_value=0.0, format="%.1f")
#     airbags = st.number_input("ادخل عدد الوسائد الهوائية", min_value=0)
#     age = st.number_input("ادخل عمر العربية بالسنين", min_value=0)
    
#     # --------------------- إعداد DataFrame ---------------------
#     df = pd.DataFrame({
#         'Manufacturer':[manu_code],
#         'Model':[model_code],
#         'Category':[category_code],
#         'Leather interior':[leather_code],
#         'Fuel type':[fuel_code],
#         'Mileage':[mileage],
#         'Gear box type':[gear_code],
#         'Drive wheels':[drive_code],
#         'Wheel':[wheel_code],
#         'Color':[color_code],
#         'Levy':[levy],
#         'Engine volume':[engine],
#         'Cylinders':[4],
#         'Airbags':[airbags],
#         'Age':[age]
#     })

#     # --------------------- التنبؤ ---------------------
#     if st.sidebar.button('Predict Price'):
#         prediction = data.predict(df)
#         st.sidebar.success(f"Predicted Price: {prediction[0]:,.2f} $")





import pandas as pd
import streamlit as st
import pickle
import io

st.title('Car Price Prediction')
st.sidebar.header('Feature Selecting')
st.sidebar.info('Enter the car features to predict its price')

st.image('https://wallpapercave.com/wp/wp6404610.jpg')

# --------------------- رفع الموديل ---------------------
uploaded_file = st.file_uploader("اختر ملف الموديل (.sav)", type="sav")

if uploaded_file is not None:
    # قراءة الملف بشكل صحيح على Streamlit
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
        'Manufacturer': [manu_code],
        'Model': [model_code],
        'Category': [category_code],
        'Leather interior': [leather_code],
        'Fuel type': [fuel_code],
        'Mileage': [mileage],
        'Gear box type': [gear_code],
        'Drive wheels': [drive_code],
        'Wheel': [wheel_code],
        'Color': [color_code],
        'Levy': [levy],
        'Engine volume': [engine],
        'Cylinders': [4],  # يمكن تعديلها إذا أردت
        'Airbags': [airbags],
        'Age': [age]
    })

    # --------------------- التنبؤ ---------------------
    if st.sidebar.button('Predict Price'):
        try:
            prediction = data.predict(df)
            st.sidebar.success(f"Predicted Price: {prediction[0]:,.2f} $")
        except Exception as e:
            st.sidebar.error(f"حدث خطأ أثناء التنبؤ: {e}")


