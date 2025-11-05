## QueryUnderstanding

> `/System/Library/PrivateFrameworks/QueryUnderstanding.framework/Versions/A/QueryUnderstanding`

```diff

-2328.7.8.7.0
-  __TEXT.__text: 0x64c4
+2333.22.13.7.0
+  __TEXT.__text: 0x67d8
   __TEXT.__auth_stubs: 0x2b0
-  __TEXT.__objc_methlist: 0x52c
-  __TEXT.__const: 0x94
-  __TEXT.__cstring: 0xcb6
-  __TEXT.__oslogstring: 0x373
-  __TEXT.__gcc_except_tab: 0x764
-  __TEXT.__unwind_info: 0x2a8
+  __TEXT.__objc_methlist: 0x71c
+  __TEXT.__const: 0xd0
+  __TEXT.__cstring: 0xcc6
+  __TEXT.__oslogstring: 0x447
+  __TEXT.__gcc_except_tab: 0x7a8
+  __TEXT.__unwind_info: 0x2b0
   __TEXT.__objc_classname: 0xad
-  __TEXT.__objc_methname: 0x12a8
-  __TEXT.__objc_methtype: 0x3fd
+  __TEXT.__objc_methname: 0x12cb
+  __TEXT.__objc_methtype: 0x425
   __TEXT.__objc_stubs: 0xe20
-  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x580
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x488
+  __DATA_CONST.__objc_selrefs: 0x528
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__objc_arraydata: 0x70
+  __DATA_CONST.__objc_arraydata: 0x60
   __AUTH_CONST.__auth_got: 0x170
   __AUTH_CONST.__const: 0x1e0
   __AUTH_CONST.__cfstring: 0x240
-  __AUTH_CONST.__objc_const: 0x11f8
+  __AUTH_CONST.__objc_const: 0xe58
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x7c

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0CC66141-C61A-34E5-8AA6-8464136B14DB
-  Functions: 143
-  Symbols:   515
-  CStrings:  530
+  UUID: 6A5EB562-51F5-3117-8C8B-B850500066F5
+  Functions: 146
+  Symbols:   518
+  CStrings:  534
 
Symbols:
+ +[QUModelFactory sharedInstance].cold.1
+ -[U2HeadWrapper getU2PredictionsForEmbedding:queryString:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:intentHint:error:]
+ -[U2HeadWrapper mapLogitsToLabels:queryString:intentHint:tokens:subtokenLenForTokens:subtokens:]
+ -[U2OwlModel getUnderstandingForQueryString:spans:intentHint:withCompletionHandler:]
+ _OBJC_CLASS_$_NSDictionary
+ __84-[U2OwlModel getUnderstandingForQueryString:spans:intentHint:withCompletionHandler:]_block_invoke.cold.1
+ __84-[U2OwlModel getUnderstandingForQueryString:spans:intentHint:withCompletionHandler:]_block_invoke.cold.2
+ __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne190102IPfS5_EEvT_T0_m
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne190102Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne190102EmRKf
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___131-[U2HeadWrapper getU2PredictionsForEmbedding:queryString:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:intentHint:error:]_block_invoke
+ ___84-[U2OwlModel getUnderstandingForQueryString:spans:intentHint:withCompletionHandler:]_block_invoke
+ ___96-[U2HeadWrapper mapLogitsToLabels:queryString:intentHint:tokens:subtokenLenForTokens:subtokens:]_block_invoke
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e41_v24?0"<QUEmbeddingOutput>"8"NSError"16l
+ ___copy_helper_block_e8_32s40s48s56s64b
+ ___destroy_helper_block_e8_32s40s48s56s64s
+ __block_literal_global.157
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$getU2PredictionsForEmbedding:queryString:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:intentHint:error:
+ _objc_msgSend$mapLogitsToLabels:queryString:intentHint:tokens:subtokenLenForTokens:subtokens:
- -[U2HeadWrapper getU2PredictionsForEmbedding:queryString:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:error:]
- -[U2HeadWrapper mapLogitsToLabels:queryString:tokens:subtokenLenForTokens:subtokens:]
- -[U2OwlModel getUnderstandingForQueryString:spans:withCompletionHandler:]
- _OBJC_CLASS_$_NSConstantDictionary
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne180100IPfS5_EEvT_T0_m
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2EmRKf
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___120-[U2HeadWrapper getU2PredictionsForEmbedding:queryString:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:error:]_block_invoke
- ___73-[U2OwlModel getUnderstandingForQueryString:spans:withCompletionHandler:]_block_invoke
- ___85-[U2HeadWrapper mapLogitsToLabels:queryString:tokens:subtokenLenForTokens:subtokens:]_block_invoke
- ___block_descriptor_72_e8_32s40s48s56bs_e41_v24?0"<QUEmbeddingOutput>"8"NSError"16l
- ___copy_helper_block_e8_32s40s48s56b
- ___destroy_helper_block_e8_32s40s48s56s
- __block_literal_global.151
- _objc_msgSend$getU2PredictionsForEmbedding:queryString:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:error:
- _objc_msgSend$loadAllParametersForClient:locale:
- _objc_msgSend$mapLogitsToLabels:queryString:tokens:subtokenLenForTokens:subtokens:
CStrings:
+ "@64@0:8@16@24@32@40@48@56"
+ "@88@0:8@16@24@32@40@48@56@64@72^@80"
+ "QueryUnderstanding_IN"
+ "[QPNLU] Couldnt find asset in %@"
+ "[QPNLU] Intent Hint Value was supplied as %d"
+ "[QPNLU] the supplied intent hint value is out of range and doesnt represent a valid intent. Defaulting back to model predicted intent"
+ "dictionaryWithObjects:forKeys:count:"
+ "getU2PredictionsForEmbedding:queryString:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:intentHint:error:"
+ "getUnderstandingForQueryString:spans:intentHint:withCompletionHandler:"
+ "mapLogitsToLabels:queryString:intentHint:tokens:subtokenLenForTokens:subtokens:"
+ "v48@0:8@\"NSString\"16@\"QUSpans\"24@\"NSNumber\"32@?<v@?@\"<QUUnderstandingOutput>\"@\"NSError\">40"
+ "v48@0:8@16@24@32@?40"
- "@56@0:8@16@24@32@40@48"
- "@80@0:8@16@24@32@40@48@56@64^@72"
- "en_IN"
- "getU2PredictionsForEmbedding:queryString:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:error:"
- "getUnderstandingForQueryString:spans:withCompletionHandler:"
- "loadAllParametersForClient:locale:"
- "mapLogitsToLabels:queryString:tokens:subtokenLenForTokens:subtokens:"
- "v40@0:8@\"NSString\"16@\"QUSpans\"24@?<v@?@\"<QUUnderstandingOutput>\"@\"NSError\">32"

```
