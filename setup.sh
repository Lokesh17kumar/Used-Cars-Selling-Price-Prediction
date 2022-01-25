mkdir -p ~/.streamlit/

echo "[theme]
primaryColor = "#41B853"
backgroundColor = "#161B40"
secondaryBackgroundColor = "#EFA500"
textColor = "#FFFFFF"
font = "serif"
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
