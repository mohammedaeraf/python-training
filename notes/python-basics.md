### Python Tutorial: Basics and Key Libraries

Python is a versatile, high-level programming language known for its readability and simplicity. It’s widely used for web development, data analysis, automation, machine learning, and more. Below is a detailed tutorial covering language basics and some essential libraries.

---

### 1. **Python Basics**

#### **1.1 Installing Python**

1. **Download Python**: Visit the official Python website ([https://www.python.org/downloads/](https://www.python.org/downloads/)) and download the latest version.
2. **Install Python**: During installation, ensure the option "Add Python to PATH" is checked.

You can verify the installation by typing `python --version` in the terminal.

#### **1.2 Variables and Data Types**

Python is dynamically typed, meaning you don’t need to declare variable types.

```python
# Variables
x = 10          # Integer
pi = 3.14       # Float
name = "John"   # String
is_active = True # Boolean
```

Common data types:

* **int**: Integer (e.g., `10`)
* **float**: Decimal numbers (e.g., `3.14`)
* **str**: String (e.g., `"Hello"`)
* **bool**: Boolean (e.g., `True`, `False`)

#### **1.3 Input and Output**

* **Input**: Use `input()` to capture user input.
* **Output**: Use `print()` to display results.

```python
name = input("Enter your name: ")
print("Hello", name)
```

#### **1.4 Control Structures**

* **Conditional Statements**:

```python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

* **Loops**:

  * **For Loop**: Iterates over a sequence (like a list, string, or range).

    ```python
    for i in range(5):
        print(i)  # Outputs numbers from 0 to 4
    ```

  * **While Loop**: Repeats as long as a condition is true.

    ```python
    i = 0
    while i < 5:
        print(i)
        i += 1
    ```

#### **1.5 Functions**

Functions in Python are defined using the `def` keyword.

```python
def greet(name):
    return "Hello, " + name

print(greet("Alice"))  # Output: Hello, Alice
```

#### **1.6 Lists, Tuples, and Dictionaries**

* **List**: Mutable sequence of items.

  ```python
  fruits = ["apple", "banana", "cherry"]
  print(fruits[0])  # Output: apple
  ```

* **Tuple**: Immutable sequence.

  ```python
  coordinates = (10, 20)
  print(coordinates[1])  # Output: 20
  ```

* **Dictionary**: Key-value pairs.

  ```python
  person = {"name": "John", "age": 30}
  print(person["name"])  # Output: John
  ```

---

### 2. **Key Libraries in Python**

#### **2.1 NumPy**

NumPy is a library for numerical computations, especially with arrays.

**Installation**: `pip install numpy`

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Output: [1 2 3 4 5]
```

**Key Features**:

* Efficient array operations.
* Mathematical functions (e.g., `np.sin()`, `np.mean()`).
* Multi-dimensional arrays.

#### **2.2 Pandas**

Pandas is used for data manipulation and analysis, especially with structured data like CSV files.

**Installation**: `pip install pandas`

```python
import pandas as pd

# Creating a DataFrame
data = {"Name": ["John", "Anna", "Mike"], "Age": [30, 24, 45]}
df = pd.DataFrame(data)
print(df)
```

**Key Features**:

* DataFrames for tabular data.
* Data cleaning and manipulation.
* File handling (CSV, Excel).

#### **2.3 Matplotlib**

Matplotlib is a plotting library for creating static, animated, and interactive visualizations in Python.

**Installation**: `pip install matplotlib`

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 40, 50]
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Plot')
plt.show()
```

**Key Features**:

* 2D plots like line graphs, bar charts, histograms, etc.
* Customization of plot styles, labels, and legends.

#### **2.4 Seaborn**

Seaborn is built on top of Matplotlib and is used for statistical data visualization.

**Installation**: `pip install seaborn`

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
tips = sns.load_dataset("tips")
sns.barplot(x="day", y="total_bill", data=tips)
plt.show()
```

**Key Features**:

* Beautiful and informative statistical graphs.
* Works seamlessly with Pandas DataFrames.
* Heatmaps, pair plots, and categorical plots.

#### **2.5 Scikit-learn**

Scikit-learn is a machine learning library in Python, offering simple and efficient tools for data mining and data analysis.

**Installation**: `pip install scikit-learn`

```python
from sklearn.linear_model import LinearRegression

# Sample data
X = [[1], [2], [3], [4], [5]]
y = [1, 2, 3, 4, 5]

# Train a model
model = LinearRegression()
model.fit(X, y)

# Predict
print(model.predict([[6]]))  # Output: [6.]
```

**Key Features**:

* Algorithms for classification, regression, clustering.
* Data preprocessing and feature extraction.
* Cross-validation.

#### **2.6 Flask**

Flask is a lightweight web framework for building web applications.

**Installation**: `pip install flask`

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

**Key Features**:

* Simple, flexible, and lightweight.
* Ideal for small web applications.
* Extensive ecosystem for extensions.

---

### 3. **Conclusion**

This tutorial introduces the basic syntax and core features of Python, along with some essential libraries. Mastering these basics will prepare you for more advanced topics like data analysis, machine learning, and web development. As you progress, practicing real-world projects and exploring more libraries will enhance your Python skills.
