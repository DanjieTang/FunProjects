import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title and header
st.title("Data Exploration Example")
st.header("Analyzing a Sample Dataset")

# Load a sample dataset (You can use your own dataset)
df = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['Column A', 'Column B', 'Column C']
)

# Display the raw data
st.subheader("Raw Dataframe")
st.write(df)

# Checkbox to select specific columns
selected_columns = st.multiselect("Choose columns to visualize:", df.columns)

# Plot the selected data
if selected_columns:
    st.subheader("Distribution of Selected Columns")
    fig, ax = plt.subplots()
    ax.hist(df[selected_columns])
    st.pyplot(fig)
