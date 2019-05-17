## Day 14 matplot Chart

### Line

```python
    plt.plot(x_data, y_data)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title)
    plt.show()
```

### Bar

```python
    plt.bar(x_data, y_data)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title)
    plt.show()
```

### Pie

```python
    labels = ['frogs', 'hogs', 'dogs', 'logs']
    sizes = [15, 20, 45, 10]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    explode = [0, 0.1 , 0, 0]
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
    plt.axis('equal')
    plt.show()
```

### Scatter

```python
    plt.scatter(x_data, y_data, s=15)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.title(title)
    plt.show()
```
