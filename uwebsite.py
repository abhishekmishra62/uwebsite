import streamlit as st
st.title("login")
username=st.text_input("Enter your name ",value=0,"%s")
a=st.number_input("Enter your Password: ",value=0,"%d")
sum1=0
sum2=0
sum3=0
sum4=0
b="1234567890"
c="@#$!&.,"
d="qwertyuiopasdfghjklzxcvbnm"
e="QWERTYUIOPASDFGHJKLZXCVBNM"
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            sum1+=1
    for j in range(len(c)):
        if a[i]==c[j]:
            sum2+=1
    for j in range(len(d)):
        if a[i]==d[j]:
            sum3+=1
    for j in range(len(e)):
        if a[i]==e[j]:
            sum4+=1
if sum1>0 and sum2>0 and sum3>0 and sum4>0:
    print("Valid password")
else:
    print("invalid")
