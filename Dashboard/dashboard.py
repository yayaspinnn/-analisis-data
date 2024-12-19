import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Load dataset
day_df = pd.read_csv("https://raw.githubusercontent.com/yayaspinnn/analisis-data/main/Dashboard/day_df.csv")

# Sidebar content
with st.sidebar:

    # Add titles and personal information
    st.title('Proyek Akhir: Analisis Data Peminjaman Sepeda :fire:')
    st.header('Nama: Yaspin Andika M')
    st.subheader('Email: andikayaspin@gmail.com')

    # Add filters
    st.header("Filter Data")
    date_range = st.date_input("Pilih Rentang Tanggal", [])
    selected_season = st.multiselect(
        "Pilih Musim:", options=day_df["season"].unique(), default=day_df["season"].unique()
    )
    selected_weather = st.multiselect(
        "Pilih Cuaca:", options=day_df["weathersit"].unique(), default=day_df["weathersit"].unique()
    )

# Apply filters
filtered_df = day_df.copy()
if date_range:
    if len(date_range) == 2:
        filtered_df = filtered_df[(filtered_df['dteday'] >= pd.to_datetime(date_range[0])) & (filtered_df['dteday'] <= pd.to_datetime(date_range[1]))]
if selected_season:
    filtered_df = filtered_df[filtered_df['season'].isin(selected_season)]
if selected_weather:
    filtered_df = filtered_df[filtered_df['weathersit'].isin(selected_weather)]

# Main dashboard title
st.header('Proyek Akhir: Analisis Data Peminjaman Sepeda :fire:')

# Section 1: Rata-rata Peminjaman Sepeda di Hari Kerja atau Akhir pekan
st.subheader('1. Rata-rata Peminjaman Sepeda di hari kerja atau akhir pekan')
st.write('''
    Berdasarkan grafik di bawah ini dapat dilihat bahwa rata-rata penggunaan penyewa sepeda lebih banyak terjadi di hari kerja daripada akhir pekan.
''')
workingday_trend = filtered_df.groupby('workingday')['count'].mean()
workingday_labels = ['Hari Libur', 'Hari Kerja']
fig_workingday = plt.figure(figsize=(12, 6))
plt.bar(x=workingday_trend.index, height=workingday_trend.values, color=['orange', 'blue'])
plt.xlabel('Working Day')
plt.ylabel('Rata-rata jumlah pengguna')
plt.title('Rata- Rata Peminjaman Sepeda di Hari Kerja atau akhir pekan')
st.pyplot(fig_workingday)

# Section 2: Rata-rata Peminjaman Sepeda di Hari libur (holiday) dan bukan hari libur
st.subheader('2. Rata-rata Peminjaman Sepeda di Hari libur (holiday) dan bukan hari libur')
st.write('''
    Berdasarkan grafik di bawah ini dapat dilihat bahwa peminjaman sepeda paling banyak terjadi bukan pada hari libur
''')
holiday_trend = filtered_df.groupby('holiday')['count'].mean()
holiday_labels = ['Bukan Libur', 'Libur']
fig_season = plt.figure(figsize=(12, 6))
plt.bar(x=holiday_trend.index, height=holiday_trend.values, color=['orange', 'blue'])
plt.xlabel('Holiday')
plt.ylabel('Rata-rata jumlah pengguna')
plt.title('Rata- Rata Peminjaman Sepeda di Hari libur dan bukan hari libur')
st.pyplot(fig_season)

# Footer
st.caption('Copyright © Yaspin 2024')
