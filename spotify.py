import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("Spotify: The Challenges of an Online Music Service")

# Introduction Section
st.markdown("""
## Overview
Founded in 2006 by Daniel Ek and Martin Lorentzon, Spotify has grown to become one of the world’s leading music streaming services. The platform offers over 30 million songs, available for streaming under its freemium model. 
While Spotify has been successful in disrupting the music industry, it faces major challenges around profitability, competition, and payouts to music rights holders.
""")

# Financial Data (2013-2014)
financial_data = {
    'Year': [2013, 2014],
    'Revenue (in € millions)': [747, 1080],
    'Net Loss (in € millions)': [-93, -162],
    'Accumulated Losses (in € millions)': [200, 262]
}

df = pd.DataFrame(financial_data)

# Revenue Growth Chart
st.markdown("### Spotify Revenue Growth (2013-2014)")
fig, ax = plt.subplots()
ax.plot(df['Year'], df['Revenue (in € millions)'], marker='o', color='green', label='Revenue')
ax.set_xlabel('Year')
ax.set_ylabel('Revenue (in € millions)')
ax.set_title('Spotify Revenue Growth')
st.pyplot(fig)

# Net Loss Trend Chart
st.markdown("### Spotify Net Loss Trend (2013-2014)")
fig, ax = plt.subplots()
ax.bar(df['Year'], df['Net Loss (in € millions)'], color='red', label='Net Loss')
ax.set_xlabel('Year')
ax.set_ylabel('Net Loss (in € millions)')
ax.set_title('Spotify Net Loss Trend')
st.pyplot(fig)

# Financial Data Summary Table
st.markdown("### Financial Summary")
st.dataframe(df)

# Competitor Comparison (Subscribers and Cost)
st.markdown("### Spotify Competitors")
competitor_data = {
    'Competitor': ['Apple Music', 'Pandora', 'Deezer', 'Tidal'],
    'Subscribers (millions)': [80, 78, 16, 3],
    'Monthly Cost (€)': [9.99, 4.99, 9.99, 19.99]
}

df_competitors = pd.DataFrame(competitor_data)

# Competitors Bar Chart (Subscribers)
fig, ax = plt.subplots()
ax.bar(df_competitors['Competitor'], df_competitors['Subscribers (millions)'], color=['blue', 'purple', 'green', 'orange'])
ax.set_title('Competitors - Subscribers in Millions')
ax.set_xlabel('Competitor')
ax.set_ylabel('Subscribers (millions)')
st.pyplot(fig)

# Competitor Data Table
st.dataframe(df_competitors)

# Monetization Strategy and Freemium Model
st.markdown("""
### Monetization Strategy and Freemium Model
Spotify operates under a **freemium** model. Users can stream music for free with ads or subscribe to **Premium** at €9.99 per month to enjoy ad-free music, offline downloads, and other perks. 
However, only **20-27% of users** convert to Premium, which accounts for **91% of Spotify’s revenue**.
""")

# Challenges Section
st.markdown("""
### Financial Challenges and Path to Profitability
Despite Spotify's growing revenue, its net losses continue to widen, largely due to the **70% payout** to music rights holders. In 2014, Spotify had accumulated losses of **€262 million**. 

To reach profitability, Spotify must focus on:
- **Increasing Premium conversions** from free users.
- **Negotiating better licensing deals** with rights holders.
- **Growing advertising revenue** from free-tier users.
""")

# Conclusion Section
st.markdown("""
### Conclusion
Spotify’s journey as a disruptor in the music industry comes with its own set of challenges. The platform needs to convert more free users into paying subscribers and address the significant costs tied to licensing fees.
Competition from Apple Music, Pandora, and other services adds further pressure. Spotify’s success hinges on finding a balance between growth and profitability.
""")

# Provide the option to download the PowerPoint file
st.markdown("### Download the Detailed PowerPoint Presentation")
with open("Spotify_Detailed_Presentation_v4.pptx", "rb") as f:
    st.download_button(label="Download Presentation", data=f, file_name="Spotify_Detailed_Presentation_v4.pptx", mime="application/vnd.openxmlformats-officedocument.presentationml.presentation")
