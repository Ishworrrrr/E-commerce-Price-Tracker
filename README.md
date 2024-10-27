# E-commerce Price Tracker 📉

Welcome to the **E-commerce Price Tracker**! This project is designed to monitor product prices on **Flipkart** and send notifications when prices fall below a specified threshold. The program uses Python and various libraries to scrape product information, making it ideal for those looking to track price changes and get the best deals.

## Table of Contents
- [Features](https://github.com/Ishworrrrr/E-commerce-Price-Tracker/blob/main/README.md#features-)
- [Technologies Used](https://github.com/Ishworrrrr/E-commerce-Price-Tracker/blob/main/README.md#technologies-used-)
- [Getting Started](https://github.com/Ishworrrrr/E-commerce-Price-Tracker/blob/main/README.md#getting-started-)
- [Usage](https://github.com/Ishworrrrr/E-commerce-Price-Tracker/blob/main/README.md#usage-)
- [Future Enhancements](https://github.com/Ishworrrrr/E-commerce-Price-Tracker/blob/main/README.md#future-enhancements-)
- [License](https://github.com/Ishworrrrr/E-commerce-Price-Tracker/blob/main/README.md#license-)

---

## Features 🌟

- **Real-Time Price Tracking**: Fetches and analyzes the current price of a product on Flipkart.
- **Price Drop Notifications**: Uses Pushbullet to send instant notifications when the price drops below a specified threshold.
- **Easy Setup**: Minimal configuration required to start tracking your desired product.
- **Customizable**: Modify the code to monitor prices of various products from multiple websites.

## Technologies Used 🛠

- **Python**: Core programming language.
- **BeautifulSoup**: For web scraping HTML data.
- **Requests**: To send HTTP requests to Flipkart’s servers.
- **Pushbullet**: For sending notifications directly to your device.

## Getting Started 🚀

### Prerequisites
- **Python 3.9+**: Ensure Python is installed. [Download Python](https://www.python.org/downloads/)
- **Pushbullet API Key**: Sign up for Pushbullet, generate an API key, and insert it into the script.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ishworrrrr/E-commerce-Price-Tracker-
   cd E-commerce-Price-Tracker
   ```

2. **Install Required Libraries**:
   ```bash
   pip install -r requirements.txt
   ```
   *(Ensure `requirements.txt` includes `requests`, `bs4`, and `pushbullet.py`)*

3. **Set Up Your API Key**:
   - Replace the placeholder `API_KEY` in the code with your Pushbullet API key.

## Usage 💡

1. **Modify the Product URL**: Update the product URL in the code with the link to your desired Flipkart product.
2. **Run the Script**:
   ```bash
   python flipkart_scrapping.py
   ```
3. **Receive Notifications**: You’ll get a notification if the product price falls below the set threshold.

## Future Enhancements 🔮

- **Support for Multiple Websites**: Expand to other e-commerce platforms like Amazon, eBay, etc.
- **Scheduled Tracking**: Automate the script to run at specific intervals for real-time price monitoring.
- **Historical Price Data**: Store price data to observe trends over time.

---

## License 📝
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Feel free to reach out with suggestions or improvements. Enjoy tracking your prices with **E-commerce Price Tracker**! 🎉
