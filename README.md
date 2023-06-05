# Real Estate Price Prediction
![durango-co-september-2021-real-estate](https://github.com/Keerthana1414/RealEstatePricePrediction/assets/122422604/9d9c80e4-7870-48f3-9835-f081a3bcbbf6)

The objective of this project is to develop a data-driven real estate price prediction model for properties in Bangalore. The model should accurately estimate property prices based on relevant features, such as location, property size, and number of rooms. This project seeks to provide valuable insights and predictions to individuals and businesses interested in the Bangalore real estate market.

### Data Collection
The dataset utilized for this project was sourced from Kaggle and contains a range of features such as area_type, availability, location, size, society, total_sqft, bath, balcony, and price.

### Data Preprocessing
The collected data was carefully cleaned and preprocessed to ensure consistency and reliability. This involved addressing missing values, removing outliers, and effectively handling any noise present in the dataset.

### Model Development 
Multiple machine learning algorithms were utilized in the development of the real estate price prediction model, including linear regression, decision trees, lasso, and support vector machine. In addition, k-fold cross-validation was performed to evaluate the performance and generalization capabilities of the real estate price prediction model. 

### Model Evaluation

#### Linear Regression
<table>
  <tr>
    <th>Mean Absolute Error (MAE)</th>
    <th>Mean Squared Error (MSE)</th>
    <th> R-squared (R2)</th>
  </tr>
  <tr>
    <td>18.60</td>
    <td>1231.50</td>
    <td>0.82</td>
  </tr>
  </table>
  
  #### Lasso Regression
<table>
  <tr>
    <th>Mean Absolute Error (MAE)</th>
    <th>Mean Squared Error (MSE)</th>
    <th> R-squared (R2)</th>
  </tr>
  <tr>
    <td>24.28</td>
    <td>2569.46</td>
    <td>0.59</td>
  </tr>
  </table>
  
  #### Decision Tree Regression
<table>
  <tr>
    <th>Mean Absolute Error (MAE)</th>
    <th>Mean Squared Error (MSE)</th>
    <th> R-squared (R2)</th>
  </tr>
  <tr>
    <td>20.55</td>
    <td>2302.94</td>
    <td>0.66</td>
  </tr>
  </table>
  
  #### Support Vector Regression
<table>
  <tr>
    <th>Mean Absolute Error (MAE)</th>
    <th>Mean Squared Error (MSE)</th>
    <th> R-squared (R2)</th>
  </tr>
  <tr>
    <td>24.32</td>
    <td>5165.44</td>
    <td>-1.34</td>
  </tr>
  </table>
  
Based on the given evaluation metrics, linear regression performs the best among the four models with the lowest MAE and MSE values, as well as the highest R2 score. This indicates that the linear regression model provides relatively accurate predictions and explains approximately 82.31% of the variance in the target variable. Therefore, choosing linear regression as the preferred model for real estate price prediction is a reasonable decision.




