# import streamlit as st
# from langchain.prompts import PromptTemplate
# from langchain_community.llms import CTransformers

# # Function to get the response from the llama2 model
# def get_response(input_text, no_words, blog_style, genre):
#     try:
#         # llama2 model
#         llm = CTransformers(
#             model='models\llama-2-7b-chat.ggmlv3.q8_0.bin',
#             model_type='llama',
#             config={'max_new_tokens': 256, 'temperature': 0.02}
#         )

#         # Prompt template
#         template = """
#         Write a story whether it is fake or real no matter for {blog_style} for a topic or scenario that
#         is given by the user {input_text} within {no_words} words and the genre is {genre}. Please write as accurately
#         as possible.
#         """

#         # Create a PromptTemplate instance
#         prompt_template = PromptTemplate(
#             input_variables=["blog_style", "input_text", "no_words", "genre"],
#             template=template
#         )

#         # Generate the prompt
#         prompt = prompt_template.format(blog_style=blog_style, input_text=input_text, no_words=no_words, genre=genre)
        
#         # Generate the response
#         response = llm(prompt)
#         return response

#     except Exception as e:
#         return f"An error occurred: {e}"

# # Streamlit web interface
# st.set_page_config(
#     page_title="The Story Generator...📔📔📔📔",
#     page_icon="📔",
#     layout='centered',
#     initial_sidebar_state='collapsed'
# )

# st.write("The best StoryTeller... ✒️📖")

# st.header("The Story Generator...📔📔📔📔")

# # Create text box
# input_text = st.text_input("Enter the scenario for the story...✒️")

# # Creating columns
# col1, col2, col3 = st.columns([5, 5, 5])

# with col1:
#     no_words = st.text_input("Number of words")

# with col2:
#     blog_style = st.selectbox(
#         "Story for the...",
#         ('Kids', 'Secondary School Student', 'Common People', 'Relatives', 'College Student', 'Adult Friends', 'Manager', 'Customer', 'Job Profile', 'Seller', 'Parents', 'Office Colleagues', 'Spouse', 'Policeman', 'Judiciary', 'Voters')
#     )

# with col3:
#     genre = st.selectbox(
#         "Select Genre...",
#         ("Action", "Adventure", "Comedy", "Drama", "Fantasy", "Horror", "Mystery", "Romance", "Science Fiction", "Thriller", "Animation", "Crime", "Documentary", "Historical", "Musical", "Western")
#     )

# submit = st.button("Generate... ✌️")

# # Final response
# if submit:
#     response = get_response(input_text, no_words, blog_style, genre)
#     st.write(response)
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

## Function To get response from LLAma 2 model

def getLLamaresponse(input_text,no_words,blog_style):

    ### LLama2 model
    llm=CTransformers(model='models\llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    ## Prompt Template

    template="""
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response






st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text=st.text_input("Enter the Blog Topic")

## creating to more columns for additonal 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Researchers','Data Scientist','Common People'),index=0)
    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))