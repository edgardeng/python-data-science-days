## Pandas I/O

Pandas implements many api for input/output

|格式类型|	数据描述|	Reader|	Writer|
|:----  |:----  |:----  |:----  |
|text	|CSV	|read_ csv|	to_csv|
|text	|JSON	|read_json|	to_json|
|text	|HTML	|read_html|	to_html|
|text	|clipboard	|read_clipboard	|to_clipboard|
|binary	|Excel	|read_excel|	to_excel|
|binary	|HDF5	|read_hdf|	to_hdf|
|binary	|Feather	|read_feather|	to_feather|
|binary	|Msgpack	|read_msgpack|	to_msgpack|
|binary	|Stata	|read_stata	|to_statav
|binary	|SAS	|read_sas||
|binary	|Python |Pickle	|read_pickle|to_pickle|
|SQL	|SQL	|read_sql	|to_sql
|SQLGoogle	|Big Query	|read_gbq	|to_gbq|

### Input

```python

def to_input(name):
    data_json = pd.read_json(name + 'json', orient='records')
    print('read json ready: \r\n', data_json)

    data_csv = pd.read_csv(name + 'csv', encoding='utf-8', header=0)
    print('read data_csv ready: \r\n', data_csv)

    data_excel = pd.read_excel(name + 'xlsx', sheet_name='student', header=0)
    print('read data_excel ready: \r\n', data_excel)

    data_html = pd.read_html(name + 'html')
    print('read data_html ready: \r\n', data_html)
```

#### read_json

Parameters:

* path_or_buf : a valid JSON string or file-like or URL

* orient : string, Indication of expected JSON string format
    ```
    ‘split’ : dict like {‘index’ -> [index], ‘columns’ -> [columns], ‘data’ -> [values]}
    
    ‘records’ : list like [{column -> value}, … , {column -> value}]
    
    ‘index’ : dict like {index -> {column -> value}}
    
    ‘columns’ : dict like {column -> {index -> value}}
    
    ‘values’ : just the values array
    
    ‘table’ : dict like {‘schema’: {schema}, ‘data’: {data}} describing the data, and the data component is like orient='records'.
    ```
    
* type : type of object to recover (series or frame), default ‘frame’

#### read_csv

* filepath_or_buffer ：tr, path object, or file-like object, url (include http, ftp, s3, and file)

* sep: str, default ‘,’ Delimiter to use.

* delimiter (定界符)：，备选分隔符（如果指定该参数，则sep参数失效）

* header (指定行数用来作为列名): int, list of int, default 0  Row (0-indexed) to use for the column labels of the parsed DataFrame. 

* names (结果的列名列表): array-like, default None List of column names to use. 

* index_col (行索引的列编号或者列名): int, list of int, default None Column (0-indexed) to use as the row labels of the DataFrame. 

#### read_excel

Parameters:

* io : str, file descriptor, pathlib.Path, ExcelFile or xlrd.Book, URL. 

* sheet_name : str, int, list, or None, default 0

    Defaults to 0: 1st sheet as a DataFrame
    1: 2nd sheet as a DataFrame
    "Sheet1": Load sheet with name “Sheet1”
    [0, 1, "Sheet5"]: Load first, second and sheet named “Sheet5” as a dict of DataFrame
    None: All sheets.

#### read_html

Parameters:

* io : str or file-like A URL, a file-like object, or a raw string containing HTML. 
  
* match : str or compiled regular expression, optional

* flavor : str or None, container of strings

  
#### read_sql

```python
import pymysql
import pandas as pd
  
con = pymysql.connect(host="127.0.0.1",user="root",password="password",db="world")
# 读取sql
data_sql=pd.read_sql("select * from *",con)

```

### Output

```python
def to_output(name, data_frame):
    data_frame.to_csv(name + 'csv', index=False)
    print('to_csv ready')
    data_frame.to_json(name + 'json', orient='records') # index, columns values table
    print('to_json ready')
    try:
        data_frame.to_excel(name + 'xlsx', sheet_name='student', engine='xlsxwriter') # index, columns values table
        print('to_excel ready')
    except ModuleNotFoundError as e:
        print(e)

    html_string = '''
        <html>
          <head><title>HTML Pandas Dataframe with CSS</title></head>
          <body>
            {table}
          </body>
        </html>.
        '''
    # OUTPUT AN HTML FILE
    with open(name + 'html', 'w') as f:
        f.write(html_string.format(table=data_frame.to_html(classes='students')))
        
```
#### to_json

#### to_csv

Parameters:

* sep : str, default ‘,’ Field delimiter for the output file.

* na_rep : str, default ‘’ Missing data representation.

* float_format : str, default None Format string for floating point numbers.

* columns : sequence, optional Columns to write.

* header : bool or list of str, default True Write out the column names. If a list of strings is given it is assumed to be aliases for the column names.

* index : bool, default True Write row names (index).

#### to_excel

#### to_html

#### to_sql

```python
from sqlalchemy import create_engine
 
table_name = "user"
 
engine = create_engine(
    "mysql+pymysql://root:0000@127.0.0.1:3306/db_test?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)
conn = engine.connect()
df.to_sql(table_name, conn, if_exists='append',index=False)
```