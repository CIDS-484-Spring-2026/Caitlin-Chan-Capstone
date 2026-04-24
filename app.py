import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Product Recommendation System",
    page_icon="🛍️",
    layout="wide"
)

# Load saved model artifacts from pickle file
@st.cache_resource
def load_model():
    with open('final_model.pkl', 'rb') as f:
        return pickle.load(f)

saved = load_model()

# Correlation-based recommendation function
def get_top5_recommendations(product_name, corr_matrix, label_map, most_recent_price, n=5):
    reverse_map = {v: k for k, v in label_map.items()}

    # Get short label for matrix lookup
    short_label = label_map.get(
        product_name,
        product_name[:30] + '...' if len(product_name) > 30 else product_name
    )

    if short_label not in corr_matrix.columns:
        return None

    # Filter to positive correlations only and return top N
    scores = (
        corr_matrix[short_label]
        .drop(short_label)
        .where(lambda x: x > 0)
        .dropna()
        .sort_values(ascending=False)
        .head(n)
    )

    if scores.empty:
        return None

    recommendations = pd.DataFrame({
        'Rank':                range(1, len(scores) + 1),
        'Recommended Product': [reverse_map.get(s, s) for s in scores.index],
        'Correlation Score':   scores.values.round(4),
        'Confidence':          pd.cut(
                                   scores.values,
                                   bins=[-1, 0.05, 0.15, 0.30, 1.0],
                                   labels=['Weak', 'Moderate', 'Strong', 'Very Strong']
                               )
    }).reset_index(drop=True)

    # Merge current price for each recommended product
    if most_recent_price is not None:
        recommendations = recommendations.merge(
            most_recent_price,
            left_on='Recommended Product',
            right_on='product_name',
            how='left'
        ).drop(columns='product_name')

        recommendations = recommendations.rename(columns={'current_price': 'Price ($)'})
        recommendations['Price ($)'] = recommendations['Price ($)'].apply(
            lambda x: f"${x:.2f}" if pd.notna(x) else "N/A"
        )

    return recommendations


# Page header
st.title("🛍️ Product Recommendation System")
st.markdown("Select a product below to see the top 5 products that are most frequently bought alongside it.")
st.divider()

# Sidebar configuration
st.sidebar.header("ℹ️ How It Works")
st.sidebar.markdown(
    "This system uses **product correlation** — it analyses which products "
    "are most commonly purchased together and recommends the strongest matches."
)
st.sidebar.markdown("---")
st.sidebar.markdown("**Confidence Guide**")
st.sidebar.markdown("🔴 **Weak** — rarely bought together")
st.sidebar.markdown("🟡 **Moderate** — some relationship")
st.sidebar.markdown("🟠 **Strong** — frequently bought together")
st.sidebar.markdown("🟢 **Very Strong** — almost always together")
st.sidebar.markdown("---")
n_recs = st.sidebar.slider("Number of Recommendations", min_value=1, max_value=10, value=5)

# Load required artifacts from pickle
corr_matrix       = saved.get('corr_matrix', None)
label_map         = saved.get('label_map', None)
most_recent_price = saved.get('most_recent_price', None)

# Validate that required artifacts are present
if corr_matrix is None or label_map is None:
    st.error(
        "corr_matrix and label_map were not found in final_model.pkl. "
        "Please re-save your pickle file to include them."
    )
    st.code("""
import pickle
with open('final_model.pkl', 'wb') as f:
    pickle.dump({
        'model':             final_model,
        'user_enc':          user_enc,
        'product_enc':       product_enc,
        'train_matrix':      train_matrix_B,
        'corr_matrix':       corr_matrix,
        'label_map':         label_map,
        'most_recent_price': most_recent_price,
        'params':            {'factors': 15, 'regularization': 0.01, 'iterations': 20},
        'precision@5':       0.1524
    }, f)
print("Saved.")
    """)
    st.stop()

# Product selector dropdown
product_list = sorted(label_map.keys())

col1, col2 = st.columns([3, 1])

with col1:
    selected_product = st.selectbox(
        "Select a Product",
        options=[""] + product_list,
        format_func=lambda x: "-- Select a product --" if x == "" else x
    )

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    run_button = st.button("Get Recommendations", type="primary", use_container_width=True)

st.divider()

# Recommendation output section
if run_button:
    if selected_product == "":
        st.warning("Please select a product first.")
    else:
        with st.spinner("Finding recommendations..."):
            recs = get_top5_recommendations(
                selected_product, corr_matrix, label_map, most_recent_price, n=n_recs
            )

        if recs is None:
            st.error(f"No positive correlations found for **{selected_product}**.")
        else:
            st.success(f"Customers who bought **{selected_product}** also tend to buy:")
            st.dataframe(
                recs,
                use_container_width=True,
                hide_index=True
            )

            # Confidence level breakdown metrics
            st.markdown("---")
            st.markdown("**Confidence Breakdown**")
            conf_counts = recs['Confidence'].value_counts()
            col1, col2, col3, col4 = st.columns(4)
            cols = [col1, col2, col3, col4]
            labels  = ['Very Strong', 'Strong', 'Moderate', 'Weak']
            colours = ['🟢', '🟠', '🟡', '🔴']
            for i, (label, colour) in enumerate(zip(labels, colours)):
                count = conf_counts.get(label, 0)
                cols[i].metric(f"{colour} {label}", count)
else:
    st.info("Select a product and click **Get Recommendations** to get started.")