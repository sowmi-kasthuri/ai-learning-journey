import streamlit as st
import requests
import os

FASTAPI_URL = os.getenv("FASTAPI_URL")
if FASTAPI_URL is None:
    st.error("FASTAPI_URL is not set. Please configure in Railway.")
    st.stop()


st.title("LLM Frontend (v0.2)")

# Create 2 tabs
tab1, tab2 = st.tabs(["📝 Generate", "📊 System Stats"])

# API_URL = "http://localhost:8000/generate"

# ----------------------------
# TAB 1: Generate UI
# ----------------------------

with tab1:
    st.header("Generate Text")
    prompt = st.text_area("Enter prompt")

    if st.button("Generate"):
        if not prompt.strip():
            st.error("Prompt is required.")
        else:
            try:
                response = requests.post(
                    f"{FASTAPI_URL}/generate",
                    json={"prompt": prompt}
                )
                data = response.json()

                st.subheader("Response")
                st.write(data.get("text"))

                st.subheader("Trace Info")
                st.json({
                    "trace_id": data.get("trace_id"),
                    "latency_ms": data.get("latency_ms"),
                    "cost": data.get("cost")
                })

                st.subheader("Token Usage")
                st.json({
                    "input_tokens": data.get("input_tokens"),
                    "output_tokens": data.get("output_tokens"),
                    "total_tokens": data.get("total_tokens")
                })

            except Exception as e:
                st.error(f"Request failed: {e}")

# ----------------------------
# TAB 2: Stats Dashboard
# ----------------------------
with tab2:
    st.header("System Stats")

    try:
        resp = requests.get(f"{FASTAPI_URL}/stats")
        data = resp.json()

        st.metric("Total Requests", data["total_requests"])
        st.metric("Total Errors", data["total_errors"])
        st.metric("Avg Latency (ms)", data["avg_latency_ms"])
        st.metric("Total Cost ($)", f"{data['total_cost']:.6f}")
    
    except Exception as e:
        st.error(f"Failed to fetch stats: {e}")