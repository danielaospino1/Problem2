import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/Administrador/Downloads/university_student_dashboard_data.csv")

st.set_page_config(page_title="Dashboard", layout="wide", initial_sidebar_state="expanded")

st.title("📊 Tendencia de estudiantes")

years = sorted(df["Year"].unique())
ranges = st.slider("Select year range", min_value=min(years), max_value=max(years), value=(min(years), max(years)))
selected_year = df[(df["Year"] >= ranges[0]) & (df["Year"] <= ranges[1])]

# Retention rate trends
st.subheader("📉 Tendencia del Retention Rate (%)")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(selected_year["Year"], selected_year["Retention Rate (%)"], marker="o", linestyle="-")
ax.set_xlabel("Año")
ax.set_ylabel("Retention Rate (%)")
ax.set_title("Tendencia del Retention Rate (%) a lo largo del tiempo")
ax.grid()
st.pyplot(fig)

# Student satisfaction
st.subheader("😊 Tendencia de Satisfacción de los Estudiantes")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['Year'], df['Student Satisfaction (%)'], marker='o', linestyle='-')
ax.set_xlabel('Año')
ax.set_ylabel('Student Satisfaction (%)')
ax.set_title('Tendencia del Student Satisfaction (%) a lo largo de los años')
ax.grid()
st.pyplot(fig)

# Enrollment breakdown by department
facultades = ["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]
df_grouped = selected_year.groupby("Year")[facultades].sum().reset_index()

st.subheader("🏫 Distribución de Estudiantes por Facultad")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=df_grouped, x="Year", y="Engineering Enrolled", marker="o", label="Engineering")
sns.lineplot(data=df_grouped, x="Year", y="Business Enrolled", marker="s", label="Business")
sns.lineplot(data=df_grouped, x="Year", y="Arts Enrolled", marker="^", label="Arts")
sns.lineplot(data=df_grouped, x="Year", y="Science Enrolled", marker="d", label="Science")

plt.xlabel("Año")
plt.ylabel("Número de Estudiantes")
plt.title("Tendencia de Matrícula por Departamento")
plt.legend(title="Departamento")
plt.grid()
st.pyplot(fig)

# Comparison between Spring vs. Fall term trends
st.subheader("🍂📅 Comparación de Inscripciones: Spring vs Fall")
terms = ['Spring', 'Fall']
applications = [30000, 30000]
enrolled = [7000, 7000]

x = np.arange(len(terms))  # [0, 1]
width = 0.4

fig, ax = plt.subplots(figsize=(8, 5))
bars1 = ax.bar(x - width/2, applications, width, label="Applications", color='royalblue')
bars2 = ax.bar(x + width/2, enrolled, width, label="Enrolled", color='orangered')

ax.set_xlabel("")
ax.set_ylabel("Number")
ax.set_title("Comparison of Spring vs. Fall Terms")
ax.set_xticks(x)
ax.set_xticklabels(terms)
ax.legend()

st.pyplot(fig)


# General enrollment
st.subheader("📈 Tendencias de Inscripción")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=selected_year, x="Year", y="Enrolled", marker="o", ax=ax)
ax.set_title("Tendencia de Inscripción de Estudiantes")
st.pyplot(fig)

# Gen
st.subheader("📊 Estadísticas Generales")
st.write(selected_year.describe())