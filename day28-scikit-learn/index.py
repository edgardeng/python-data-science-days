import matplotlib.pyplot as plt
import numpy as np
import sklearn as sk
import seaborn as sns
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def simple_linear_regression():
    rng = np.random.RandomState(42)
    x = 10 * rng.rand(50)
    y = 2 * x - 1 + rng.randn(50)
    plt.scatter(x, y)

    from sklearn.linear_model import LinearRegression

    model = LinearRegression(fit_intercept=True)
    shape_x = x[:, np.newaxis]
    print(shape_x.shape)
    model.fit(shape_x, y)

    xfit = np.linspace(-1, 11)
    x_fit = xfit[:, np.newaxis]
    y_fit = model.predict(x_fit)

    # plt.scatter(x, y)
    plt.plot(x_fit, y_fit)
    plt.show()


# a Supervised learning example
def iris_classification():
    iris = sns.load_dataset('iris')
    print(iris.head())
    X_iris = iris.drop('species', axis=1)
    print('X_iris.shape:', X_iris.shape)
    y_iris = iris['species']
    print('y_iris.shape:', y_iris.shape)

    from sklearn.model_selection import train_test_split
    # from sklearn.cross_decomposition import train_test_split # Deprecated
    Xtrain, Xtest, ytrain, ytest = train_test_split(X_iris, y_iris, random_state=1)
    from sklearn.naive_bayes import GaussianNB  # 1. choose model class
    model = GaussianNB()                        # 2. instantiate model
    model.fit(Xtrain, ytrain)                   # 3. fit model to data
    y_model = model.predict(Xtest)              # 4. predict on new data

    from sklearn.metrics import accuracy_score
    score = accuracy_score(ytest, y_model)
    print(score)


# Unsupervised learning example:
def iris_dimensionality():
    iris = sns.load_dataset('iris')
    print(iris.head())
    X_iris = iris.drop('species', axis=1)
    print(X_iris.shape)

    from sklearn.decomposition import PCA  # 1. Choose the model class
    model = PCA(n_components=2)            # 2. Instantiate the model with hyperparameters
    model.fit(X_iris)                      # 3. Fit to data. Notice y is not specified!
    X_2D = model.transform(X_iris)         # 4. Transform the data to two dimensions

    # plot the results
    iris['PCA1'] = X_2D[:, 0]
    iris['PCA2'] = X_2D[:, 1]
    sns.lmplot("PCA1", "PCA2", hue='species', data=iris, fit_reg=False);
    plt.show()


# Unsupervised learning:
def iris_clustering():
    iris = sns.load_dataset('iris')
    X_iris = iris.drop('species', axis=1)

    from sklearn.decomposition import PCA  # 1. Choose the model class
    model = PCA(n_components=2)            # 2. Instantiate the model with hyperparameters
    model.fit(X_iris)                      # 3. Fit to data. Notice y is not specified!
    X_2D = model.transform(X_iris)         # 4. Transform the data to two dimensions

    # plot the results
    iris['PCA1'] = X_2D[:, 0]
    iris['PCA2'] = X_2D[:, 1]

    from sklearn.mixture import GaussianMixture      # 1. Choose the model class
    model = GaussianMixture(n_components=3, covariance_type='full')  # 2. Instantiate the model with hyperparameters
    model.fit(X_iris)                    # 3. Fit to data. Notice y is not specified!
    y_gmm = model.predict(X_iris)        # 4. Determine cluster labels

    iris['PCA1'] = X_2D[:, 0]
    iris['PCA2'] = X_2D[:, 1]
    iris['cluster'] = y_gmm
    sns.lmplot("PCA1", "PCA2", data=iris, hue='species', col='cluster', fit_reg=False)
    plt.show()


def exploring_hand_written_digits():
    from sklearn.datasets import load_digits
    digits = load_digits()
    print('image shape:', digits.images.shape)

    fig, axes = plt.subplots(10, 10, figsize=(8, 8),
                             subplot_kw={'xticks':[], 'yticks':[]},
                             gridspec_kw=dict(hspace=0.1, wspace=0.1))

    for i, ax in enumerate(axes.flat):
        ax.imshow(digits.images[i], cmap='binary', interpolation='nearest')
        ax.text(0.05, 0.05, str(digits.target[i]),
                transform=ax.transAxes, color='green')
    X = digits.data
    print('x shape:', X.shape)
    y = digits.target
    print('y shape:', y.shape)

    from sklearn.manifold import Isomap
    iso = Isomap(n_components=2)
    iso.fit(digits.data)
    data_projected = iso.transform(digits.data)
    print('data_projected.shape:', data_projected.shape)

    plt.figure(2)
    #  plot this data to see if we can learn anything from its structure:
    plt.scatter(data_projected[:, 0], data_projected[:, 1], c=digits.target,
                edgecolor='none', alpha=0.5,
                cmap=plt.cm.get_cmap('Spectral', 10))
    plt.colorbar(label='digit label', ticks=range(10))
    plt.clim(-0.5, 9.5)
    plt.show()

    from sklearn.model_selection import train_test_split
    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=0)
    from sklearn.naive_bayes import GaussianNB
    model = GaussianNB()
    model.fit(Xtrain, ytrain)
    y_model = model.predict(Xtest)
    from sklearn.metrics import accuracy_score
    score = accuracy_score(ytest, y_model)
    print('accuracy_score:', score)

    from sklearn.metrics import confusion_matrix
    mat = confusion_matrix(ytest, y_model)
    plt.figure(3)
    sns.heatmap(mat, square=True, annot=True, cbar=False)
    plt.xlabel('predicted value')
    plt.ylabel('true value')
    plt.show()

    plt.figure(4)
    fig, axes = plt.subplots(10, 10, figsize=(8, 8),
                             subplot_kw={'xticks':[], 'yticks':[]},
                             gridspec_kw=dict(hspace=0.1, wspace=0.1))

    test_images = Xtest.reshape(-1, 8, 8)

    for i, ax in enumerate(axes.flat):
        ax.imshow(test_images[i], cmap='binary', interpolation='nearest')
        ax.text(0.05, 0.05, str(y_model[i]),
                transform=ax.transAxes,
                color='green' if (ytest[i] == y_model[i]) else 'red')
    plt.show()


if __name__ == '__main__':
    print('Numpy Version:', np.__version__)
    print('sklearn Version:', sk.__version__)

    # simple_linear_regression()
    # iris_classification()
    # iris_dimensionality()
    # iris_clustering()
    exploring_hand_written_digits()