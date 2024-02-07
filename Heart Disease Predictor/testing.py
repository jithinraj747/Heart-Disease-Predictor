import numpy as np
import pandas as pd
import pickle

load_model=pickle.load(open('heart_disease_pred.sav','rb'))

test_dataset = pd.read_csv('test_dataset.csv')

index=100
print(test_dataset.values.tolist()[index][-1])

test_input = np.asarray(test_dataset.values.tolist()[index][:-1],dtype='float32')
test_input = test_input.reshape(1,-1)

pred_val=load_model.predict(test_input)

if pred_val==0:
    print('The person does not have heart disease.')
elif pred_val==1:
    print('The person has heart disease.')
else:
    print('Error!')