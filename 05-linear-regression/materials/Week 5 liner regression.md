# Week 5 liner regression

##  1. Explain the difference between classification and regression

> * Classification makes predictions from among a finite range of categorical values.
> * Regression is a process which can predict continuous value targets. And it can output continuous values as predictions of some target feature values.

## 2. Describe the basic idea behind error-based learning

> * Error-based learning can treat the feature values as coordinates in a N-dimensional hyperplane. 
> * Behind the error-based learning , we can define a error function (also called a loss function) which measures the total residuals  from the line to the points in our dataset.

##  3. What is the predictor function in linear regression

> * The predictor function is that we use p-value and t-test to do something.
> * When considering machine learning model performance, we measure how well the generated model predicts targets from a test set for which we already know the results. In regression models we need to use different performance measures than those we use in classification models. By its nature, linear regression is already minimising the residual error within the training set to fit a hyperplane model for the points it trains with.   

##  4. What is the role of the error function in determining the optimal predictor function?

> * Because of the error function, we can find the minimum of the target values which can determining the optimal predictor function.
> * To obtain the global minimum for this system of two weights and one feature we take the partial derivates of our loss function with respect to w[0] and with respect to w[1].   

##   5. What is gradient decent and, briefly, how does it work?

> * Gradient decent is just like someone go down the mountain. We can choose a point randomly and then go down this mountain.
> * The algorithm starts with some randomly initialised points on the hyperplane and the proceeds to find the global minimum with respect to all the dimensions until it converges at the lowest point.

##   6. How should be treat categorical descriptive features in linear regression?

> * In linear regression , the categorical descriptive features all should use the gradient decent method to get the minimum value. And we use this value as the optimal features. And use in the linear regression.