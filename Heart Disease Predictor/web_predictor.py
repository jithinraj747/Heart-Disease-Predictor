import numpy as np
import pickle
import streamlit as st

# streamlit recognizes only absolute file paths. Here, relative paths are used for representation. Please change it.

load_model = pickle.load(open('heart_disease_pred.sav', 'rb'))

def heart_disease_prediction(test_input):
    test_input = np.asarray(test_input,dtype='float32')
    test_input = test_input.reshape(1,-1)
    pred_val = load_model.predict(test_input)
    if pred_val == 0:
        return 'The person does not have heart disease.'
    elif pred_val == 1:
        return 'The person has heart disease.'
    else:
        return 'Error!'

def main():
    st.title('Heart Disease Predictor')

    Age = st.text_input('Enter Age:')

    Sex_M = 0
    Sex = st.radio('Select Sex:', ['M', 'F'])
    if Sex == 'M':
        Sex_M = 1

    ChestPainType_ATA = 0
    ChestPainType_NAP = 0
    ChestPainType_TA = 0
    ChestPainType = st.radio('Select Type of Chest Pain:', ['ATA', 'NAP', 'ASY', 'TA'])
    if ChestPainType == 'ATA':
        ChestPainType_ATA = 1
    elif ChestPainType == 'NAP':
        ChestPainType_NAP = 1
    elif ChestPainType == 'TA':
        ChestPainType_TA = 1

    RestingBP = st.text_input('Enter Resting BP:')
    Cholesterol = st.text_input('Enter Cholesterol Level:')
    FastingBS = st.text_input('Enter Fasting BS:')

    RestingECG_Normal = 0
    RestingECG_ST = 0
    RestingECG = st.radio('Select Resting ECG:', ['Normal', 'ST', 'LVH'])
    if RestingECG == 'Normal':
        RestingECG_Normal = 1
    elif RestingECG == 'ST':
        RestingECG_ST = 1

    MaxHR = st.text_input('Enter Max HR:')

    ExerciseAngina_Y = 0
    ExerciseAngina = st.radio('Was exercise angina detected?', ['No', 'Yes'])
    if ExerciseAngina == 'Yes':
        ExerciseAngina_Y = 1

    Oldpeak = st.text_input('Enter Oldpeak value:')

    ST_Slope_Flat = 0
    ST_Slope_Up = 0
    ST_Slope = st.radio('Select ST Slope:', ['Up', 'Flat', 'Down'])
    if ST_Slope == 'Flat':
        ST_Slope_Up = 1
    elif ST_Slope == 'Up':
        ST_Slope = 1

    diagnosis = ''

    if st.button('Click for Results'):
        diagnosis = heart_disease_prediction(
            [[Age, RestingBP, Cholesterol, FastingBS, MaxHR, Oldpeak, Sex_M, ChestPainType_ATA, ChestPainType_NAP,
             ChestPainType_TA, RestingECG_Normal, RestingECG_ST, ExerciseAngina_Y, ST_Slope_Flat, ST_Slope_Up]])

    st.success(diagnosis)


if __name__ == '__main__':
    main()
