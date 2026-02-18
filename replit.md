# Open Dev Data

## Overview
A Python CLI/TUI tool providing a taxonomy of open source blockchain, web3, cryptocurrency, and decentralized ecosystems and their code repositories. Includes commands for validating migrations, exporting taxonomy data, downloading parquet files, and an interactive SQL TUI for data exploration.

## Project Architecture
- **Language**: Python 3.13
- **Package Manager**: uv
- **Entry Point**: `src/open_dev_data/commands.py` → `main()`
- **Package Name**: `open-dev-data`
- **Type**: CLI/TUI application (no web frontend)

### Directory Structure
- `src/open_dev_data/` - Main Python package
  - `commands.py` - CLI argument parsing and command dispatch
  - `taxonomy.py` - Core taxonomy logic (load, validate, export)
  - `tui.py` - Interactive SQL TUI using Harlequin
  - `download.py` - Parquet file downloading
  - `duckify.py` - DuckDB import utilities
  - `cli.py` - Additional CLI utilities
- `migrations/` - Taxonomy migration data files (timestamped directories)

### Key Dependencies
- `duckdb` - Embedded SQL database for analytics
- `harlequin` - Terminal-based SQL IDE for TUI mode
- `aiohttp` - Async HTTP for downloads
- `blake3` - Fast hashing for file verification
- `rich` - Terminal formatting and progress bars
- `platformdirs` - Cross-platform cache directory management

## How to Run
```bash
uv run open-dev-data --help
uv run open-dev-data validate
uv run open-dev-data export output.jsonl
uv run open-dev-data tui --lite
```

## Recent Changes
- 2025-02-18: Initial Replit setup with Python 3.13 and uv dependency management
