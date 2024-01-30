# 1. Write
import streamlit as st
import pandas as pd
st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))

# 1. Write

# 2. Text
# 2.1 markdown()
# import streamlit as st 
st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    Bagian markdown
    """
)

# 2.2 title()
# import streamlit as st
st.title('Belajar Analisis Data, Bagian title')

# 2.3 header()
# import streamlit as st
st.header('Pengembangan Dashboard, Bagian header')

# 2.4 subheader()
# import streamlit as st
st.subheader('Pengembangan Dashboard, Bagian subheader')

# 2.5 caption()
# import streamlit as st
st.caption('Copyright (c) 2023, Bagian caption')

# 2.6 code()
# import streamlit as st
code = """def hello():
    print("Hello, Streamlit!, Bagian code")"""
st.code(code, language='python')

# 2.7 text()
# import streamlit as st
st.text('Halo, calon praktisi data masa depan, Bagian text.')

# 2.8 latex()
# import streamlit as st
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

# 2. Text

# 3. Data Display
# 3.1 dataframe()
# import pandas as pd
# import streamlit as st
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.dataframe(data=df, width=500, height=150)

# 3.2 table()
# import pandas as pd
# import streamlit as st
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df)

# 3.3 metric()
# import streamlit as st
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

# 3.4 json()
# import streamlit as st
st.json({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})

# 3. Data Display

# 4. Chart
# 4.1 pyplot()
import matplotlib.pyplot as plt
import numpy as np
# import streamlit as st
x = np.random.normal(15, 5, 250)
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)

# 4. Chart