# Algorithm Analysis and Visualization

This repository contains various algorithms implemented in Python, organized into different labs. Each lab focuses on a specific set of algorithms and includes analysis and visualization of their performance.

## Lab Descriptions

### Lab 1
- **Sorting Algorithms**: Implementation and analysis of various sorting algorithms including Heap Sort, Insertion Sort, Merge Sort, Quick Sort, and Selection Sort.

### Lab 2
- **Activity Selection**: Implementation of the Activity Selection problem.
- **Graph Algorithms**: Implementation and visualization of graph algorithms.
- **N-Queens Problem**: Implementation and visualization of the N-Queens problem.

### Lab 3
- **Advanced Algorithms**: Implementation and analysis of advanced algorithms including Clique, Fibonacci, Hamiltonian Cycle, Knapsack, Las Vegas N-Queens, Miller-Rabin, Parallel Merge Sort, Parallel Quick Sort, Prefix Sum, and Traveling Salesman Problem (TSP).

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- `pip` (Python package installer)

### Create a Python Environment

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

    Or extract the zip file in the appropriate location.

2. **Create a virtual environment**:
    ```sh
    python -m venv env
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        .\env\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source env/bin/activate
        ```

4. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Python Files

To run any Python file, use the following command:
```sh
python <path-to-python-file>
```
For example, to run the TSP algorithm in Lab 3:
```sh
python Lab3/TSP.py
```

### Jupyter Notebooks

To run the Jupyter notebooks for analysis, use the following command:

```sh
jupyter notebook
```

This will open the Jupyter notebook interface in your web browser, where you can navigate to the desired notebook and run the cells.