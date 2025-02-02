import pandas as pd
from app.utils.preprocessing import clean_product_name
from app.scrapers.scraper_example import scrape_product_prices

# # Load dataset
DATA_PATH = "app/data/product_prices.csv"
data = pd.read_csv(DATA_PATH)

def update_data_with_scraping():
    # Example scraping from a mock site
    scraped_data = scrape_product_prices("https://shopee.co.id/")
    if scraped_data:
        # Clean and prepare scraped data
        df_scraped = pd.DataFrame(scraped_data)
        
        # Feature extraction or standardization
        # For example: clean and add missing features, preprocess data
        df_scraped = preprocess_scraped_data(df_scraped)
        
        # Append cleaned scraped data to the CSV file
        df_scraped.to_csv(DATA_PATH, mode="a", header=False, index=False)

def preprocess_scraped_data(df):
    # Example preprocessing: clean product names, fill missing values, etc.
    df["product_name"] = df["product_name"].apply(clean_product_name)
    df["category"] = df["category"].fillna("Unknown")
    df["price"] = df["price"].fillna(df["price"].mean())
    
    return df

# Recommendation logic
def recommend_price(product_name: str):
    update_data_with_scraping()  # Update data before recommendations

    product_name = clean_product_name(product_name)
    product_prices = data[data["product_name"].str.lower() == product_name.lower()]

    if product_prices.empty:
        return {"message": "Product not found."}

    avg_price = product_prices["price"].mean()
    recommended_price = round(avg_price * 1.1, 2)

    return {
        "product_name": product_name,
        "recommended_price": recommended_price,
        "average_price": avg_price,
    }