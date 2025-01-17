# H&M Article Price Prediction Project

## Table of Contents
1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [Data Selection and Preparation](#data-selection-and-preparation)
4. [Feature Engineering and Selection](#feature-engineering-and-selection)
5. [Model Building and Evaluation](#model-building-and-evaluation)
6. [Key Findings and Insights](#key-findings-and-insights)
7. [Real-World Application and Impact](#real-world-application-and-impact)
8. [Challenges and Learnings](#challenges-and-learnings)
9. [Future Work and Improvements](#future-work-and-improvements)

## Introduction

In the highly competitive retail industry, accurate pricing strategies are crucial for maintaining profitability and market relevance. H&M, a global leader in fashion retail, has a vast inventory of articles, each with varying characteristics such as color and type. These attributes can significantly influence customer perceptions and purchasing decisions, ultimately affecting the product's price.

To enhance pricing strategies, this project aims to develop a predictive model that estimates the prices of H&M store articles based on their color and type. By leveraging machine learning techniques, we intend to uncover patterns and relationships within the data that can provide valuable insights into price determination.

### Project Overview
This project aims to predict the prices of H&M articles based on their characteristics, specifically color and type. By developing an accurate predictive model, H&M can optimize its pricing strategy, improve inventory management, and enhance customer satisfaction.

### Objectives and Impact
- **Objective**: To build a robust machine learning model that accurately predicts article prices based on color and type.
- **Potential Impact**: Improved pricing strategies, optimized inventory management, and enhanced customer satisfaction.

## Data Selection and Preparation

### Dataset Description
- **Source**: H&M article dataset containing characteristics and prices.
- **Key Characteristics**: Article color, type, and price.

### Data Cleaning and Preprocessing
- Handled missing values and ensured data consistency.
- Applied one-hot encoding for categorical variables.

## Feature Engineering and Selection

### Feature Engineering
- Created new features from existing data to enhance model performance.
- Utilized PCA for dimensionality reduction to retain essential information while reducing feature set complexity.

### Feature Selection
- Selected features based on their relevance to the target variable (price).

## Model Building and Evaluation

### Models Experimented
- **K-Nearest Neighbors (KNN)**
- **Random Forest**
- **Gradient Boosting**
- **Bagging**
- **Linear Regression**

### Evaluation Metrics and Validation Techniques
- Metrics: Mean Absolute Error (MAE), Mean Squared Error (MSE), R-squared (R²)
- Validation: Train-test split, cross-validation

### Improvements Achieved
- Enhanced model performance through systematic hyperparameter tuning.

## Key Findings and Insights

### Major Findings
- **Random Forest**: Best performance with the lowest MAE and MSE and highest R² score.
- **Linear Regression, Gradient Boosting, Bagging**: Also performed well but slightly less accurate than Random Forest.
- **KNN**: Has the lowest R² score, indicating it explains less variance compared to the other models.

### Insights
- Ensemble methods like Random Forest and Bagging are highly effective for this type of regression problem.

## Real-World Application and Impact

### Application
- Can be applied to optimize pricing strategies in H&M stores.
- Potential to improve inventory management and marketing strategies.

### Impact
- Enhanced profitability through optimized pricing.
- Better customer satisfaction due to more accurate and fair pricing.

### Ethical Considerations
- Ensure pricing strategies do not lead to unfair pricing or discrimination.

## Challenges and Learnings

### Challenges Faced
- Handling large and complex datasets.
- Ensuring data consistency and quality.

### Learnings
- Importance of data preprocessing and feature engineering.
- Value of ensemble methods in improving model accuracy.

## Future Work and Improvements

### Areas for Future Research
- Explore additional features that may impact pricing.
- Experiment with more advanced machine learning techniques.

### Potential Improvements
- Incorporate more sophisticated feature engineering techniques.
- Utilize larger datasets for training to improve model robustness.

---

## Analysis

### Mean Absolute Error (MAE) Analysis

### Mean Absolute Error (MAE) Comparison
![MAE Comparison](https://github.com/DaniCoco31/hm-fashion-recomendations/blob/Daniela/Data/Charts/MAE.png)

- The Random Forest model has the lowest MAE (0.012079), followed closely by the Bagging and Gradient Boosting models. This indicates that these models have the smallest average errors in their predictions.
- The KNN model has a slightly higher MAE (0.013167), but it is still reasonably close to the other top models.
- The Linear Regression model performs comparably to the ensemble models with an MAE of 0.012232.

### Mean Squared Error (MSE) Analysis

### Mean Squared Error (MSE) Comparison
![MSE Comparison](https://github.com/DaniCoco31/hm-fashion-recomendations/blob/Daniela/Data/Charts/R2_Score.png)

- Similar to the MAE results, the Random Forest and Bagging models have the lowest MSE (0.000475), suggesting they have the smallest average squared errors.
- The Gradient Boosting model follows closely with an MSE of 0.000490.
- The KNN model has a slightly higher MSE (0.000539), but it is still close to the top-performing models.
- The Linear Regression model has an MSE of 0.000482, performing better than KNN and close to the top models.

### R2 Score Analysis

### R2 Score Comparison
![R2 Score Comparison](https://github.com/DaniCoco31/hm-fashion-recomendations/blob/Daniela/Data/Charts/R2_Score.png)

- The Random Forest model has the highest R2 score (0.292370), meaning it explains the highest proportion of the variance in the target variable.
- The Bagging model follows closely with an R2 score of 0.291828, and the Gradient Boosting model has an R2 score of 0.269941.
- The KNN model has a lower R2 score (0.197233), indicating it explains less variance compared to the other top models.
- The Linear Regression model performs well with an R2 score of 0.282263.
### Conclusion

- The Random Forest model is the best-performing model overall, with the lowest MAE and MSE and the highest R2 score.
- Bagging and Gradient Boosting models also perform well, showing competitive MAE, MSE, and R2 scores.
- The KNN model performs reasonably well but is slightly less accurate compared to the ensemble models.
- The Linear Regression model performs comparably to the ensemble models, making it a viable option for prediction.
- This analysis suggests focusing on ensemble methods like Random Forest and Bagging for better prediction accuracy in this dataset.

- **Team Members**: Dalreen Soares, Daniela Trujillo, Lāsma Oficiere
- [Project Slides](https://www.canva.com/design/DAGNMsfo2Og/fZwq_sNEquhILKD86jjcVQ/edit?utm_content=DAGNMsfo2Og&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
- [Kaggle Database](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data?select=articles.csv)




