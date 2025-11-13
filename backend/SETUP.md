# Backend Setup Guide

## Quick Start

### 1. Create Virtual Environment

```bash
# Navigate to backend directory
cd backend

# Create virtual environment using uv (recommended)
uv venv

# Or using standard Python
python3.13 -m venv .venv
```

### 2. Activate Virtual Environment

```bash
# On Linux/Mac
source .venv/bin/activate

# On Windows
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Using uv (fastest)
uv pip sync

# Or using pip
pip install -e .
```

### 4. Set Environment Variables

Create a `.env` file in the backend directory:

```bash
# backend/.env
ANTHROPIC_API_KEY=your_api_key_here
```

### 5. Verify Installation

```bash
python -c "import langchain; import langgraph; print('✓ All packages installed')"
```

## Type Inference Setup

### Basedpyright Configuration

The project uses **basedpyright** for maximum type inference from your venv.

#### Configuration Files:
- `.zed/settings.json` - Zed editor LSP configuration
- `pyrightconfig.json` - Type checker configuration at project root

#### Key Features Enabled:

1. **Virtual Environment Detection**
   - Automatically uses `backend/.venv/bin/python`
   - Loads type stubs from installed packages

2. **Library Code Type Inference**
   - `useLibraryCodeForTypes: true` - Infers types from library source code
   - Gets full type information from LangChain, FastAPI, etc.

3. **Auto Search Paths**
   - Automatically finds modules in your project
   - Includes `backend/` and `backend/app/` in search paths

4. **Smart Diagnostics**
   - Disabled overly strict checks for LangChain compatibility:
     - `reportArgumentType: none` - Fixes LangChain invoke type issues
     - `reportCallIssue: none` - Handles dynamic tool calls
     - `reportUnknownMemberType: none` - Better inference for complex types

### Reloading Type Checker

After installing new packages or changing settings:

**In Zed:**
- Cmd+Shift+P → "Reload Window"
- Or restart Zed

**Check if it's working:**
```python
# backend/app/test_types.py
from langchain_core.messages import HumanMessage

# Should show full type information on hover
msg = HumanMessage(content="test")
print(msg.content)  # Type checker knows this is str
```

## Project Structure

```
backend/
├── .env                  # Environment variables (create this)
├── .venv/                # Virtual environment (created by uv/python)
├── app/
│   ├── agent.py         # LangGraph agent implementation
│   ├── endpoint.py      # FastAPI endpoints
│   ├── main.py          # FastAPI app
│   ├── router.py        # API router
│   └── schemas.py       # Pydantic schemas
├── pyproject.toml       # Dependencies
└── uv.lock              # Lock file
```

## Running the Server

```bash
# Development mode with auto-reload
cd backend
fastapi dev app/main.py

# Production mode
fastapi run app/main.py
```

Server runs at: `http://localhost:8000`

## Testing the Agent

```bash
# Run basic test
python app/agent.py

# Or use curl
curl -X POST http://localhost:8000/api/v1/chats/langgraph \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What is the weather in San Francisco?",
    "thread_id": "test_123",
    "use_tools": true
  }'
```

## Dependencies

### Core Packages:
- **langgraph** - Agent workflow orchestration
- **langchain-anthropic** - Anthropic Claude integration
- **langchain-core** - Core LangChain types and utilities
- **fastapi** - Web framework
- **asyncpg** - PostgreSQL async driver
- **sqlalchemy** - Database ORM

### Development Tools:
- **basedpyright** - Type checker (installed in Zed)
- **uv** - Fast Python package manager

## Troubleshooting

### "Module not found" errors
```bash
# Ensure venv is activated
which python  # Should show backend/.venv/bin/python

# Reinstall dependencies
uv pip sync
```

### Type checker not working
```bash
# Check Python path in Zed
# Should be: ./backend/.venv/bin/python

# Verify pyrightconfig.json exists at project root
ls ../pyrightconfig.json

# Reload Zed window
```

### API Key not found
```bash
# Check .env file exists
ls .env

# Verify it's loaded
python -c "from dotenv import load_dotenv; load_dotenv(); import os; print(os.getenv('ANTHROPIC_API_KEY'))"
```

### LangChain type errors
The configuration disables strict type checking for LangChain's dynamic types.
If you still see errors:
- Add `# type: ignore[arg-type]` comment
- Or wrap in `cast(Any, ...)` from `typing`

## IDE Setup

### VS Code (Alternative)
If using VS Code instead of Zed:

```json
// .vscode/settings.json
{
  "python.defaultInterpreterPath": "./backend/.venv/bin/python",
  "python.analysis.typeCheckingMode": "standard",
  "python.analysis.autoSearchPaths": true,
  "python.analysis.useLibraryCodeForTypes": true,
  "python.analysis.extraPaths": ["./backend", "./backend/app"]
}
```

### PyCharm
- File → Project Structure → Add Content Root → Select `backend/app`
- Settings → Python Interpreter → Select `backend/.venv`
- Settings → Editor → Inspections → Python → Disable strict type checking

## Next Steps

1. ✅ Create and activate venv
2. ✅ Install dependencies
3. ✅ Set ANTHROPIC_API_KEY in .env
4. ✅ Reload Zed window
5. ✅ Start coding with full type inference!

## Resources

- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [LangChain Docs](https://python.langchain.com/docs/get_started/introduction)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Basedpyright](https://docs.basedpyright.com/)