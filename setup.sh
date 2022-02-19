mkdir -p ~/.streamlit/
echo "\
[theme]
primaryColor = '#41B853'
backgroundColor = '#161B40'
secondaryBackgroundColor = '#EFA500'
textColor= '#FFFFFF'
font = 'serif'
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml