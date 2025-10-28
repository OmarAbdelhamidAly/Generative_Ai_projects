# Multimodal E-commerce AI Platform

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.9+-ee4c2c)](https://pytorch.org/)
[![Transformers](https://img.shields.io/badge/🤗%20Transformers-4.20+-ffcc00)](https://huggingface.co/transformers/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Overview

Multimodal E-commerce AI is a state-of-the-art platform that revolutionizes e-commerce interactions through advanced natural language processing and deep learning. This enterprise-grade solution combines multiple AI models to deliver accurate, context-aware responses to customer queries and enable powerful semantic product search capabilities.

## ✨ Key Features

### 🤖 Intelligent Question Answering
- **Dual-Encoder Architecture**: Advanced neural architecture for semantic matching of questions and answers
- **Multi-Model Ensemble**: Combines extractive and generative AI models for comprehensive responses
- **Context-Aware Responses**: Understands and maintains conversation context for natural interactions

### 🔍 Semantic Product Search
- **Vector Similarity Search**: FAISS-powered ultra-fast similarity matching
- **Multilingual Support**: Built on `paraphrase-multilingual-MiniLM-L12-v2` for global reach
- **Category-Aware Filtering**: Precise filtering across multiple product categories

### 🏗️ Advanced Architecture
- **Model Optimization**: Implements LoRA and 4-bit quantization for efficient inference
- **Scalable Design**: Modular architecture for easy integration and scaling
- **Production-Ready**: Includes REST API endpoints and web interface

## 🛠 Technical Stack

### Core Technologies
- **Backend**: Python 3.8+, PyTorch, Transformers
- **Vector Database**: FAISS (Facebook AI Similarity Search)
- **Web Framework**: Flask
- **Model Serving**: ONNX Runtime (optional)

### AI/ML Components
- **Dual-Encoder Models**: Custom transformer-based architecture
- **Pre-trained Models**:
  - `sentence-transformers/all-MiniLM-L6-v2`
  - `distilbert/distilbert-base-cased-distilled-squad`
  - `google/flan-t5-base`
- **Efficient Training**: LoRA for parameter-efficient fine-tuning

## 📊 Performance Metrics

- **Retrieval Accuracy**:
  - Top-1 Accuracy: 5.7%
  - Top-5 Accuracy: 14.8%
  - *Note: Accuracy can be further improved with additional training data*

- **Inference Speed**:
  - <100ms response time for typical queries
  - Batch processing support for high-throughput scenarios

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- CUDA-compatible GPU (recommended)
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/multimodal-ecommerce-ai.git
cd multimodal-ecommerce-ai
```

2. **Create and activate virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Configuration

1. **Set up environment variables**
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
```

## 🏃‍♂️ Running the Application

### Start the QA Service
```bash
python chat-qna.py
```

### Start the Search Service
```bash
python search.py
```

Access the web interface at `http://localhost:5000`

## 📚 Documentation

### API Endpoints

#### Chat/Q&A Service
- `POST /api/ask` - Submit a question and get an AI-generated response

#### Search Service
- `GET /` - Search interface
- `GET /recommend` - API endpoint for product recommendations

### Model Training

#### Fine-tuning the Dual-Encoder
```bash
python train_dual_encoder.py --model_name sentence-transformers/all-MiniLM-L6-v2 --batch_size 32 --epochs 10
```

#### Training with LoRA
```bash
python train_lora.py --model_name distilbert/distilbert-base-cased-distilled-squad --use_4bit
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for the Transformers library
- [Facebook Research](https://research.facebook.com/) for FAISS
- The open-source community for invaluable tools and libraries

---

<div align="center">
  <h3>Built with ❤️ for the future of e-commerce</h3>
  <p>Enhancing customer experiences through AI</p>
</div>
