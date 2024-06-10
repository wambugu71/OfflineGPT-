import  streamlit  as st 
from openai import  OpenAI
from streamlit_shadcn_ui.py_components import button
st.set_page_config(page_icon=":bot", page_title="KINYUALocalGPT", layout="wide", initial_sidebar_state="expanded")
    
st.title("Query")
@st.experimental_fragment
def chat_llamacpp(prompt,temp, max_tokens):
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you with your  data?"}]
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.chat_message(msg["role"], avatar="user.svg").write(msg["content"],unsafe_allow_html=True)
        elif msg["role"] == "assistant":
            st.chat_message(msg["role"],avatar="ai.svg").write(msg["content"],unsafe_allow_html=True)
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user", avatar="user.svg").write(prompt)
        try:
            @st.cache_resource(show_spinner=False)
            def  client_openai():
                client = OpenAI(base_url="http://localhost:8000/v1", api_key="fk_openai")
                return client
            assistant_response = st.write_stream(client_openai().chat.completions.create(messages=[{"role":"system", "content":"You are a  helpful assistant, your  name  is  'wambugu Kinyualocal GPT'"},{"role": "user","content": f"{prompt}"}],model="wambuguGPT",stream=True, temperature= temp, max_tokens=max_tokens))
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
        except:
            st.error("An error occured, server  not  running!", icon="❗")
with st.sidebar:
    sys_prompt = st.text_area(label="System Prompt")
    temp = st.slider(label="Temperature", min_value=0.0001, step = 0.01, max_value=1.00, value=0.4)
    max_tokens = st.number_input(label="Max tokens", min_value=256, max_value=4096, value=512)
    if  button(text="stop output"):
        st.stop()  
prompt =st.chat_input("Ask your question...", )
chat_llamacpp(prompt=prompt, temp = temp, max_tokens = max_tokens)
