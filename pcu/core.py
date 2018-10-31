import sys
import os

from configuration import getPathFromConfig
from configuration import getLanguageFromConfig
from configuration import getNLPFromConfig
from configuration import getKeyphraseFromConfig
from configuration import getRelationFromConfig
from pcu_language import detectLanguage
from pcu_io import pathExists
from pcu_io import isFile
from pcu_io import isDirectory
from pcu_io import getFileList
from pcu_io import getEquivalentTextfile
from pcu_io import getContent
from pcu_keyphrase import extractKeyphrases 
from pcu_relation import createInputFiles
from pcu_relation import extractRelations 
from pcu_nlp import spacyPipeline

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

def applyWorkflow(file):
	"""Apply workflow (NLP, machine learning) on a file.
	Parameter :
	file -- a file 
	"""
	textfile = getEquivalentTextfile(file) # get file's equivalent text file (if file is not a .txt file, it will be parsed)
	language = getLanguage(textfile) # get main language used within this file 
	nlp = getNLPFromConfig() # get NLP pipeline to use
	annotations = [] # semantic annotations on the text
	if(nlp=="spacy"): # if NLP pipeline is spacy
		annotations = spacyPipeline(language,getContent(textfile)) # apply spacy NLP pipeline and get its syntactic annotations
	""" this is where you should call another possible NLP pipeline to apply """	
	if(getKeyphraseFromConfig()): # if keyphrase extraction is enabled (from configuration file)
		print("**************** Keyphrases extraction. ****************")
		keyphrases = extractKeyphrases(getContent(textfile)) # extract keyphrases within the text file
		if(getRelationFromConfig()): # if relation extraction is enabled (from configuration file)
			print("**************** Relations extraction. ****************")
			createInputFiles(getContent(textfile),keyphrases) # create necessary input files for relation extraction from keyphrases
			returncode = extractRelations(keyphrases) # extract relations within the file and get returncode of relations extraction program
			if(returncode == 0): # if everything went well
				print("**************** Done ****************")

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

if __name__ == '__main__':
	path = getPathFromConfig() # get path to data from configuration file
	if(pathExists(path)): # if path exists
		initWorkflow(path) # initialize workflow on this path
	else:
		print("Incorrect config file : '%s' is not a valid path" % path)
		sys.exit()

	