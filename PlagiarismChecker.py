from cleantext import clean_words
from pathlib import Path

class MyFile:
  def __init__(topic,articleo,articlet):
    topic.articleo =Path(articleo)
    topic.articlet = Path(articlet)
  def words(topic):
    numofwords = 0
    for word in (topic.articleo).read_text().strip().split():
      numofwords += 1
    return numofwords
  def unique_words(topic):
    chars = ['.',',','?','!',':',';']
    uniquewords = clean_words((topic.articleo).read_text(),stopwords=True)
    uniquewords = set(uniquewords)
    
    uniquewords = {word.replace(char,"").lower() for word in uniquewords for char in chars}
    return uniquewords
  def unique_wordstwo(topic):
    chars = ['.',',','?','!',':',';']
    uniquewords = clean_words((topic.articlet).read_text(),stopwords=True)
    uniquewords = set(uniquewords)
    
    uniquewords = {word.replace(char,"").lower() for word in uniquewords for char in chars}
    return uniquewords
  def dict_of_words(topic):
    chars = ['.',';',':','!','?']
    
    wordsdict = {}
    for word in (topic.articleo).read_text().strip().split():
      for char in word:
        if char in chars:
          (word.replace(char, "")).lower()
      if word.lower() in wordsdict.keys():
        wordsdict[word.lower()] += 1
      else:
        wordsdict[word.lower()] = 1
    return wordsdict
  def num_of_sentences(topic):
    chars = ['.','?','!']
    
    sentences = 0
    for word in (topic.articleo).read_text().strip().split():
      for char in word:
        if char in chars:
          sentences += 1
    return sentences

  def num_of_paragraphs(topic):
    paragraphs = 1
    with open(topic.articleo) as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
    for element in lines:
      if element == '\n':
        paragraphs += 1
    return paragraphs
  def plagrism_checker(topic):
    u1 = topic.unique_words()
    u2 = topic.unique_wordstwo()
    j=len(u1.intersection(u2))/len(u1.union(u2))
    j = j * 100
    print("There is a " + str(round(j,2)) + "% chance that plagrism has occured")
    if j < 15:
      print("You don't need to edit your article")
    elif j > 15 and j < 40:
      print("You should edit your article as this is above the amount of same words.")
    elif j > 40:
      print("You definetly need to edit your article if you submitted it you would get a 0 for plagiarism")
    elif j == 100:
      print("This is the exact same article please redo this")
articleone = str(input("Input the file path of the first article: "))
articletwo = str(input("Input the file path of the second article: "))
instance = MyFile(articleone,articletwo)
instance.plagrism_checker()
