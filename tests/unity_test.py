import unittest
import pandas as pd
from pipeline.main import Pipeline

class TestRetailFashionDataEngineering(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pipeline = Pipeline()
        pipeline.run()
        # Load the preprocessed DataFrame from the 'outcome' folder
        cls.df_preped = pd.read_parquet('output_data/processed_data.parquet')

    def test_columns_exist(self):
        # Test that all required columns exist
        expected_columns = [
            'ds', 'unique_id', 'y', 'season', 'sales_season', 'actual_season',
            'iscovid', 'is_pub_holidays', 'color', 'item_value__w', 'nopendays',
            'is_active', 'discount_perc', 'gender', 'family', 'family2', 'article'
        ]
        self.assertTrue(set(expected_columns).issubset(self.df_preped.columns))

    def test_date_range(self):
        # Test that 'ds' column has the correct date range
        self.assertEqual(self.df_preped['ds'].min(), pd.Timestamp('2023-01-02'))
        self.assertEqual(self.df_preped['ds'].max(), pd.Timestamp('2023-12-25'))

    def test_unique_id_count(self):
        # Test that 'unique_id' column has the correct number of unique values
        self.assertEqual(self.df_preped['unique_id'].nunique(), 2269)

    def test_season_values(self):
        # Test that 'season' column contains only expected values
        expected_seasons = ['2023SS', '2023FW']
        self.assertTrue(set(self.df_preped['season'].unique()).issubset(expected_seasons))

    def test_sales_season_values(self):
        # Test that 'sales_season' column contains only 0 and 1
        expected_sales_season = [0, 1]
        self.assertTrue(set(self.df_preped['sales_season'].unique()).issubset(expected_sales_season))

    def test_actual_season_values(self):
        # Test that 'actual_season' column contains only expected values
        expected_actual_season = ['WINTER', 'SPRING', 'SUMMER', 'AUTUMN']
        self.assertTrue(set(self.df_preped['actual_season'].unique()).issubset(expected_actual_season))

    def test_color_values(self):
        # Test that 'color' column contains only expected values
        expected_colors = ['Grey', 'Special', 'Black', 'White', 'Brown', 'Beige', 'Pink',
                           'Green', 'Blue', '-', 'Yellow', 'Red', 'Purple', 'Orange']
        self.assertTrue(set(self.df_preped['color'].unique()).issubset(expected_colors))

    def test_gender_values(self):
        # Test that 'gender' column contains only expected values
        expected_genders = ['Unisex', 'Men', 'Women']
        self.assertTrue(set(self.df_preped['gender'].unique()).issubset(expected_genders))

    def test_family_values(self):
        # Test that 'family' column contains only expected values
        expected_families = ['Underwear And Pyjamas', 'Accessories And Jewelry', 'Bags',
                             'Sweaters', 'Pants', 'Tops And T-Shirts', 'Coats And Jackets',
                             'Shorts And Skirts', 'Shoes', 'Dresses And Jumpsuits']
        self.assertTrue(set(self.df_preped['family'].unique()).issubset(expected_families))

    def test_family2_values(self):
        # Test that 'family2' column contains only expected values
        expected_family2 = ['Socks', 'Sunglasses', 'Hat and cap', 'Scarves and shawls',
                            'Beach bag', 'Boxer shorts', 'Hooded sweater', 'Jogging',
                            'Long-sleeved T-shirt', 'Short-sleeved T-shirt',
                            'Hoodless sweater', 'Suit pants', 'Sport jacket', 'Bomber',
                            'Special shape top', 'Sports skirts and shorts', 'Polo shirt',
                            'Puffer vest', 'Straight-cut jeans', 'Long coat',
                            'Raincoat and windproof jacket', 'Fleecejacket and quilted jacket',
                            'Jean jacket', 'Bras', 'Panties and briefs', 'Tank top',
                            'Mid-high boots', 'Sneakers', 'Rain and snow boots', 'High boots',
                            'Shorts and Bermuda shorts', 'Blazer', 'Wide-leg pants',
                            'Straight-leg pants and chinos', 'Other coat and jacket',
                            'Jacket without sleeves', 'Knit sweater', 'Legging',
                            'Other overalls and dresses', 'Cardigan', 'Mid-length skirt',
                            'Long dress', 'Crop Top', 'Slim and skinny jeans', 'Mini dress',
                            'Parka', 'Turtleneck sweater', 'Mini skirt', 'Blouse',
                            'Long skirts', 'Mid dress', 'Trench', 'Espadrilles sandals and clogs',
                            'Other footwear', 'Handbag', 'Pouch', 'Luggage suitcase and travel bag',
                            'Shoulder bag', 'Earrings', 'Necklace', 'Belt', 'Beanie']
        self.assertTrue(set(self.df_preped['family2'].unique()).issubset(expected_family2))

    def test_article_count(self):
        # Test that 'article' column has the correct number of unique values
        self.assertEqual(self.df_preped['article'].nunique(), 630)

    def test_resampling(self):
        # Test that the data is resampled correctly per W-MON
        example_dates = ['2023-06-05', '2023-06-06', '2023-06-07', '2023-06-08', '2023-06-09', '2023-06-10', '2023-06-11']
        resampled_date = pd.Timestamp('2023-06-05')
        example_df = pd.DataFrame({'ds': pd.to_datetime(example_dates)})
        example_df.set_index('ds', inplace=True)
        resampled_df = example_df.resample('W-MON').asfreq()
        self.assertEqual(resampled_df.index[0], resampled_date)


if __name__ == '__main__':
    unittest.main()
