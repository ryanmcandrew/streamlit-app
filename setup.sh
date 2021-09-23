mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
# [theme]\n\
# primaryColor = '#7792E3'\n\
# backgroundColor = '#273346'\n\
# secondaryBackgroundColor = '#73abd6'\n\
# textColor = '#FFFFFF'\n\
# font = 'sans serif'\n\
\n\
" > ~/.streamlit/config.toml

