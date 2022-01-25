mkdir -p ~/.streamlit/

echo "
[theme]
primaryColor = '#41B853'
backgroundColor = '#161B40'
secondaryBackgroundColor = '#EFA500'
textColor = '#FFFFFF'
font = 'serif'
[server]
port = $PORT
enableCORS = false
headless = true
" > ~/.streamlit/config.toml
