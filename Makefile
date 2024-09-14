# Makefile for running individual and all unit tests

# Define the path to the test script
TEST_SCRIPT = tests/unity_test.py

# Targets to run each individual test
test_columns_exist:
	python -m unittest $(TEST_SCRIPT).TestRetailFashionDataEngineering.test_columns_exist

test_date_range:
	python -m unittest $(TEST_SCRIPT).TestRetailFashionDataEngineering.test_date_range

test_unique_id_count:
	python -m unittest $(TEST_SCRIPT).TestRetailFashionDataEngineering.test_unique_id_count

test_season_values:
	python -m unittest $(TEST_SCRIPT).TestRetailFashionDataEngineering.test_season_values

test_sales_season_values:
	python -m unittest $(TEST_SCRIPT).TestRetailFashionDataEngineering.test_sales_season_values

test_actual_season_values:
	python -m unittest $(TEST_SCRIPT).TestRetailFashionDataEngineering.test_actual_season_values

test_color_values:
	python -m unittest $(TEST_SCRIPT).TestRetailFashionDataEngineering.test_color_values

test_gender_values:
	python -m unittest $(TEST_SCRIPT).TestRetailFashionDataEngineering.test_gender_values

test_family_values:
	python -m unittest $(TEST_SCRIPT).TestRetailFashionDataEngineering.test_family_values

test_family2_values:
	python -m unittest $(TEST_SCRIPT).TestRetailFashionDataEngineering.test_family2_values

test_article_count:
	python -m unittest $(TEST_SCRIPT).TestRetailFashionDataEngineering.test_article_count

test_resampling:
	python -m unittest $(TEST_SCRIPT).TestRetailFashionDataEngineering.test_resampling

# Target to run all tests at once
test_all:
	python -m unittest discover -s tests -p "unity_test.py"

# Default target
all: test_all
