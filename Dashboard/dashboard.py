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

# Main dashboard title
st.header('Proyek Akhir: Analisis Data Peminjaman Sepeda :fire:')

# Section 1: Rata-rata Peminjaman Sepeda di Hari Kerja atau Akhir pekan
st.subheader('1. Rata-rata Peminjaman Sepeda di hari kerja atau akhir pekan')
st.write('''
    Berdasarkan grafik di bawah ini dapat dilihat bahwa rata-rata penggunaan penyewa sepeda lebih banyak terjadi di hari kerja daripada akhir pekan.
''')
workingday_trend = day_df.groupby('workingday')['count'].mean()
workingday_labels = ['Hari Libur', 'Hari Kerja']
fig_workingday = plt.figure(figsize=(12, 6))
plt.bar(x=workingday_trend.index, y=workingday_trend.values, color=['orange', 'blue'])
plt.xlabel('Working Day')
plt.ylabel('Rata-rata jumlah pengguna')
plt.title('Rata- Rata Peminjaman Sepeda di Hari Kerja atau akhir pekan')
st.pyplot(fig_workingday)

# Section 2: Rata-rata Peminjaman Sepeda di Hari libur (holiday) dan bukan hari libur
st.subheader('2. Rata-rata Peminjaman Sepeda di Hari libur (holiday) dan bukan hari libur')
st.write('''
    Berdasarkan grafik di bawah ini dapat dilihat bahwa peminjaman sepeda paling banyak terjadi bukan pada hari libur
''')
holiday_trend = day_df.groupby('holiday')['count'].mean()
holiday_labels = ['Bukan Libur', 'Libur']
fig_season = plt.figure(figsize=(12, 6))
plt.bar(x=holiday_trend.index, y=holiday_trend.values, color=['orange', 'blue'])
plt.xlabel('Holiday')
plt.ylabel('Rata-rata jumlah pengguna')
plt.title('Rata- Rata Peminjaman Sepeda di Hari libur dan bukan hari libur')
st.pyplot(fig_season)

st.caption('Copyright © Yaspin 2024')
