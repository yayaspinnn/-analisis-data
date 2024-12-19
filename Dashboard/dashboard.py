import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='darkgrid')  # Gaya visualisasi

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
    selected_season = st.multiselect(
        "Pilih Musim:", options=day_df["season"].unique(), default=day_df["season"].unique()
    )
    selected_weather = st.multiselect(
        "Pilih Cuaca:", options=day_df["weather_situation"].unique(), default=day_df["weather_situation"].unique()
    )

# Apply filters
filtered_df = day_df.copy()

# Filter by season
if selected_season:
    filtered_df = filtered_df[filtered_df['season'].isin(selected_season)]

# Filter by weather
if selected_weather:
    filtered_df = filtered_df[filtered_df['weather_situation'].isin(selected_weather)]

# Main dashboard title
st.header('Proyek Akhir: Analisis Data Peminjaman Sepeda :fire:')

# Section 1: Rata-rata Peminjaman Sepeda di Hari Kerja atau Akhir Pekan
st.subheader('1. Rata-rata Peminjaman Sepeda di Hari Kerja atau Akhir Pekan')
st.write('''
    Berdasarkan grafik di bawah ini dapat dilihat bahwa rata-rata penggunaan penyewa sepeda lebih banyak terjadi di hari kerja daripada akhir pekan.
''')
workingday_trend = filtered_df.groupby('workingday')['count'].mean()
workingday_labels = ['Hari Libur', 'Hari Kerja'] if 0 in workingday_trend.index else []
fig_workingday, ax = plt.subplots(figsize=(12, 6))
ax.bar(workingday_trend.index, workingday_trend.values, color=['orange', 'blue'])
ax.set_xticks(workingday_trend.index)
ax.set_xticklabels(workingday_labels)
ax.set_xlabel('Working Day')
ax.set_ylabel('Rata-rata Jumlah Pengguna')
ax.set_title('Rata-Rata Penggunaan Sepeda: Hari Kerja vs Akhir Pekan')
st.pyplot(fig_workingday)

# Section 2: Rata-rata Peminjaman Sepeda di Hari Libur dan Bukan Hari Libur
st.subheader('2. Rata-rata Peminjaman Sepeda di Hari Libur dan Bukan Hari Libur')
st.write('''
    Berdasarkan grafik di bawah ini dapat dilihat bahwa peminjaman sepeda paling banyak terjadi bukan pada hari libur.
''')
holiday_trend = filtered_df.groupby('holiday')['count'].mean()
holiday_labels = ['Bukan Libur', 'Libur'] if 0 in holiday_trend.index else []
fig_holiday, ax = plt.subplots(figsize=(12, 6))
ax.bar(holiday_trend.index, holiday_trend.values, color=['orange', 'blue'])
ax.set_xticks(holiday_trend.index)
ax.set_xticklabels(holiday_labels)
ax.set_xlabel('Holiday')
ax.set_ylabel('Rata-rata Jumlah Pengguna')
ax.set_title('Rata-Rata Penggunaan Sepeda: Hari Libur vs Bukan Hari Libur')
st.pyplot(fig_holiday)

# Footer
st.caption('Copyright © Yaspin 2024')
