Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> from nltk.book import *
*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
>>>  text3
 
SyntaxError: unexpected indent
>>> text3
<Text: The Book of Genesis>
>>>  train_text = text3[500:700]
 
SyntaxError: unexpected indent
>>> train_text = text3[500:700]
>>> from nltk.tokenize import PunktSentenceTokenizer
>>> def process_content() :
	try:
		for i in test_text:
			words=nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			print(tagged)
	                except Exception as e:
		        print(str(e))
		        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> try :

		for i in test_text:

			words = nltk.word_tokenize(i)

			tagged = nltk.pos_tag(words)

			print(tagged)

	except Exception as e:

		print(str(e))
		
SyntaxError: unindent does not match any outer indentation level
>>> def process_content() :

	try :

		for i in test_text:

			words = nltk.word_tokenize(i)

			tagged = nltk.pos_tag(words)

			print(tagged)

	except Exception as e:

		print(str(e))


>>> process_content()
name 'test_text' is not defined
>>> train_text = text3[500:700]
>>> test_text=text[100:500]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    test_text=text[100:500]
NameError: name 'text' is not defined
>>> test_text=text3[100:500]
>>> process_content()
[('first', 'RB')]
[('day', 'NN')]
[('.', '.')]
[('And', 'CC')]
[('God', 'NNP')]
[('said', 'VBD')]
[(',', ',')]
[('Let', 'VB')]
[('there', 'RB')]
[('be', 'VB')]
[('a', 'DT')]
[('firmament', 'NN')]
[('in', 'IN')]
[('the', 'DT')]
[('midst', 'NN')]
[('of', 'IN')]
[('the', 'DT')]
[('waters', 'NNS')]
[(',', ',')]
[('and', 'CC')]
[('let', 'VB')]
[('it', 'PRP')]
[('divide', 'NN')]
[('the', 'DT')]
[('waters', 'NNS')]
[('from', 'IN')]
[('the', 'DT')]
[('waters', 'NNS')]
[('.', '.')]
[('And', 'CC')]
[('God', 'NNP')]
[('made', 'VBN')]
[('the', 'DT')]
[('firmament', 'NN')]
[(',', ',')]
[('and', 'CC')]
[('divided', 'VBN')]
[('the', 'DT')]
[('waters', 'NNS')]
[('which', 'WDT')]
[('were', 'VBD')]
[('under', 'IN')]
[('the', 'DT')]
[('firmament', 'NN')]
[('from', 'IN')]
[('the', 'DT')]
[('waters', 'NNS')]
[('which', 'WDT')]
[('were', 'VBD')]
[('above', 'IN')]
[('the', 'DT')]
[('firmame', 'NN')]
[('and', 'CC')]
[('it', 'PRP')]
[('was', 'VBD')]
[('so', 'RB')]
[('.', '.')]
[('And', 'CC')]
[('God', 'NNP')]
[('called', 'VBN')]
[('the', 'DT')]
[('firmament', 'NN')]
[('Heaven', 'NN')]
[('.', '.')]
[('And', 'CC')]
[('the', 'DT')]
[('evening', 'VBG')]
[('and', 'CC')]
[('the', 'DT')]
[('morning', 'NN')]
[('were', 'VBD')]
[('the', 'DT')]
[('second', 'JJ')]
[('day', 'NN')]
[('.', '.')]
[('And', 'CC')]
[('God', 'NNP')]
[('said', 'VBD')]
[(',', ',')]
[('Let', 'VB')]
[('the', 'DT')]
[('waters', 'NNS')]
[('under', 'IN')]
[('the', 'DT')]
[('heaven', 'NN')]
[('be', 'VB')]
[('gathered', 'VBN')]
[('together', 'RB')]
[('unto', 'NN')]
[('one', 'CD')]
[('place', 'NN')]
[(',', ',')]
[('and', 'CC')]
[('let', 'VB')]
[('the', 'DT')]
[('dry', 'NN')]
[('land', 'NN')]
[('appe', 'NN')]
[('and', 'CC')]
[('it', 'PRP')]
[('was', 'VBD')]
[('so', 'RB')]
[('.', '.')]
[('And', 'CC')]
[('God', 'NNP')]
[('called', 'VBN')]
[('the', 'DT')]
[('dry', 'NN')]
[('land', 'NN')]
[('Earth', 'NN')]
[(';', ':')]
[('and', 'CC')]
[('the', 'DT')]
[('gathering', 'NN')]
[('together', 'RB')]
[('of', 'IN')]
[('the', 'DT')]
[('waters', 'NNS')]
[('called', 'VBN')]
[('he', 'PRP')]
[('Se', 'NN')]
[('and', 'CC')]
[('God', 'NNP')]
[('saw', 'NN')]
[('that', 'IN')]
[('it', 'PRP')]
[('was', 'VBD')]
[('good', 'JJ')]
[('.', '.')]
[('And', 'CC')]
[('God', 'NNP')]
[('said', 'VBD')]
[(',', ',')]
[('Let', 'VB')]
[('the', 'DT')]
[('earth', 'NN')]
[('bring', 'NN')]
[('forth', 'NN')]
[('grass', 'NN')]
[(',', ',')]
[('the', 'DT')]
[('herb', 'NN')]
[('yielding', 'VBG')]
[('seed', 'NN')]
[(',', ',')]
[('and', 'CC')]
[('the', 'DT')]
[('fruit', 'NN')]
[('tree', 'NN')]
[('yielding', 'VBG')]
[('fruit', 'NN')]
[('after', 'IN')]
[('his', 'PRP$')]
[('kind', 'NN')]
[(',', ',')]
[('whose', 'WP$')]
[('seed', 'NN')]
[('is', 'VBZ')]
[('in', 'IN')]
[('itself', 'PRP')]
[(',', ',')]
[('upon', 'IN')]
[('the', 'DT')]
[('ear', 'NN')]
[('and', 'CC')]
[('it', 'PRP')]
[('was', 'VBD')]
[('so', 'RB')]
[('.', '.')]
[('And', 'CC')]
[('the', 'DT')]
[('earth', 'NN')]
[('brought', 'NN')]
[('forth', 'NN')]
[('grass', 'NN')]
[(',', ',')]
[('and', 'CC')]
[('herb', 'NN')]
[('yielding', 'VBG')]
[('seed', 'NN')]
[('after', 'IN')]
[('his', 'PRP$')]
[('kind', 'NN')]
[(',', ',')]
[('and', 'CC')]
[('the', 'DT')]
[('tree', 'NN')]
[('yielding', 'VBG')]
[('fruit', 'NN')]
[(',', ',')]
[('whose', 'WP$')]
[('seed', 'NN')]
[('was', 'VBD')]
[('in', 'IN')]
[('itself', 'PRP')]
[(',', ',')]
[('after', 'IN')]
[('his', 'PRP$')]
[('ki', 'NN')]
[('and', 'CC')]
[('God', 'NNP')]
[('saw', 'NN')]
[('that', 'IN')]
[('it', 'PRP')]
[('was', 'VBD')]
[('good', 'JJ')]
[('.', '.')]
[('And', 'CC')]
[('the', 'DT')]
[('evening', 'VBG')]
[('and', 'CC')]
[('the', 'DT')]
[('morning', 'NN')]
[('were', 'VBD')]
[('the', 'DT')]
[('third', 'JJ')]
[('day', 'NN')]
[('.', '.')]
[('And', 'CC')]
[('God', 'NNP')]
[('said', 'VBD')]
[(',', ',')]
[('Let', 'VB')]
[('there', 'RB')]
[('be', 'VB')]
[('lights', 'NNS')]
[('in', 'IN')]
[('the', 'DT')]
[('firmament', 'NN')]
[('of', 'IN')]
[('the', 'DT')]
[('heaven', 'NN')]
[('to', 'TO')]
[('divide', 'NN')]
[('the', 'DT')]
[('day', 'NN')]
[('from', 'IN')]
[('the', 'DT')]
[('night', 'NN')]
[(';', ':')]
[('and', 'CC')]
[('let', 'VB')]
[('them', 'PRP')]
[('be', 'VB')]
[('for', 'IN')]
[('signs', 'NNS')]
[(',', ',')]
[('and', 'CC')]
[('for', 'IN')]
[('seasons', 'NNS')]
[(',', ',')]
[('and', 'CC')]
[('for', 'IN')]
[('days', 'NNS')]
[(',', ',')]
[('and', 'CC')]
[('yea', 'NN')]
[('And', 'CC')]
[('let', 'VB')]
[('them', 'PRP')]
[('be', 'VB')]
[('for', 'IN')]
[('lights', 'NNS')]
[('in', 'IN')]
[('the', 'DT')]
[('firmament', 'NN')]
[('of', 'IN')]
[('the', 'DT')]
[('heaven', 'NN')]
[('to', 'TO')]
[('give', 'VB')]
[('light', 'NN')]
[('upon', 'IN')]
[('the', 'DT')]
[('ear', 'NN')]
[('and', 'CC')]
[('it', 'PRP')]
[('was', 'VBD')]
[('so', 'RB')]
[('.', '.')]
[('And', 'CC')]
[('God', 'NNP')]
[('made', 'VBN')]
[('two', 'CD')]
[('great', 'JJ')]
[('lights', 'NNS')]
[(';', ':')]
[('the', 'DT')]
[('greater', 'JJR')]
[('light', 'NN')]
[('to', 'TO')]
[('rule', 'NN')]
[('the', 'DT')]
[('day', 'NN')]
[(',', ',')]
[('and', 'CC')]
[('the', 'DT')]
[('lesser', 'NN')]
[('light', 'NN')]
[('to', 'TO')]
[('rule', 'NN')]
[('the', 'DT')]
[('nig', 'NN')]
[('he', 'PRP')]
[('made', 'VBN')]
[('the', 'DT')]
[('stars', 'NNS')]
[('also', 'RB')]
[('.', '.')]
[('And', 'CC')]
[('God', 'NNP')]
[('set', 'NN')]
[('them', 'PRP')]
[('in', 'IN')]
[('the', 'DT')]
[('firmament', 'NN')]
[('of', 'IN')]
[('the', 'DT')]
[('heaven', 'NN')]
[('to', 'TO')]
[('give', 'VB')]
[('light', 'NN')]
[('upon', 'IN')]
[('the', 'DT')]
[('earth', 'NN')]
[(',', ',')]
[('And', 'CC')]
[('to', 'TO')]
[('rule', 'NN')]
[('over', 'IN')]
[('the', 'DT')]
[('day', 'NN')]
[('and', 'CC')]
[('over', 'IN')]
[('the', 'DT')]
[('night', 'NN')]
[(',', ',')]
[('and', 'CC')]
[('to', 'TO')]
[('divide', 'NN')]
[('the', 'DT')]
[('light', 'NN')]
[('from', 'IN')]
[('the', 'DT')]
[('darkne', 'NN')]
[('and', 'CC')]
[('God', 'NNP')]
[('saw', 'NN')]
[('that', 'IN')]
[('it', 'PRP')]
[('was', 'VBD')]
[('good', 'JJ')]
[('.', '.')]
[('And', 'CC')]
[('the', 'DT')]
[('evening', 'VBG')]
[('and', 'CC')]
[('the', 'DT')]
[('morning', 'NN')]
[('were', 'VBD')]
[('the', 'DT')]
[('fourth', 'JJ')]
[('day', 'NN')]
[('.', '.')]
[('And', 'CC')]
[('God', 'NNP')]
[('said', 'VBD')]
[(',', ',')]
[('Let', 'VB')]
[('the', 'DT')]
[('waters', 'NNS')]
[('bring', 'NN')]
[('forth', 'NN')]
[('abundantly', 'RB')]
[('the', 'DT')]
[('moving', 'VBG')]
[('creature', 'NN')]
[('that', 'IN')]
[('hath', 'NN')]
[('life', 'NN')]
[(',', ',')]
[('and', 'CC')]
[('fowl', 'NN')]
[('that', 'IN')]
[('may', 'MD')]
[('fly', 'NN')]
[('above', 'IN')]
[('the', 'DT')]
[('earth', 'NN')]
[('in', 'IN')]
[('the', 'DT')]
[('open', 'JJ')]
[('firmament', 'NN')]
[('of', 'IN')]
[('heaven', 'NN')]
[('.', '.')]
[('And', 'CC')]
[('God', 'NNP')]
[('created', 'VBN')]
[('great', 'JJ')]
>>> 