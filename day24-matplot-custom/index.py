import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.legend import Legend

plt.style.use('classic')


def custom_legend():
    x = np.linspace(0, 10, 1000)
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), '-b', label='Sine')
    ax.plot(x, np.cos(x), '--r', label='Cosine')
    ax.axis('equal')
    leg = ax.legend()
    # specify the location and turn off the frame:
    ax.legend(loc='upper left', frameon=False)
    # specify the number of columns in the legend:
    ax.legend(frameon=False, loc='lower center', ncol=2)
    # use a rounded box (``fancybox``) or add a shadow,
    # change the transparency (alpha value) of the frame,
    # change the padding around the text:
    ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
    plt.show()


def choose_element_legend():
    x = np.linspace(0, 10, 1000)
    ## Choosing Elements for the Legend
    y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))
    lines = plt.plot(x, y)
    # lines is a list of plt.Line2D instances
    plt.legend(lines[:2], ['first', 'second'])
    plt.plot(x, y[:, 0], label='first')
    plt.plot(x, y[:, 1], label='second')
    plt.plot(x, y[:, 2:])
    plt.legend(framealpha=1, frameon=True)
    plt.show()


def points_size():
    '''
    Legend for Size of Points
    '''
    cities = pd.read_csv('../assets/data/california_cities.csv')
    # Extract the data we're interested in
    lat, lon = cities['latd'], cities['longd']
    population, area = cities['population_total'], cities['area_total_km2']
    # Scatter the points, using size and color but no label
    plt.scatter(lon, lat, label=None,
                c=np.log10(population), cmap='viridis',
                s=area, linewidth=0, alpha=0.5)
    plt.axis(aspect='equal')
    plt.xlabel('longitude')
    plt.ylabel('latitude')
    plt.colorbar(label='log$_{10}$(population)')
    plt.clim(3, 7)

    # Here we create a legend:
    # we'll plot empty lists with the desired size and label
    for area in [100, 300, 500]:
        plt.scatter([], [], c='k', alpha=0.3, s=area,
                    label=str(area) + ' km$^2$')
    plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Area')
    plt.title('California Cities: Area and Population')
    plt.show()


def multiple_legends():
    fig, ax = plt.subplots()
    lines = []
    styles = ['-', '--', '-.', ':']
    x = np.linspace(0, 10, 1000)
    for i in range(4):
        lines += ax.plot(x, np.sin(x - i * np.pi / 2),
                         styles[i], color='black')
    ax.axis('equal')
    # specify the lines and labels of the first legend
    ax.legend(lines[:2], ['line A', 'line B'], loc='upper right', frameon=False)
    # Create the second legend and add the artist manually.
    leg = Legend(ax, lines[2:], ['line C', 'line D'], loc='lower right', frameon=False)
    ax.add_artist(leg)
    plt.show()


def custom_color_bars():
    x = np.linspace(0, 10, 1000)
    y = np.sin(x) * np.cos(x[:, np.newaxis])
    plt.imshow(y)
    plt.colorbar()
    # plt.imshow(y, cmap='gray')
    # plt.cm.ma
    plt.show()


def gray_scale_cmap(cmap):
    from matplotlib.colors import LinearSegmentedColormap

    """Return a grayscale version of the given colormap"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))

    # convert RGBA to perceived grayscale luminance
    # cf. http://alienryderflex.com/hsp.html
    RGB_weight = [0.299, 0.587, 0.114]
    luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
    colors[:, :3] = luminance[:, np.newaxis]

    return LinearSegmentedColormap.from_list(cmap.name + "_gray", colors, cmap.N)


def view_colormap(cmap):
    """Plot a colormap with its grayscale equivalent"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))

    cmap = gray_scale_cmap(cmap)
    grayscale = cmap(np.arange(cmap.N))

    fig, ax = plt.subplots(2, figsize=(6, 2),
                           subplot_kw=dict(xticks=[], yticks=[]))
    ax[0].imshow([colors], extent=[0, 10, 0, 1])
    ax[1].imshow([grayscale], extent=[0, 10, 0, 1])
    plt.show()


def choose_color_bar():
    x = np.linspace(0, 10, 1000)
    I = np.sin(x) * np.cos(x[:, np.newaxis])
    speckles = (np.random.random(I.shape) < 0.01)
    I[speckles] = np.random.normal(0, 3, np.count_nonzero(speckles))

    plt.figure(figsize=(10, 3.5))

    plt.subplot(1, 2, 1)
    plt.imshow(I, cmap='RdBu')
    plt.colorbar()

    plt.subplot(1, 2, 2)
    plt.imshow(I, cmap='RdBu')
    plt.colorbar(extend='both')
    plt.clim(-1, 1)

    ### Discrete Color Bars
    plt.imshow(I, cmap=plt.cm.get_cmap('Blues', 6))
    plt.colorbar()
    plt.clim(-1, 1)
    plt.show()


def exmaple_handwritten_digits():
    from sklearn.manifold import Isomap
    from sklearn.datasets import load_digits
    digits = load_digits(n_class=6)

    fig, ax = plt.subplots(8, 8, figsize=(6, 6))
    for i, axi in enumerate(ax.flat):
        axi.imshow(digits.images[i], cmap='binary')
        axi.set(xticks=[], yticks=[])
    iso = Isomap(n_components=2)
    projection = iso.fit_transform(digits.data)

    # plot the results
    plt.scatter(projection[:, 0], projection[:, 1], lw=0.1,
                c=digits.target, cmap=plt.cm.get_cmap('cubehelix', 6))
    plt.colorbar(ticks=range(6), label='digit value')
    plt.clim(-0.5, 5.5)
    plt.show()


def sub_plot_by_hand():
    # ax1 = plt.axes()  # standard axes
    # ax2 = plt.axes([0.65, 0.65, 0.2, 0.2])

    fig = plt.figure()
    ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4],
                       xticklabels=[], ylim=(-1.2, 1.2))
    ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4],
                       ylim=(-1.2, 1.2))

    x = np.linspace(0, 10)
    ax1.plot(np.sin(x))
    ax2.plot(np.cos(x))
    plt.show()


def grid_of_plots():
    fig = plt.figure()
    fig.subplots_adjust(hspace=0.4, wspace=0.4)

    for i in range(1, 7):
        ax = fig.add_subplot(2, 3, i)
        ax.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')

    fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
    for i in range(2):
        for j in range(3):
            ax[i, j].text(0.5, 0.5, str((i, j)), fontsize=18, ha='center')

    plt.show()


def complicated_arrangements_plots():
    # grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
    mean = [0, 0]
    cov = [[1, 1], [1, 2]]
    x, y = np.random.multivariate_normal(mean, cov, 3000).T

    # Set up the axes with gridspec
    fig = plt.figure(figsize=(6, 6))
    grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
    main_ax = fig.add_subplot(grid[:-1, 1:])
    y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
    x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)

    # scatter points on the main axes
    main_ax.plot(x, y, 'ok', markersize=3, alpha=0.2)

    # histogram on the attached axes
    x_hist.hist(x, 40, histtype='stepfilled',
                orientation='vertical', color='gray')
    x_hist.invert_yaxis()

    y_hist.hist(y, 40, histtype='stepfilled',
                orientation='horizontal', color='gray')
    y_hist.invert_xaxis()
    plt.show()


if __name__ == '__main__':
    # custom_legend()
    # choose_element_legend()
    # points_size()
    # multiple_legends()
    # custom_color_bars()
    # view_colormap('jet')
    # view_colormap('viridis') # cubehelix, RdBu
    # choose_color_bar()
    # exmaple_handwritten_digits()
    # sub_plot_by_hand()
    # grid_of_plots()
    complicated_arrangements_plots()