## To do

[x] -> Passives ()

 -> How can we easily tell passive and active sentences apart. 
 -> If the verb.theme comes before the verb.agent we can say that this is a passive sentence, in which case we can apply a transformation to the relations.
 -> If no verb.agent it is a passive sentence wth no agent. 
 -> how do we deal with was
 -> aux:pass
 -> 123 (seems to be done already though)

[x] -> prepositions - to
    -> How to tell between 'to' infinitive and 'to' preposition. 
    -> If the verb is verb.recipient then it is a preposition.
    -> If the 'to' is for infinitives, the infinitive verb is 'ccomp' and  the 'to' is 'mark'. 
    -> 16980 for infinitive and 16969 for preposition, 16961 for an article

[x] -> nmod - relation between the index at the first position and the index at the second position (maybe change the whole code to do this instead)
    -> 

[x] -> adp - how to set the head of them when it can be the next word but also the word after depending on whether the next word is a name or a standard noun

[ ] -> multiple relations

[ ] -> that 
    -> how to assign the head

[ ] -> questions
    -> We need to get the information from the question mark, copy this information over to the question word and then treat the question mark as punctuation. 
    -> change heads to be a dictionary so we can index by key(word form)
    -> aux for the auxiliary verb

[x] -> 'by', 'to', 'that', 'who', 'what'
    -> 123, 121, 



Figure out the right order of if statements

{'standalone_NP_PP', 'primitive', 'wh_Q_simple_trans', 'exposure_example_obj_proper', 'exposure_example_pp_dative', 'exposure_example_unacc', 'object_modifying_RC', 'exposure_example_obj_common', 'cp_4', 'exposure_example_transitive_subj', 'exposure_example_do_dative', 'exposure_example_passive', 'center_embed_4', 'pp_4', 'standalone_NP_RC', 'exposure_example_active', 'exposure_example_unacc_subj', 'in_distribution', 'exposure_example_subj_proper', 'center_embed_2', 'exposure_example_obj_omitted_transitive', 'exposure_example_subj_common'}

Relations:

{'theme', 'xcomp', 'recipient', 'ccomp', }

1410
'by'


Also need to include the sentence id and text at the start of the conllu format for each sentence. 

