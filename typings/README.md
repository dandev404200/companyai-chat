# Generated Type Stubs

This directory contains automatically generated type stubs for better IDE support and type inference.

## Generated Files

- `langchain_custom/` - Manual stubs for common LangChain patterns
- `runtime/` - Stubs generated from runtime inspection
  - `langchain.pyi` - LangChain type stubs
  - `langchain_anthropic.pyi` - Anthropic integration stubs
  - `langchain_core.pyi` - Core component stubs
  - `common_patterns.pyi` - Usage-based patterns

## Usage

These stubs are automatically used by:
- Basedpyright (Zed's Python language server)
- Pyright
- Other Python type checkers

## Regeneration

To regenerate stubs, run:
```bash
./update_typings.sh
```

Or manually:
```bash
python generate_runtime_typings.py
```

## Configuration

The basedpyright configuration (`.basedpyrightconfig.json`) is automatically updated to include these typings directories in the `extraPaths` array.

