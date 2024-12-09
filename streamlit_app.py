import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

# Mockup Data
customer_data = pd.DataFrame({
    "ID": ["C001", "C002", "C003"],
    "Location": ["Zone A", "Zone B", "Zone C"],
    "Behavior": ["ดูเสื้อผ้า", "ค้นหาร้านอาหาร", "ค้นหาโปรโมชั่น"]
})

merchant_data = pd.DataFrame({
    "ID": ["M001", "M002", "M003"],
    "Category": ["เสื้อผ้า", "อาหาร", "ของใช้ในครัวเรือน"],
    "Revenue": [25000, 30000, 15000],
    "Rent Status": ["เต็ม", "เต็ม", "ว่าง 50%"]
})

area_data = pd.DataFrame({
    "Zone": ["Zone A", "Zone B", "Zone C"],
    "Rent Status": ["100%", "50%", "20%"],
    "Heatmap": ["คนเดินเยอะ", "นิยม", "ปานกลาง"]
})

sentiment_data = pd.DataFrame({
    "Sentiment": ["Positive", "Neutral", "Negative"],
    "Percentage": [80, 10, 10]
})

alerts_data = [
    "M002 ค้างจ่าย 2 เดือน",
    "พื้นที่โซน C ต้องการทำความสะอาด"
]

# Streamlit UI
st.title("AI-Powered Market Dashboard")

# Slide Menu
menu = st.sidebar.selectbox("Select Section", ["Customer Overview", "Merchant Insights", "Area Management", "AI Recommendations", "Customer Density Heatmap"])

if menu == "Customer Overview":
    st.subheader("Sentiment Analysis")
    fig_sentiment = px.pie(sentiment_data, names="Sentiment", values="Percentage", title="Customer Sentiment", )
    st.plotly_chart(fig_sentiment)

elif menu == "Merchant Insights":
    st.header("Merchant Insights")
    st.subheader("Merchant Revenue")
    fig_revenue = px.bar(merchant_data,x="Category",y="Revenue",color="Category",color_discrete_sequence=px.colors.qualitative.Pastel,  # ใช้ชุดสี Pastel
    title="Merchant Revenue by Category"
)
    st.plotly_chart(fig_revenue)

    st.subheader("Rent Payment Status")
    st.write(merchant_data[["ID", "Category", "Rent Status"]])

elif menu == "Area Management":
    st.header("Area Management")
    st.subheader("Area Status")
    st.write(area_data)

    st.subheader("Alerts")
    for alert in alerts_data:
        st.warning(alert)

elif menu == "AI Recommendations":
    st.header("AI Recommendations")
    st.write("1. แนะนำสินค้าใหม่: เสื้อผ้าสีสดลด 20%")
    st.write("2. โซนที่แนะนำให้ตั้งร้าน: Zone B (นิยม)")

elif menu == "Customer Density Heatmap":
    st.header("Customer Density Heatmap")
    
    # Generate mock density data
    x = np.random.randint(0, 80, 500)  # Random X coordinates
    y = np.random.randint(0, 40, 500)  # Random Y coordinates

    # Plot density heatmap with layout background
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Heatmap
    heatmap = ax.hexbin(x, y, gridsize=30, cmap='YlOrRd', extent=(10, 58, 10, 34))
    
    # Load and overlay the uploaded image (replace with your image file path)
    img = plt.imread('image01.png')  # Ensure your uploaded image path matches
    ax.imshow(img, extent=[0, 80, 0, 40], alpha=0.6, zorder=1)
    
    # Add colorbar
    cb = fig.colorbar(heatmap, ax=ax, label="Customer Density")
    # Remove axes
    ax.axis('off')
    
    ax.set_title("Customer Density Heatmap Over Layout")
    #ax.set_xlabel("Meters (Width)")
    #ax.set_ylabel("Meters (Height)")
    
    # Display in Streamlit
    st.pyplot(fig)
