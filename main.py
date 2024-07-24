import streamlit as st
st.title('이름을 입력해주세요 : ')
name = st.text_input('좋아하는 음식을 선택하십시옹', ['연어회', '연어초밥', '연어장덮밥'])
if st.button('인삿말 생성') :
    st.write(f'안녕 {name}을 좋아하는구나! 나랑 취향 잘 맞네ㅔ')
