import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title Slide
st.title("Spotify: The Challenges of an Online Music Service")

# Introduction Section
st.markdown("""
## Slide 2: Introduction
### Spotify’s Background:
- Founded in 2006 by Daniel Ek and Martin Lorentzon in Sweden.
- Aimed to address the growing issue of illegal music downloads by offering a legal alternative for consumers.
- Offers over 30 million songs, allowing users to stream music from any location with an internet connection.

### Challenges for Spotify:
- Securing licensing agreements with major record labels (Warner, Sony, Universal).
- Profitability remains a challenge due to the 70% revenue share paid to music rights holders.
- Ensuring fair compensation for artists while keeping subscription fees affordable.
""")

# Financial Data (2013-2014)
financial_data = {
    'Year': [2013, 2014],
    'Revenue (in € millions)': [747, 1080],
    'Net Loss (in € millions)': [-93, -162],
    'Accumulated Losses (in € millions)': [200, 262]
}

df = pd.DataFrame(financial_data)

# Display Financial Data
st.markdown("## Slide 3: Key Financials (2013-2014)")
st.dataframe(df)

# Revenue Growth Chart
st.markdown("### Spotify Revenue Growth (2013-2014)")
fig, ax = plt.subplots()
ax.plot(df['Year'], df['Revenue (in € millions)'], marker='o', color='green')
ax.set_xlabel('Year')
ax.set_ylabel('Revenue (in € millions)')
ax.set_title('Spotify Revenue Growth (2013-2014)')
st.pyplot(fig)

# Net Loss Chart
st.markdown("### Spotify Net Loss (2013-2014)")
fig, ax = plt.subplots()
ax.bar(df['Year'], df['Net Loss (in € millions)'], color='red')
ax.set_xlabel('Year')
ax.set_ylabel('Net Loss (in € millions)')
ax.set_title('Spotify Net Loss (2013-2014)')
st.pyplot(fig)

# Monetization Strategy and Freemium Model
st.markdown("""
## Slide 4: Monetization Strategy and Freemium Model
### Freemium Model:
- Free access with ads or €9.99/month for Premium with no ads and extra features like offline listening.
- As of 2014, only 20-27% of users converted to Premium; majority use the ad-supported version.

### Revenue Breakdown:
- Less than 10% from advertising, 91% from Premium subscriptions.
- Heavy reliance on Premium for profitability.

### Challenges:
- Growing competition, especially from Apple Music (launched 2015).
- Struggle to convert more free users into paying subscribers.
""")

# Spotify Competitors
competitors_data = {
    'Competitor': ['Apple Music', 'Pandora', 'Deezer', 'Tidal'],
    'Service Overview': ['Tied to iTunes, with exclusive artist deals', 
                         'U.S.-based, radio-style service', 
                         'French streaming service', 
                         'Focuses on high-quality audio'],
    'Catalog Size (million songs)': [35, 32, 35, 25],
    'Monthly Subscription Cost (€)': [9.99, 4.99, 9.99, 19.99]
}

df_competitors = pd.DataFrame(competitors_data)

# Competitors Table
st.markdown("## Slide 5: Spotify's Market Position")
st.dataframe(df_competitors)

# Competitors Chart
fig, ax = plt.subplots()
ax.bar(df_competitors['Competitor'], df_competitors['Monthly Subscription Cost (€)'], color=['blue', 'purple', 'green', 'orange'])
ax.set_xlabel('Competitors')
ax.set_ylabel('Monthly Subscription Cost (€)')
ax.set_title('Spotify Competitors: Monthly Subscription Cost Comparison')
st.pyplot(fig)

# Financial Challenges and Path to Profitability
st.markdown("""
## Slide 6: Financial Challenges and Path to Profitability
### Revenue vs. Costs:
- Spotify pays 70% of its gross revenue to rights holders.
- Despite growth in revenue, high licensing fees result in ongoing net losses (€162 million in 2014).

### Capital Investments:
- Raised $300 million in external funding but faces continued losses.

### Path to Profitability:
- Increase Premium conversions from free users.
- Negotiate better licensing deals to reduce content acquisition costs.
- Expand into new regions and grow advertising revenue from free users.
""")

# Conclusion
st.markdown("""
## Slide 7: Conclusion
### Spotify’s Strategic Path:
- Built a successful platform but profitability remains challenging due to reliance on Premium and high payouts to rights holders.

### Challenges Ahead:
- Balancing profitability, managing growing content acquisition costs, and competition from Apple Music.
- Continued innovation and focus on converting free users into Premium subscribers.
""")

# Download the PowerPoint File
st.markdown("## Download the Detailed PowerPoint Presentation")
with open("Spotify_Detailed_Presentation_v5.pptx", "rb") as f:
    st.download_button(label="Download Presentation", data=f, file_name="Spotify_Detailed_Presentation_v5.pptx", mime="application/vnd.openxmlformats-officedocument.presentationml.presentation")
