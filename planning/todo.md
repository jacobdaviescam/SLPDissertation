# To-Do List

- [x] Finish writing the conversion script
    - [x] Questions with dangling 'to'
    - [x] Deal with passives
        - [x] Lemma of 'was' is 'be'
    - [x] Deal with unaccusatives (these are linked with passives and the way that we deal with them)
        - [x] Dictionary mapping first
    - [x] Deal with 'that'
    - [x] Deal with 'to'
    - [x] Deal with center embeddings
    - [x] Add code to convert each sentence in the dataset
    - [x] Add code to include the distribution and text of the sentence
    - [x] Punctuation
        - [x] Identify the main verb (the one that has no incoming edges)
    - [x] Unittests
    - [x] Sanity Checks
        - [x] Check that there is only one root
        - [x] Check that the length of forms, lemmas, pos, heads, deprel are the same
    - [x] 'To' as mark is wrong in the generalisation dataset for RC_modif_iobj and Q_modified_NPs
    - [x] Add them to the full generalisation set
- [x] Alter the parser code
    - [x] Add BERT embeddings
        - [x] In the repo from Matthias
    - [x] Add a way to evaluate with respect to the distribution
        - [x] Line 179 in conll17_ud_eval.py - do we need to change this?
- [x] Write introduction chapter
- [ ] Write background chapter
    - [x] Contextual Embeddings
    - [x] Feature Representations
- [x] Conduct experiments for data collection
    - [x] Run experiments on Cirrus
        - [x] Start by running a parse of a subset of the dataset
        - [x] Write a slurm script
        - [x] Run the parser on the entire dataset
    - [x] Rerun the training on both the transition and graph based parsers - as there is an error with the training script. 
    - [x] Rerun the conversion on Q_long_mv as the punctuation is wrong in the gold.
        - [x] Find a way to get this type back into the generalisation dataset. 
    - [ ] Run the transition model with less and more stack elements
    - [x] Run the graph-based model and force projectivity
    - [x] Run both graph and transition one more time and then average the result over the different seeds - report seeds for each random initialisation. 
    - [x] Run the models with BERT embeddings
    - [ ] Run the models with the external embeddings (GLOVE)
    - [x] Run  the models with POS embedding size = 25
        - [x] Run the transition parser with POS embedding size = 25
- [ ] Analyze collected data
    - [ ] Remake the graphs
        - [ ] With the POS results
        - [ ] With BERT
    - [x] Remake the tables
        - [x] With the POS results
        - [x] With BERT
    - [ ] Labeled attachment score by sentence length 
    - [x] Labeled F-score by dependency length
    - [x] Labeled F-score by distance to root
    - [ ] Labeled precision and recall for non-projective dependencies
    - [x] Accuracies on different parts of speech
    - [ ] Test what happens if we just use one LSTM on the graph based parser on PP depth. 
        word_emb_size = 100
        pos_emb_size = 0
        tbank_emb_size = 0
        char_lstm_output_size = 100
        lstm_input_size = 300
        lstm_output_size = 125
    - [x] What is the effect of using external BERT embeddings on the performance of the parser?
- [x] Write methodology chapter
    - [x] How did I create the dataset
- [x] Revise literature review
- [ ] Write results and discussion chapter
    - [ ] t-SNE plot 
        - [ ] Get the word embeddings after training using the get_word_embeddings function. 
        - [ ] Plot the word embedding for a word from the random initialised word embedding and the BERT word embedding
    - [ ] What is the difference between the AM parser and our graph based parser (AM parser is a graph based parser)
        - [ ] Dist embedding
- [ ] Write conclusion chapter
- [ ] Write abstract
- [ ] Proofread and edit entire dissertation
- [ ] Submit final dissertation

-[x] Look at Q_subj_passive in transition2
-[x] Rerun the models to get more consistent results
-[ ] Change the template to make the margins wider to include the tables and figures. 
-[ ] Remake the graphs. 
-[ ] Confusion Matrices - what do we want them to show?
-[ ] Go through the PP_modif_iobj and subtype and then analysis on each of the subtypes. 
-[ ] Rename sections to something more jazzy. 

Graph-based parsing does better at long sentences. We don't see this as the long sentences are do not correlate with the generalisation. 