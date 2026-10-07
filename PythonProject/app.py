import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

# Title of the app
st.title("Graph Visualization with Streamlit")

# Example dataset
st.header("Example Dataset: Iris")
df = sns.load_dataset('iris')
st.dataframe(df)

# Matplotlib Example
st.header("Matplotlib Graph")
fig, ax = plt.subplots()
ax.scatter(df['sepal_length'], df['sepal_width'], c='blue', alpha=0.5)
ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')
ax.set_title('Sepal Length vs Width')
st.pyplot(fig)

# Seaborn Example
st.header("Seaborn Heatmap")
correlation_matrix = df.corr(numeric_only=True)
fig, ax = plt.subplots()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Plotly Example
st.header("Interactive Plotly Graph")
plotly_fig = px.scatter(df, x='sepal_length', y='sepal_width', color='species',
                        title="Interactive Scatter Plot")
st.plotly_chart(plotly_fig)

# User Input Example
st.header("Dynamic Graphs Based on User Input")
species = st.selectbox("Select Species", df['species'].unique())
filtered_data = df[df['species'] == species]
st.write(f"Filtered Data for {species}")
st.dataframe(filtered_data)

st.write("Scatter Plot for Selected Species")
fig, ax = plt.subplots()
ax.scatter(filtered_data['sepal_length'], filtered_data['sepal_width'], c='red', alpha=0.5)
ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')
ax.set_title(f'{species}: Sepal Length vs Width')
st.pyplot(fig)
