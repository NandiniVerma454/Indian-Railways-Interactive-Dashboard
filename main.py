import streamlit as st
import requests
from datetime import date
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown("""
<style>

/* Main content glass effect */
.block-container {
    background: rgba(0, 0, 0, 0.45);   /* black with transparency */
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 1.2rem;
    border-radius: 18px;
    border: 1px solid rgba(255, 255, 255, 0.15); /* subtle glass edge */
}
</style>
""", unsafe_allow_html=True)


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Train Status Checker",
    page_icon="🚆",
    layout="wide"
)
add_bg_from_local("bg.jpg")
st.markdown("""
<style>

/* Metric label */
div[data-testid="stMetricLabel"] {
    font-size: 16px;
    color: #6c757d;
}

/* Metric value */
div[data-testid="stMetricValue"] {
    font-size: 20px;
    font-weight: 700;
    color: yellow;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🚆 About Trains")
import random
history = [
"1853: First passenger train ran in India",
"1854: First railway workshop established",
"1861: Railways expanded nationwide",
"1870: Network crossed 5,000 km",
"1881: First tramway introduced",
"1900: Rail electrification began",
"1925: First electric train ran",
"1930: Steam engines expanded",
"1947: Railways aided independence movement",
"1951: Indian Railways nationalized",
"1955: Regional zones formed",
"1969: Rajdhani Express launched",
"1972: Shatabdi planning began",
"1980: Metro rail concept emerged",
"1986: Computerized reservations started",
"1995: Freight modernization began",
"1999: IRCTC established",
"2002: Online ticket booking launched",
"2008: Dedicated freight corridors planned",
"2010: High-speed rail proposals",
"2014: Station redevelopment initiatives",
"2016: Bio-toilets introduced",
"2018: WiFi at stations expanded",
"2019: Vande Bharat launched",
"2020: Shramik Special trains operated",
"2021: Driverless metro introduced",
"2022: Smart station upgrades",
"2023: New Vande Bharat routes",
"2024: Modern station designs announced",
"1856: First goods train ran",
"1865: Railways reached southern India",
"1875: Rail bridges expanded",
"1890: Gauge standardization started",
"1910: Mechanical signaling introduced",
"1920: Electric traction studies",
"1935: Diesel locomotives tested",
"1940: Railways used for wartime logistics",
"1950: Freight operations expanded",
"1960: Suburban rail expanded",
"1970: Reservation systems improved",
"1985: Railway automation began",
"1990: Digital signaling introduced",
"2000: GPS systems piloted",
"2005: E-ticket adoption increased",
"2012: High-speed corridor planning",
"2015: Clean station drives",
"2017: Coach modernization",
"2018: LED signaling upgrades",
"2019: Semi-high-speed era began",
"2020: Railways ensured supply chains",
"2021: AI-based monitoring",
"2022: Green energy adoption",
"2023: Station retail expansion",
"2024: Passenger experience focus",
"1857: Railways aided troop movement",
"1860: Rail workshops expanded",
"1872: Railways crossed rivers",
"1885: Mail transport expanded",
"1895: Track maintenance mechanized",
"1905: Safety protocols improved",
"1915: Signaling upgrades",
"1928: Route electrification studied",
"1938: Locomotive standardization",
"1948: Post-independence expansion",
"1958: New train categories",
"1965: Freight corridors discussed",
"1975: Reservation capacity increased",
"1982: Metro rail inaugurated",
"1992: Computer networks introduced",
"1998: Digital ticketing tested",
"2004: Online services expanded",
"2009: Station redevelopment",
"2011: Energy-efficient engines",
"2013: GPS tracking expanded",
"2016: Clean energy push",
"2018: Smart station rollout",
"2020: Emergency rail operations",
"2021: Passenger safety tech",
"2022: AI traffic management",
"2023: Infrastructure upgrades",
"2024: Rail modernization drive"
]


st.sidebar.markdown("### 📜 Today in Rail History")
st.sidebar.warning(random.choice(history))

facts = [
"Indian Railways is among the world’s largest networks",
"Over 23 million passengers travel daily",
"IR runs more than 13,000 passenger trains",
"Railways employ over 1.2 million people",
"India has luxury tourist trains",
"Some stations run fully on solar power",
"IR produces its own coaches",
"Longest route exceeds 4,200 km",
"Train wheels self-correct alignment",
"IR has its own hospitals",
"Railways run schools for staff",
"Clocks across stations are synchronized",
"IRCTC is a global e-ticket leader",
"Some trains run weekly only",
"Railways own their own police force",
"Women-only stations exist in India",
"Railway bridges rank among world’s highest",
"Tracks expand with temperature",
"Railways help during disasters",
"IR uses satellite tracking",
"Stations are becoming smart hubs",
"Railways manage huge freight volumes",
"IR owns power plants",
"Some stations are over 150 years old",
"Railway catering serves millions daily",
"IR manages hill railways",
"Railway workshops date back to 1854",
"Railways connect remote regions",
"India has UNESCO heritage railways",
"Railway engines are built locally",
"IR supports defense logistics",
"Train numbers are unique",
"Railways manage vast land assets",
"IR uses advanced signaling",
"Railways reduce road congestion",
"Railways save fuel per passenger",
"IR uses bio-toilets",
"Stations are digitally monitored",
"Railways support rural economy",
"IR handles massive data daily",
"Train punctuality is tracked centrally",
"Railways operate staff townships",
"IR uses AI in operations",
"Railways transport food grains",
"IR helps pilgrimage travel",
"Stations have WiFi facilities",
"IR runs parcel services",
"Railways use electric traction widely",
"IR owns heritage locomotives",
"Railways reduce carbon footprint",
"IR supports tourism economy",
"Railways operate museums",
"IR uses GPS systems",
"Railways handle emergency evacuations",
"IR supports national unity",
"Railways run mobile medical units",
"IR uses modern coaches",
"Railways connect borders",
"IR promotes Make in India",
"Railways train skilled workforce",
"IR uses automated inspections",
"Railways handle mail transport",
"IR uses centralized control",
"Railways operate helplines",
"IR supports urban transport",
"Railways modernize signaling",
"IR promotes green energy",
"Railways support trade",
"IR connects hill regions",
"Railways manage time tables centrally",
"IR uses digital displays",
"Railways ensure passenger safety",
"IR develops freight corridors",
"Railways operate container services",
"IR uses predictive maintenance",
"Railways support economy growth",
"IR adapts new technology",
"Railways employ diverse workforce",
"IR runs inspection trains",
"Railways support defense mobility",
"IR uses cloud systems",
"Railways ensure national connectivity",
"IR supports emergency logistics",
"Railways shape national growth",
"IR modernizes stations",
"Railways innovate continuously",
"IR connects cultures",
"Railways symbolize progress"
]

st.sidebar.markdown("### 💡 Did You Know?")
st.sidebar.info(random.choice(facts))
tips = [
"Book tickets early for better availability",
"Keep a digital copy of tickets",
"Carry valid ID proof",
"Reach station at least 30 minutes early",
"Check live train status before departure",
"Keep luggage locked during night",
"Carry essential medicines",
"Travel light for comfort",
"Charge devices before journey",
"Use official apps for updates",
"Avoid sharing OTPs",
"Label your luggage",
"Choose aisle seats for mobility",
"Upper berths are safer overnight",
"Carry drinking water",
"Keep emergency contacts offline",
"Download entertainment beforehand",
"Check platform display boards",
"Avoid peak travel hours",
"Keep cash for emergencies",
"Use e-catering services",
"Wear comfortable clothing",
"Keep sanitizer handy",
"Check weather before packing",
"Save important numbers",
"Verify coach position",
"Board train calmly",
"Respect fellow passengers",
"Secure valuables before sleeping",
"Keep power bank",
"Travel insurance is helpful",
"Use station WiFi carefully",
"Keep snacks for long trips",
"Confirm chart preparation status",
"Check PNR updates",
"Choose window seat for views",
"Carry earphones",
"Avoid last-minute rushing",
"Know emergency chain procedure",
"Follow railway rules",
"Keep luggage under seat",
"Avoid overcrowded doors",
"Check destination weather",
"Carry torch for night travel",
"Read safety instructions",
"Use station maps",
"Keep ticket handy",
"Avoid unattended baggage",
"Plan station exit beforehand",
"Be alert at junctions",
"Check connecting transport",
"Carry extra mask",
"Choose less crowded coaches",
"Verify train number",
"Check coach sequence",
"Keep backup charger",
"Know arrival platform",
"Travel during daylight if possible",
"Stay hydrated",
"Follow signage",
"Avoid loud calls at night",
"Respect cleanliness",
"Dispose waste properly",
"Carry small lock",
"Keep footwear handy",
"Be polite to staff",
"Keep mobile silent at night",
"Track train delays",
"Use alarm for arrival",
"Carry rain protection",
"Know pantry timings",
"Confirm seat number",
"Check reservation chart",
"Avoid unsafe shortcuts",
"Read train notices",
"Keep itinerary saved",
"Share journey details with family",
"Stay patient during delays",
"Follow safety announcements",
"Prepare exit early",
"Keep calm during crowding",
"Follow official updates",
"Trust verified information",
"Enjoy the journey"
]

st.sidebar.markdown("### 🧠 Travel Tip")
st.sidebar.success(random.choice(tips))
st.sidebar.markdown("---")
st.sidebar.caption("By Nandini Verma")

# ---------------- MAIN TITLE ----------------
st.title("🚆 Live Train Status Checker")
st.caption("Check real-time running status of Indian Railways trains as well as weather information of your desired location.")

# ---------------- INPUT SECTION ----------------
st.subheader("🔍 Search Train")
col1, col2 = st.columns(2)

with col1:
    
    train_no = st.text_input("🚆 Enter Train Number", placeholder="e.g. 12303")

with col2:
    journey_date = st.date_input("📅 Journey Date", value=date.today())

# ---------------- BUTTON ----------------
st.markdown("""
<style>
div.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 1em;
    font-size: 18px;
    background-color: #0d6efd;
    color: white;
    display: block;
    margin: 0 auto;
}
</style>
""", unsafe_allow_html=True)

check_btn = st.button("🔍 Check Status")

# ---------------- API CALL ----------------
if check_btn:

    if train_no.strip() == "":
        st.warning("⚠️ Please enter a valid train number")

    else:
        with st.spinner("Fetching live train status..."):

            # ----------- API DETAILS (REPLACE THESE) -----------
            url = "https://rappid.in/apis/train.php?train_no="

        

            try:
                response = requests.get(url, params={"train_no": train_no}, timeout=10)

                if response.status_code == 200:
                    data = response.json()

                    st.success("✅ Train status fetched successfully")

                    # ---------------- DISPLAY METRICS ----------------
                    st.subheader("🚆 Train Overview")

                    m1, m2, m3 = st.columns(3)

                    m1.metric(
                        label="Train Name",
                        value=data.get("train_name", "N/A")
                    )

                    m2.metric(
                        label="Current Status",
                        value=data.get("message", "N/A")
                    )

                    m3.metric(
                        label="Last Updated",
                        value=str(data.get("updated_time", "N/A"))
                    )

                    # ---------------- ROUTE / STATION TABLE ----------------
                    if "data" in data:
                        st.subheader("📍 Station-wise Running Status")
                        st.dataframe(data["data"], use_container_width=True)
                    else:
                        st.info("Route details not available")

                else:
                    st.error("❌ Failed to fetch data from API")

            except requests.exceptions.RequestException as e:
                st.error("⚠️ Network error or API not reachable")
                st.caption(str(e))

st.subheader("🌦 Check Weather")

city = st.text_input("Enter City Name", placeholder="city_name")

if st.button("Get Weather"):
    # ---------- STEP 1: GEOCODING ----------
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_res = requests.get(geo_url).json()

    if "results" not in geo_res:
        st.error("City not found")
    else:
        location = geo_res["results"][0]
        lat = location["latitude"]
        lon = location["longitude"]
        country = location["country"]

        # ---------- STEP 2: WEATHER ----------
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}&current_weather=true"
        )
        weather_res = requests.get(weather_url).json()
        weather = weather_res["current_weather"]

        # ---------- STEP 3: DISPLAY ----------
        st.success(f"📍 {city}, {country}")

        col1, col2, col3 = st.columns(3)

        col1.metric("🌡 Temperature", f"{weather['temperature']} °C")
        col2.metric("💨 Wind Speed", f"{weather['windspeed']} km/h")
        col3.metric("⏰ Time", weather["time"])

        # Day / Night
        if weather["is_day"] == 1:
            st.info("☀ Day Time")
        else:
            st.info("🌙 Night Time")

# ---------------- FOOTER ----------------

quotes = [
    "Success is the sum of small efforts repeated daily",
    "Dream big, start small, act now",
    "Consistency beats motivation every time",
    "Your future depends on what you do today",
    "Hard work turns dreams into reality",
    "Believe you can and you’re halfway there",
    "Growth begins at the edge of comfort",
    "Discipline is choosing what you want most",
    "Focus on progress, not perfection",
    "Small steps lead to big changes",
    "Learning never exhausts the mind",
    "Effort today creates ease tomorrow",
    "Failure is a lesson in disguise",
    "Courage starts with showing up",
    "Make today count",
    "Action is the antidote to fear",
    "Persistence makes the impossible possible",
    "Your mindset shapes your reality",
    "Don’t wait for opportunity, create it",
    "Success favors the prepared",
    "Stay hungry, stay curious",
    "One day or day one—you decide",
    "The grind always pays off",
    "Improvement is better than perfection",
    "Knowledge grows when shared",
    "Confidence comes from preparation",
    "Work quietly, let results speak",
    "Your potential is limitless",
    "The best investment is in yourself",
    "Discipline builds freedom",
    "Every expert was once a beginner",
    "Focus fuels success",
    "Dreams demand dedication",
    "Effort compounds over time",
    "Your attitude defines your altitude",
    "Challenges build character",
    "Start where you are",
    "Growth is a daily choice",
    "Learning is a lifelong journey",
    "Stay consistent, stay winning",
    "Hustle with purpose",
    "Progress requires patience",
    "Mindset matters more than talent",
    "Today’s actions shape tomorrow",
    "Excellence is a habit",
    "Failure refines success",
    "Vision drives action",
    "Believe in your process",
    "Success starts with self-belief",
    "Turn obstacles into stepping stones",
    "Passion powers persistence",
    "Results reward resilience",
    "Learn, adapt, grow",
    "Purpose fuels performance",
    "Your journey is unique",
    "Keep moving forward",
    "Effort creates opportunity",
    "Stay focused, stay fearless",
    "Growth loves discipline",
    "Action creates clarity",
    "Your work defines your legacy",
    "Persistence outlasts talent",
    "Confidence is built, not gifted",
    "Every day is a chance to improve",
    "Start now, refine later",
    "Focus beats distraction",
    "Growth requires patience",
    "The process creates progress",
    "Discipline sharpens ambition",
    "Small wins matter",
    "Learn from every experience",
    "Progress over perfection",
    "Consistency creates momentum",
    "Success loves preparation",
    "Push beyond limits",
    "Effort unlocks excellence",
    "Stay curious, stay driven",
    "Vision without action is nothing",
    "Growth begins with belief",
    "Dedication builds destiny",
    "Results come from repetition",
    "Every step forward counts",
    "Learn fast, execute faster",
    "Purpose gives power",
    "Momentum beats motivation",
    "Action shapes outcomes",
    "The journey builds the champion"
]

st.subheader("✨ Quote 4 U ✨") 
st.write(f"> *{random.choice(quotes)}*")

st.caption(" Best Wishes By Nandini Verma")

