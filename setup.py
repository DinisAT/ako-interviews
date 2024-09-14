import pandas as pd

def merge_weekly():

    transac_sku_pos_d_1z_df = pd.read_parquet('s3://dinis-data-bucket-for-texting/transac.parquet')
    ac_last_update_df = pd.read_parquet('s3://dinis-data-bucket-for-texting/ac_last_update.parquet')
    pos_last_update_df = pd.read_parquet('s3://dinis-data-bucket-for-texting/pos_last_update.parquet')
    sku_last_update_df = pd.read_parquet('s3://dinis-data-bucket-for-texting/sku_last_update.parquet')



    transac_sku_pos_d_1z_df["date"] = pd.to_datetime(transac_sku_pos_d_1z_df["date"])
    transac_sku_pos_d_1z_df["date"] = transac_sku_pos_d_1z_df['date'] - \
        pd.to_timedelta(transac_sku_pos_d_1z_df['date'].dt.weekday, unit='D')

    transac_sku_pos_d_1z_df['nopendays'] = 1



    #logger.info(f'Creating nopendays column')

    transac_sku_pos_d_1z = transac_sku_pos_d_1z_df.groupby(
        ["sku","pos","date"]
        ).agg(
            qty=("qty","sum"),
            item_selling_price=("item_selling_price","mean"),
            item_prediscount_price=("item_prediscount_price","max"),
            item_production_cost=("item_production_cost","max"),
            currency=("currency","first"),
            nopendays=("nopendays",'sum')).reset_index()
    del transac_sku_pos_d_1z_df

    start_date = transac_sku_pos_d_1z.date.min()

    end_date = transac_sku_pos_d_1z.date.max()

    mondays = pd.date_range(start=start_date,end=end_date,freq='W-MON')

    mondays_df = pd.DataFrame(mondays,columns=['date'])
    del mondays

    sku_pos_df = transac_sku_pos_d_1z[["sku","pos"]].drop_duplicates()\
                                                    .reset_index(drop=True)

    sku_pos_date_df = sku_pos_df.merge(
                                    mondays_df,
                                    how='cross')
    del sku_pos_df

    df_sales = sku_pos_date_df.merge(
                                transac_sku_pos_d_1z,
                                on=["sku","pos","date"],
                                how="left",
                                validate="1:1")
    del sku_pos_date_df
    del transac_sku_pos_d_1z

    df_sales.qty = df_sales.qty.fillna(0)

    df_sales.nopendays = df_sales.nopendays.fillna(0)

    df_sales.currency = "EUR"
    df_sales = pd.concat([df_sales[["sku","pos"]],
                          df_sales.groupby(["sku","pos"]).ffill()],
                          axis=1)

    sku_2_production_cost = df_sales.dropna().groupby("sku").item_production_cost\
        .first().to_frame().reset_index()

    df_sales = df_sales.drop(columns=["item_production_cost"])

    df_sales = df_sales.merge(
                        sku_2_production_cost,
                        on="sku",
                        how="left",
                        validate="m:1")
    del sku_2_production_cost

    df_sales["item_prediscount_price"] = df_sales.groupby(
        ["sku","pos"]).item_prediscount_price.bfill()

    sku_2_item_prediscount_price = df_sales.dropna().groupby("sku")\
        .item_prediscount_price.max().rename("item_prediscount_price2")\
            .to_frame().reset_index()

    df_sales = df_sales.merge(
                        sku_2_item_prediscount_price,
                        on="sku",
                        how="left",
                        validate="m:1")
    del sku_2_item_prediscount_price

    df_sales.loc[df_sales.item_prediscount_price.isna(),
                 "item_prediscount_price"] = df_sales.loc[df_sales\
                     .item_prediscount_price.isna(), "item_prediscount_price2"]

    df_sales = df_sales.drop(columns=["item_prediscount_price2"])

    df_sales.loc[df_sales.item_selling_price.isna(),
                 "item_selling_price"] = df_sales.loc[
                     df_sales.item_selling_price.isna(),
                     "item_prediscount_price"
                     ]

    product = ac_last_update_df.merge(
                                sku_last_update_df,
                                on="ac",
                                how="right",
                                validate="1:m")

    del ac_last_update_df
    del sku_last_update_df

    df_sales = df_sales.merge(
                        product,
                        on="sku",
                        how="left",
                        validate="m:1")
    del product

    df_sales = df_sales.drop(columns='is_active')

    df_sales = df_sales.merge(
                        pos_last_update_df,
                        on="pos",
                        how="left",
                        validate="m:1")
    del pos_last_update_df


    return df_sales

merge_weekly()
