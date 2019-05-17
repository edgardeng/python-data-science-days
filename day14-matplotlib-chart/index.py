# matplotlib chart

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as matplot


# pie
def pie_plot():
    labels = ['frogs', 'hogs', 'dogs', 'logs']
    sizes = [15, 20, 45, 10]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    explode = [0, 0.1 , 0, 0]
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
    plt.axis('equal')
    plt.show()


# line
def line_plot(x_data, y_data, x_label="", y_label="", title=""):
    plt.plot(x_data, y_data)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title)
    plt.show()


# scatter
def scatter_plot(x_data, y_data, x_label="", y_label="", title=""):
    plt.scatter(x_data, y_data, s=15)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title)
    plt.show()


# Histogram
def histogram_plot(x_data, y_data, x_label="", y_label="", title=""):
    plt.bar(x_data, y_data)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title)
    plt.show()


# Stack Bar
def stack_bar_plot(x_data, y_data, legends, x_label="", y_label="", title=""):
    p1 = plt.bar(x_data, y_data[0], 1)
    p2 = plt.bar(x_data, y_data[1], 1, bottom=y_data[0])
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title)
    plt.legend((p1[0], p2[0]), (legends[0], legends[1]))
    plt.show()


def figure_chart():
    ages = np.arange(1, 6)
    names = ['A', 'B', 'C', 'D', 'E']
    weight_min = [9.1, 15.2, 13.0, 18.8, 16.6]
    weight_max = [11.3, 17.0, 16.4, 18.3, 21.1]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    plt.figure(figsize=(6, 15))

    plt.subplot(5, 2, 1)
    plt.plot(ages, weight_min)
    plt.plot(ages, weight_max)
    # plt.plot(ages, weight_min, 'ro')
    # plt.plot(ages, weight_max, 'go')
    plt.title('Line')
    plt.grid(True)

    plt.subplot(5, 2, 2)
    plt.barh(ages, weight_min, 0.5)
    plt.title('barh')
    plt.grid(True)

    plt.subplot(5, 2, 3)
    plt.pie(weight_min, labels=names, autopct='%1.1f%%',
            shadow=True, startangle=90)
    plt.axis('equal')
    plt.title('Pie')

    # ring
    plt.subplot(5, 2, 4)
    size = 0.3
    plt.pie(weight_min, radius=1, autopct='%1.1f%%', colors=colors, wedgeprops=dict(width=size, edgecolor='w'))
    plt.pie(weight_max, radius=1-size, autopct='%1.1f%%', colors=colors, wedgeprops=dict(width=size, edgecolor='w'))
    # plt.set(aspect="equal", title='Pie plot with `ax.pie`')
    plt.title('Ring')

    # bar
    width = 0.35
    plt.subplot(5, 2, 5)
    plt.bar(ages - width/2, weight_min, width, color='SkyBlue')
    plt.bar(ages + width/2, weight_max, width, color='IndianRed')
    plt.title('bar')

    # histogram
    plt.subplot(5, 2, 6)
    plt.bar(ages,weight_min,width,color='b')
    plt.bar(ages,weight_max,width,color='r', bottom=weight_min) #叠加sales_SH的层叠图 图2
    plt.title('stack bar')

    plt.subplot(5, 2, 7)
    plt.scatter(ages, weight_min, s=15)
    plt.title('scatter')

    r = 2 * np.random.rand(20)
    theta = 2 * np.pi * np.random.rand(20)
    area = 10 * r**2
    colors = theta
    plt.subplot(5, 2, 8, projection='polar')
    plt.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
    plt.title('polar scatter')

    data = np.random.randint(10, size=(20, 5))
    # data = np.random.lognormal(size=(20, 5), mean=1.5, sigma=1.75)
    plt.subplot(5, 2, 9)
    plt.boxplot(data, labels=names)
    plt.title('box')

    plt.subplot(5, 2, 10)
    plt.boxplot(data, labels=names, showfliers=False)
    plt.title('box')

    plt.show()


if __name__ == '__main__':
    print('Numpy Version:', np.__version__)
    print('MatplotVersion:', matplot.__version__)
    # line_plot(ages, weight_min, 'Age', 'Min Weight', 'Children-Age-Weight')
    # pie_plot()
    # scatter_plot(ages, weight_min, 'Age', 'Min Weight', 'Children-Age-Weight')
    # histogram_plot(ages, weight_min, 'Age', 'Min Weight', 'Children-Age-Weight')
    # stack_bar_plot(ages, [weight_min, weight_max], ['Min Weight', 'Max Weight'], 'Age', 'Min Weight', 'Children-Age-Weight')
    figure_chart()
