import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_distribution(data):
    plt.style.use('dark_background')
    
    plt.hist(data, bins='auto', density=True, color=(70/255, 130/255, 180/255), edgecolor=(55/255, 55/255, 55/255), alpha=0.7)
    sns.kdeplot(data, color='grey')

    plt.xlabel('Value', color='white')
    plt.ylabel('Density', color='white')
    plt.title('Distribution Plot', color='white')

    plt.xticks(rotation=30, color='white')
    plt.yticks(color='white')

    plt.gca().set_facecolor('black')

    return plt

def plot_bar(data):
    proportions = data.value_counts(normalize=True)

    plt.style.use('dark_background')

    plt.bar(proportions.index, proportions.values, color=(70/255, 130/255, 180/255), edgecolor=(55/255, 55/255, 55/255), alpha=0.7)

    plt.xlabel('Category', color='white')
    plt.ylabel('Proportion', color='white')
    plt.title('Proportions of each category level', color='white')

    plt.xticks(rotation=85, color='white', fontsize=6)
    plt.yticks(color='white')

    plt.gca().set_facecolor('black')

    return plt


st.title('Exploratory Data Analysis (EDA) Application')

uploaded_file = st.file_uploader('Upload a CSV file', type='csv')

if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file)

    st.subheader('Dataset Statistics')
    st.write('Number of rows:', df.shape[0])
    st.write('Number of columns:', df.shape[1])
    st.write('Number of categorical variables:', len(df.select_dtypes(include='object').columns))
    st.write('Number of numerical variables:', len(df.select_dtypes(include=['int64', 'float64']).columns))
    st.write('Number of boolean variables:', len(df.select_dtypes(include='bool').columns))

    option = st.selectbox('Select a column from the data', df.columns)

    if option is not None:
        df_column = df[option]

        if np.issubdtype(df[option].dtype, np.number):
            st.write('This column is numerical')
            st.table(df[option].describe()[['min', '25%', '50%', '75%', 'max']])
            st.pyplot(plot_distribution(df[option]))
        else:
            st.write("This column is categorical")
            st.write('Proportions of each category level:')
            proportions = df[option].value_counts(normalize=True)
            st.table(proportions)
            st.pyplot(plot_bar(df[option]))
            