# Pandas I/O

import pandas as pd
import numpy as np


def to_input(name):
    data_json = pd.read_json(name + 'json', orient='records')
    print('read json ready: \r\n', data_json)

    data_csv = pd.read_csv(name + 'csv', encoding='utf-8', header=0)
    print('read data_csv ready: \r\n', data_csv)

    data_excel = pd.read_excel(name + 'xlsx', sheet_name='student', header=0)
    print('read data_excel ready: \r\n', data_excel)

    data_html = pd.read_html(name + 'html')
    print('read data_html ready: \r\n', data_html)


def to_output(name, data_frame):
    data_frame.to_csv(name + 'csv', index=False)
    print('to_csv ready')
    data_frame.to_json(name + 'json', orient='records') # index, columns values table
    print('to_json ready')
    try:
        data_frame.to_excel(name + 'xlsx', sheet_name='student', index=False, engine='xlsxwriter') # index, columns values table
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
        f.write(html_string.format(table=data_frame.to_html(classes='students', index=False)))
    print('to_html ready')


if __name__ == '__main__':
    print('Numpy Version:', np.__version__)
    print('Pandas Version:', pd.__version__)
    json = pd.read_json('../assets/data/data.json', orient='records')
    print(json)
    name = '../assets/data/student.'
    to_output(name, json)
    to_input(name)
