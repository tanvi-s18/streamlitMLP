import streamlit as st
import pandas as pd
from clean_data import fetch_student_data, clean_data
from data_visualization import scatterplot
from preproc_data import prepare_data, feature_selection, normalization, pca
from regression import regression

def midtermPage():
    st.title("Midterm Checkpoint")
    
    data = fetch_student_data()
    cleaned_data = clean_data(data)

    X, y = prepare_data(cleaned_data)

    X_selected = feature_selection(X, y)
    X_normalized = normalization(X_selected)
    X_pca = pca(X_normalized)

    processed_data = pd.concat([pd.DataFrame(X_pca), cleaned_data[['G3']]], axis=1)

    series1, series2 = regression(processed_data)
    regression_data = pd.DataFrame({
        'Actual Grades': series1,
        'Predicted Grades': series2
    })
    st.line_chart(regression_data)

    st.header("Visualizations")
    scatterplot(regression_data)
    st.caption("Scatter Plot")

import streamlit as st

# Results and Discussion Section
st.header("Results and Discussion")

# Quantitative Metrics
st.subheader("Quantitative Metrics:")
st.write("**Mean Squared Error (MSE):** 2.93")
st.write("**Mean Absolute Error (MAE):** 0.93")
st.write("**R-squared Score:** 0.81")
st.write(
    """
    These metrics provide a quantitative summary of the model's performance. An R-squared score of 0.81 indicates that 
    81% of the variance in the actual grades is explained by our model, which is relatively high. The MSE and MAE values 
    suggest that, on average, our predictions deviate slightly from the actual values, with the model having a small 
    margin of error. The relatively low MAE indicates that the absolute errors are minimal, suggesting that the model 
    is consistently accurate without large deviations.
    """
)

# Analysis of Model Performance
st.subheader("Analysis of Model Performance:")
st.write(
    """
    The model performs well overall, as shown by the R-squared score and the alignment between the predicted and 
    actual values in the visualization. However, some discrepancies remain, particularly in areas where the predicted 
    grades diverge slightly from the actual grades. The relatively low MSE suggests that larger errors (outliers) are 
    minimized, while the low MAE indicates that the model is accurate across most data points. The model’s performance 
    may stem from its ability to capture linear relationships in the data, but limitations could arise if the underlying 
    relationship is non-linear or if there are influential outliers.
    """
)

# Next Steps Section
st.subheader("Next Steps:")

# Data Enhancement
st.markdown("**Data Enhancement:**")
st.write(
    """
    We will consider collecting more data or engineering additional features that may capture further nuances influencing 
    student grades. This could improve our model’s ability to generalize to different patterns.
    """
)

# Algorithm Tuning
st.markdown("**Algorithm Tuning:**")
st.write("Explore hyperparameter tuning for the current model to further optimize its accuracy.")

# Model Comparison
st.markdown("**Model Comparison:**")
st.write(
    """
    We might experiment with different algorithms, such as decision trees, random forests, or neural networks, which might 
    capture non-linear relationships in the data.
    """
)

# Error Analysis
st.markdown("**Error Analysis:**")
st.write(
    """
    We can investigate samples with larger errors to understand patterns in misprediction. This may reveal specific cases 
    where the model struggles, providing insight into areas for improvement.
    """
)

# Conclusion
st.write(
    """
    By following these next steps, we aim to enhance model accuracy, reduce error, and ensure robust predictions across 
    varied scenarios.
    """
)

            
if __name__ == "__main__":
    midtermPage()
