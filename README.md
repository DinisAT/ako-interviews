# Retail-Fashion Data Engineering Challenge

## Setup

To download the current repo:

`git clone https://github.com/your-username/your-private-repo.git`

## Data Overview

The data is represented in 4 tables related to the retail-fashion industry.


### Tables

1. **transac.parquet**: Represents each sale that occurred for each SKU item.
2. **pos.parquet**: Represents the stores for a particular client, whether they are active or not, and their features.
3. **sku.parquet**: Represents the association from SKU to AC.
4. **ac.parquet**: Represents the features and hierarchy of each AC.


### Table Columns

#### **transac.parquet**
- **sku**: Item reference.
- **pos**: Store where it was sold.
- **date**: Date of the transaction.
- **country**: Store country.
- **qty**: Number of items sold in that transaction.
- **item_prediscount_price**: Item's original price.
- **item_selling_price**: Item's sold price.
- **currency**: Currency used for the transaction.

#### **pos.parquet**
- **pos**: Store name.
- **category**: Store type.
- **address**: Store physical address.
- **country**: Country where the store is located.
- **cluster**: Group to which the store belongs.
- **geographical_cluster**: Geographical group to which the store belongs.
- **max_storage_unit_capacity_sku**: Storage capacity per each item reference.
- **is_active**: 0 or 1, where 1 identifies the store is active and 0 identifies it is not active anymore.
- **city**: City where the store is located.

#### **sku.parquet**
- **sku**: Item reference denominated by Article-Size.
- **ac**: Article-Color reference (without size).
- **size**: Item size (e.g., 36, 38, 40, M, L, XXL, etc.).

#### **ac.parquet**
- **ac**: Article-Color reference.
- **color**: Item's main color.
- **gender**: Male | Female | Unisex.
- **material**: Main material used.
- **collection**: Winter or the season of the year it was launched.
- **article**: Article reference without color or size.
- **family_old**: Older denomination for the family.
- **family2_old**: Older denomination of family2.
- **family**: Family name to which the article belongs.
- **family2**: Family2 name to which the article belongs.
- **attributes**: Item attributes.
- **replaced_ac**: Old AC reference the current AC reference is replacing.
- **marketing_rate**: Scale from 1 to 4 (currently not in use).
- **is_active**: 0 or 1, where 1 identifies the AC is active and 0 identifies it is not active anymore.
- **article_color**: Article reference with color.
- **leadtime_prod_w**: Item production information.


## Test Goal
From these 4 tables, create a pipeline of data cleaning and transformation, where we expect the following outcome:

### Outcome Columns

- **ds**: Date.
- **unique_id**: AC reference.
- **y**: Quantity of articles sold.
- **season**: Season (Winter/Summer) it was sold and the year, e.g., **2023SS**.
- **sales_season**: Boolean (Was it sold during the sales season or not). Sales Seasons: June 01 - July 15 | January 01 - February 15 | Black Friday.
- **actual_season**: Season it was launched, e.g., unique values: ['WINTER', 'SPRING', 'SUMMER', 'AUTUMN'].
This are the values corresponding to actual_season column
        {12: 'WINTER', 1: 'WINTER', 2: 'WINTER',   # December, January, February
        3: 'SPRING', 4: 'SPRING', 5: 'SPRING',     # March, April, May
        6: 'SUMMER', 7: 'SUMMER', 8: 'SUMMER',     # June, July, August
        9: 'AUTUMN', 10: 'AUTUMN', 11: 'AUTUMN'}    # September, October, November

- **iscovid**: Boolean (1 if sold during the COVID season, 0 if not).
- **is_pub_holidays**: Boolean (1 if sale happened during a public holiday, 0 if not). Note: Sales happened in France.
- **color**: Main color of the AC reference.
- **item_value__w**: Average original price for the corresponding week (per AC).
- **nopendays**: Average number of open days the stores were open during that week (Note: Not every store will sell the same ACs, so it corresponds to the stores selling the current AC).
- **is_active**: Boolean (Current identifier if AC is active or not).
- **discount_perc**: Average sale discount for that current week (per AC).
- **gender**: Male | Female | Unisex.
- **family**: Family name to which the AC belongs.
- **family2**: Family2 name to which the AC belongs.
- **article**: Article reference to which the AC belongs.



### Outcome Format

#### Table

| Idx | Column           | Non-Null Count | Dtype          |
|-----|------------------|----------------|----------------|
| 0   | ds               | 117988 non-null| datetime64[ns] |
| 1   | unique_id        | 117988 non-null| object         |
| 2   | y                | 117988 non-null| float64        |
| 3   | season           | 117988 non-null| object         |
| 4   | sales_season     | 117988 non-null| int64          |
| 5   | actual_season    | 117988 non-null| object         |
| 6   | iscovid          | 117988 non-null| int64          |
| 7   | is_pub_holidays  | 117988 non-null| int64          |
| 8   | color            | 117988 non-null| object         |
| 9   | item_value__w    | 117988 non-null| float32        |
| 10  | nopendays        | 117988 non-null| float64        |
| 12  | is_active        | 117988 non-null| int64          |
| 13  | discount_perc    | 117988 non-null| float32        |
| 14  | gender           | 117988 non-null| object         |
| 15  | family           | 117988 non-null| object         |
| 16  | family2          | 117988 non-null| object         |
| 17  | article          | 117988 non-null| object         |


### Sampling

The rows should be resampled by week on a Monday.

**Example:**

- **original_dates** = ['2023-06-05', '2023-06-06', '2023-06-07', '2023-06-08', '2023-06-09', '2023-06-10', '2023-06-11']
- **resampled_date** = '2023-06-05'




# Code Evaluation

### Code Quality

- Write clean, readable, and well-structured code.
- Follow Python best practices and PEP 8 standards.
- Use meaningful variable and function names to enhance code readability.


### Modular Design

- Divide the code into well-defined functions and/or classes.
- Ensure that each function or class has a single responsibility and is reusable.
- Avoid hard-coding values. Instead, use parameters or configuration files.


### Documentation

- Include comments and docstrings to explain the logic, input, and output of functions or classes.
- Provide a README file explaining the approach, assumptions, and how to run the code.
- Document any dependencies or libraries used.


### Error Handling

- Include proper error handling and logging to manage unexpected issues.
- Handle missing data or incorrect data types gracefully.


## Efficiency and Performance

- Consider the computational efficiency of your solution. Optimize where possible to handle large datasets.
- Provide an analysis of time complexity or profiling results if there are performance concerns.


# Savings Results
The results have to be saved on the output_data folder, name processed_data in parquet format.

"output_data/processed_data.parquet"

# Tests

## How to test your final pipeline
- Use the 'make' cli command to ensure your pipeline passes all the tests before you submit the result.
- Ensure you only need the method .run() to source, transform, save the data.

## Submiting Results
- Create a repository in github.com, and upload your code, together with all the necessary files to run the code.
- Share the repository to dinis.timoteo@ako-ai.com

## Results Evaluation:
1. Processed data passes all tests
2. Code Evaluation (mentioned above)
3. Efficiency and Performance (mentioned above)


# Final Considerations
1. Ensure the setup.py is code to install all the necessary packages.
2. Ensure the requirements.txt contain the packages and versions used.
3. Bonus points for the use of Dask instead of Pandas.
