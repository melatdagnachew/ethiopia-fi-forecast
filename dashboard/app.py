import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Selam Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Load Data
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/raw/ethiopia_fi_unified_data.csv")

data = load_data()
# -----------------------------
# Load Forecast Data
# -----------------------------
@st.cache_data
def load_forecasts():
    account = pd.read_csv("outputs/account_ownership_forecast.csv")
    usage = pd.read_csv("outputs/mobile_money_usage_forecast.csv")
    return account, usage

account_forecast, usage_forecast = load_forecasts()

st.title("📊 Ethiopia Financial Inclusion Forecast Dashboard")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Overview",
        "Trends",
        "Forecasts",
        "Inclusion Projections"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
### Selam Analytics

**Financial Inclusion Forecasting Dashboard**

**Country:** Ethiopia

**Forecast Period:** 2025–2027

This dashboard explores Ethiopia's financial inclusion landscape using historical indicators, market events, impact modeling, and forecasting.
"""
)
if page == "Overview":

    st.header("📊 Dashboard Overview")

    observations = data[data["record_type"] == "observation"].copy()

    account = observations[
        (observations["indicator"] == "Account Ownership Rate") &
        (observations["gender"] == "all")
    ].sort_values("observation_date")

    latest_account = account.iloc[-1]["value_numeric"]

    mobile_activity = observations[
        observations["indicator"] == "Mobile Money Activity Rate"
    ]

    latest_activity = mobile_activity.iloc[-1]["value_numeric"]

    telebirr = observations[
        observations["indicator"] == "Telebirr Registered Users"
    ]

    latest_users = telebirr.iloc[-1]["value_numeric"]

    fayda = observations[
        observations["indicator"] == "Fayda Digital ID Enrollment"
    ]

    latest_fayda = fayda.iloc[-1]["value_numeric"]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Account Ownership",
            f"{latest_account:.0f}%",
            "+3 pp since 2021"
        )

    with col2:
        st.metric(
            "Mobile Money Activity",
            f"{latest_activity:.0f}%",
            "+12 pp"
        )

    with col3:
        st.metric(
            "Telebirr Users",
            f"{latest_users/1_000_000:.1f} M"
        )

    with col4:
        st.metric(
            "Fayda Digital IDs",
            f"{latest_fayda/1_000_000:.1f} M"
        )

    st.markdown("---")

    st.subheader("Key Highlights")

    st.success(
        """
- Account ownership increased from **22% (2014)** to **49% (2024)**.
- Mobile money activity reached **66%**.
- Telebirr surpassed **54 million** registered users.
- Fayda Digital ID exceeded **15 million** enrollments.
"""
    )

    st.subheader("Digital Payment Milestone")

    st.info(
        """
**P2P Transactions surpassed ATM Transactions in 2024.**

This milestone reflects Ethiopia's transition toward a digital-first payment ecosystem and is considered one of the strongest indicators of increasing financial inclusion.
"""
    )

    st.subheader("Dashboard Purpose")

    st.write(
        """
This dashboard enables stakeholders to:

- Monitor financial inclusion indicators
- Explore historical trends
- Understand policy and market event impacts
- Compare future forecasting scenarios
- Evaluate progress toward Ethiopia's financial inclusion targets
"""
    )
    
elif page == "Trends":
    st.header("📈 Historical Trends")

    observations = data[data["record_type"] == "observation"].copy()

    # Convert to datetime
    observations["observation_date"] = pd.to_datetime(
        observations["observation_date"],
        errors="coerce"
    )

    # Create year column
    observations["year"] = observations["observation_date"].dt.year

    # Remove rows without a year
    observations = observations.dropna(subset=["year"])

    # Convert to integer
    observations["year"] = observations["year"].astype(int)

    # Indicator selector
    indicator = st.selectbox(
        "Select Indicator",
        sorted(observations["indicator"].unique())
    )

    # Filter indicator
    plot_data = observations[
        observations["indicator"] == indicator
    ].copy()

    # Keep overall values only
    if "gender" in plot_data.columns:
        plot_data = plot_data[
            (plot_data["gender"] == "all") |
            (plot_data["gender"].isna())
        ]

    fig = px.line(
        plot_data,
        x="year",
        y="value_numeric",
        markers=True,
        title=indicator
    )

    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Value"
    )
    

    st.plotly_chart(fig, use_container_width=True)
    st.markdown("---")

    st.subheader("Major Financial Inclusion Events")

    events = data[data["record_type"] == "event"]

    events = events[
        [
            "observation_date",
            "indicator",
            "category"
        ]
    ].sort_values("observation_date")

    st.dataframe(events, use_container_width=True)
elif page == "Forecasts":

    st.header("📈 Financial Inclusion Forecasts (2025–2027)")

    st.write(
        """
        This page presents the forecasted Account Ownership Rate for Ethiopia
        under different scenarios using the forecasting model developed in Task 4.
        """
    )

    # ------------------------------------
    # Scenario Selector
    # ------------------------------------
    scenario = st.selectbox(
        "Select Forecast Scenario",
        ["Baseline", "Optimistic", "Pessimistic"]
    )

    if scenario == "Baseline":
        forecast_column = "baseline_forecast"

    elif scenario == "Optimistic":
        forecast_column = "optimistic"

    else:
        forecast_column = "pessimistic"

    # ------------------------------------
    # Historical Data
    # ------------------------------------
    observations = data[data["record_type"] == "observation"].copy()

    observations["observation_date"] = pd.to_datetime(
        observations["observation_date"],
        errors="coerce"
    )

    observations["year"] = observations["observation_date"].dt.year

    history = observations[
        (observations["indicator"] == "Account Ownership Rate") &
        (observations["gender"] == "all")
    ][["year", "value_numeric"]].copy()

    history = history.sort_values("year")

    # ------------------------------------
    # Plot Historical + Forecast
    # ------------------------------------
    fig = go.Figure()

    # Historical
    fig.add_trace(
        go.Scatter(
            x=history["year"],
            y=history["value_numeric"],
            mode="lines+markers",
            name="Historical"
        )
    )

    # Forecast
    fig.add_trace(
        go.Scatter(
            x=account_forecast["year"],
            y=account_forecast[forecast_column],
            mode="lines+markers",
            name=scenario
        )
    )

    # Confidence Interval
    fig.add_trace(
        go.Scatter(
            x=account_forecast["year"],
            y=account_forecast["upper_ci"],
            mode="lines",
            line=dict(width=0),
            showlegend=False
        )
    )

    fig.add_trace(
        go.Scatter(
            x=account_forecast["year"],
            y=account_forecast["lower_ci"],
            mode="lines",
            fill="tonexty",
            fillcolor="rgba(0,100,80,0.2)",
            line=dict(width=0),
            name="Confidence Interval"
        )
    )

    fig.update_layout(
        title="Forecast of Account Ownership Rate",
        xaxis_title="Year",
        yaxis_title="Account Ownership Rate (%)",
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ------------------------------------
    # Forecast Table
    # ------------------------------------
    st.subheader("Forecast Values")

    display_table = account_forecast[
        [
            "year",
            "baseline_forecast",
            "optimistic",
            "pessimistic",
            "lower_ci",
            "upper_ci"
        ]
    ]

    st.dataframe(display_table, use_container_width=True)

    # ------------------------------------
    # Key Milestones
    # ------------------------------------
    st.subheader("Key Projected Milestones")

    latest = account_forecast.iloc[-1]

    st.markdown(
        f"""
        - **2025 Forecast:** {account_forecast.iloc[0]['baseline_forecast']:.1f}%
        - **2026 Forecast:** {account_forecast.iloc[1]['baseline_forecast']:.1f}%
        - **2027 Forecast:** {latest['baseline_forecast']:.1f}%
        - Forecast suggests Ethiopia approaches **60% account ownership** by 2027.
        """
    )

    # ------------------------------------
    # Download Forecast
    # ------------------------------------
    csv = account_forecast.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Forecast CSV",
        data=csv,
        file_name="account_ownership_forecast.csv",
        mime="text/csv"
    )
    st.markdown("---")

    st.subheader("Forecast Interpretation")

    st.write("""
    The baseline forecast suggests continued but slower growth in account ownership through 2027.

    The optimistic scenario assumes:

    - Continued Telebirr expansion
    - Strong M-Pesa adoption
    - Increased Fayda enrollment
    - Continued infrastructure investments

    The pessimistic scenario assumes slower digital adoption and weaker policy impacts.
    """)
elif page == "Inclusion Projections":

    st.header("🎯 Financial Inclusion Projections")

    st.write("""
    This page summarizes Ethiopia's projected financial inclusion trajectory
    between 2025 and 2027 under different forecasting scenarios.
    """)

    # ---------------------------------------------------
    # Scenario Selection
    # ---------------------------------------------------
    scenario = st.selectbox(
        "Select Projection Scenario",
        ["Baseline", "Optimistic", "Pessimistic"]
    )

    if scenario == "Baseline":
        projection_values = account_forecast["baseline_forecast"]

    elif scenario == "Optimistic":
        projection_values = account_forecast["optimistic"]

    else:
        projection_values = account_forecast["pessimistic"]

    # ---------------------------------------------------
    # Projection DataFrame
    # ---------------------------------------------------
    projection = pd.DataFrame({
        "Year": account_forecast["year"],
        "Projected Account Ownership": projection_values
    })

    target = 60

    projection["Progress (%)"] = (
        projection["Projected Account Ownership"] / target
    ) * 100

    # ---------------------------------------------------
    # Interactive Projection Chart
    # ---------------------------------------------------
    fig = px.line(
        projection,
        x="Year",
        y="Projected Account Ownership",
        markers=True,
        title="Projected Account Ownership Rate (2025–2027)"
    )

    fig.add_hline(
        y=60,
        line_dash="dash",
        annotation_text="60% Target"
    )

    st.plotly_chart(fig, use_container_width=True)

    # ---------------------------------------------------
    # Projection Table
    # ---------------------------------------------------
    st.subheader("Projection Table")

    st.dataframe(
        projection,
        use_container_width=True
    )

    # ---------------------------------------------------
    # Progress Indicator
    # ---------------------------------------------------
    latest_projection = projection.iloc[-1]["Projected Account Ownership"]

    latest_progress = projection.iloc[-1]["Progress (%)"]

    st.subheader("Progress Toward National Target")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "2027 Projection",
            f"{latest_projection:.1f}%"
        )

    with col2:
        st.metric(
            "Target Achievement",
            f"{latest_progress:.1f}%"
        )

    st.progress(min(latest_progress / 100, 1.0))

    st.write(
        f"The selected scenario achieves **{latest_progress:.1f}%** "
        f"of the national 60% financial inclusion target."
    )

    # ---------------------------------------------------
    # Consortium Questions
    # ---------------------------------------------------
    st.subheader("Key Insights for the Consortium")

    if scenario == "Baseline":

        st.success(
            """
            **Baseline Scenario**

            • Account ownership continues to grow steadily.

            • Ethiopia approaches the national 60% target by 2027.

            • Continued investment in digital finance remains important.
            """
        )

    elif scenario == "Optimistic":

        st.success(
            """
            **Optimistic Scenario**

            • Faster adoption of Telebirr and M-Pesa.

            • Stronger impact from Fayda Digital ID rollout.

            • Ethiopia exceeds the 60% financial inclusion target.
            """
        )

    else:

        st.warning(
            """
            **Pessimistic Scenario**

            • Slower adoption of digital financial services.

            • Infrastructure and regulatory challenges reduce growth.

            • Ethiopia remains below the national target.
            """
        )

    st.subheader("Major Drivers of Future Growth")

    st.markdown("""
- Telebirr ecosystem expansion
- M-Pesa market competition
- Fayda Digital ID enrollment
- Continued 4G infrastructure expansion
- National Financial Inclusion Strategy (NFIS-II)
- Increased digital payment adoption
""")

    st.subheader("Key Uncertainties")

    st.markdown("""
- Future regulatory changes
- Pace of mobile money adoption
- Economic conditions
- Expansion of digital infrastructure
- Consumer trust and digital literacy
""")

    # ---------------------------------------------------
    # Download Button
    # ---------------------------------------------------
    csv = projection.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Projection Data",
        data=csv,
        file_name="financial_inclusion_projection.csv",
        mime="text/csv"
    )
    st.markdown("---")

    st.subheader("Recommendations")

    st.success("""
    Recommendations for policymakers:

    • Continue expanding digital infrastructure.

    • Accelerate Fayda Digital ID enrollment.

    • Promote mobile money interoperability.

    • Encourage competition among financial service providers.

    • Improve digital financial literacy nationwide.
    """)
    st.markdown("---")

    st.caption(
        "Selam Analytics | Ethiopia Financial Inclusion Forecasting Dashboard"
    )

    st.caption(
        "Data Sources: Global Findex, National Bank of Ethiopia, Telebirr, M-Pesa Ethiopia, Fayda Digital ID"
    )
        
