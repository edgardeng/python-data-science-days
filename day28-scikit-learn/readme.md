# Scikit-Learn

> [Scikit-Learn](http://scikit-learn.org), a package that provides efficient versions of a large number of common algorithms.
Scikit-Learn is characterized by a clean, uniform, and streamlined API, as well as by very useful and complete online documentation.

### Data Representation in Scikit-Learn S-L中的数据形式

Machine learning is about creating models from data: for that reason, we'll start by discussing how data can be represented in order to be understood by the computer.

### Data as table

A basic table is a two-dimensional grid of data, in which the rows represent individual elements of the dataset, and the columns represent quantities related to each of these elements.

For example, consider the [Iris dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set), famously analyzed by Ronald Fisher in 1936.

```python

import seaborn as sns
iris = sns.load_dataset('iris')
iris.head()

```

In general, we will refer to the rows of the matrix as *samples*, and the number of rows as ``n_samples``.

Likewise, we will refer to the columns of the matrix as *features*, and the number of columns as ``n_features``.

#### Features matrix

The samples (i.e., rows) always refer to the individual objects described by the dataset.
For example, the sample might be a flower, a person, a document, an image, a sound file, a video, an astronomical object, or anything else you can describe with a set of quantitative measurements.

The features (i.e., columns) always refer to the distinct observations that describe each sample in a quantitative manner.
Features are generally real-valued, but may be Boolean or discrete-valued in some cases.

#### Target array

In addition to the feature matrix ``X``, we also generally work with a *label* or *target* array, which by convention we will usually call ``y``.
The target array is usually one dimensional, with length ``n_samples``, and is generally contained in a NumPy array or Pandas ``Series``.
The target array may have continuous numerical values, or discrete classes/labels.
While some Scikit-Learn estimators do handle multiple target values in the form of a two-dimensional, ``[n_samples, n_targets]`` target array, we will primarily be working with the common case of a one-dimensional target array.

## [Scikit-Learn's Estimator API](https://scikit-learn.org/stable/modules/classes.html) 评估API

The Scikit-Learn API is designed with the following guiding principles in mind:

- *Consistency/一致性* : All objects share a common interface drawn from a limited set of methods, with consistent documentation.

- *Inspection/检验*: All specified parameter values are exposed as public attributes.

- *Limited object hierarchy / 有限的对象层次*: Only algorithms are represented by Python classes; datasets are represented
  in standard formats (NumPy arrays, Pandas ``DataFrame``s, SciPy sparse matrices) and parameter
  names use standard Python strings.

- *Composition 组成*: Many machine learning tasks can be expressed as sequences of more fundamental algorithms,
  and Scikit-Learn makes use of this wherever possible.

- *Sensible defaults 合理的默认值*: When models require user-specified parameters, the library defines an appropriate default value.

### Basics of the API

Most commonly, the steps in using the Scikit-Learn estimator API are as follows:

1. Choose a class of model by importing the appropriate estimator class from Scikit-Learn. 通过引入评估器来选择模型
2. Choose model hyperparameters by instantiating this class with desired values. 通过值来实例化，从而选择模型的超参数
3. Arrange data into a features matrix and target vector following the discussion above. 将数据整理成特征矩阵和目标向量
4. Fit the model to your data by calling the ``fit()`` method of the model instance. 通过fit方法，使模型适合您的数据
5. Apply the Model to new data:
   - For supervised learning, often we predict labels for unknown data using the ``predict()`` method. 监督学习中，通过predict方法，来预测类
   - For unsupervised learning, we often transform or infer properties of the data using the ``transform()`` or ``predict()`` method. 非监督学习中，通过transform、predict方法，来转换或推断数据的属性
                  

### Supervised learning example: Simple linear regression 监督学习案例之 简单的线性回归

As an example of this process, let's consider a simple linear regression—that is, the common case of fitting a line to $(x, y)$ data.

use the following simple data for our regression example:

```python

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.RandomState(42)
x = 10 * rng.rand(50)
y = 2 * x - 1 + rng.randn(50)
plt.scatter(x, y)

```

#### 1. Choose a class of model

If we would like to compute a simple linear regression model, we can import the linear regression class:

Note that other more general linear regression models in the [``sklearn.linear_model`` module documentation](http://Scikit-Learn.org/stable/modules/linear_model.html).

#### 2. Choose model hyperparameters 

Once we have decided on our model class, there are still some options open to us.
Depending on the model class we are working with, we might need to answer one or more questions like the following:

- Would we like to fit for the offset (i.e., *y*-intercept)?
- Would we like the model to be normalized?
- Would we like to preprocess our features to add model flexibility?
- What degree of regularization would we like to use in our model?
- How many model components would we like to use?

These are examples of the important choices that must be made *once the model class is selected*.
These choices are often represented as *hyperparameters*, or parameters that must be set before the model is fit to data.
In Scikit-Learn, hyperparameters are chosen by passing values at model instantiation.
We will explore how you can quantitatively motivate the choice of hyperparameters in [Hyperparameters and Model Validation](05.03-Hyperparameters-and-Model-Validation.ipynb).

For our linear regression example, we can instantiate the ``LinearRegression`` class and specify that we would like to fit the intercept using the ``fit_intercept`` hyperparameter:
```python

from sklearn.linear_model import LinearRegression

model = LinearRegression(fit_intercept=True)
model
```

Keep in mind that when the model is instantiated, the only action is the storing of these hyperparameter values.
In particular, we have not yet applied the model to any data: the Scikit-Learn API makes very clear the distinction between *choice of model* and *application of model to data*.

#### 3. Arrange data into a features matrix and target vector

Previously we detailed the Scikit-Learn data representation, which requires a two-dimensional features matrix and a one-dimensional target array.

Here our target variable ``y`` is already in the correct form (a length-``n_samples`` array), but we need to massage the data ``x`` to make it a matrix of size ``[n_samples, n_features]``.

我们的目标变量y已经处于正确的形式(一个长度为n的样本数组)，但是我们需要对数据x进行处理，使其成为一个大小为[n个样本，n个特征]的矩阵

```python
X = x[:, np.newaxis]
X.shape
```

#### 4. Fit the model to your data

Now it is time to apply our model to data  with the ``fit()`` method of the model:
```python
model.fit(X, y)
```

This ``fit()`` command causes a number of model-dependent internal computations to take place, and the results of these computations are stored in model-specific attributes that the user can explore.

使用fit方法后，会触发许多依赖于模型的内部计算，这些计算的结果存储在用户可以探索的特定于模型的属性中。


In Scikit-Learn, by convention all model parameters that were learned during the ``fit()`` process have trailing underscores;
在Scikit-Learn中，按照惯例，在“fit()”过程中学习的所有模型参数都有尾随下划线

`model.coef_` 和 `model.intercept_`, 这两个参数表示：对数据的简单线性拟合的斜率和截距

One question that frequently comes up regards the uncertainty in such internal model parameters.
In general, Scikit-Learn does not provide tools to draw conclusions from internal model parameters themselves: interpreting model parameters is much more a *statistical modeling* question than a *machine learning* question.
Machine learning rather focuses on what the model *predicts*.

经常出现的一个问题是关于这种内部模型参数的不确定性。通常，Scikit-Learn不提供从内部模型参数本身得出结论的工具:解释模型参数更像是一个“统计建模”问题，而不是“机器学习”问题。机器学习更关注模型“预测”的内容。

#### 5. Predict labels for unknown data

Once the model is trained, the main task of supervised machine learning is to evaluate it based on what it says about new data that was not part of the training set.

一旦模型被训练好，监督机器学习的主要任务就是根据它对不属于训练集的新数据的描述来评估它。

```python
xfit = np.linspace(-1, 11)
Xfit = xfit[:, np.newaxis]
yfit = model.predict(Xfit)

plt.scatter(x, y)
plt.plot(xfit, yfit);

```

As before, we need to coerce these *x* values into a ``[n_samples, n_features]`` features matrix, after which we can feed it to the model

在预测之前，将这些x值强制为一个[n个样本，n个特征]特征矩阵，然后我们可以将其输入模型

### Supervised learning example: Iris classification 

For this task, we will use an extremely simple generative model known as Gaussian naive Bayes, which proceeds by assuming each class is drawn from an axis-aligned Gaussian distribution (see [In Depth: Naive Bayes Classification](05.05-Naive-Bayes.ipynb) for more details).
Because it is so fast and has no hyperparameters to choose, Gaussian naive Bayes is often a good model to use as a baseline classification, before exploring whether improvements can be found through more sophisticated models.

对于这个任务，我们将使用一个极其简单的生成模型，称为高斯朴素贝叶斯，它假设每个类都是从一个轴向对齐的高斯分布中抽取的(更多细节请参阅深入:朴素贝叶斯分类)。由于高斯朴素贝叶斯算法速度快，而且没有超参数可供选择，所以在探索是否可以通过更复杂的模型进行改进之前，它通常是一个很好的基线分类模型。

We would like to evaluate the model on data it has not seen before, and so we will split the data into a *training set* and a *testing set*.
我们想要在模型之前没有见过的数据上对模型进行评估，因此我们将数据分为一个训练集和一个测试集. 使用: ``train_test_split`` utility function:

```python
from sklearn.cross_validation import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris, random_state=1)

```

With the data arranged, we can follow our recipe to predict the labels:
通过这些数据，我们就可以按照我们的食谱来预测标签

```python
from sklearn.naive_bayes import GaussianNB # 1. choose model class
model = GaussianNB()                       # 2. instantiate model
model.fit(Xtrain, ytrain)                  # 3. fit model to data
y_model = model.predict(Xtest)             # 4. predict on new data
```

Finally, we can use the ``accuracy_score`` utility to see the fraction of predicted labels that match their true value:
最后，我们可以使用“准确度评分”, 来查看预测标签与真实值匹配的比例

```python
from sklearn.metrics import accuracy_score
accuracy_score(ytest, y_model)
```

### Unsupervised learning example: Iris dimensionality

As an example of an unsupervised learning problem, let's take a look at reducing the dimensionality of the Iris data so as to more easily visualize it.
作为一个无监督学习问题的例子，对Iris data 进行降维，以便更容易地可视化它。

Recall that the Iris data is four dimensional: there are four features recorded for each sample.
回忆一下Iris数据是四维的:每个样本记录有四个特征。

The task of dimensionality reduction is to ask whether there is a suitable lower-dimensional representation that retains the essential features of the data.
降维的任务是询问是否有合适的低维表示形式来保留数据的基本特征。

Often dimensionality reduction is used as an aid to visualizing data: after all, it is much easier to plot data in two dimensions than in four dimensions or higher!
通常降维，将有有助于可视化数据。 毕竟，在二维中绘制数据要比在四维或更高维度中绘制数据容易得多

Here we will use principal component analysis (PCA; see [In Depth: Principal Component Analysis]()）, which is a fast linear dimensionality reduction technique.
这里我们将使用 主成分分析法(PCA;这是一种快速的线性降维技术。

```python
from sklearn.decomposition import PCA  # 1. Choose the model class
model = PCA(n_components=2)            # 2. Instantiate the model with hyperparameters
model.fit(X_iris)                      # 3. Fit to data. Notice y is not specified!
X_2D = model.transform(X_iris)         # 4. Transform the data to two dimensions


# plot the results
iris['PCA1'] = X_2D[:, 0]
iris['PCA2'] = X_2D[:, 1]
sns.lmplot("PCA1", "PCA2", hue='species', data=iris, fit_reg=False);

```

We see that in the two-dimensional representation, the species are fairly well separated, even though the PCA algorithm had no knowledge of the species labels!
可见，在二维表示中，物种是相当好的分离，即使PCA算法没有物种标签的信息!

This indicates to us that a relatively straightforward classification will probably be effective on the dataset, as we saw before.
这表明，相对简单的分类可能对数据集有效，就像我们之前看到的那样。

### Unsupervised learning: Iris clustering

A clustering algorithm attempts to find distinct groups of data without reference to any labels.
聚类算法试图在不引用任何标签的情况下找到不同的数据组。

Here we will use a powerful clustering method called a Gaussian mixture model (GMM), discussed in more detail in [In Depth: Gaussian Mixture Models](05.12-Gaussian-Mixtures.ipynb).
在这，我们将使用一个强大的聚类方法，称为高斯混合模型(GMM)，更详细地讨论[深入:高斯混合模型]()。

A GMM attempts to model the data as a collection of Gaussian blobs.
GMM试图将数据建模为高斯块的集合

```python
from sklearn.mixture import GMM      # 1. Choose the model class
model = GMM(n_components=3,
            covariance_type='full')  # 2. Instantiate the model with hyperparameters
model.fit(X_iris)                    # 3. Fit to data. Notice y is not specified!
y_gmm = model.predict(X_iris)        # 4. Determine cluster labels

# add the cluster label to the Iris ``DataFrame`` and use Seaborn to plot the results:

iris['cluster'] = y_gmm
sns.lmplot("PCA1", "PCA2", data=iris, hue='species', col='cluster', fit_reg=False);

```

By splitting the data by cluster number, we see exactly how well the GMM algorithm has recovered the underlying label: the *setosa* species is separated perfectly within cluster 0, while there remains a small amount of mixing between *versicolor* and *virginica*.
通过按簇号分割数据，我们可以清楚地看到GMM算法恢复底层标签的效果: *setosa*物种在簇0内被完美地分离，而*versicolor*和*virginica*之间仍有少量混合。

even without an expert to tell us the species labels of the individual flowers, the measurements of these flowers are distinct enough that we could *automatically* identify the presence of these different groups of species with a simple clustering algorithm!
即使没人告诉我们单个花的物种标签，这些花的测量值也足够明显，我们可以用一个简单的聚类算法“自动”识别出这些不同物种的存在!

This sort of algorithm might further give experts in the field clues as to the relationship between the samples they are observing.
这种算法可能会进一步为该领域的专家提供线索，了解他们正在观察的样本之间的关系


### Application: Exploring Hand-written Digits

1. Loading and visualizing the digits data

```python
# load data
from sklearn.datasets import load_digits
digits = load_digits()
digits.images.shape

```

The images data is a three-dimensional array: 1,797 samples each consisting of an 8 × 8 grid of pixels.

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(10, 10, figsize=(8, 8),
                         subplot_kw={'xticks':[], 'yticks':[]},
                         gridspec_kw=dict(hspace=0.1, wspace=0.1))

for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap='binary', interpolation='nearest')
    ax.text(0.05, 0.05, str(digits.target[i]),
            transform=ax.transAxes, color='green')
```
=
We can accomplish this by treating each pixel in the image as a feature: that is, by flattening out the pixel arrays so that we have a length-64 array of pixel values representing each digit.
我们可以通过将图像中的每个像素作为一个特征来实现，将像素数组展平，每个数字的像素值是长度为64的数组。

Additionally, we need the target array, which gives the previously determined label for each digit.
此外，需要目标数组，为每个数字提供确定的标签

```python
X = digits.data
X.shape

y = digits.target
y.shape
```
There are 1,797 samples and 64 features. 这里有1797个样本和64特征

2. Unsupervised learning: Dimensionality reduction

We'd like to visualize our points within the 64-dimensional parameter space, but it's difficult to effectively visualize points in such a high-dimensional space.
我们想要在64维参数空间中可视化我们的点，但是在这样的高维空间中很难有效地可视化点。

Instead we'll reduce the dimensions to 2, using an unsupervised method.
相反，我们将使用无监督方法将维数减少到2。

[In-Depth: Manifold Learning]()（Isometric Feature Mapping）是流行学习的一种，用于非线性数据降维，是一种无监督算法。

```python
from sklearn.manifold import Isomap
iso = Isomap(n_components=2)
iso.fit(digits.data)
data_projected = iso.transform(digits.data)
data_projected.shape

#  plot this data to see if we can learn anything from its structure:

plt.scatter(data_projected[:, 0], data_projected[:, 1], c=digits.target,
            edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('spectral', 10))
plt.colorbar(label='digit label', ticks=range(10))
plt.clim(-0.5, 9.5);

```

This plot gives us some good intuition into how well various numbers are separated in the larger 64-dimensional space. 
这个图给了我们一些很好的直觉，让我们知道在更大的64维空间中，不同的数是如何被很好地分隔开的。
For example, zeros (in black) and ones (in purple) have very little overlap in parameter space.
0(黑色)和1(紫色)在参数空间中几乎没有重叠。
Intuitively, this makes sense: a zero is empty in the middle of the image, while a one will generally have ink in the middle.
直观地说，这是有道理的:0在图像的中间是空的，而1通常在中间有墨水。
On the other hand, there seems to be a more or less continuous spectrum between ones and fours: we can understand this by realizing that some people draw ones with "hats" on them, which cause them to look similar to fours.
另一方面，1和4之间似乎有一个或多或少的连续谱:我们可以通过意识到有些人画的1上面有“帽子”，这使得它们看起来像4来理解这一点。

Overall, however, the different groups appear to be fairly well separated in the parameter space: this tells us that even a very straightforward supervised classification algorithm should perform suitably on this data.
总的来说，不同的组在参数空间中似乎是相当分离的: 即使是非常简单的监督分类算法也应该对这些数据执行适当的分类。

3. Classification on digits 

```python
# split the data into a training and testing set, and fit a Gaussian naive Bayes model:
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0)

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(Xtrain, ytrain)
y_model = model.predict(Xtest)
```

Now that we have predicted our model, we can gauge its accuracy by comparing the true values of the test set to the predictions:

```python
from sklearn.metrics import accuracy_score
accuracy_score(ytest, y_model)
```

However, this single number doesn't tell us *where* we've gone wrong—one nice way to do this is to use the *confusion matrix*
单一的数字并不能告诉我们哪里出了问题，一个很好的方法是使用混淆矩阵

```python
from sklearn.metrics import confusion_matrix

mat = confusion_matrix(ytest, y_model)

sns.heatmap(mat, square=True, annot=True, cbar=False)
plt.xlabel('predicted value')
plt.ylabel('true value');
```

This shows us where the mis-labeled points tend to be: for example, a large number of twos here are mis-classified as either ones or eights.
此处可以看到，错误标记的点的位置:例如，这里大量的2被错误地分类为1或8。
Another way to gain intuition into the characteristics of the model is to plot the inputs again, with their predicted labels.
了解模型特性的另一种方法是再次绘制输入，使用它们的预测标签。
We'll use green for correct labels, and red for incorrect labels:
正确的标签用绿色，错误的标签用红色:

```python
fig, axes = plt.subplots(10, 10, figsize=(8, 8),
                         subplot_kw={'xticks':[], 'yticks':[]},
                         gridspec_kw=dict(hspace=0.1, wspace=0.1))

test_images = Xtest.reshape(-1, 8, 8)

for i, ax in enumerate(axes.flat):
    ax.imshow(test_images[i], cmap='binary', interpolation='nearest')
    ax.text(0.05, 0.05, str(y_model[i]),
            transform=ax.transAxes,
            color='green' if (ytest[i] == y_model[i]) else 'red')
```


Examining this subset of the data, we can gain insight regarding where the algorithm might be not performing optimally.
检查数据的这个子集，可以了解算法在哪些地方执行得不是最优的。

To go beyond our 80% classification rate, we might move to a more sophisticated algorithm such as support vector machines (see [In-Depth: Support Vector Machines]()), random forests (see [In-Depth: Decision Trees and Random Forests]()) or another classification approach.
超越80%的分类率,可以使用一个更复杂的算法,如支持向量机([ support vector machines]()),随机树，或其他分类方法。


