# K-Means Clustering
### Utilizing a psychological assesment dataset to find trends in metacognitive abilities

Using mock-data organized in a fashion which resembles results from the Metacognitive Assesment Scale, this repo provides an example of a k-means clustering analysis to identify group trends in metacognitive ability. 

This example demonstrates how an exploratory analysis could be used to set the ground for further investigation. 

The dataset includs subjects who have been administered the MAS-A to assess metacognitive ability, as well as had a personality disorder interview to quantify personality disorder traits. 

In this example dataset, we would expect to see two cluster: High Metacog-Low PD individuals (healhty), and Low Metacog-High PD individuals (unhealthy). 

However, when we visualize this dataset using an elbow plot, we see that there is a strong inflection point at k=3, meaning that there is likely 3 identifiable clusters in our dataset.

![alt text](https://github.com/NGabry/K-Means-Clustering-Metacognition/blob/main/images/Elbow.png?raw=true)

Then, in running a k-means cluster analysis with a k value of 3, we clearly see that there is High Metacog-High PD cluster of individuals!

![alt text](https://github.com/NGabry/K-Means-Clustering-Metacognition/blob/main/images/Clusters.png?raw=true)

Given the results, we then realize that further investigation is warranted to discern additional psychological factors which contribute to the third identified cluster.

The provided jupyter-notebook contains the full walkhtrough from data cleaning to visualizaitons. 

The dependencies necessary for this analysis are as follows:
* pandas
* numpy
* matplotlib
* sklearn

Please note that this data was manipulated so that obvious clusters could be identified, and does not resemble true findings from a clinical investigation.   
