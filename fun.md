# keras-tqdm

Keras integration with TQDM progress bars.

- TQDM supports nested progress bars. If you have Keras fit and predict loops within an outer TQDM loop, the nested loops will display properly.
- TQDM supports Jupyter/IPython notebooks.
- TQDM looks great!

`TQDMNotebookCallback` with `leave_inner=False` (default)

[![Keras TQDM leave_inner=False](https://github.com/bstriner/keras-tqdm/raw/master/docs/images/leave_inner_False.png)](https://github.com/bstriner/keras-tqdm/raw/master/docs/images/leave_inner_False.png)

`TQDMNotebookCallback` with `leave_inner=True`

[![Keras TQDM leave_inner=True](https://github.com/bstriner/keras-tqdm/raw/master/docs/images/leave_inner_True.png)](https://github.com/bstriner/keras-tqdm/raw/master/docs/images/leave_inner_True.png)

`TQDMCallback` for command-line scripts

[![Keras TQDM CLI](https://github.com/bstriner/keras-tqdm/raw/master/docs/images/console.png)](https://github.com/bstriner/keras-tqdm/raw/master/docs/images/console.png)

## Installation

Stable release

```
pip install keras-tqdm

```

Development release

```
git clone https://github.com/bstriner/keras-tqdm.git
cd keras-tqdm
python setup.py install

```

## Keras

[Keras](https://github.com/fchollet/keras) is an awesome machine learning library for Theano or TensorFlow.

## TQDM

[TQDM](https://github.com/tqdm/tqdm) is a progress bar library with good support for nested loops and Jupyter/IPython notebooks.

## Basic TQDM Usage

Use TQDM to wrap enumerators within loops to create a progress bar. Review TQDM documentation for display options.

```
from tqdm import tqdm
import time
for i in tqdm(range(10)):
    time.sleep(1)

```

## Keras TQDM

Use `keras_tqdm` to utilize TQDM progress bars for Keras fit loops. `keras_tqdm` loops can be nested inside TQDM loops to display nested progress bars (although you can use them inside ordinary for loops as well). Set `verbose=0`to suppress the default progress bar.

```
from keras_tqdm import TQDMCallback
from tqdm import tqdm
for model in tqdm(models, desc="Training several models"):
    model.fit(x, y, verbose=0, callbacks=[TQDMCallback()])
```