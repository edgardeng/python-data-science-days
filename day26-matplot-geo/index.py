import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from itertools import chain

'''
python3 pip无法安装Basemap 需要源码下载后直接安装
'''

def geographic_plots():
    plt.figure(figsize=(8, 8))
    m = Basemap(projection='ortho', resolution=None, lat_0=50, lon_0=-100)
    m.bluemarble(scale=0.5);

    # We'll use an etopo image (which shows topographical features both on land and under the ocean) as the map background:
    fig = plt.figure(figsize=(8, 8))
    m = Basemap(projection='lcc', resolution=None,
                width=8E6, height=8E6,
                lat_0=45, lon_0=-100,)
    m.etopo(scale=0.5, alpha=0.5)

    # Map (long, lat) to (x, y) for plotting
    x, y = m(-122.3, 47.6)
    plt.plot(x, y, 'ok', markersize=5)
    plt.text(x, y, ' Seattle', fontsize=12);

def draw_map(m, scale=0.2):
    # draw a shaded-relief image
    m.shadedrelief(scale=scale)

    # lats and longs are returned as a dictionary
    lats = m.drawparallels(np.linspace(-90, 90, 13))
    lons = m.drawmeridians(np.linspace(-180, 180, 13))

    # keys contain the plt.Line2D instances
    lat_lines = chain(*(tup[1][0] for tup in lats.items()))
    lon_lines = chain(*(tup[1][0] for tup in lons.items()))
    all_lines = chain(lat_lines, lon_lines)

    # cycle through these lines and set the desired style
    for line in all_lines:
        line.set(linestyle='-', alpha=0.3, color='w')


if __name__ == '__main__':
    print('Numpy Version:', np.__version__)
    geographic_plots()


