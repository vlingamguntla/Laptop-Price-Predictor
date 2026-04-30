import streamlit as st
import pickle
import numpy as np
import pandas as pd

# --- STEP 1: LOAD THE BRAIN & DATA ---
# We load the files we saved on Day 6 using Pickle
pipe = pickle.load(open('pipe.pkl','rb')) # 'rb' means Read Binary
df = pickle.load(open('df.pkl','rb'))

# --- STEP 2: BUILD THE USER INTERFACE (UI) ---
st.title("Laptop Price Predictor 💻")

# Create dropdowns and sliders for user input
# We use df['Column'].unique() to ensure the dropdown only shows options from our dataset

company =st.selectbox('Brand',df['Company'].unique())

type = st.selectbox('Type' , df['TypeName'].unique())

ram=st.selectbox('RAM (in GB)', [2,4,6,8,12,16,24,32,64])

weight = st.number_input('Weight of the Laptop (kg)')

touchscreen = st.selectbox('Touchscreen',['No','Yes'])

ips = st.selectbox('IPS',['No','Yes'])

# Screen Size Slider
screen_size=st.slider('Screensize in inches', 10.0,18.0,15.6)

# Resolution Dropdown
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800',
    '2880x1800','2560x1600','2560x1440','2304x1440'])
# --- STEP 2 (REVISED): DEPENDENT DROPDOWNS ---
# 1. CPU SELECTION
# 1. User selects the Company (Intel/AMD)
cpu_company = st.selectbox('CPU Brand', df['CPU_Company'].unique())

# 2. Logic to show different UI options based on the Brand
if cpu_company == 'AMD':
    # We show the user specific choices for a better "Portfolio Presentation"
    display_cpu_type = st.selectbox('CPU Type', ['Ryzen 7', 'Ryzen 5', 'Ryzen 3', 'A9-Series', 'A6-Series', 'Other AMD'])
    # In the background, we force the value to 'AMD' so the model doesn't crash
    model_cpu_type = 'AMD'
else:
    # For Intel, we use your existing filtered unique values (i3, i5, i7, etc.)
    filtered_cpu_types = df[df['CPU_Company'] == cpu_company]['Cpu_Type'].unique()
    display_cpu_type = st.selectbox('CPU Type', filtered_cpu_types)
    model_cpu_type = display_cpu_type

# 2. GPU SELECTION
gpu_company = st.selectbox('GPU Brand', df['GPU_Company'].unique())

# Filter the dataframe to only show GPU Types belonging to the chosen company
filtered_gpu_types = df[df['GPU_Company'] == gpu_company]['GPU_Type'].unique()
gpu_type = st.selectbox('GPU Type', filtered_gpu_types)


hdd = st.selectbox('HDD (in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD (in GB)', [0,8,128,256,512,1024])

os = st.selectbox('OS', df['os'].unique())

# ---STEP 3: THE PREDICTION LOGIC ---
if st.button('Predict Price'):
    # 1. Handle Categorical logic
    touchscreen_val = 1 if touchscreen == 'Yes' else 0
    ips_val = 1 if ips == 'Yes' else 0

    # 2. Calculate PPI
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    # 3. Create the input as a DATAFRAME
    # The order must match your X_train EXACTLY
    query_data = {
        'Company': [company],
        'TypeName': [type],
        'CPU_Company': [cpu_company], # Providing a default or adding a widget
        'CPU_Frequency (GHz)': [2.5],                   # Default value to satisfy the model
        'RAM (GB)': [ram],
        'GPU_Company': [gpu_company],
        'GPU_Type': [gpu_type],       # Default from your dataset
        'Weight (kg)': [weight],
        'Touchscreen': [touchscreen_val],
        'Ips': [ips_val],
        'ppi': [ppi],
        'Cpu_Type': [model_cpu_type],
        'HDD': [hdd],
        'SSD': [ssd],
        'os': [os]
    }
    
    query_df = pd.DataFrame(query_data)

    # 4. Predict using the DataFrame
    # No more "String to Float" or "Numpy Array" errors! after using Dictionary mapping with Label name and its value
    # Since model is trained on Log Price, we use np.exp to get real Euro
    prediction = int(np.exp(pipe.predict(query_df)[0]))

    st.title(f"The predicted price of this laptop is : €{prediction}")