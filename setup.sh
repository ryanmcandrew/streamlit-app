mkdir -p ~/.streamlit/

echo "\
[server]
headless = true
port = $PORT
enableCORS = false
[theme]
primaryColor = '#7792E3'
backgroundColor = '#273346'
secondaryBackgroundColor = '#73abd6'
textColor = '#FFFFFF'
font = 'sans serif'

" > ~/.streamlit/config.toml

