import streamlit as st
import os
import json
import pandas as pd

def run():
    k_data_sources = json.load(open(os.getcwd() + '/src/config/kaggle_data_links.json','r'))

    stcontainer = st.container()
    col1, col2 = stcontainer.columns(2)
    dataframes = []
    count=0
    for i in k_data_sources['kl_data']:
        df = pd.read_csv(os.getcwd() +i['storage_path'] + i['filename'])
        dataframes.append(df)
        # cols = st.columns(len(dataframes))
        # cols[count]
        # for j in cols:
            # j.title(i['filename'] + " Report")
            # j.write(df)
        # 
        # st.write(df)
        # chart_df = pd.DataFrame(df, columns=df.columns)
        # st.line_chart(chart_df)
        
        if (count % 2) == 0:
            
            col1.header(i['filename'])
            col1.dataframe(df)
        else:
            
            col2.header(i['filename'])
            col2.dataframe(df)
            # col2.line_chart()
        count+=1

    #setup

    #body
    

    for i in dataframes:
        # print(dataframes.index(i))
        # print((dataframes.index(i) % 2))
        # if (dataframes.index(i) % 2) == 0:
            # col1.write(i)
        # else:
            # col2.write(i)
        pass