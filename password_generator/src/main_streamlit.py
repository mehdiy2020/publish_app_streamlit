import string
from random import choices
from abc import ABC, abstractmethod
import streamlit as st
from typing import List
import nltk
from nltk.corpus import words

nltk.download('words')
english_word = words.words()

st.title("_Password Generator_ :closed_lock_with_key:", width=600)

with st.sidebar:
  st.image("password_generator/image/mehdi_logo.png", width=200)
  your_selection = st.selectbox(
    label="What is your favorite type of password",
    options=["Random Password", "Memorable Password", "Pin Code Password"]
  )  



class PasswordGenerator(ABC):
  """An abstract base class that serves as blueprint for all
  the other password generator classes. It defines a common interface that all
  concerete subclasses must follow.

  :param ABC: Defines the abstract base class comes from the'abc' moudle.
  :type ABC: class
  """
  def __init__(self, name: str="name"):
    """Atribute to provide a name for owner of password.
    
    """
    self.name = name
    self.alphabet_list = [letter for letter in string.ascii_letters ]
    self.number_list = [str(num) for num in list(range(0, 10))]
    self.symbol_list = [sbl for sbl in string.punctuation]
  
  @abstractmethod
  def generate(self) -> str:
    """Under @abstractmethod decorator to enforce a consistent
    structure or define a common interface for subclasses. Here, 
    we create a dictionary of all the pissible character that are 
    required to use and to create a password
    """
    passwrod_dic = {'letter': self.alphabet_list,
    'number': self.number_list,
    'symbol': self.symbol_list,}
    return passwrod_dic
  


class RandomPasswordGenerator(PasswordGenerator):
  """This class generate a rather suphsticated random 
  password that may contain all the characters, numbers, and
  permitted symbols in python

  """
  def __init__(self, name):
    super().__init__(name)
    
  def generate(self):
    return super().generate()
  
  def random_password(
    self,
    n: int = 10,
    num_included: bool=False,
    symbo_included: bool=False,
    all_charac: bool=False
    ):
    """This method creates a random password that can be all strings,
    strings and numbers, strings and allowed symbols, or all together.    
    """
    if num_included:
      random_password = "".join(choices(self.generate()['letter'] + self.generate()['number'], k=n))
      return random_password
    elif symbo_included:
      random_password = "".join(choices(self.generate()['letter'] + self.generate()['symbol'], k=n))
      return random_password
    elif all_charac:
      random_password = "".join(choices(self.generate()['letter'] + self.generate()['symbol'] + self.generate()['number'], k=n))
      return random_password
    else:
      random_password = "".join(choices(self.generate()['letter'], k=n))
      return random_password


     
class MemorablePasswordGenerator(PasswordGenerator):
  """
  This class generates a memorable password.
  """
  def __init__(
    self,
    name,
    number_of_words: int=8,
    capitalized: bool=False
    ):
    super().__init__(name)
    self.number_of_words: int=number_of_words
    self.capitalized: bool=capitalized
    self.english_list: List[str]=choices(english_word, k=number_of_words)
    self.separators = {
      'hyphen': '-',
      'space': ' ',
      'dot': '.',
      'underscore': '_',
      'comma': ',',
      'slash': '/' 
      }
    
  def generate(self):
      return super().generate()

  def generate_password(self, separator: str='hyphen'):
    if self.capitalized:
      word_capitalized = [word.upper() for word in self.english_list]
      return self.separators[separator].join(word_capitalized)
    else:
      return self.separators[separator].join(self.english_list)
    
   

class PinCodeGenerator(PasswordGenerator):
  def __init__(self, name):
    super().__init__(name)
    
  def generate(self):
    return super().generate()
    
  def generate_password(self, length: int=4):
    return "".join(choices(self.number_list, k=length))


if your_selection == "Random Password":

  your_name = st.text_input(label="Your Name (any string is acceptable!)", value=" ")
  length_of_password = x= st.slider('select a value', min_value=6, max_value=50)
  option = st.radio(label="Select One of the Options to Includein Your Password",
                    options=[
                      "Include Numbers",
                      "Include Symbols",
                      "Include Numbers and Symbols"
                      ])
    
  if your_selection:
    if option ==  "Include Numbers" and your_name != " ":
      password_random = RandomPasswordGenerator(your_name)
      outcome = password_random.random_password(
        n=length_of_password,
        num_included=True
        )
      cont = st.container(border=True)
      cont.write(outcome)
    elif option ==  "Include Symbols" and your_name != " ":
      password_random = RandomPasswordGenerator(your_name)
      outcome = password_random.random_password(
        n=length_of_password,
        symbo_included=True
        )
      st.write(outcome)
    elif option ==  "Include Numbers and Symbols" and your_name != " ":
      password_random = RandomPasswordGenerator(your_name)
      outcome = password_random.random_password(
        n=length_of_password,
        all_charac=True
        )
      st.write(outcome)
    elif your_name != " ":
      password_random = RandomPasswordGenerator(your_name)
      outcome = password_random.random_password(n=length_of_password)
      st.write(outcome)
elif your_selection ==  "Memorable Password":
    your_name = st.text_input(label="Your Name (any string is acceptable!)", value=" ")
    x= st.slider('Select number of words', min_value=3, max_value=20)
    capital= st.radio(label="Do you want to see the password capitalized?",
                    options=[
                      True,
                      False
                      ])
    sep = st.radio(label="Do you want to see the password capitalized?",
                    options=[
                      'hyphen', 'space', 'dot','underscore','comma', 'slash'])
    if your_name != " " and x:
      memorable_password = MemorablePasswordGenerator(name=your_name, number_of_words=x, capitalized=capital)
      outcome = memorable_password.generate_password(separator=sep)
      st.write(outcome)
elif your_selection ==  "Pin Code Password":
  your_name = st.text_input(label="Your Name (any string is acceptable!)", value=" ")
  length_of_password = x= st.slider('select a value', min_value=6, max_value=50)
  if your_name != " " and length_of_password:
    password = PinCodeGenerator(name = your_name)
    pin_code = password.generate_password(length= length_of_password)
    st.write(pin_code)
else:
  st.write("Choose on of the options on the right side to create your password!")  

        
        

  



