#!/usr/bin/env python@3.10
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("Data Analysis Dashboard")

hours_df = pd.read_csv("hour.csv")
hours_group = hours_df.groupby(by="hr").cnt.mean()
days_df = pd.read_csv("day.csv")

st.subheader("Data Preview - hour")
st.write(hours_df.head())
    
st.subheader("Data Preview - day")
st.write(days_df.head())

st.subheader("Visualisasi Data")

col1, col2 = st.columns(2)
with col1:
    st.write("Tren Rata-rata Jumlah Penyewaan Sepeda Setiap Jam")
    plt.plot(hours_group.index, hours_group.values)
    plt.xlabel("Jam")
    plt.ylabel("Jumlah")
    plt.xlim(0,24)
    st.pyplot(plt)
    with st.expander("See explanation"):
        st.write(
            """Dari grafik menunjukkan pengguna sepeda memuncak di jam berangkat 
            kerja sekitar jam 8 pagi dan memuncak kembali di jam pulang kerja 
            sekitar jam 5 sore.
            """
        )
with col2:
    st.write("Korelasi antara suhu dan jumlah penyewaan sepeda")
    sns.regplot(x=days_df["temp"], y=days_df["cnt"])
    plt.xlim(0, 1)
    st.pyplot(plt)
    with st.expander("See explanation"):
        st.write(
            """Dari nilai korelasi menunjukkan 0.628844 lebih mendekati angka 1 
            dibandingkan angka 0 dan dari grafik menunjukkan kenaikan, maka
            disimpulkan suhu dan jumlah penyewaan sepeda memiliki korelasi positive
            yang cukup erat.
            """
        )
