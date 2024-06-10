# LocalGPT

A Streamlit app for interacting with LLAMACPP-based GPT models locally in llama_cpp . 
Download or convert `safetensors` language models  from hugging  face to gguf format.
Tested  [Phi3](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf) model on i5 8th gen CPU with output  of  12 token/s.
## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)-
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Overview
LocalGPT is a Streamlit app that enables users to interact with LLAMACPP GPT models locally, without the need for an internet connection or remote server. It provides a user-friendly interface for generating text (streaming), and exploring the capabilities of the  model.

## Installation
To install the LocalGPT Streamlit app, follow these steps:
1. Clone the repository:
   ```
   git clone https://github.com/wambugu71/OfflineGPT-
   ```
2. Navigate to the project directory:
   ```
   cd OfflineGPT-
   ```
3.Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. (Optional) If you plan to use a GPU for acceleration (nvidia,intel,amd) gpu's install the GPU-specific packages:
   - See [llama_cpp_python installation GPU](https://llama-cpp-python.readthedocs.io/en/latest/)
5. Run your  model as a  server  from the  terminal.
   ```Bash
    python -m llama_cpp.server --model <llama_cpp model name>.gguf 
   ```

## Usage
To run the LocalGPT Streamlit app, simply execute the following command in the project directory:
```
cd src
streamlit run app.py
```
This will launch the app in your default web browser. You can then interact with the app (after running  the  server) by providing input text, and generating text.

## Customization
LocalGPT allows for customization of the app to suit your specific needs. You can modify the `app.py` file to  adjust the generation settings, or add additional functionality. Refer to the [Streamlit documentation](https://docs.streamlit.io/) for more information on customizing Streamlit apps.

## Contributing
Contributions are welcome! If you have suggestions, improvements, or bug fixes, feel free to create a pull request or open an issue.
## License
LocalGPT is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
