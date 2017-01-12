README
------
This is the README file for the Spanish language.

Corpora
-------

All annotated data come from one of these sources:
1. `Ancora`: The original Ancora corpus.
2. `Ancora_UD`: The Universal Dependencies version of the Ancora Corpus.
3. `IXA_UD`: A corpus compiled by the IXA group in the University of the Basque country and processed with the UD tools.

Extra corpus data
-----------------

The train and test PARSEME-TSV file is perfectly aligned to a CoNLL-U file.
  * Lemmas (CoNLL-U): Available in the two UD corpora (automatically annotated).
  * POS-tags (CoNLL-U): Available in the two UD corpora. The tagset is [Universal POS-tags](http://universaldependencies.org/u/pos).
  * Morphological features (CoNLL-U): Available in the two UD corpora (automatically annotated).
  * Dependency relations (CoNLL-U): Available in the two UD corpora (automatically annotated). The inventory is [Universal Dependency Relations](http://universaldependencies.org/u/dep).
  * No-space information (PARSEME-TSV): Available (automatically annotated) for Ancora. Not available for the UD corpora.
  
Tokenization
------------

  * Hyphens: Always split as a single token in UD.
  * Contractions: In the Ancora corpus contractions are kept as a single unit (not-split). In the UD corpora, most of them are split.
  
Annotation
----------

VMWEs in this language are annotated for the following categories: ID, LVC, IReflV, OTH.
