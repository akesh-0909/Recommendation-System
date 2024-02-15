import streamlit as st 
import pickle as pkl
from helper.recommender_system import recommender
st.set_page_config(layout="wide")



st.title('Product Recommender System')

product_names = pkl.load(open('pickled/product_name.pkl','rb'))
similarity_metrix = pkl.load(open('pickled/top10 Similar Products Index Matrix.pkl','rb'))
image_urls = pkl.load(open('pickled/Image_file.pkl','rb'))
product_urls = pkl.load(open('pickled/product_link_file.pkl','rb'))

# st.write(product_detail)


selected_product = st.selectbox("Type or Select", product_names)
selected_product_index = product_names[product_names==selected_product].index[0]
print('Index of selected Product :',selected_product_index)

if st.button('Search'):
    
    recommended_ids = recommender(selected_product_index,similarity_metrix)
    
    st.title(selected_product)
   

    st.image('https://m.media-amazon.com/images/'+ image_urls[selected_product_index],width=450)

    st.markdown('''
      -----
      -----
             ''',unsafe_allow_html=True)
    st.title('See Similar Product')
    columns = st.columns(5),st.columns(5)
    
    index = 0
    for r in range(2):
        for col in range(5):
            with columns[r][col]:
                
                st.image('https://m.media-amazon.com/images/'+image_urls[recommended_ids[index]],width=100,use_column_width=100)
                st.markdown(product_names[recommended_ids[index]])
                # st.write('https://m.media-amazon.com/images/'+image_urls[index])
        
            index+=1
    
    


    
