import configparser

def getRelationFromConfig():
	"""Return relation extraction enablement from configuration file.
	Return :
	relation -- relation extraction enablement
	"""	
	config = configparser.ConfigParser()
	config.read('config.ini') # read configuration file
	pipeline = config['pipeline'] 
	relation = pipeline.getboolean('relation') # get relation extraction enablement from configuration file
	return relation

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

def getPathFromConfig():
	"""Return data path from configuration file.
	Return :
	path -- data path
	"""
	config = configparser.ConfigParser() 
	config.read('config.ini') # read configuration file
	data = config['data'] 
	path = data['path'] # get path to data from configuration file
	return path