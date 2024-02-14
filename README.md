## Heart Disease Predictor

A binary classification ensemble model was build for predicting the potential development of heart disease or maybe even diagnose in real time. The model is based on a dataset that uses 11 features. The model was build by first selecting the best three classification models through the assessment of kfold cross validation scores, confusion matrices, recall values, precision values and f-measure values. The selected models were combined using the voting process to create an ensemble model which was again assessed based on the aforementioned criteria. The model attained a training and testing score of ~85%. The model was test-deployed in streamlit which uses a form to collect the input details or features from the user. 

1.  Age: age of the patient [years]
2.  Sex: sex of the patient [M: Male, F: Female]
3.  ChestPainType: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
4.  RestingBP: resting blood pressure [mm Hg]
5.  Cholesterol: serum cholesterol [mm/dl]
6.  FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]
7.  RestingECG: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST       elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria]
8.  MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]
9.  ExerciseAngina: exercise-induced angina [Y: Yes, N: No]
10. Oldpeak: oldpeak = ST [Numeric value measured in depression]
11.  ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]

### How to use model

Download the Heart Disease Predictor directory containing the web-predictor.py and heart_disease_pred.sav model. Run the following command with the absolute path location of the web_predictor.py file within quotes:  

                              streamlit run '../Heart Disease Predictor/web_predictor.py'
