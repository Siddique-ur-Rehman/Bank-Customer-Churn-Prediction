import streamlit as st
import joblib
import pandas as pd

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Bank Customer Churn Prediction",
    page_icon="🏦",
    layout='wide'
)

# ----------------------------
# Load Model
# ----------------------------
model = joblib.load("churn_model.pkl")

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Compact title */
    h1 {
        text-align: center;
        font-size: 2rem !important;
        margin-bottom: 0.2rem !important;
        padding-top: 0.5rem !important;
    }
    
    /* Subheader */
    h3 {
        margin-top: 0 !important;
        margin-bottom: 0.5rem !important;
        font-size: 1.1rem !important;
    }
    
    /* Card Style */
    .card {
        background-color: #f8f9fa;
        padding: 12px 15px;
        border-radius: 10px;
        border: 1px solid #e6e6e6;
        margin-bottom: 8px;
    }
    
    /* Compact columns */
    .row-widget.stColumns {
        gap: 0.5rem !important;
    }
    
    /* Compact inputs */
    .stNumberInput, .stSelectbox {
        margin-bottom: 0.3rem !important;
    }
    
    .stNumberInput label, .stSelectbox label {
        font-size: 0.85rem !important;
        font-weight: 500 !important;
        margin-bottom: 0.1rem !important;
    }
    
    .stNumberInput input, .stSelectbox select {
        padding: 0.3rem 0.5rem !important;
        font-size: 0.9rem !important;
        border-radius: 6px !important;
    }
    
    /* Compact divider */
    hr {
        margin: 0.5rem 0 !important;
    }
    
    /* Button */
    div[data-testid="stButton"] button {
        width: 100%;
        height: 45px;
        font-size: 16px;
        font-weight: 600;
        border-radius: 8px;
        margin: 0.2rem 0;
    }
    
    /* Prediction result */
    .element-container {
        margin-bottom: 0.2rem !important;
    }
    
    .stAlert {
        padding: 0.5rem 0.8rem !important;
        margin-bottom: 0.3rem !important;
    }
    
    .stAlert p {
        margin: 0 !important;
        font-size: 0.95rem !important;
    }
    
    /* Expandable */
    .streamlit-expanderHeader {
        font-size: 0.9rem !important;
        padding: 0.3rem 0.5rem !important;
    }
    
    /* Caption */
    .stCaption {
        text-align: center;
        font-size: 0.75rem !important;
        margin-top: 0.2rem !important;
    }
    
    /* Tab and other spacing */
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
        max-width: 1200px !important;
    }
    
    /* Grid layout */
    .css-1r6slb0 {
        gap: 0.3rem !important;
    }
    
    /* Custom column spacing */
    .css-1offfwp {
        padding: 0 0.3rem !important;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------
# Header
# ----------------------------
st.title("🏦 Bank Customer Churn Prediction")

st.markdown(
    """
    <p style='text-align: center; margin-top: -0.5rem; margin-bottom: 0.5rem; color: #666;'>
    Predict customer churn based on demographic and financial data
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ----------------------------
# Input Section - Compact 3-column layout
# ----------------------------
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    credit_score = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=900,
        value=650,
        step=10,
        help="Customer's credit score (300-900)"
    )
    
    country = st.selectbox(
        "Country",
        ["France", "Spain", "Germany"],
        help="Customer's country of residence"
    )
    
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"],
        help="Customer's gender"
    )
    
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=35,
        help="Customer's age in years"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    tenure = st.number_input(
        "Tenure (Years)",
        min_value=0,
        max_value=10,
        value=5,
        help="Number of years with the bank"
    )
    
    balance = st.number_input(
        "Account Balance ($)",
        min_value=0.0,
        value=50000.0,
        step=1000.0,
        format="%.0f",
        help="Customer's account balance"
    )
    
    products_number = st.number_input(
        "Products Used",
        min_value=1,
        max_value=4,
        value=1,
        help="Number of bank products used"
    )
    
    estimated_salary = st.number_input(
        "Salary ($)",
        min_value=0.0,
        value=50000.0,
        step=1000.0,
        format="%.0f",
        help="Estimated annual salary"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    credit_card = st.selectbox(
        "Has Credit Card",
        ["No", "Yes"],
        help="Does the customer have a credit card?"
    )
    
    active_member = st.selectbox(
        "Active Member",
        ["No", "Yes"],
        help="Is the customer an active member?"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Predict button in the third column
    predict = st.button(
        "🔍 Predict Churn",
        type="primary",
        use_container_width=True,
    )

st.divider()

# ----------------------------
# Prediction
# ----------------------------
if predict:
    # Convert inputs to model format
    input_data = pd.DataFrame([{
        "credit_score": credit_score,
        "country": country,
        "gender": gender,
        "age": age,
        "tenure": tenure,
        "balance": balance,
        "products_number": products_number,
        "credit_card": 1 if credit_card == "Yes" else 0,
        "active_member": 1 if active_member == "Yes" else 0,
        "estimated_salary": estimated_salary
    }])

    with st.spinner("Analyzing customer data..."):
        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)[0][1] if hasattr(model, 'predict_proba') else None

    if prediction[0] == 1:
        st.error(
            f"⚠️ **High Churn Risk** - This customer is likely to churn."
            + (f" (Probability: {probability:.1%})" if probability is not None else "")
        )
        
        col_rec1, col_rec2 = st.columns(2)
        with col_rec1:
            st.warning("📋 **Action Items**")
            st.markdown("""
            - 🎯 Offer personalized discounts
            - 📞 Proactive customer contact  
            - 📊 Review account activity
            - 💡 Improve engagement strategies
            """)
        with col_rec2:
            st.info("📈 **Risk Factors**")
            st.markdown("""
            - Consider loyalty programs
            - Monitor transaction patterns
            - Offer premium services
            - Schedule retention call
            """)
    else:
        st.success(
            f"✅ **Low Churn Risk** - This customer is likely to stay."
            + (f" (Confidence: {(1-probability):.1%})" if probability is not None else "")
        )
        st.balloons()
        
        col_rec1, col_rec2 = st.columns(2)
        with col_rec1:
            st.info("💎 **Recommendations**")
            st.markdown("""
            - ⭐ Continue quality service
            - 🎁 Offer loyalty rewards
            - 📧 Maintain engagement
            - 📈 Cross-sell opportunities
            """)
        with col_rec2:
            st.success("📊 **Customer Profile**")
            st.markdown("""
            - Strong retention potential
            - Good engagement metrics
            - Recommend premium products
            - Consider ambassador program
            """)

    st.divider()

# ----------------------------
# About Model - Compact
# ----------------------------
with st.expander("ℹ️ About This Application"):
    col_info1, col_info2 = st.columns(2)
    with col_info1:
        st.markdown("""
        **Features Analyzed:**
        - Credit Score & Age
        - Country & Gender  
        - Tenure & Balance
        - Product Usage
        - Credit Card Status
        - Active Membership
        - Estimated Salary
        """)
    with col_info2:
        st.markdown("""
        **Model Information:**
        - Trained Machine Learning Model
        - Predicts customer churn risk
        - Real-time predictions
        - Confidence scores included
        """)

# ----------------------------
# Footer
# ----------------------------
st.divider()
st.caption("🏦 Bank Customer Churn Prediction System | Powered by Machine Learning")