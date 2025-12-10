import streamlit as st
import requests

st.title("LLM Frontend (v0.1)")

API_URL = "http://localhost:8000/generate"

prompt = st.text_area("Enter prompt")

if st.button("Generate"):
    if not prompt.strip():
        st.error("Prompt is required.")
    else:
        try:
            response = requests.post(
                API_URL,
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
