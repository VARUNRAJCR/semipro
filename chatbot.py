import streamlit as st
from google import genai
from google.genai import types

def render_ai_chatbot():
    st.write("---")
    st.markdown("<h3 style='font-weight:600; color:#ffffff; font-size:1.2rem;'>🎛️ Real-Time Silicon AI Evaluation Engine</h3>", unsafe_allow_html=True)
    st.caption("Ask technical questions on CMOS scaling, Logical Effort networks, or SDC syntax parameters.")

    st.markdown("<div class='terminal-box'>", unsafe_allow_html=True)
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(f"<p style='color:#3b82f6; margin-bottom:4px;'><strong>[STUDENT_VECTOR] ></strong> {chat['text']}</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='color:#10b981; margin-bottom:12px; white-space: pre-wrap;'><strong>[AI_COACH_MATRIX] ></strong> {chat['text']}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    chat_query = st.text_input("Enter command query loop syntax:", placeholder="Type a physical design or transistor logic question...", key="chat_input_field")

    if st.button("Execute Chat Query Pipeline"):
        if chat_query:
            st.session_state.chat_history.append({"role": "user", "text": chat_query})
            with st.spinner("Processing telemetry analysis vectors..."):
                try:
                    client = genai.Client()
                    system_instruction_context = "You are the master tutor of SemiPro Academy, an elite VLSI Physical Design Engineering specialist. Never use emojis. Keep explanations crisp."
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=chat_query,
                        config=types.GenerateContentConfig(system_instruction=system_instruction_context)
                    )
                    ai_response_text = response.text
                except Exception:
                    ai_response_text = f"Telemetry Loop Verified: Received '{chat_query}'. Connect API key in secrets dashboard for full live processing."
                    
            st.session_state.chat_history.append({"role": "ai", "text": ai_response_text})
            st.rerun()
