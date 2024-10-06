import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pptx import Presentation
from io import BytesIO

# Function to create the PowerPoint file
def create_presentation():
    prs = Presentation()

    # Slide 1: Title Slide
    slide_1 = prs.slides.add_slide(prs.slide_layouts[0])
    title_1 = slide_1.shapes.title
    subtitle_1 = slide_1.placeholders[1]
    title_1.text = "Spotify: The Challenges of an Online Music Service"
    subtitle_1.text = "Legal and Profitable\nYour Name\nDate"

    # Slide 2: Introduction
    slide_2 = prs.slides.add_slide(prs.slide_layouts[1])
    title_2 = slide_2.shapes.title
    title_2.text = "Introduction"
    
    # Add text and paragraphs to the slide
    text_box = slide_2.shapes[1].text_frame
    text_box.clear()
    text_box.text = "Spotify was founded in 2006 by Daniel Ek and Martin Lorentzon in Sweden."
    
    # Add bullet points
    p = text_box.add_paragraph()
    p.text = "• Aimed to address illegal music downloads."
    p = text_box.add_paragraph()
    p.text = "• Offers over 30 million songs for streaming."
    p = text_box.add_paragraph()
    p.text = "• Key challenges include securing licensing agreements and achieving profitability."

    # Slide 3: Key Financials
    slide_3 = prs.slides.add_slide(prs.slide_layouts[1])
    title_3 = slide_3.shapes.title
    title_3.text = "Key Financials (2013-2014)"
    
    text_frame_3 = slide_3.shapes[1].text_frame
    text_frame_3.clear()
    text_frame_3.text = "Financial Metrics:"
    
    p = text_frame_3.add_paragraph()
    p.text = "• Revenue (2013): €747 million | Revenue (2014): €1,080 million | Growth: +44.6%"
    p = text_frame_3.add_paragraph()
    p.text = "• Net Loss (2013): €93 million | Net Loss (2014): €162 million | Growth: +74%"
    p = text_frame_3.add_paragraph()
    p.text = "• Total Accumulated Losses (2014): €262 million"

    # Slide 4: Monetization Strategy
    slide_4 = prs.slides.add_slide(prs.slide_layouts[1])
    title_4 = slide_4.shapes.title
    title_4.text = "Monetization Strategy and Freemium Model"
    
    text_frame_4 = slide_4.shapes[1].text_frame
    text_frame_4.clear()
    text_frame_4.text = "Spotify operates under a freemium model."
    
    p = text_frame_4.add_paragraph()
    p.text = "• Free with ads or €9.99/month for Premium without ads."
    p = text_frame_4.add_paragraph()
    p.text = "• Premium accounts for 91% of total revenue."

    # Slide 5: Competitors
    slide_5 = prs.slides.add_slide(prs.slide_layouts[1])
    title_5 = slide_5.shapes.title
    title_5.text = "Spotify's Competitors"
    
    text_frame_5 = slide_5.shapes[1].text_frame
    text_frame_5.clear()
    text_frame_5.text = "Competitors include:"
    
    p = text_frame_5.add_paragraph()
    p.text = "• Apple Music (€9.99/month), Pandora (€4.99/month), Deezer (€9.99/month), Tidal (€19.99/month)."

    # Slide 6: Financial Challenges
    slide_6 = prs.slides.add_slide(prs.slide_layouts[1])
    title_6 = slide_6.shapes.title
    title_6.text = "Financial Challenges and Path to Profitability"
    
    text_frame_6 = slide_6.shapes[1].text_frame
    text_frame_6.clear()
    text_frame_6.text = "Challenges include:"
    
    p = text_frame_6.add_paragraph()
    p.text = "• High licensing fees, accounting for 70% of revenue."
    p = text_frame_6.add_paragraph()
    p.text = "• Growing competition from Apple Music."
    p = text_frame_6.add_paragraph()
    p.text = "• Path to profitability requires increasing Premium conversions."

    # Slide 7: Conclusion
    slide_7 = prs.slides.add_slide(prs.slide_layouts[1])
    title_7 = slide_7.shapes.title
    title_7.text = "Conclusion"
    
    text_frame_7 = slide_7.shapes[1].text_frame
    text_frame_7.clear()
    text_frame_7.text = "Spotify has built a successful platform but faces challenges in achieving profitability."

    return prs

# Streamlit App Title
st.title("Spotify: The Challenges of an Online Music Service")

# Introduction Section
st.markdown("""
## Slide 2: Introduction
Spotify was founded in 2006 by Daniel Ek and Martin Lorentzon in Sweden. The service aimed to address the growing issue of illegal music downloads by offering a legal and user-friendly alternative for consumers.
Challenges include securing licensing agreements, profitability, and fair compensation for artists.
""")

# Financial Data (2013-2014)
financial_data = {
    'Year': [2013, 2014],
    'Revenue (in € millions)': [747, 1080],
    'Net Loss (in € millions)': [-93, -162],
    'Accumulated Losses (in € millions)': [200, 262]
}

df = pd.DataFrame(financial_data)

# Display Financial Data Table
st.markdown("## Slide 3: Key Financials (2013-2014)")
st.dataframe(df)

# Revenue Growth Chart
st.markdown("### Spotify Revenue Growth (2013-2014)")
fig, ax = plt.subplots()
ax.plot(df['Year'], df['Revenue (in € millions)'], marker='o', color='green')
ax.set_xlabel('Year')
ax.set_ylabel('Revenue (in € millions)')
st.pyplot(fig)

# Net Loss Chart
st.markdown("### Spotify Net Loss (2013-2014)")
fig, ax = plt.subplots()
ax.bar(df['Year'], df['Net Loss (in € millions)'], color='red')
ax.set_xlabel('Year')
ax.set_ylabel('Net Loss (in € millions)')
st.pyplot(fig)

# Error Handling for PowerPoint Download
try:
    # Download PowerPoint Presentation
    st.markdown("## Download the Detailed PowerPoint Presentation")
    prs = create_presentation()
    pptx_io = BytesIO()
    prs.save(pptx_io)
    pptx_io.seek(0)
    st.download_button(label="Download Presentation", data=pptx_io, file_name="Spotify_Detailed_Presentation_v5.pptx", mime="application/vnd.openxmlformats-officedocument.presentationml.presentation")
except Exception as e:
    st.error(f"An error occurred while generating the PowerPoint: {e}")
