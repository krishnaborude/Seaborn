import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("iris")

# Sidebar for user selection
species = st.sidebar.selectbox("Select Species", df["species"].unique())

# Filter data
filtered_df = df[df["species"] == species]

# Create plot
st.write(f"Scatter Plot for {species}")
fig, ax = plt.subplots()
sns.scatterplot(x="sepal_length", y="sepal_width", data=filtered_df, ax=ax)
st.pyplot(fig)
plt.show()

