## Pandas Aggregation in Pandas

### Simple Aggregation

```python
rng = np.random.RandomState(42)
ser = pd.Series(rng.rand(5))
ser.sum()
ser.mean()

df = pd.DataFrame({'A': rng.rand(5),
                   'B': rng.rand(5)})
df.mean()
df.mean(axis='columns')                 

```

The following table summarizes some other built-in Pandas aggregations:

|Aggregation	|Description|
|:----|:----|
|count()	|Total number of items|
|first(), last()	|First and last item|
|mean(), median()	|Mean and median|
|min(), max()	|Minimum and maximum|
|std(), var()	|Standard deviation and variance|
|mad()	|Mean absolute deviation|
|prod()	|Product of all items|
|sum()	|Sum of all items|


### GroupBy

```python
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'data': range(6)}, columns=['key', 'data'])
df.groupby('key').sum()
```

#### The GroupBy object

The GroupBy object supports column indexing in the same way as the DataFrame, and returns a modified GroupBy object

```python
planets.groupby('method')
planets.groupby('method')['orbital_period']
planets.groupby('method')['orbital_period'].median()

# direct iteration over the groups, returning each group as a Series or DataFrame:

for (method, group) in planets.groupby('method'):
    print("{0:30s} shape={1}".format(method, group.shape))
    
# the describe() method of DataFrames to perform a set of aggregations that describe each group in the data:
planets.groupby('method')['year'].describe().unstack()

    
```

#### Aggregate, filter, transform, apply

In particular, GroupBy objects have aggregate(), filter(), transform(), and apply() methods that efficiently implement a variety of useful operations before combining the grouped data.

```python
def filter_func(x):
    return x['data2'].std() > 4


def norm_by_data2(x):
    # x is a DataFrame of group values
    x['data1'] /= x['data2'].sum()
    return x


def before_combining():
    rng = np.random.RandomState(0)
    df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                       'data1': range(6),
                       'data2': rng.randint(0, 10, 6)},
                      columns=['key', 'data1', 'data2'])
    # take a string, a function, or a list thereof, and compute all the aggregates at once
    agg1 = df.groupby('key').aggregate(['min', np.median, max])
    agg2 = df.groupby('key').aggregate({'data1': 'min',
                                        'data2': 'max'})
    agg3 = df.groupby('key').std()
    filt = df.groupby('key').filter(filter_func) # drop data based on the group properties.
    t = df.groupby('key').transform(lambda x: x - x.mean()) # some transformed version of the full data to recombine.
    # apply an arbitrary function to the group results
    a = df.groupby('key').apply(norm_by_data2)
   
    # Specifying the split key
    L = [0, 1, 0, 1, 2, 0]
    s1= df.groupby(L).sum() # A list, array, series, or index providing the grouping keys
    s2 = df.groupby(df['key']).sum()
    df2 = df.set_index('key')
    mapping = {'A': 'vowel', 'B': 'consonant', 'C': 'consonant'}
    s3 = df2.groupby(mapping).sum() # dictionary
    agg4 = df2.groupby(str.lower).mean() # function
    agg5 = df2.groupby([str.lower, mapping]).mean() # list
```

put all these together and count discovered planets by method and by decade:
 
```python
decade = 10 * (planets['year'] // 10)
decade = decade.astype(str) + 's'
decade.name = 'decade'
planets.groupby(['method', decade])['number'].sum().unstack().fillna(0)
```
