import sys
import os
import configparser

from pcu_language.pcu_language import detectLanguage
from pcu_io.pcu_io import pathExists
from pcu_io.pcu_io import isFile
from pcu_io.pcu_io import isDirectory
from pcu_io.pcu_io import getFileList
from pcu_io.pcu_io import getEquivalentTextfile
from pcu_io.pcu_io import getContent
from pcu_keyphrase.pcu_keyphrase import extractKeyphrases 
from pcu_relation.pcu_relation import createInputFiles
from pcu_relation.pcu_relation import extractRelations 
from pcu_nlp.pcu_nlp import spacyPipeline

def getKeyphraseFromConfig():
	"""Return keyphrase extraction enablement from configuration file.
	Return :
	keyphrase -- keyphrase extraction enablement
	"""	
	config = configparser.ConfigParser()
	config.read('config.ini') # read configuration file
	pipeline = config['pipeline']
	keyphrase = pipeline.getboolean('keyphrase') # get keyphrase extraction enablement from configuration file
	return keyphrase

def getNLPFromConfig():
	"""Return NLP pipeline from configuration file.
	Return :
	nlpPipeline -- NLP pipeline
	"""
	config = configparser.ConfigParser()
	config.read('config.ini') # read configuration file
	pipeline = config['pipeline']
	nlpPipeline = pipeline['nlp'] # get NLP pipeline from configuration file
	return nlpPipeline

def getLanguageFromConfig():
	"""Return language from configuration file.
	Return :
	language -- language
	"""
	config = configparser.ConfigParser()
	config.read('config.ini') # read configuration file
	pipeline = config['pipeline']
	language = pipeline['language'] # get language from configuration file
	return language

def getLanguage(file):
	"""Return main language used within a file, either from configuration file or automatic detection from text analysis.
	Parameter :
	file -- file to analyse
	Return :
	language -- main language used within the file
	"""
	language = getLanguageFromConfig() # get language from configuration file
	if(language==''): # if configuration file does not set a default language
		language = detectLanguage(file) # automatically detect language
	return language	

def applyMLAlgorithms(textfile):
	if(getKeyphraseFromConfig()): # if keyphrase extraction is enabled (from configuration file)
		print("**************** Keyphrases extraction. ****************")
		keyphrases = extractKeyphrases(getContent(textfile)) # extract keyphrases within the text file

def applyWorkflow(file):
	"""Apply workflow (NLP, machine learning) on a file.
	Parameter :
	file -- a file 
	"""
	textfile = getEquivalentTextfile(file) # get file's equivalent text file (if file is not a .txt file, it will be parsed)
	print("_______")
	print(textfile)
	language = getLanguage(textfile) # get main language used within this file 
	nlp = getNLPFromConfig() # get NLP pipeline to use
	annotations = [] # semantic annotations on the text
	if(nlp=="spacy"): # if NLP pipeline is spacy
		annotations = spacyPipeline(language,getContent(textfile)) # apply spacy NLP pipeline and get its syntactic annotations
	""" this is where you should call another possible NLP pipeline to apply """	
	applyMLAlgorithms(textfile)

def initWorkflow(path):
	"""Initialize workflow (NLP, machine learning) on data. 
	If data represents a file, then the workflow will be applied on this file.
	If data represents a directory, then the workflow will be applied on each file contained in this directory or its subdirectories.
	Parameter :
	path -- path to data
	"""
	if(isFile(path)): # data is contained in a file
		applyWorkflow(path) # apply workflow on file
	else :
		if(isDirectory(path)): # data is contained in a directory
			filelist = getFileList(path) # get list of files within directory and subdirectories
			for file in filelist:
				print(file)
				applyWorkflow(file) # apply workflow on each file
		else:
			print("Incorrect data path : '%s' is neither a file nor a directory" % path)
			sys.exit()

def core():
	if(len(sys.argv)==2):
		path=sys.argv[1]
		print("Data to process : '%s'" % path)
		if(pathExists(path)): # if path exists
			initWorkflow(path) # initialize workflow on this path
		else:
			print("Incorrect config file : '%s' is not a valid path" % path)
			sys.exit()
	else:
		print("Incorrect number of arguments : please use the appropriate command line described in the README")
		sys.exit()

if __name__ == '__main__':
	core()
	
