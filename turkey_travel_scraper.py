import requests
from bs4 import BeautifulSoup
import json
import csv
import os
from datetime import datetime, timedelta
import time

class TurkeyTravelScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

        # Create directories for saving travel data
        self.create_directories()

        # Turkish cities and attractions
        self.turkish_cities = {
            'Istanbul': {'lat': 41.0082, 'lon': 28.9784},
            'Ankara': {'lat': 39.9334, 'lon': 32.8597},
            'Izmir': {'lat': 38.4192, 'lon': 27.1287},
            'Antalya': {'lat': 36.8969, 'lon': 30.7133},
            'Cappadocia': {'lat': 38.6431, 'lon': 34.8288},
            'Bodrum': {'lat': 37.0345, 'lon': 27.4305},
            'Pamukkale': {'lat': 37.9200, 'lon': 29.1200}
        }

    def create_directories(self):
        """Create directories for saving travel data"""
        directories = ['turkey_weather', 'turkey_attractions', 'turkey_reports', 'turkey_data']
        for dir_name in directories:
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
                print(f"Created directory: {dir_name}")

    def get_weather_data(self, city):
        """Get weather forecast for Turkish cities"""
        print(f"🌤️  Getting weather for {city}...")

        # Using OpenWeatherMap-like service (free tier)
        try:
            # Alternative: Use a simple weather API
            url = f"https://api.openweathermap.org/data/2.5/weather"
            # Note: You'll need to get a free API key from openweathermap.org
            # For demo purposes, we'll simulate weather data

            # Simulated weather data for Turkey (replace with real API call)
            weather_data = {
                'city': city,
                'temperature': '22°C',
                'condition': 'Sunny',
                'humidity': '60%',
                'wind_speed': '10 km/h',
                'forecast_date': datetime.now().strftime('%Y-%m-%d'),
                'description': 'Perfect weather for sightseeing!'
            }

            return weather_data

        except Exception as e:
            print(f"Error getting weather for {city}: {e}")
            return None

    def scrape_turkey_travel_info(self):
        """Scrape general Turkey travel information"""
        print("🇹🇷 Scraping Turkey travel information...")

        try:
            # Scraping Turkey tourism information (using a travel site)
            url = "https://www.lonelyplanet.com/turkey"

            response = self.session.get(url, timeout=15)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            travel_info = {
                'destination': 'Turkey',
                'scraped_at': datetime.now().isoformat(),
                'highlights': [],
                'travel_tips': [],
                'best_time_to_visit': 'April to October',
                'currency': 'Turkish Lira (TRY)',
                'language': 'Turkish',
                'visa_info': 'e-Visa required for most tourists'
            }

            # Look for highlights and tips
            highlight_elements = soup.find_all(['h2', 'h3', 'p'], text=lambda x: x and any(keyword in str(x).lower() for keyword in ['highlight', 'attraction', 'must see', 'best', 'top']))

            for element in highlight_elements[:10]:
                text = element.get_text(strip=True)
                if len(text) > 20 and len(text) < 200:
                    travel_info['highlights'].append(text)

            return travel_info

        except Exception as e:
            print(f"Error scraping Turkey travel info: {e}")
            # Return default information about Turkey
            return {
                'destination': 'Turkey',
                'scraped_at': datetime.now().isoformat(),
                'highlights': [
                    'Hagia Sophia - Iconic Byzantine architecture in Istanbul',
                    'Cappadocia - Hot air balloons over fairy chimneys',
                    'Pamukkale - White travertine terraces and thermal pools',
                    'Blue Mosque - Beautiful Ottoman architecture',
                    'Grand Bazaar - Historic covered market in Istanbul',
                    'Ephesus - Ancient Greek and Roman ruins',
                    'Turkish Baths (Hammam) - Traditional spa experience',
                    'Bosphorus Cruise - Bridge between Europe and Asia',
                    'Mount Nemrut - Ancient statues and sunrise views',
                    'Turkish Cuisine - Kebabs, baklava, and Turkish delight'
                ],
                'travel_tips': [
                    'Learn basic Turkish phrases - locals appreciate the effort',
                    'Bargain in bazaars and markets - it\'s expected',
                    'Try Turkish breakfast - it\'s a feast!',
                    'Remove shoes when entering mosques',
                    'Carry cash - many places don\'t accept cards',
                    'Book Cappadocia hot air balloon rides in advance'
                ],
                'best_time_to_visit': 'April to October (spring and autumn are ideal)',
                'currency': 'Turkish Lira (TRY)',
                'language': 'Turkish (English widely spoken in tourist areas)',
                'visa_info': 'e-Visa required - apply online before travel'
            }

    def get_currency_rates(self):
        """Get current USD to Turkish Lira exchange rate"""
        print("💱 Getting currency exchange rates...")

        try:
            # Using a free currency API
            url = "https://api.exchangerate-api.com/v4/latest/USD"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()

            currency_info = {
                'base_currency': 'USD',
                'target_currency': 'TRY',
                'exchange_rate': data['rates'].get('TRY', 'N/A'),
                'last_updated': data.get('date', datetime.now().strftime('%Y-%m-%d')),
                'budget_guide': {
                    'budget_daily': '$30-50 USD',
                    'mid_range_daily': '$50-100 USD',
                    'luxury_daily': '$100+ USD',
                    'meal_costs': {
                        'street_food': '$2-5 USD',
                        'restaurant': '$10-20 USD',
                        'fine_dining': '$30+ USD'
                    }
                }
            }

            return currency_info

        except Exception as e:
            print(f"Error getting currency rates: {e}")
            return {
                'base_currency': 'USD',
                'target_currency': 'TRY',
                'exchange_rate': 'Check current rates online',
                'last_updated': datetime.now().strftime('%Y-%m-%d'),
                'note': 'Turkey is generally affordable for tourists'
            }

    def create_turkey_itinerary(self, days=7):
        """Create a suggested itinerary for Turkey"""
        print(f"📅 Creating {days}-day Turkey itinerary...")

        itineraries = {
            7: [
                {'day': 1, 'city': 'Istanbul', 'activities': 'Arrive, Hagia Sophia, Blue Mosque, Grand Bazaar'},
                {'day': 2, 'city': 'Istanbul', 'activities': 'Topkapi Palace, Bosphorus Cruise, Turkish Bath'},
                {'day': 3, 'city': 'Cappadocia', 'activities': 'Travel to Cappadocia, Goreme Open Air Museum'},
                {'day': 4, 'city': 'Cappadocia', 'activities': 'Hot Air Balloon, Underground City, Pottery Workshop'},
                {'day': 5, 'city': 'Pamukkale', 'activities': 'Travel to Pamukkale, Travertine Terraces, Hierapolis'},
                {'day': 6, 'city': 'Istanbul', 'activities': 'Return to Istanbul, Galata Tower, Turkish Cuisine Tour'},
                {'day': 7, 'city': 'Istanbul', 'activities': 'Last-minute shopping, Departure'}
            ],
            14: [
                {'day': 1, 'city': 'Istanbul', 'activities': 'Arrive, Sultanahmet District'},
                {'day': 2, 'city': 'Istanbul', 'activities': 'Museums and Palaces'},
                {'day': 3, 'city': 'Istanbul', 'activities': 'Bosphorus and Asian Side'},
                {'day': 4, 'city': 'Cappadocia', 'activities': 'Travel and Exploration'},
                {'day': 5, 'city': 'Cappadocia', 'activities': 'Hot Air Balloon and Valleys'},
                {'day': 6, 'city': 'Cappadocia', 'activities': 'Underground Cities'},
                {'day': 7, 'city': 'Antalya', 'activities': 'Mediterranean Coast'},
                {'day': 8, 'city': 'Antalya', 'activities': 'Ancient Sites and Beaches'},
                {'day': 9, 'city': 'Pamukkale', 'activities': 'Thermal Springs'},
                {'day': 10, 'city': 'Ephesus', 'activities': 'Ancient Ruins'},
                {'day': 11, 'city': 'Bodrum', 'activities': 'Aegean Coast'},
                {'day': 12, 'city': 'Izmir', 'activities': 'Modern Turkish City'},
                {'day': 13, 'city': 'Istanbul', 'activities': 'Return and Rest'},
                {'day': 14, 'city': 'Istanbul', 'activities': 'Departure'}
            ]
        }

        return itineraries.get(days, itineraries[7])

    def save_travel_report(self, travel_data, weather_data, currency_data, itinerary):
        """Save complete Turkey travel report"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        # Save as HTML report
        html_filename = f"turkey_travel_report_{timestamp}.html"
        html_filepath = os.path.join('turkey_reports', html_filename)

        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🇹🇷 Turkey Travel Guide</title>
    <style>
        body {{ font-family: 'Georgia', serif; margin: 0; padding: 20px; background: linear-gradient(135deg, #e74c3c, #c0392b); color: white; }}
        .container {{ max-width: 900px; margin: 0 auto; background: white; color: #333; padding: 30px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }}
        .header {{ text-align: center; margin-bottom: 30px; }}
        .flag {{ font-size: 3em; margin-bottom: 10px; }}
        h1 {{ color: #e74c3c; margin: 0; font-size: 2.5em; text-shadow: 2px 2px 4px rgba(0,0,0,0.1); }}
        .section {{ margin: 25px 0; padding: 20px; background: #f8f9fa; border-radius: 10px; border-left: 5px solid #e74c3c; }}
        .section h2 {{ color: #c0392b; margin-top: 0; }}
        .highlight {{ background: #fff3cd; padding: 15px; border-radius: 8px; margin: 10px 0; border-left: 4px solid #ffc107; }}
        .itinerary-day {{ background: white; margin: 10px 0; padding: 15px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
        .weather {{ background: linear-gradient(45deg, #3498db, #2980b9); color: white; padding: 15px; border-radius: 10px; text-align: center; }}
        .currency {{ background: linear-gradient(45deg, #27ae60, #229954); color: white; padding: 15px; border-radius: 10px; }}
        ul {{ padding-left: 20px; }}
        li {{ margin: 8px 0; }}
        .footer {{ text-align: center; margin-top: 30px; color: #666; font-style: italic; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="flag">🇹🇷</div>
            <h1>Turkey Travel Guide</h1>
            <p style="color: #666; font-size: 1.1em;">Your Complete Guide to Türkiye</p>
            <p style="color: #999;">Generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</p>
        </div>

        <div class="section">
            <h2>🌟 Top Highlights & Attractions</h2>
"""

        for highlight in travel_data['highlights']:
            html_content += f'            <div class="highlight">✨ {highlight}</div>\n'

        html_content += f"""
        </div>

        <div class="section">
            <h2>🌤️ Weather Information</h2>
            <div class="weather">
"""

        for city, weather in weather_data.items():
            if weather:
                html_content += f"""
                <strong>{city}:</strong> {weather['temperature']} - {weather['condition']}<br>
                Humidity: {weather['humidity']} | Wind: {weather['wind_speed']}<br><br>
"""

        html_content += f"""
            </div>
        </div>

        <div class="section">
            <h2>💱 Currency & Budget Information</h2>
            <div class="currency">
                <strong>Exchange Rate:</strong> 1 USD = {currency_data['exchange_rate']} TRY<br>
                <strong>Daily Budget:</strong><br>
                💰 Budget: {currency_data['budget_guide']['budget_daily']}<br>
                💳 Mid-range: {currency_data['budget_guide']['mid_range_daily']}<br>
                💎 Luxury: {currency_data['budget_guide']['luxury_daily']}
            </div>
        </div>

        <div class="section">
            <h2>📅 Suggested 7-Day Itinerary</h2>
"""

        for day_plan in itinerary:
            html_content += f"""
            <div class="itinerary-day">
                <strong>Day {day_plan['day']}: {day_plan['city']}</strong><br>
                📍 {day_plan['activities']}
            </div>
"""

        html_content += f"""
        </div>

        <div class="section">
            <h2>💡 Travel Tips</h2>
            <ul>
"""

        for tip in travel_data['travel_tips']:
            html_content += f'                <li>{tip}</li>\n'

        html_content += f"""
            </ul>
        </div>

        <div class="section">
            <h2>📋 Essential Information</h2>
            <p><strong>Best Time to Visit:</strong> {travel_data['best_time_to_visit']}</p>
            <p><strong>Currency:</strong> {travel_data['currency']}</p>
            <p><strong>Language:</strong> {travel_data['language']}</p>
            <p><strong>Visa:</strong> {travel_data['visa_info']}</p>
        </div>

        <div class="footer">
            <p>🧳 Happy travels to beautiful Turkey! 🇹🇷</p>
            <p>Generated by Python Travel Scraper</p>
        </div>
    </div>
</body>
</html>
"""

        with open(html_filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"💾 Saved travel report: {html_filepath}")
        return html_filepath

    def run_complete_turkey_analysis(self):
        """Run complete Turkey travel data collection"""
        print("🚀 Starting Complete Turkey Travel Analysis...")
        print("=" * 60)

        # Collect all data
        print("\n1️⃣ Gathering Turkey travel information...")
        travel_data = self.scrape_turkey_travel_info()

        print("\n2️⃣ Getting weather data for major cities...")
        weather_data = {}
        for city in ['Istanbul', 'Cappadocia', 'Antalya', 'Pamukkale']:
            weather_data[city] = self.get_weather_data(city)
            time.sleep(1)  # Be respectful to APIs

        print("\n3️⃣ Getting currency information...")
        currency_data = self.get_currency_rates()

        print("\n4️⃣ Creating suggested itinerary...")
        itinerary = self.create_turkey_itinerary(7)

        print("\n5️⃣ Generating travel report...")
        report_file = self.save_travel_report(travel_data, weather_data, currency_data, itinerary)

        # Save raw data as JSON
        all_data = {
            'travel_info': travel_data,
            'weather': weather_data,
            'currency': currency_data,
            'itinerary': itinerary,
            'generated_at': datetime.now().isoformat()
        }

        json_filename = f"turkey_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        json_filepath = os.path.join('turkey_data', json_filename)

        with open(json_filepath, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, indent=2, ensure_ascii=False)

        print(f"\n✅ Turkey Travel Analysis Complete!")
        print(f"🌐 HTML Report: {report_file}")
        print(f"📊 JSON Data: {json_filepath}")
        print(f"\n🇹🇷 Ready for your Turkish adventure! 🎉")

        return all_data

# Usage
if __name__ == "__main__":
    scraper = TurkeyTravelScraper()
    turkey_data = scraper.run_complete_turkey_analysis()