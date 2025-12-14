#!/bin/bash

# Create Streamlit config directory
mkdir -p ~/.streamlit/

# Write Streamlit configuration
echo "\
[server]
headless = true
enableCORS = false
port = \$PORT

[theme]
primaryColor = '#6366f1'
backgroundColor = '#ffffff'
secondaryBackgroundColor = '#f9fafb'
textColor = '#1f2937'
font = 'sans serif'

[browser]
gatherUsageStats = false
" > ~/.streamlit/config.toml
