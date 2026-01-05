import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Cyber Analytics Dashboard",
    layout="wide",
    page_icon="🛡️"
)

st.title("🛡️ Cyber Analytics & Ethical Hacking Intelligence Dashboard")

# ---------- DATA ---------- #

threat_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Attacks": [320, 410, 520, 610],
    "Blocked": [290, 360, 460, 550],
    "Successful": [30, 50, 60, 60]
})

vuln_data = pd.DataFrame({
    "Severity": ["Critical", "High", "Medium", "Low"],
    "Count": [18, 42, 67, 91]
})

model_data = pd.DataFrame({
    "Model": ["Random Forest", "XGBoost", "Neural Network", "Logistic Regression"],
    "Accuracy": [94.2, 96.1, 95.4, 89.7]
})

traffic_data = pd.DataFrame({
    "Time": ["10AM", "12PM", "2PM", "4PM"],
    "Normal Traffic": [1200, 1400, 1100, 1600],
    "Malicious Traffic": [120, 240, 310, 180]
})

ids_data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Alerts": [85, 110, 140, 95, 160],
    "False Positives": [12, 18, 25, 14, 30]
})

# ---------- LAYOUT ---------- #

col1, col2, col3 = st.columns(3)

with col1:
    fig1 = px.bar(threat_data, x="Month", y="Attacks",
                  color_discrete_sequence=["#00e5ff"])
    fig1.add_scatter(x=threat_data["Month"], y=threat_data["Blocked"],
                     mode='lines+markers',
                     name="Blocked",
                     line=dict(color="#ffa726"))
    fig1.update_layout(title="Threat Detection Overview",
                       template="plotly_dark")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.bar(vuln_data, x="Severity", y="Count",
                  color="Severity",
                  color_discrete_map={
                      "Critical": "#ff1744",
                      "High": "#ff9100",
                      "Medium": "#ffeb3b",
                      "Low": "#00e676"
                  })
    fig2.update_layout(title="Vulnerability Severity Analysis",
                       template="plotly_dark")
    st.plotly_chart(fig2, use_container_width=True)

with col3:
    fig3 = px.bar(model_data, x="Accuracy", y="Model",
                  orientation="h",
                  color="Accuracy",
                  color_continuous_scale="Blues")
    fig3.update_layout(title="ML Model Performance (%)",
                       template="plotly_dark")
    st.plotly_chart(fig3, use_container_width=True)

col4, col5, col6 = st.columns(3)

with col4:
    fig4 = px.area(traffic_data, x="Time",
                   y=["Normal Traffic", "Malicious Traffic"],
                   color_discrete_sequence=["#00e5ff", "#ff1744"])
    fig4.update_layout(title="Network Traffic Pattern",
                       template="plotly_dark")
    st.plotly_chart(fig4, use_container_width=True)

with col5:
    fig5 = px.line(ids_data, x="Day",
                   y=["Alerts", "False Positives"],
                   markers=True,
                   color_discrete_sequence=["#00e5ff", "#ff9100"])
    fig5.update_layout(title="Intrusion Detection Trends",
                       template="plotly_dark")
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    risk_score = 72
    fig6 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_score,
        title={'text': "Cyber Risk Score"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#ff1744"},
            'steps': [
                {'range': [0, 40], 'color': "#00e676"},
                {'range': [40, 70], 'color': "#ffeb3b"},
                {'range': [70, 100], 'color': "#ff1744"}
            ]
        }
    ))
    fig6.update_layout(template="plotly_dark")
    st.plotly_chart(fig6, use_container_width=True)

st.markdown("### 🔒 Status: **High Risk – Immediate Action Recommended**")
