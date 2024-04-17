# import streamlit as st
# import pandas as pd
# import time 
# from datetime import datetime

# ts=time.time()
# date=datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
# timestamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")

# from streamlit import st_autorefresh

# count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

# if count == 0:
#     st.write("Count is zero")
# elif count % 3 == 0 and count % 5 == 0:
#     st.write("FizzBuzz")
# elif count % 3 == 0:
#     st.write("Fizz")
# elif count % 5 == 0:
#     st.write("Buzz")
# else:
#     st.write(f"Count: {count}")


# df=pd.read_csv("Recognize/Recognize_" + date + ".csv")

# st.dataframe(df.style.highlight_max(axis=0))
import streamlit as st
import pandas as pd
import time 
from datetime import datetime

ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")

count = 0  # Initialize count

# HTML meta tag for auto-refresh
st.markdown("<meta http-equiv='refresh' content='2'>", unsafe_allow_html=True)

if count == 0:
    st.write("Count is zero")
elif count % 3 == 0 and count % 5 == 0:
    st.write("FizzBuzz")
elif count % 3 == 0:
    st.write("Fizz")
elif count % 5 == 0:
    st.write("Buzz")
else:
    st.write(f"Count: {count}")

df = pd.read_csv("Recognize/Recognize_" + date + ".csv")
st.dataframe(df.style.highlight_max(axis=0))
