# import streamlit as st
# import requests

# # Backend API URL
# BACKEND_URL = "http://127.0.0.1:8050"

# st.title("📊 AI-Powered Data Visualization & Insights")

# # File Upload Section
# st.header("1️⃣ Upload Your Dataset")
# uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# if uploaded_file is not None:
#     files = {"file": uploaded_file.getvalue()}
#     response = requests.post(f"{BACKEND_URL}/upload/", files=files)
#     if response.status_code == 200:
#         file_data = response.json()
#         file_path = file_data["file_path"]
#         st.success("✅ File uploaded successfully!")
#         st.session_state["file_path"] = file_path  # Store file path for later use
#         columns = file_data["columns"]
#     else:
#         st.error("❌ Error uploading file. Try again.")
#         st.stop()
# else:
#     st.stop()

# # Graph Generation Section
# st.header("2️⃣ Generate Graph")
# graph_type = st.selectbox("Select Graph Type", ["bar", "line", "scatter","heatmap","pie","histogram","boxplot"])
# x_column = st.selectbox("Select X-axis Column", columns)
# y_column = st.selectbox("Select Y-axis Column", [None]+columns)

# if st.button("Generate Graph"):
#     data = {
#         "file_path": st.session_state["file_path"],
#         "graph_type": graph_type,
#         "x_column": x_column,
#         "y_column": y_column
#     }
#     response = requests.post(f"{BACKEND_URL}/generate_graph/", data=data)
#     if response.status_code == 200:
#         graph_data = response.json()
#         graph_url = graph_data["graph_url"]  # Get the correct graph URL
#         # st.image(graph_url, caption="📊 Generated Graph", use_container_width=True)
#         st.session_state["graph_url"] = graph_url
#     else:
#         st.error("❌ Error generating graph.")
# if "graph_url" in st.session_state:
#     st.image(st.session_state["graph_url"], caption="📊 Generated Graph", use_container_width=True)
# # Insight Query Section
# st.header("3️⃣ Get AI-Powered Insights")
# user_query = st.text_area("Enter your question about the graph")

# if st.button("Generate Insights"):
#     data = {"file_path": st.session_state["file_path"], "user_query": user_query}
#     response = requests.post(f"{BACKEND_URL}/generate_insights/", data=data)
#     if response.status_code == 200:
#         insights_data = response.json()
#         st.write("### 🔍 Insights:")
#         st.write(insights_data["insights"])
#     else:
#         st.error("❌ Error generating insights.")
import streamlit as st
import requests

# Backend API URL
BACKEND_URL = "http://127.0.0.1:8050"

# ================== Custom CSS ==================
st.markdown("""
<style>
/* Background and main container */
body, .main {
    background-color: #f4f6f8;
    font-family: 'Segoe UI', sans-serif;
}

/* Header Title */
.title-container {
    text-align: center;
    padding: 2rem 0 1rem 0;
}
.title-container h1 {
    font-size: 2.8rem;
    color: #2c3e50;
    font-weight: 800;
}
.title-container h1 span {
    color: #1abc9c;
}

/* Section Headers */
.section {
    margin-top: 30px;
    padding: 20px;
    background: rgba(0,0,0,0.7);
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
}

/* Upload + Select Styling */
.stFileUploader, .stSelectbox, .stTextArea, .stButton>button {
    font-size: 1rem;
}

/* Buttons */
.stButton>button {
    background-color: #1abc9c;
    color: white;
    font-weight: bold;
    border-radius: 12px;
    padding: 0.6rem 1.2rem;
    margin-top: 1rem;
    border: none;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background-color: #16a085;
    transform: scale(1.03);
}

/* Insight Box */
.insight-box {
    background: linear-gradient(to right, #dff6f0, #eafaf7);
    padding: 1.5rem;
    border-left: 6px solid #1abc9c;
    border-radius: 10px;
    margin-top: 1rem;
    font-size: 1.05rem;
    color: #2c3e50;
}

/* Image */
img {
    border-radius: 10px;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ================== Title ==================
st.markdown("""
<div class="title-container">
    <h1>📊 <span>AI-Powered</span> Graph and Insights Extractor</h1>
</div>
""", unsafe_allow_html=True)

# ================== 1. Upload Section ==================
with st.container():
    st.markdown('<div class="section"><h4>1️⃣ Upload Your Dataset (CSV)</h4>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file is not None:
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(f"{BACKEND_URL}/upload/", files=files)
    if response.status_code == 200:
        file_data = response.json()
        file_path = file_data["file_path"]
        st.session_state["file_path"] = file_path
        columns = file_data["columns"]
        st.success("✅ File uploaded successfully!")
    else:
        st.error("❌ Error uploading file.")
        st.stop()
else:
    st.stop()

# ================== 2. Graph Generation Section ==================
st.markdown('<div class="section"><h4>2️⃣ Generate a Graph</h4>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
graph_type = col1.selectbox("📈 Select Graph Type", ["bar", "line", "scatter", "heatmap", "pie", "histogram", "boxplot"])
x_column = col1.selectbox("🔹 X-axis", columns)
y_column = col2.selectbox("🔸 Y-axis", [None] + columns)

if st.button("Generate Graph"):
    data = {
        "file_path": st.session_state["file_path"],
        "graph_type": graph_type,
        "x_column": x_column,
        "y_column": y_column
    }
    response = requests.post(f"{BACKEND_URL}/generate_graph/", data=data)
    if response.status_code == 200:
        graph_data = response.json()
        graph_url = graph_data["graph_url"]
        st.session_state["graph_url"] = graph_url
        st.success("📊 Graph generated!")
    else:
        st.error("❌ Error generating graph.")

# Display the Graph if available
if "graph_url" in st.session_state:
    st.image(st.session_state["graph_url"], caption="Generated Graph", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# ================== 3. Insight Section ==================
st.markdown('<div class="section"><h4>3️⃣ Get AI-Powered Insights</h4>', unsafe_allow_html=True)
user_query = st.text_area("💬 Ask a question related to the graph or dataset")

if st.button("Generate Insights"):
    data = {
        "file_path": st.session_state["file_path"],
        "user_query": user_query
    }
    response = requests.post(f"{BACKEND_URL}/generate_insights/", data=data)
    if response.status_code == 200:
        insights_data = response.json()
        st.markdown(f"<div class='insight-box'>{insights_data['insights']}</div>", unsafe_allow_html=True)
    else:
        st.error("❌ Error generating insights.")

st.markdown('</div>', unsafe_allow_html=True)
