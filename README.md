# PCU
Plateforme de Connaissances Unifiées (PCU) project (*i.e* Unified Knowledge Platform).

Semantic platform for valuing data. Open-source, configurable, written in Python 3.

----

## Components

The platform is composed of several components :

* **[pcu_io][pcu_io]** : Parse a file to get its textual content. 
  * **[pcu_pdf][pcu_pdf]** : Parse PDF files (to an extent, files format supported by **[Apache Tika][tika]**).
  * **[pcu_json][pcu_json]** : Parse JSON files.
* **[pcu_language][pcu_language]** : Detect the main language used or all the languages used within a text. Based on **[langdetect][langdetect]**.
* **[pcu_nlp][pcu_nlp]** : Get syntactic annotations of a text. Based on **[spacy.io][spacy]**.
* **[pcu_keyphrase][pcu_keyphrase]** : Get keyphrases of a text. Based on **[kleis][kleis]**.
* **[pcu_relation][pcu_relation]** : Get semantic relationships existing between keyphrases of a text. Based on **[Kata Gábor][gabor]**'s algorithm.

[tika]: https://tika.apache.org
[langdetect]:https://pypi.org/project/langdetect/
[spacy]: https://spacy.io
[kleis]: https://github.com/sdhdez/kleis-keyphrase-extraction
[gabor]: http://www.inalco.fr/enseignant-chercheur/kata-gabor
[pcu_io]: https://github.com/zevio/pcu_io
[pcu_pdf]: https://github.com/zevio/pcu_pdf 
[pcu_json]: https://github.com/zevio/pcu_json
[pcu_language]: https://github.com/zevio/pcu_language
[pcu_nlp]: https://github.com/zevio/pcu_nlp
[pcu_keyphrase]: https://github.com/zevio/pcu_keyphrase
[pcu_relation]: https://github.com/zevio/pcu_relation

![PCU components](http://pix.toile-libre.org/upload/original/1540912595.png)

## Installation

To install requirements, go to pcu/ directory and execute the Makefile with the following command line :

`make install`

## Usage

The semantic platform is entirely configurable. To use it, download the sources, go to pcu/ directory and tune the configuration file as you wish.

```
[data]
path=data/IE.pdf
; path to data to analyse
[pipeline]
language=
; default language : if empty, language will be automatically detected
nlp=spacy 
; name of the NLP pipeline to use
keyphrase=yes
; yes if keyphrase extraction is enabled, no otherwise
relation=no
; yes if relation extraction is enabled, no otherwise
```

* **path** : path to data to analyse (file or folder)
* **language** : default language (en for English, fr for French). If empty, language will be automatically detected
* **nlp** : name of the NLP pipeline to use (spacy)
* **keyphrase** : yes if keyphrase extraction algorithm is enabled, no otherwise
* **relation** : yes if semantic relations extraction algorithm is enabled, no otherwise

## Test

To test your installation, go to pcu/ directory and execute the Makefile with the following command line : 

`make test`
