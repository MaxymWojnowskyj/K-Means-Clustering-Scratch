# K-means clustering implementation from scratch in Python using only numpy
In this project, I have implemented the K-means clustering algorithm from scratch using only the numpy library in Python. The purpose of this project was to deepen my understanding of how the K-means algorithm works and to gain practical experience in implementing it.

# How K-means Clustering works
K-means clustering is a unsupervised machine learning algorithm used to classify data points into clusters based on their similarities. The algorithm starts by iteratively assigning each data point to the closest cluster and then reassigning each cluster value to the mean of all of its assigned points. This process is repeated until the clusters no longer update in value or a number of iterations is reached equal to a preset maximum iterations value.

# Code Implementation
The code starts by generating a test dataset consisting of 40,000 data points with four features each. The first 10,000 data points have a value of 30 in all four features, the second 10,000 have a value of 60, the third 10,000 have a value of 90, and the last 10,000 have a value of 120. The dataset is then shuffled to ensure that the data points are distributed randomly.

Next, the number of clusters is set to four, and the algorithm is run for ten different variations. For each variation, the algorithm randomly selects four data points from the dataset to use as the initial cluster values. The algorithm then iteratively assigns each data point to the nearest cluster and recalculates the center of each cluster. This process continues until the clusters no longer change. (I did not set a maximum number of iterations as I knew with this simple dataset that it would converge to a non increasing mean cluster value).

After each variation, the sum of the variances of each cluster is calculated and stored. Finally, the variation with the minimum sum of variances is selected as the optimal set of clusters.

# Running the Code
To run this code, simply download Python file and run it. You will need to have the numpy library installed. The code will output the optimal set of clusters and their corresponding variances. Feel free to modify the dataset, number of clusters, or number of variations to experiment with different scenarios.

