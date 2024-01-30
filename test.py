print ("Genomics Open Dataset")

# Learn #

!pip show pandas 
import pandas as pd

dataset = pd.read_csv("https://raw.githubusercontent.com/sudarshan-koirala/Logistic-Regression-for-Titanic-Dataset/master/Train_Titanic.csv")

dataset.head()
