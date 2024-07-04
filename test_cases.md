## Current Errors

1. multiple_relations
    **solution** = list a set of control verbs and make a condition when there are two agents to select the control verb. 

    **relative clauses** = find the relative clause verb and remove this from the heads list


2. to

    1. Do a sanity check through both datasets to see if there are any instances of multiple ditransitives where to is the last word. 

        If there is we need to incorporate a similar method to 'that'
        
        If not we can attribute the head of 'to' to the recipient in the sentence. 

        There is one instance where there are two ditransitives in the sentence. 

3. that (center embedding) DONE

**solution** use linear previous word to identify the subject of the relative verb and from their identify the relative verb which that must attach to. 

4. deprel_to

5. passive

6. unaccusative

### gen_cogsLF
1. test_Q_iobj_ditransV

    **sentence** = Who did Emma give the cake to ?

    ****sentence_id**** = 14001

    **Issue** = The head of 'to' is attributed to the next word but it should be attributed to the question mark and then to the question word

    **issue_type** = to

    [left]:  [3, 3, 3, 0, 5, 3, 7, 3]

    [right]: [3, 3, 3, 0, 5, 3, 0, 3]

    **semantics** =  * cake ( x _ 5 ) ; give . agent ( x _ 3 , Emma ) AND give . theme ( x _ 3 , x _ 5 ) AND give . recipient ( x _ 3 , ? )

    **Code line**: 247

2. test_Q_subj_active
    **sentence**= Who hated to dust ?

    **sentence_id** = 11001

    **Issue**= The head of ? and 'who' is attributed to the last verb 'dust' when it should be attributed to both the main verb 'hate' and the secondary verb 'dust'

    **issue_type** = multiple_relations

    **solution** = list a set of control verbs and make a condition when there are two agents to select the control verb. 

    [left]:  [3, 0, 3, 1, 3]

    [right]: [1, 0, 3, 1, 1]

    **semantics** =  hate . agent ( x _ 1 , ? ) AND hate . xcomp ( x _ 1 , x _ 3 ) AND dust . agent ( x _ 3 , ? )

    **Code line**: 

3. test_RC_iobj_extracted
    **sentence**= Ella cooked the servant that Emma gave a tool to .

    **sentence_id** = 10001

    **Issue**= There are two issues. The first is that there are two heads for 'servant' - the main verb 'cooked' (obj) and the secondary verb 'gave' (iobj).

    **issue_type** = to + multiple_relations

    [left]:  [1, 0, 3, 6, 6, 6, 3, 8, 6, 10, 1]

    [right]: [1, 0, 3, 1, 6, 6, 3, 8, 6, 3, 1]

    **semantics** = * servant ( x _ 3 ) ; cook . agent ( x _ 1 , Ella ) AND cook . theme ( x _ 1 , x _ 3 ) AND servant . nmod ( x _ 3 , x _ 6 ) AND give . agent ( x _ 6 , Emma ) AND give . theme ( x _ 6 , x _ 8 ) AND give . recipient ( x _ 6 , x _ 3 ) AND tool ( x _ 8 )


code_line = 247 + 

4. test_RC_modif_iobj
    **sentence**= Emma gave a bird that was lent the cookie a cake .

    **sentence_id** = 9001

    **Issue**= There are two heads for 'bird' - the main verb 'gave' (iobj) and the secondary verb 'lent' (nsubj:pass).

    **issue_type** = multiple_relations

    [left]:  [1, 0, 3, 6, 6, 6, 3, 8, 6, 10, 1, 1]

    [right]: [1, 0, 3, 1, 6, 6, 3, 8, 6, 10, 1, 1]

    **semantics** = * cookie ( x _ 8 ) ; give . agent ( x _ 1 , Emma ) AND give . recipient ( x _ 1 , x _ 3 ) AND give . theme ( x _ 1 , x _ 10 ) AND bird ( x _ 3 ) AND bird . nmod ( x _ 3 , x _ 6 ) AND lend . recipient ( x _ 6 , x _ 3 ) AND lend . theme ( x _ 6 , x _ 8 ) AND cake ( x _ 10 )


    **Code line** = 

4. test_RC_modif_subj
    **sentence**= A cake that Liam found was investigated by the cat .

    **sentence_id** = 9001

    **Issue**= The head for 'that' is attributed to the main verb 'investigated' when it should be attributed to the RC verb 'found'. 

    **issue_type** = that

    [left]:  [1, 6, 6, 4, 1, 6, 0, 9, 9, 6, 6]

    [right]: [1, 6, 4, 4, 1, 6, 0, 9, 9, 6, 6]

    **semantics** = * cat ( x _ 9 ) ; cake ( x _ 1 ) AND cake . nmod ( x _ 1 , x _ 4 ) AND find . agent ( x _ 4 , Liam ) AND find . theme ( x _ 4 , x _ 1 ) AND investigate . theme ( x _ 6 , x _ 1 ) AND investigate . agent ( x _ 6 , x _ 9 )

    **Code line** = 243

### train

1. test_center_embed_2 (this is now updated)

    **sentence** = A boy helped the cat that the girl that Emma changed rolled .

    ****sentence_id**** = 15876

    **Issues** = 
    
    1. 'Cat' has multiple relations - ('help', obj) and ('rolled', obj)

    2. The head of the second 'that' is attributed to the final verb instead of its respective verb. 

    **issue_type** = multiple_relations, center_embedded

    [left]:  [1, 2, 0, 4, 11, 11, 7, 11, 11, 10, 7, 4, 2]

    [right]: [1, 2, 0, 4, 2, 11, 7, 11, 10, 10, 7, 4, 2]

    **semantics** =  * cat ( x _ 4 ) ; * girl ( x _ 7 ) ; boy ( x _ 1 ) AND help . agent ( x _ 2 , x _ 1 ) AND help . theme ( x _ 2 , x _ 4 ) AND cat . nmod ( x _ 4 , x _ 11 ) AND girl . nmod ( x _ 7 , x _ 10 ) AND change . agent ( x _ 10 , Emma ) AND change . theme ( x _ 10 , x _ 7 ) AND roll . agent ( x _ 11 , x _ 7 ) AND roll . theme ( x _ 11 , x _ 4 )

    **Code line**: 243

2. test_center_embed_4 

    **sentence** = Charlotte burned a penny that the president that the girl that a boy that Ava enlarged ate crumpled tolerated .

    ****sentence_id**** = 15881

    **Issues** = 
    
    1. 'penny' has two heads - ('burned', obj) and ('tolerated', obj)

    2. all the heads of 'that' are attributed to the final verb and not to their respective verbs

    **issue_type** = multiple_relations, center_embedded 

    [left]:  [1, 0, 3, 18, 18, 6, 18, 18, 9, 17, 18, 12, 16, 18, 15, 12, 9, 6, 3, 1]

    [right]: [1, 0, 3, 1, 18, 6, 18, 17, 9, 17, 16, 12, 16, 15, 15, 12, 9, 6, 3, 1]

    **semantics** =  * president ( x _ 6 ) ; * girl ( x _ 9 ) ; burn . agent ( x _ 1 , Charlotte ) AND burn . theme ( x _ 1 , x _ 3 ) AND penny ( x _ 3 ) AND penny . nmod ( x _ 3 , x _ 18 ) AND president . nmod ( x _ 6 , x _ 17 ) AND girl . nmod ( x _ 9 , x _ 16 ) AND boy ( x _ 12 ) AND boy . nmod ( x _ 12 , x _ 15 ) AND enlarge . agent ( x _ 15 , Ava ) AND enlarge . theme ( x _ 15 , x _ 12 ) AND eat . agent ( x _ 16 , x _ 12 ) AND eat . theme ( x _ 16 , x _ 9 ) AND crumple . agent ( x _ 17 , x _ 9 ) AND crumple . theme ( x _ 17 , x _ 6 ) AND tolerate . agent ( x _ 18 , x _ 6 ) AND tolerate . theme ( x _ 18 , x _ 3 )

    **Code line**: 243

3. test_cp_4 

    **sentence** = A baby respected that the host confessed that Emma admired that a girl liked that a bunny was offered a block on the tabletop .

    ****sentence_id**** = 16220

    **Issues** = 
    
    1. The heads of 'that' are attributed to the last verb instead of their respective verbs

    **issue_type** = that

    [left]:  [1, 2, 0, 20, 5, 6, 2, 20, 9, 6, 20, 12, 13, 9, 20, 16, 18, 18, 13, 20, 18, 23, 23, 20, 2]

    [right]: [1, 2, 0, 6, 5, 6, 2, 9, 9, 2, 13, 12, 13, 2, 18, 16, 18, 18, 2, 20, 18, 23, 23, 20, 2]

    **semantics** =  * host ( x _ 5 ) ; * tabletop ( x _ 23 ) ; baby ( x _ 1 ) AND respect . agent ( x _ 2 , x _ 1 ) AND respect . ccomp ( x _ 2 , x _ 6 ) AND confess . agent ( x _ 6 , x _ 5 ) AND confess . ccomp ( x _ 6 , x _ 9 ) AND admire . agent ( x _ 9 , Emma ) AND admire . ccomp ( x _ 9 , x _ 13 ) AND girl ( x _ 12 ) AND like . agent ( x _ 13 , x _ 12 ) AND like . ccomp ( x _ 13 , x _ 18 ) AND bunny ( x _ 16 ) AND offer . recipient ( x _ 18 , x _ 16 ) AND offer . theme ( x _ 18 , x _ 20 ) AND block ( x _ 20 ) AND block . nmod . on ( x _ 20 , x _ 23 )	cp_4
A cow ate .	cow ( x _ 1 ) AND eat . agent ( x _ 2 , x _ 1 )

    **Code line**: 243

4. test_exposure_example_pp_dative 

    **sentence** = The girl shipped a cookie in a container to Scarlett .

    ****sentence_id**** = 3346

    **Issues** = 
    
    1. The deprel tag of 'Scarlett' is given 'iobj' but it should be 'obl:to'. We need to check whether when there is a recipient, it is with 'to' or without. If it is with 'to' it should be given the 'obl:to' tag and without 'to', the 'iobj' tag. 

    **issue_type** = to_deprel

    [left]:  [det, nsubj, root, det, obj, case, det, nmod:in, case, iobj, punct]
    
    [right]: [det, nsubj, root, det, obj, case, det, nmod:in, case, obl:to, punct]

    **semantics** =  * girl ( x _ 1 ) ; ship . agent ( x _ 2 , x _ 1 ) AND ship . theme ( x _ 2 , x _ 4 ) AND ship . recipient ( x _ 2 , Scarlett ) AND cookie ( x _ 4 ) AND cookie . nmod . in ( x _ 4 , x _ 7 ) AND container ( x _ 7 )

    **Code line**: 247

5. test_exposure_example_unacc 

    **sentence** = Julian shattered .

    ****sentence_id**** = 15694

    **Issues** = 
    
    1. The deprel tag of 'Julian' is given 'nsubj:pass' rather than 'nsubj'. This is an issue which is inherited from the way that passives are identified. Currently, unaccusatives are captured by the passive identification. Passives need to be identified more accurately by finding the previous 'was'. 

    **issue_type** = passive, unaccusative

    [left]:  [nsubj:pass, root, punct]

    [right]: [nsubj, root, punct]

    **semantics** =  shatter . theme ( x _ 1 , Julian )

    **Code line**: 149

6. test_exposure_example_unacc_subj 

    **sentence** = A landlord hoped that the hippo decomposed .

    ****sentence_id**** = 13564

    **Issues** = 
    
    1. The deprel tag of 'hipp' is given 'obj' rather than 'nsubj'. This is an issue which is inherited from the way that passives are identified. Currently, unaccusatives are captured by the passive identification. Passives need to be identified more accurately by finding the previous 'was'. 

    **issue_type** = passive, unaccusative

    [left]:  [det, nsubj, root, mark, det, obj, ccomp, punct]

    [right]: [det, nsubj, root, mark, det, nsubj, ccomp, punct]

    **semantics** =  * hippo ( x _ 5 ) ; landlord ( x _ 1 ) AND hope . agent ( x _ 2 , x _ 1 ) AND hope . ccomp ( x _ 2 , x _ 6 ) AND decompose . theme ( x _ 6 , x _ 5 )

    **Code line**: 149

7. test_object_modifying_RC 

    **sentence** = Emma adored a drink that Noah liked .

    ****sentence_id**** = 10795

    **Issues** = 
    
    1. There are two heads of 'drink' - ('adored', obj) and ('liked', obj)

    **issue_type** = multiple_relations

    [left]:  [1, 0, 3, 6, 6, 6, 3, 1]

    [right]: [1, 0, 3, 1, 6, 6, 3, 1]

    **semantics** =  adore . agent ( x _ 1 , Emma ) AND adore . theme ( x _ 1 , x _ 3 ) AND drink ( x _ 3 ) AND drink . nmod ( x _ 3 , x _ 6 ) AND like . agent ( x _ 6 , Noah ) AND like . theme ( x _ 6 , x _ 3 )

    **Code line**: 

8. test_standalone_NP_RC 

    **sentence** = the girl that Mia liked

    ****sentence_id**** = 19295

    **Issues** = 
    
    1. There is no root identified in this sentence. This is because it is not a full sentence. There is a head of 'girl' - ('liked', obj) but it is also the root. 

    **issue_type** = multiple_relations, root

    [left]:  [1, 4, 4, 4, 1]

    [right]: [1, 0, 4, 4, 1]

    **semantics** =  * girl ( x _ 1 ) ; girl . nmod ( x _ 1 , x _ 4 ) AND like . agent ( x _ 4 , Mia ) AND like . theme ( x _ 4 , x _ 1 )

    **Code line**: 








