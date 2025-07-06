# 🤖 Suhaib - AI Education Assistant

A powerful AI-powered education assistant built with LangChain that helps students with their studies by providing intelligent responses to questions using Wikipedia and YouTube search capabilities.

## 🌟 Features

- **Intelligent Question Answering**: Uses OpenAI's GPT models to provide accurate and helpful responses
- **Wikipedia Integration**: Searches Wikipedia for detailed textual information and explanations
- **YouTube Video Search**: Finds relevant educational videos on YouTube for visual learning
- **LangSmith Tracing**: Built-in observability and tracing for debugging and monitoring
- **Robust Error Handling**: Comprehensive exception handling with detailed logging
- **Modular Architecture**: Clean, maintainable code structure with separated concerns

## 🏗️ Architecture

The project follows a modular architecture with the following components:

```
Agent/
├── main.py              # Main application entry point
├── agent.py             # Agent configuration and setup
├── model.py             # Language model configuration
├── tools.py             # Custom tools (Wikipedia, YouTube search)
├── prompt_template.py   # Agent prompt template
├── exception.py         # Custom exception handling
├── logger.py            # Logging configuration
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
├── setup.py            # Package setup
└── Logs/               # Application logs
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- LangSmith API key (optional, for tracing)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Agent
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   MODEL_NAME=gpt-3.5-turbo
   LANGCHAIN_PROJECT=education_bot
   LANGCHAIN_API_KEY=your_langsmith_api_key_here  # Optional
   LANGCHAIN_TRACING_V2=true  # Optional
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

## 🛠️ Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes | - |
| `MODEL_NAME` | OpenAI model to use | No | `gpt-3.5-turbo` |
| `LANGCHAIN_PROJECT` | LangSmith project name | No | `education_bot` |
| `LANGCHAIN_API_KEY` | LangSmith API key for tracing | No | - |
| `LANGCHAIN_TRACING_V2` | Enable LangSmith tracing | No | `false` |

### Model Configuration

The application uses OpenAI's ChatOpenAI model with the following settings:
- **Temperature**: 0 (deterministic responses)
- **Max Tokens**: 600
- **Model**: Configurable via environment variable

## 🔧 Available Tools

### 1. Wikipedia Search Tool
- **Purpose**: Provides detailed textual information from Wikipedia
- **Use Case**: Best for explaining concepts, definitions, and factual information
- **Returns**: Wikipedia article summaries and content

### 2. YouTube Search Tool
- **Purpose**: Finds relevant educational videos on YouTube
- **Use Case**: Best for visual learning, tutorials, and demonstrations
- **Returns**: List of YouTube video URLs (up to 5 results)

## 📝 Usage Examples

### Example 1: Academic Questions
```
Query: "Explain how photosynthesis works"
```
The agent will use Wikipedia search to provide a detailed explanation.

### Example 2: Visual Learning
```
Query: "Show me videos about Kashmir travel"
```
The agent will use YouTube search to find relevant travel videos.

### Example 3: Mixed Content
```
Query: "What is machine learning and show me tutorial videos"
```
The agent will combine Wikipedia for explanation and YouTube for tutorials.

## 🔍 How It Works

1. **Question Processing**: The agent receives a user query
2. **Tool Selection**: Based on the query, the agent decides which tool(s) to use
3. **Information Retrieval**: Tools fetch relevant information from Wikipedia or YouTube
4. **Response Generation**: The agent synthesizes the information into a coherent response
5. **Tracing**: All interactions are logged and traced (if LangSmith is enabled)

## 🏛️ Project Structure

### Core Modules

- **`main.py`**: Application entry point and orchestration
- **`agent.py`**: LangChain agent configuration with ReAct pattern
- **`model.py`**: OpenAI model setup and configuration
- **`tools.py`**: Custom tools for Wikipedia and YouTube search
- **`prompt_template.py`**: Agent prompt template for consistent behavior

### Supporting Modules

- **`exception.py`**: Custom exception handling with detailed error information
- **`logger.py`**: Structured logging configuration
- **`config.py`**: Path and configuration management

## 🐛 Error Handling

The application includes comprehensive error handling:

- **CustomException**: Detailed error tracking with file and line information
- **Graceful Degradation**: Individual tool failures don't crash the entire system
- **Detailed Logging**: All errors are logged with context for debugging
- **User-Friendly Messages**: Clear error messages for end users

## 📊 Logging

The application uses structured logging with the following features:

- **Log Directory**: `Logs/` folder with timestamped log files
- **Log Levels**: INFO, ERROR, DEBUG levels for different types of information
- **Context Information**: File names, line numbers, and stack traces
- **Performance Tracking**: Execution time and resource usage

## 🔧 Development

### Adding New Tools

1. Create a new function in `tools.py`
2. Decorate it with `@tool`
3. Add proper type hints and docstrings
4. Register it in the `get_tools()` function

### Customizing the Agent

- Modify `prompt_template.py` to change agent behavior
- Update `agent.py` for different agent types or configurations
- Adjust model parameters in `model.py`

## 📦 Package Management

The project includes `setup.py` for package distribution:

```bash
# Install in development mode
pip install -e .

# Build package
python setup.py sdist bdist_wheel
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **LangChain**: For the powerful framework
- **OpenAI**: For the language models
- **Wikipedia**: For the knowledge base
- **YouTube**: For video content

## 📞 Support

For questions, issues, or contributions, please open an issue on the repository.

---

**Built with ❤️ for education**
