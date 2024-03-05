# OpenAI API Call Workshop
# Stanford Women in Computer Science - Sureen Heer
# This project is intended to familiarize fellows with how to create embeddings for a piece of text, how to determine the similarity between two pieces of text, and generating an image from text.

# Here are the relevant import statements
from openai import OpenAI
import numpy as np

# first set up the API key
client = OpenAI(api_key='FILL', organization='FILL')

# create embedding for the input text
def get_embedding(text):
  pass

# determine similarities between the two texts
def determine_similarity(embedding1, embedding2):
  pass

# generate an image from text
def get_image(text):
  pass

# user gives two input texts
def main():
  query1 = input("Type the text that you want to create an embedding for!\n")
  query2 = input("Type another piece of text you want to create an embedding for!\n")
  embedding1 = get_embedding(query1)
  embedding2 = get_embedding(query2)
  score = determine_similarity(embedding1, embedding2)
  print("This is how similar the inputs are: ", score)
  print("Generating an image for the first input!\n")
  image_url = get_image(query1)
  print("Here is the image URL: ", image_url)

if __name__ == "__main__":
   main()