mkdir -p ~/.streamlit/

echo "
[theme]
primaryColor = 'F36295'
backgroundColor = '#F0FF33'
secondaryBackgroundColor = '#3183D1'
textColor = '#03080C'
font = 'sans-serif'
[server]
port = $PORT
enableCORS = false
headless = true
" > ~/.streamlit/config.toml
