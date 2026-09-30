## QueryUnderstanding

> `/System/Library/PrivateFrameworks/QueryUnderstanding.framework/QueryUnderstanding`

```diff

-3505.14.1.0.0
-  __TEXT.__text: 0x5d7c
-  __TEXT.__auth_stubs: 0x460
+3520.57.3.0.0
+  __TEXT.__text: 0x63c8
+  __TEXT.__auth_stubs: 0x400
   __TEXT.__objc_methlist: 0x724
-  __TEXT.__const: 0xc8
+  __TEXT.__const: 0xa0
   __TEXT.__cstring: 0xce4
   __TEXT.__oslogstring: 0x46a
-  __TEXT.__gcc_except_tab: 0x820
-  __TEXT.__unwind_info: 0x290
+  __TEXT.__gcc_except_tab: 0x810
+  __TEXT.__unwind_info: 0x2f8
   __TEXT.__objc_classname: 0xad
   __TEXT.__objc_methname: 0x12ef
   __TEXT.__objc_methtype: 0x401

   __DATA_CONST.__objc_selrefs: 0x530
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x248
+  __AUTH_CONST.__auth_got: 0x218
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x300
   __AUTH_CONST.__objc_const: 0xe58

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 972A7409-7AF1-3225-B7CC-9D042673BD27
+  UUID: 9B93A86E-DE5D-3371-9434-873D913E4168
   Functions: 134
-  Symbols:   664
+  Symbols:   658
   CStrings:  547
 
Symbols:
+ __ZNSt12length_errorC1B9nqe210106EPKc
+ __ZNSt3__119__allocate_at_leastB9nqe210106INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB9nqe210106EPKc
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB9nqe210106Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB9nqe210106IPfS5_EEvT_T0_m
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB9nqe210106Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B9nqe210106Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B9nqe210106EmRKf
+ __ZSt28__throw_bad_array_new_lengthB9nqe210106v
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne200100Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne200100IPfS5_EEvT_T0_m
- __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne200100Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne200100EmRKf
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x9
Functions:
~ -[U2HeadInput initWithInput_mask:input_span_features:sequence_output:] : 188 -> 172
~ -[U2HeadInput featureValueForName:] : 232 -> 252
~ -[U2HeadInput setInput_mask:] : 12 -> 64
~ -[U2HeadInput setInput_span_features:] : 12 -> 64
~ -[U2HeadInput setSequence_output:] : 12 -> 64
~ -[U2HeadOutput initWithTop_arg_ids:arg_conf_scores:intent_scores:safety_head_scores:] : 224 -> 208
~ -[U2HeadOutput featureValueForName:] : 276 -> 300
~ -[U2HeadOutput setTop_arg_ids:] : 12 -> 64
~ -[U2HeadOutput setArg_conf_scores:] : 12 -> 64
~ -[U2HeadOutput setIntent_scores:] : 12 -> 64
~ -[U2HeadOutput setSafety_head_scores:] : 12 -> 64
~ +[U2Head URLOfModelInThisBundle] : 180 -> 192
~ -[U2Head init] : 76 -> 80
~ -[U2Head initWithConfiguration:error:] : 108 -> 112
~ ___60+[U2Head loadContentsOfURL:configuration:completionHandler:]_block_invoke : 156 -> 164
~ -[U2Head predictionFromFeatures:error:] : 128 -> 132
~ -[U2Head predictionFromFeatures:options:error:] : 396 -> 432
~ -[U2Head predictionFromFeatures:completionHandler:] : 200 -> 196
~ ___51-[U2Head predictionFromFeatures:completionHandler:]_block_invoke : 416 -> 456
~ -[U2Head predictionFromFeatures:options:completionHandler:] : 220 -> 212
~ ___59-[U2Head predictionFromFeatures:options:completionHandler:]_block_invoke : 416 -> 456
~ -[U2Head predictionFromInput_mask:input_span_features:sequence_output:error:] : 180 -> 176
~ -[U2Head predictionsFromInputs:options:error:] : 576 -> 624
~ -[U2Output argIds] : 396 -> 408
~ -[U2Output argScores] : 396 -> 408
~ -[U2Output setConfidenceScore:] : 12 -> 64
~ -[U2Output setIntentId:] : 12 -> 64
~ -[U2Output setSafetyScore:] : 12 -> 64
~ -[U2Output setTokens:] : 12 -> 64
~ -[U2Output setTokenRanges:] : 12 -> 64
~ -[U2Output setArgIdsForTokens:] : 12 -> 64
~ -[U2Output setArgScoresForTokens:] : 12 -> 64
~ +[U2HeadWrapper log] : 160 -> 176
~ ___20+[U2HeadWrapper log]_block_invoke : 132 -> 136
~ +[U2HeadWrapper signpostLog] : 160 -> 176
~ ___28+[U2HeadWrapper signpostLog]_block_invoke : 132 -> 136
~ +[U2HeadWrapper U2HeadBundle] : 12 -> 60
~ +[U2HeadWrapper setU2HeadBundle:] : 16 -> 64
~ -[U2HeadWrapper initWithLocale:] : 132 -> 124
~ -[U2HeadWrapper metadata] : 132 -> 144
~ -[U2HeadWrapper assetURL] : 1068 -> 1132
~ -[U2HeadWrapper loadWithCompletionHandler:] : 632 -> 648
~ ___43-[U2HeadWrapper loadWithCompletionHandler:]_block_invoke : 924 -> 968
~ -[U2HeadWrapper argmaxWithIndex:] : 360 -> 376
~ __ZL27scoreFromSubtokenScoresProd_block_invoke_6 : 684 -> 732
~ -[U2HeadWrapper getTokenScoresfromScoreTensor:intentIndex:tokens:subtokenLenForTokens:subtokens:scoreFromSubtokenScores:] : 1148 -> 1164
~ -[U2HeadWrapper mapLogitsToLabels:queryString:queryID:intentHint:tokens:subtokenLenForTokens:subtokens:] : 2332 -> 2424
~ ___104-[U2HeadWrapper mapLogitsToLabels:queryString:queryID:intentHint:tokens:subtokenLenForTokens:subtokens:]_block_invoke : 264 -> 280
~ -[U2HeadWrapper getU2PredictionsForEmbedding:queryString:queryID:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:intentHint:error:] : 2176 -> 2236
~ ___139-[U2HeadWrapper getU2PredictionsForEmbedding:queryString:queryID:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:intentHint:error:]_block_invoke : 880 -> 904
~ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne200100Em -> __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B9nqe210106Em : 120 -> 108
~ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne200100EmRKf -> __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B9nqe210106EmRKf : 276 -> 132
~ +[QUModelFactory log] : 160 -> 176
~ ___21+[QUModelFactory log]_block_invoke : 108 -> 112
~ +[QUModelFactory sharedInstance] : 68 -> 84
~ -[QUModelFactory init] : 156 -> 160
~ -[QUModelFactory quModel] : 8 -> 56
~ -[QUModelFactory getModelForLocale:withTimeoutMS:] : 940 -> 980
~ ___50-[QUModelFactory getModelForLocale:withTimeoutMS:]_block_invoke : 596 -> 608
~ -[QUModelFactory releaseModel] : 224 -> 228
~ -[QUModelFactory loadError] : 80 -> 76
~ -[QUModelFactory setLoadError:] : 12 -> 64
~ +[U2OwlModel log] : 160 -> 176
~ ___17+[U2OwlModel log]_block_invoke : 108 -> 112
~ -[U2OwlModel initWithLocale:] : 148 -> 140
~ -[U2OwlModel loadWithCompletionHandler:] : 396 -> 400
~ ___40-[U2OwlModel loadWithCompletionHandler:]_block_invoke : 520 -> 544
~ ___40-[U2OwlModel loadWithCompletionHandler:]_block_invoke.4 : 248 -> 252
~ -[U2OwlModel modelMetadata] : 92 -> 100
~ -[U2OwlModel getUnderstandingForQueryString:queryID:spans:intentHint:withCompletionHandler:] : 300 -> 272
~ ___92-[U2OwlModel getUnderstandingForQueryString:queryID:spans:intentHint:withCompletionHandler:]_block_invoke : 532 -> 552
~ -[U2OwlModel setLocale:] : 12 -> 64

```
