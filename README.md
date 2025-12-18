# NumPy Learning Summary

---

## 🚀 Why NumPy?

- NumPy arrays are **significantly faster** than Python lists due to optimized C-level implementations.
- They consume **less memory** compared to Python lists.
- NumPy supports **vectorization**, eliminating the need for slow Python loops.
- Designed specifically for **numerical and scientific computing**.

---

## 📦 Array Creation

NumPy arrays can be created in multiple ways:

### From Python Objects
- Create arrays from Python lists and tuples.

### From Scratch
- `np.zeros()` → Creates arrays filled with zeros  
- `np.ones()` → Creates arrays filled with ones  
- `np.full()` → Creates arrays filled with a constant value  
- `np.eye()` → Creates identity matrices  
- `np.arange()` → Generates values like Python `range()`  
- `np.linspace()` → Generates evenly spaced values within a range  

---

## 🔍 Array Properties

Key attributes used to inspect arrays:

- `shape` → Rows and columns of the array  
- `size` → Total number of elements  
- `ndim` → Number of dimensions (1D, 2D, 3D, etc.)  
- `dtype` → Data type of elements (system-dependent)

---

## 🧠 Data Types (dtypes)

NumPy arrays are **homogeneous**, meaning all elements share the same data type.

Common dtypes:
- `int32`, `int64`
- `float32`, `float64`
- `bool`
- `complex64`, `complex128`
- `object` (for Python objects or strings)

### Type Casting
- Data types can be changed using `.astype()` to optimize memory or computation.

---

## 🔄 Reshaping & Flattening

- `reshape()` → Changes array dimensions without changing data
- `flatten()` / `ravel()` → Converts multi-dimensional arrays into 1D

---

## ✂️ Indexing & Slicing

- Supports **basic indexing**, **slicing**, and **multi-dimensional indexing**
- NumPy slicing returns a **view**, not a copy  
  - Changes in the sliced array affect the original array
  - Use `.copy()` to preserve the original data

---

## 🎯 Advanced Indexing

- **Fancy Indexing** → Extract elements using index arrays
- **Boolean Masking** → Filter data using conditions

---

## 🧭 Understanding Axes

Each dimension in NumPy is called an **axis**:

- 1D array → axis 0  
- 2D array → axis 0 (rows), axis 1 (columns)  
- 3D array → axis 0 (depth), axis 1 (rows), axis 2 (columns)

Understanding axes is critical for aggregation and transformations.

---

## ⚡ Vectorization & Broadcasting

- **Vectorization** allows operations on entire arrays without loops.
- **Broadcasting** enables operations on arrays of different shapes without copying data.
- These features greatly improve **performance and memory efficiency**.

---

## 📊 Mathematical & Statistical Functions

NumPy provides optimized functions such as:
- `mean`, `min`, `max`
- `std`, `median`
- `sum`, `unique`
- Element-wise mathematical operations

---

## 🧩 Multidimensional Arrays

- Efficient handling of 2D and 3D arrays
- Crucial for data science, image processing, and machine learning
- Indexing and axis manipulation are key concepts

---

## ✅ Additional Concepts

- `np.where()` for conditional selection
- `np.concatenate()`, `np.vstack()`, `np.hstack()` for array joining
- `copy()` vs `view()` distinction
- `axis` parameter in aggregation functions
- Difference between `flatten()` and `ravel()`

---

## 📌 Conclusion

NumPy forms the **foundation of the Python data ecosystem**. Mastering array creation, indexing, broadcasting, vectorization, and axis manipulation is essential before moving to libraries like Pandas, Matplotlib, and machine learning frameworks.

This repository serves as a structured reference for my NumPy fundamentals and practice.

---

# Pandas – Data Analysis & Manipulation

Pandas is a powerful Python library designed for **data manipulation, cleaning, exploration, and analysis**. It provides high-level data structures that make working with structured data intuitive, efficient, and expressive.

---

## 📦 Core Data Structures

### 1. Series
- One-dimensional labeled data structure
- Similar to a column in a table
- Supports index-based alignment and vectorized operations

### 2. DataFrame
- Two-dimensional tabular data structure
- Rows and columns with labels
- Primary object used for data analysis tasks

---

## 📥 Data Ingestion

Pandas supports loading data from multiple real-world sources:
- CSV and text files
- Excel spreadsheets
- JSON data
- SQL databases
- APIs and external data pipelines

This makes Pandas ideal for **end-to-end data workflows**, starting from raw data.

---

## 🔍 Data Inspection & Understanding

Key concepts for understanding datasets:
- Viewing top and bottom records
- Understanding column names and data types
- Shape and dimensionality of data
- Summary statistics for numerical features
- Identifying missing and inconsistent values

This step is crucial before any analysis or modeling.

---

## 🧹 Data Cleaning & Preprocessing

Pandas plays a central role in data cleaning, which consumes most of a data analyst’s time.

Covered concepts include:
- Handling missing values
- Removing duplicates
- Fixing inconsistent formats
- Renaming and reordering columns
- Type conversion for optimization and correctness
- Detecting and handling outliers

Clean data leads to reliable insights.

---

## ✂️ Indexing, Selection & Filtering

Pandas offers powerful data selection techniques:
- Label-based indexing
- Position-based indexing
- Boolean filtering using conditions
- Selecting subsets of rows and columns

These operations enable precise and readable data extraction.

---

## 🔄 Data Transformation

Common transformation operations include:
- Creating new derived columns
- Applying functions across rows or columns
- Replacing and mapping values
- Sorting data
- Ranking and binning values

Transformation helps convert raw data into **analysis-ready formats**.

---

## 📊 Exploratory Data Analysis (EDA)

Pandas is heavily used during EDA to:
- Understand data distributions
- Identify trends and patterns
- Detect anomalies and correlations
- Perform quick aggregations

It integrates seamlessly with visualization libraries for deeper insights.

---

## 🧮 Aggregation & Grouping

Grouping is one of Pandas’ most powerful features.

Concepts include:
- Grouping data by one or multiple keys
- Applying aggregation functions
- Summarizing data at different granularities
- Generating business-level metrics

This is widely used in reporting and analytics.

---

## 🔗 Merging & Joining Data

Real-world data often comes from multiple sources.

Pandas supports:
- Combining datasets using joins
- Concatenation of datasets
- Aligning data based on indexes or keys

This enables relational-style data analysis.

---

## ⏱️ Time Series Handling

Pandas provides strong support for time-based data:
- Date and time parsing
- Indexing by time
- Resampling and frequency conversion
- Rolling and window-based operations

Essential for financial, log, and temporal datasets.

---

## ⚡ Performance & Efficiency

Key performance principles:
- Vectorized operations instead of loops
- Memory-efficient data handling
- Optimized backend built on NumPy

Understanding these helps scale analysis to larger datasets.

---

## 📌 Role of Pandas in Data Science

Pandas sits at the **center of the data science lifecycle**:
- Used after data collection
- Critical during data cleaning and EDA
- Feeds clean data into visualization and machine learning workflows

It acts as the **bridge between raw data and insights**.

---

## ✅ Summary

Pandas is an essential library for:
- Structured data handling
- Data cleaning and transformation
- Exploratory data analysis
- Business and analytical reporting

---

# Matplotlib & Seaborn – Data Visualization

Matplotlib and Seaborn are Python libraries used for **data visualization**, enabling analysts and data scientists to explore data, identify patterns, and communicate insights effectively through visual representations.

Visualization plays a critical role during **Exploratory Data Analysis (EDA)** and **communication of results**.

---

## 📊 Matplotlib – Core Visualization Library

Matplotlib is the **foundational plotting library** in Python. Most visualization libraries, including Seaborn, are built on top of it.

### Key Characteristics
- Low-level, highly customizable plotting library
- Full control over plot elements
- Suitable for both simple and complex visualizations
- Widely used for static visual outputs

---

## 📈 Common Plot Types in Matplotlib

Matplotlib supports a wide range of visualizations, including:
- Line plots (trends over time)
- Bar charts (categorical comparisons)
- Histograms (distribution analysis)
- Scatter plots (relationship between variables)
- Box plots (spread and outliers)
- Pie charts (proportions)

Each plot can be customized in terms of labels, titles, scales, colors, and layout.

---

## 🎯 Customization & Control

Matplotlib allows fine-grained control over:
- Axes and ticks
- Figure size and resolution
- Labels, titles, and legends
- Grid lines and annotations
- Multiple plots in a single figure

This makes it suitable for **publication-quality** visuals.

---

## 🔍 Role of Matplotlib in Data Science

Matplotlib is commonly used for:
- Quick data inspection
- Creating custom visualizations
- Understanding numerical trends
- Building the base for advanced visual libraries

It is often the first visualization library learned in Python.

---

## 🌊 Seaborn – Statistical Data Visualization

Seaborn is a **high-level visualization library** built on top of Matplotlib that simplifies the creation of **statistical and aesthetically pleasing plots**.

It is especially powerful for **EDA and pattern discovery**.

---

## 📌 Key Features of Seaborn

- Built-in themes and color palettes
- Works seamlessly with Pandas DataFrames
- Automatically handles labels and legends
- Simplifies complex statistical plots
- Focused on visualizing relationships in data

---

## 📊 Common Plot Types in Seaborn

Seaborn provides specialized plots for statistical analysis:
- Distribution plots (histograms, KDE)
- Box plots and violin plots
- Scatter and line plots with grouping
- Pair plots for multivariate analysis
- Heatmaps for correlation analysis
- Categorical plots for group comparisons

These plots help reveal patterns that are difficult to see in raw data.

---

## 🧠 Statistical Insights with Seaborn

Seaborn is commonly used to:
- Understand data distributions
- Analyze relationships between variables
- Detect correlations and trends
- Compare categories visually
- Identify outliers and anomalies

It reduces the effort required to perform **statistical visualization**.

---

## 🔄 Matplotlib vs Seaborn

| Aspect | Matplotlib | Seaborn |
|------|------------|---------|
| Level | Low-level | High-level |
| Customization | Very high | Moderate |
| Ease of Use | Verbose | Simple & concise |
| Aesthetics | Manual | Built-in |
| Best Use | Custom plots | Statistical EDA |

They are often used **together**, not as alternatives.

---

## 📌 Role in Data Science Workflow

Matplotlib and Seaborn are mainly used during:
- Exploratory Data Analysis (EDA)
- Feature understanding
- Result validation
- Reporting and storytelling

Clear visuals lead to better decision-making.
