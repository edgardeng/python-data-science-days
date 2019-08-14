## Machine Learning
> In many ways, machine learning is the primary means by which data science manifests itself to the broader world. 
Machine learning is where these computational and algorithmic skills of data science meet the statistical thinking of data science, and the result is a collection of approaches to inference and data exploration that are not about effective theory so much as effective computation.

### Qualitative Examples of Machine Learning Applications 机器学习的应用
To make these ideas more concrete, let's take a look at a few very simple examples of a machine learning task. These examples are meant to give an intuitive, non-quantitative overview of the types of machine learning tasks we will be looking at in this chapter. In later sections, we will go into more depth regarding the particular models and how they are used. For a preview of these more technical aspects, you can find the Python source that generates the following figures in the Appendix: Figure Code.

#### Classification: Predicting discrete labels 分类:预测离散标签

Some important classification algorithms

* Gaussian naive Bayes (see In Depth: Naive Bayes Classification), 
* support vector machines (see In-Depth: Support Vector Machines),
* random forest classification (see In-Depth: Decision Trees and Random Forests).

#### Regression: Predicting continuous labels 回归:预测连续标签

Some important regression algorithms：

* linear regression (see In Depth: Linear Regression)
* support vector machines (see In-Depth: Support Vector Machines)
* random forest regression (see In-Depth: Decision Trees and Random Forests).

#### Clustering: Inferring labels on unlabeled data 聚类:推断未标记数据上的标签

Some important Clustering algorithms：

* the k-means algorithm in more depth in In Depth: K-Means Clustering.
* Gaussian mixture models (See In Depth: Gaussian Mixture Models)
* spectral clustering (See Scikit-Learn's clustering documentation).

#### Dimensionality reduction: Inferring structure of unlabeled data 降维:未标记数据的推理结构

Some important dimensionality reduction algorithms：
 * principal component analysis (see In Depth: Principal Component Analysis) 
 * various manifold learning algorithms, including Isomap 
 * locally linear embedding (See In-Depth: Manifold Learning).

## Categories of Machine Learning

At the most fundamental level, machine learning can be categorized into two main types: supervised learning and unsupervised learning.

* Supervised learning 监督学习
    >involves somehow modeling the relationship between measured features of data and some label associated with the data; 
    once this model is determined, it can be used to apply labels to new, unknown data. 
    This is further subdivided into classification tasks and regression tasks: in classification, the labels are discrete categories, while in regression, the labels are continuous quantities. 
 
* Unsupervised learning 无监督学习
    > involves modeling the features of a dataset without reference to any label, and is often described as "letting the dataset speak for itself." 
    These models include tasks such as clustering and dimensionality reduction. Clustering algorithms identify distinct groups of data, while dimensionality reduction algorithms search for more succinct representations of the data.
    