# Financial Data Analysis

This repository contains the code and analysis for a financial dataset. The dataset includes information about various companies' market capitalization and quarterly sales.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Data Cleaning](#data-cleaning)
- [Visualizations](#visualizations)
- [Top Companies](#top-companies)
- [Correlation Analysis](#correlation-analysis)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The purpose of this project is to analyze financial data to gain insights into the market capitalization and quarterly sales of different companies. The analysis includes handling missing values, generating visualizations, and identifying top companies based on market capitalization and sales.

## Dataset

The dataset used in this project consists of 488 entries with the following columns:
- `S.No.`: Serial number
- `Name`: Company name
- `Mar Cap - Crore`: Market Capitalization in crores
- `Sales Qtr - Crore`: Quarterly Sales in crores

## Data Cleaning

The following data cleaning steps were performed:
- Dropped the 'Unnamed: 4' column due to a high number of missing values.
- Filled missing values in 'Mar Cap - Crore' and 'Sales Qtr - Crore' columns with their respective means.

## Visualizations

The project includes several visualizations to explore the data:
1. **Distribution of Market Capitalization**
2. **Distribution of Quarterly Sales**
3. **Scatter plot of Market Capitalization vs. Quarterly Sales**
4. **Correlation Heatmap**

## Top Companies

Identified the top 10 companies based on:
- Market Capitalization
- Quarterly Sales

## Correlation Analysis

Calculated the correlation between Market Capitalization and Quarterly Sales to understand their relationship.

## Installation

To run the code and analysis, you need to have Python and the following packages installed:

- pandas
- matplotlib
- seaborn
- openpyxl
- python-docx

You can install the required packages using pip:

```bash
pip install pandas matplotlib seaborn openpyxl python-docx
```

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/GokulR2003/Financial-Data-analysis
    ```

2. Navigate to the project directory:
    ```bash
    cd financial-data-analysis
    ```

3. Run the analysis script:
    ```bash
    Analysis.py
    ```
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
