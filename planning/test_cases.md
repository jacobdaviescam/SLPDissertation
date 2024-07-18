## train

## gen_cogs

test_RC_modif_iobj

Emma gave a bird that was lent the cookie a cake .

* cookie ( x _ 8 ) ; give . agent ( x _ 1 , Emma ) AND give . recipient ( x _ 1 , x _ 3 ) AND give . theme ( x _ 1 , x _ 10 ) AND bird ( x _ 3 ) AND bird . nmod ( x _ 3 , x _ 6 ) AND lend . recipient ( x _ 6 , x _ 3 ) AND lend . theme ( x _ 6 , x _ 8 ) AND cake ( x _ 10 )

[left]:  [nsubj, root, det, nsubj:pass, mark, aux:pass, acl:relcl, det, obj, det, obj, punct]
[right]: [nsubj, root, det, iobj, mark, aux:pass, acl:relcl, det, obj, det, obj, punct]

test_PP_modif_iobj

A cake was passed to a passenger beside a tree by the boy .

* boy ( x _ 12 ) ; cake ( x _ 1 ) AND pass . theme ( x _ 3 , x _ 1 ) AND pass . recipient ( x _ 3 , x _ 6 ) AND pass . agent ( x _ 3 , x _ 12 ) AND passenger ( x _ 6 ) AND passenger . nmod . beside ( x _ 6 , x _ 9 ) AND tree ( x _ 9 )	

[det, nsubj:pass, aux:pass, root, case, det, nsubj:pass, case, det, nmod:beside, case, det, obl:agent, punct]
[det, nsubj:pass, aux:pass, root, case, det, obl:to, case, det, nmod:beside, case, det, obl:agent, punct]