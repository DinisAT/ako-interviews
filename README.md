# Data

The data is represented in 4 tables, and correspondes to Retail-Fashion.

## Tables
**transac.parquet** : Represent each sale occured for each SKU item
**pos.parquet** : Represents the stores for a particular client that are activate or not, and its features.
**sku.parquet** : Represents the association from SKU to AC
**ac.parquet** : Represent the features and hierchy of each AC.

## Tables Columns
###
**transac.parquet**
*sku* : Item reference
*pos* : Store it was sold
*date* : Date of the transaction
*country* : Store Country
*qty* : Number of items sold in that transaction
*item_prediscount_price* : Item original price
*item_selling_price* : Item sold price
*currency* : Currency used for the transaction

**pos.parquet**
*pos* : Store Name
*category* : Store type
*addres* : Store Physical Address
*country* : Country where the store is located
*cluster* : Group to which the store belongs
*geographical_cluster* : Geo group to which the store belongs
*max_storage_unit_capacity_sku* : Storage Capacity per each item reference.
*is_active* : 0 or 1 where 1 identifies the Store is active and 0 identifies is not active anymore.
*city* : City where the store is located

**sku.parquet**
*sku* : Item reference denominated by Article-Size
*ac* : Article-Color reference (without size)
*size* : Item size (eg.: 36, 38, 40, M, L XXL, etc)

**ac.parquet**
*ac* : Article-Color reference
*color* : Item main color
*gender* : Male | Female | Unisex
*material* : Main material used
*collection* : Winter or Season of the Year it was launched
*article* : Article reference without Color or Size
*family_old* : Older denominations for family
*family2_old* : Older denomination of family2
*family* : Family name to which the Article belongs too.
*family2* : Family2 name to which the Article belongs too.
*attributes* : Item attributes
*replaced_ac* : Old AC reference the current AC reference is replacing
*marketing_rate* : Scale from 1 to 4 (currently not in use)
*is_active* : 0 or 1 where 1 identifies the AC is active and 0 identifies is not active anymore.
*article_color* : Article Reference with color
'image' : item image
'leadtime_prod_w' : Item production information


# Test Goal

From this 4 tables, create a pipeline of cleaning and transsformation, where we expect the following:

## Outcome Columns:

*ds* : Date
*unique_id* : ac reference
*y* : quantity of articles sold
*season* : Season (Winter/Summer) it was sold and year eg. format: **2023SS**
*sales_season* : Boolean (was it sold during sales season or not) Sales Seasons: June-01 till July-15 | January-01 till February-15 | Black Friday
*actual_season* : Season it was launched eg. unique values: ['WINTER', 'SPRING', 'SUMMER', 'AUTUMN']
*iscovid* : Boolean (1 if sold during covid season, 0 if not)
*is_pub_holidays* : Boolean (1 if sale happen during a public holiday, 0 if not) Note: sales happened in France.
*color* : main color of the AC reference
*item_value__w* : Average original for the corresponding week (per AC)
*nopendays* : Average number of open days the Stores was open on that week (Note: Not every store will sell the sames AC's, so it's corresponding to the Stores selling that current AC)
*is_active* : Boolean (current identifier if AC is active or not)
*discount_perc* : Average Sale discount for that current week (per AC)
*gender* : Male | Female | Unisex
*family* : Family name to which the AC belongs too.
*family2* : Family2 name to which the AC belongs too.
*article* : Article reference to which the AC belongs too.

## Outcome Format

### Table

Idx  Column           Non-Null Count   Dtype
---  ------           --------------   -----
 0   ds               117988 non-null  datetime64[ns]
 1   unique_id        117988 non-null  object
 2   y                117988 non-null  float64
 3   season           117988 non-null  object
 4   sales_season     117988 non-null  int64
 5   actual_season    117988 non-null  object
 6   iscovid          117988 non-null  int64
 7   is_pub_holidays  117988 non-null  int64
 8   color            117988 non-null  object
 9   item_value__w    117988 non-null  float32
 10  nopendays        117988 non-null  float64
 12  is_active        117988 non-null  int64
 13  discount_perc    117988 non-null  float32
 14  gender           117988 non-null  object
 15  family           117988 non-null  object
 16  family2          117988 non-null  object
 17  article          117988 non-null  object

### Sampling

The rows should be resampled by Week on a Monday

**Example:**

*original_dates* = ['2023-06-05', '2023-06-06', '2023-06-07', '2023-06-08',
                  '2023-06-09', '2023-06-10', '2023-06-11']

*resampled_date* = '2023-06-05'

## Code Evaluation:
### Code Quality:
- Write clean, readable, and well-structured code.
- Follow Python best practices and PEP 8 standards.
- Use meaningful variable and function names to enhance code readability.

### Modular Design:
- Divide the code into well-defined functions and/or classes.
- Ensure that each function or class has a single responsibility and is reusable.
- Avoid hard-coding values. Instead, use parameters or configuration files.

### Documentation:
- Include comments and docstrings to explain the logic, input, and output of functions or classes.
- Provide a README file explaining the approach, assumptions, and how to run the code.
- Document any dependencies or libraries used.

### Error Handling:
- Include proper error handling and logging to manage unexpected issues.
- Handle missing data or incorrect data types gracefully.

## Efficiency and Performance:
- Consider the computational efficiency of your solution. Optimize where possible to handle large datasets.
- Provide an analysis of time complexity or profiling results if there are performance concerns.
