import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def preprocess_and_create_heatmap_df(df):
    # One-hot encoding for categorical variables
    colour = pd.get_dummies(df, columns=['perceived_colour_master_name'])
    product = pd.get_dummies(df, columns=['product_type_name'])
    
    # Merge the dataframes
    merged_df = pd.merge(colour, product, on='article_id', how='inner')
    
    # Select the product columns for PCA
    product_columns = [
        'product_type_name_Accessories set', 'product_type_name_Alice band', 'product_type_name_Baby Bib',
        'product_type_name_Backpack', 'product_type_name_Bag', 'product_type_name_Ballerinas',
        'product_type_name_Beanie', 'product_type_name_Belt', 'product_type_name_Bikini top',
        'product_type_name_Blanket', 'product_type_name_Blazer', 'product_type_name_Blouse',
        'product_type_name_Bodysuit', 'product_type_name_Bootie', 'product_type_name_Boots',
        'product_type_name_Bra', 'product_type_name_Bra extender', 'product_type_name_Bracelet',
        'product_type_name_Braces', 'product_type_name_Bucket hat', 'product_type_name_Bumbag',
        'product_type_name_Cap', 'product_type_name_Cap/peaked', 'product_type_name_Cardigan',
        'product_type_name_Chem. cosmetics', 'product_type_name_Clothing mist', 'product_type_name_Coat',
        'product_type_name_Costumes', 'product_type_name_Cross-body bag', 'product_type_name_Cushion',
        'product_type_name_Dog Wear', 'product_type_name_Dog wear', 'product_type_name_Dress',
        'product_type_name_Dungarees', 'product_type_name_Earring', 'product_type_name_Earrings',
        'product_type_name_Eyeglasses', 'product_type_name_Felt hat', 'product_type_name_Fine cosmetics',
        'product_type_name_Flat shoe', 'product_type_name_Flat shoes', 'product_type_name_Flip flop',
        'product_type_name_Garment Set', 'product_type_name_Giftbox', 'product_type_name_Gloves',
        'product_type_name_Hair clip', 'product_type_name_Hair string', 'product_type_name_Hair ties',
        'product_type_name_Hair/alice band', 'product_type_name_Hairband', 'product_type_name_Hat/beanie',
        'product_type_name_Hat/brim', 'product_type_name_Headband', 'product_type_name_Heeled sandals',
        'product_type_name_Heels', 'product_type_name_Hoodie', 'product_type_name_Jacket',
        'product_type_name_Jumpsuit/Playsuit', 'product_type_name_Keychain', 'product_type_name_Kids Underwear top',
        'product_type_name_Leg warmers', 'product_type_name_Leggings/Tights', 'product_type_name_Long John',
        'product_type_name_Marker pen', 'product_type_name_Mobile case', 'product_type_name_Moccasins',
        'product_type_name_Necklace', 'product_type_name_Night gown', 'product_type_name_Nipple covers',
        'product_type_name_Other accessories', 'product_type_name_Other shoe', 'product_type_name_Outdoor Waistcoat',
        'product_type_name_Outdoor overall', 'product_type_name_Outdoor trousers', 'product_type_name_Polo shirt',
        'product_type_name_Pre-walkers', 'product_type_name_Pumps', 'product_type_name_Pyjama bottom',
        'product_type_name_Pyjama jumpsuit/playsuit', 'product_type_name_Pyjama set', 'product_type_name_Ring',
        'product_type_name_Robe', 'product_type_name_Sandals', 'product_type_name_Sarong', 'product_type_name_Scarf',
        'product_type_name_Sewing kit', 'product_type_name_Shirt', 'product_type_name_Shorts',
        'product_type_name_Shoulder bag', 'product_type_name_Side table', 'product_type_name_Skirt',
        'product_type_name_Sleep Bag', 'product_type_name_Sleeping sack', 'product_type_name_Slippers',
        'product_type_name_Sneakers', 'product_type_name_Socks', 'product_type_name_Soft Toys',
        'product_type_name_Stain remover spray', 'product_type_name_Straw hat', 'product_type_name_Sunglasses',
        'product_type_name_Sweater', 'product_type_name_Swimsuit', 'product_type_name_Swimwear bottom',
        'product_type_name_Swimwear set', 'product_type_name_Swimwear top', 'product_type_name_T-shirt',
        'product_type_name_Tailored Waistcoat', 'product_type_name_Tie', 'product_type_name_Top',
        'product_type_name_Tote bag', 'product_type_name_Towel', 'product_type_name_Toy',
        'product_type_name_Trousers', 'product_type_name_Umbrella', 'product_type_name_Underdress',
        'product_type_name_Underwear Tights', 'product_type_name_Underwear body', 'product_type_name_Underwear bottom',
        'product_type_name_Underwear corset', 'product_type_name_Underwear set', 'product_type_name_Unknown',
        'product_type_name_Vest top', 'product_type_name_Wallet', 'product_type_name_Washing bag',
        'product_type_name_Watch', 'product_type_name_Waterbottle', 'product_type_name_Wedge',
        'product_type_name_Weekend/Gym bag', 'product_type_name_Wireless earphone case', 'product_type_name_Wood balls',
        'product_type_name_Zipper head'
    ]
    
    # Ensure all columns are present in the DataFrame
    x_df = merged_df[product_columns]
    
    # Standardize the features for PCA
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x_df)
    
    # Apply PCA to reduce dimensionality
    pca = PCA(n_components=0.7)  # Adjust the number of components or the explained variance ratio as needed
    x_pca = pca.fit_transform(x_scaled)
    
    # Create a new DataFrame with PCA result
    df_pca = pd.DataFrame(data=x_pca)
    
    # Combine the PCA results with the original dataframe
    heatmap_df = pd.concat([colour, df_pca], axis=1)
    
    # Drop unnecessary columns
    heatmap_df = heatmap_df.drop(columns=['article_id', 'perceived_colour_master_id', 'product_type_no', 'product_type_name'])
    
    return heatmap_df
