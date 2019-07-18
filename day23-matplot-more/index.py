import matplotlib.pyplot as plt
import numpy as np


def error_bar():
    plt.style.use('seaborn-whitegrid')
    x = np.linspace(0, 10, 50)
    dy = 0.8
    y = np.sin(x) + dy * np.random.randn(50)

    plt.errorbar(x, y, yerr=dy, fmt='.k')
    plt.errorbar(x, y, yerr=dy, fmt='o', color='black',
                ecolor='lightgray', elinewidth=3, capsize=0)
    plt.show()


def continuous_error():
    from sklearn.gaussian_process import GaussianProcess
    # define the model and draw some data
    model = lambda x: x * np.sin(x)
    xdata = np.array([1, 3, 5, 6, 8])
    ydata = model(xdata)

    # Compute the Gaussian process fit
    gp = GaussianProcess(corr='cubic', theta0=1e-2, thetaL=1e-4, thetaU=1E-1,
                         random_start=100)
    gp.fit(xdata[:, np.newaxis], ydata)

    xfit = np.linspace(0, 10, 1000)
    yfit, MSE = gp.predict(xfit[:, np.newaxis], eval_MSE=True)
    dyfit = 2 * np.sqrt(MSE)  # 2*sigma ~ 95% confidence region
    # Visualize the result
    plt.plot(xdata, ydata, 'or')
    plt.plot(xfit, yfit, '-', color='gray')
    plt.fill_between(xfit, yfit - dyfit, yfit + dyfit,
                     color='gray', alpha=0.2)
    plt.xlim(0, 10)

def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)


def density_contour():
    plt.style.use('seaborn-white')
    x = np.linspace(0, 5, 50)
    y = np.linspace(0, 5, 40)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    # a standard line-only contour plot:
    # plt.contour(X, Y, Z, colors='black');
    # the lines can be color-coded by specifying a colormap with the ``cmap`` argument.
    plt.contour(X, Y, Z, 20, cmap='RdGy') # chose the ``RdGy`` (short for *Red-Gray*) colormap
    #  add a ``plt.colorbar()`` command, which automatically creates an additional axis with labeled color information for the plot:
    # plt.colorbar()

    # plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy')
    # plt.colorbar()
    # plt.axis(aspect='image')
    #
    contours = plt.contour(X, Y, Z, 3, colors='black')
    plt.clabel(contours, inline=True, fontsize=8)
    plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy', alpha=0.5)
    plt.colorbar()
    plt.show()


def hist():
    plt.style.use('seaborn-white')
    # data = np.random.randn(1000)
    # # plt.hist(data)
    # plt.hist(data, bins=30, density=True, alpha=0.8, histtype='stepfilled', color='steelblue', edgecolor='none')
    # x1 = np.random.normal(0, 0.8, 1000)
    # x2 = np.random.normal(-2, 1, 1000)
    # x3 = np.random.normal(3, 2, 1000)
    # kwargs = dict(histtype='stepfilled', alpha=0.3, density=True, bins=50)
    # plt.hist(x1, **kwargs)
    # plt.hist(x2, **kwargs)
    # plt.hist(x3, **kwargs)
    # counts, bin_edges = np.histogram(data, bins=5)
    # print(counts)
    # plt.show()

    # Two-Dimensional Histograms and Binnings 二维直方图
    mean = [0, 0]
    cov = [[1, 1], [1, 2]]
    x, y = np.random.multivariate_normal(mean, cov, 10000).T
    # plt.hist2d(x, y, bins=30, cmap='Blues')
    # cb = plt.colorbar()
    # cb.set_label('counts in bin')
    # counts, xedges, yedges = np.histogram2d(x, y, bins=30)
    # plt.show()

    '''
    The two-dimensional histogram creates a tesselation of squares across the axes.
    Another natural shape for such a tesselation is the regular hexagon.
    '''
    # plt.hexbin(x, y, gridsize=30, cmap='Blues')
    # cb = plt.colorbar(label='count in bin')
    # plt.show()

    '''
    Kernel density estimation
    Another common method of evaluating densities in multiple dimensions is *kernel density estimation* (KDE).
    '''
    from scipy.stats import gaussian_kde
    data = np.vstack([x, y])  # fit an array of size [Ndim, Nsamples]
    kde = gaussian_kde(data)

    # evaluate on a regular grid
    xgrid = np.linspace(-3.5, 3.5, 40)
    ygrid = np.linspace(-6, 6, 40)
    Xgrid, Ygrid = np.meshgrid(xgrid, ygrid)
    Z = kde.evaluate(np.vstack([Xgrid.ravel(), Ygrid.ravel()]))

    # Plot the result as an image
    plt.imshow(Z.reshape(Xgrid.shape),
               origin='lower', aspect='auto',
               extent=[-3.5, 3.5, -6, 6],
               cmap='Blues')
    cb = plt.colorbar()
    cb.set_label("density")
    plt.show()


if __name__ == '__main__':
    print('Numpy Version:', np.__version__)
    # error_bar()
    # continuous_error()
    # density_contour()
    hist()