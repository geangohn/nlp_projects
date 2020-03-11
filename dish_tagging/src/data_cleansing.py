import pandas as pd
import numpy as np


def clean(df):
    """Cleans the dataset"""
    
    # Drop dishes that does not have product name
    df = df[~df['product_name'].isna()]
    print('taking into account only dishes with product names: {}'.format(df.shape[0]))

    #  Drop dishes without ingredients information
    df = df[~df['ingredients_text'].isna()]
    print('taking into account only dishes with ingredients info: {}'.format(df.shape[0]))

    # Drop dishes that do not have category
    df = df[~df['main_category'].isna()]
    print('taking into account only dishes with category: {}'.format(df.shape[0]))

    # Drop dishes that have category name NOT in English
    df = df[df.main_category.str.contains('en:')]
    print('taking into account only dishes with category in English: {}'.format(df.shape[0]))

    # Drop categories with small value_counts
    big_categories = df.main_category.value_counts()[df.main_category.value_counts() > 300].index.tolist()
    df = df[df['main_category'].isin(big_categories)]
    print('taking into account only categories with value_count > 300: {}'.format(df.shape[0]))

    # Let's drop some confusing categories (that can contain another categories). For example,
    # "Breakfast" can contain "meals"
    drop_categories = ['en:breakfasts', 'en:baby-foods']
    df = df[~df['main_category'].isin(drop_categories)]
    print('taking into account only non-confusing categories: {}'.format(df.shape[0]))

    # Drop dishes with product name lengths < 3 (there are some strange items like 'O')
    df = df[df['product_name'].apply(lambda x: len(x) >= 3)]
    print(
        'taking into account only dishes with correct product_name (product name length >= 3): {}'.format(df.shape[0]))

    # Drop dishes with ingredient info lengths < 5
    df = df[df['ingredients_text'].apply(lambda x: len(x) >= 5)]
    print('taking into account only dishes with correct ingredients_text (ingredients text length >= 5): {}'.format(
        df.shape[0]))

    return df