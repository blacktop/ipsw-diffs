## QueryUnderstanding

> `/System/Library/PrivateFrameworks/QueryUnderstanding.framework/QueryUnderstanding`

```diff

-2374.0.1.0.0
-  __TEXT.__text: 0x5bb0
+2381.0.1.0.0
+  __TEXT.__text: 0x5c04
   __TEXT.__auth_stubs: 0x460
   __TEXT.__objc_methlist: 0x724
   __TEXT.__const: 0xc0
   __TEXT.__cstring: 0xcd4
-  __TEXT.__oslogstring: 0x447
+  __TEXT.__oslogstring: 0x46a
   __TEXT.__gcc_except_tab: 0x7c4
   __TEXT.__unwind_info: 0x298
   __TEXT.__objc_classname: 0xad
-  __TEXT.__objc_methname: 0x12d7
-  __TEXT.__objc_methtype: 0x3f1
+  __TEXT.__objc_methname: 0x12ef
+  __TEXT.__objc_methtype: 0x3fd
   __TEXT.__objc_stubs: 0xe20
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__const: 0x6c0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 856D9F44-3B66-30D5-A356-3C45E7BD8A62
+  UUID: 48414E61-5E04-320A-9A48-D2723B789C1A
   Functions: 134
   Symbols:   664
   CStrings:  543
Symbols:
+ -[U2HeadWrapper getU2PredictionsForEmbedding:queryString:queryID:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:intentHint:error:]
+ -[U2HeadWrapper mapLogitsToLabels:queryString:queryID:intentHint:tokens:subtokenLenForTokens:subtokens:]
+ -[U2OwlModel getUnderstandingForQueryString:queryID:spans:intentHint:withCompletionHandler:]
+ ___104-[U2HeadWrapper mapLogitsToLabels:queryString:queryID:intentHint:tokens:subtokenLenForTokens:subtokens:]_block_invoke
+ ___139-[U2HeadWrapper getU2PredictionsForEmbedding:queryString:queryID:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:intentHint:error:]_block_invoke
+ ___92-[U2OwlModel getUnderstandingForQueryString:queryID:spans:intentHint:withCompletionHandler:]_block_invoke
+ ___92-[U2OwlModel getUnderstandingForQueryString:queryID:spans:intentHint:withCompletionHandler:]_block_invoke.cold.1
+ ___92-[U2OwlModel getUnderstandingForQueryString:queryID:spans:intentHint:withCompletionHandler:]_block_invoke.cold.2
+ ___block_descriptor_88_e8_32s40s48s56s64bs_e41_v24?0"<QUEmbeddingOutput>"8"NSError"16ls64l8s32l8s40l8s48l8s56l8
+ _objc_msgSend$getU2PredictionsForEmbedding:queryString:queryID:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:intentHint:error:
+ _objc_msgSend$mapLogitsToLabels:queryString:queryID:intentHint:tokens:subtokenLenForTokens:subtokens:
- -[U2HeadWrapper getU2PredictionsForEmbedding:queryString:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:intentHint:error:]
- -[U2HeadWrapper mapLogitsToLabels:queryString:intentHint:tokens:subtokenLenForTokens:subtokens:]
- -[U2OwlModel getUnderstandingForQueryString:spans:intentHint:withCompletionHandler:]
- ___131-[U2HeadWrapper getU2PredictionsForEmbedding:queryString:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:intentHint:error:]_block_invoke
- ___84-[U2OwlModel getUnderstandingForQueryString:spans:intentHint:withCompletionHandler:]_block_invoke
- ___84-[U2OwlModel getUnderstandingForQueryString:spans:intentHint:withCompletionHandler:]_block_invoke.cold.1
- ___84-[U2OwlModel getUnderstandingForQueryString:spans:intentHint:withCompletionHandler:]_block_invoke.cold.2
- ___96-[U2HeadWrapper mapLogitsToLabels:queryString:intentHint:tokens:subtokenLenForTokens:subtokens:]_block_invoke
- ___block_descriptor_80_e8_32s40s48s56s64bs_e41_v24?0"<QUEmbeddingOutput>"8"NSError"16ls64l8s32l8s40l8s48l8s56l8
- _objc_msgSend$getU2PredictionsForEmbedding:queryString:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:intentHint:error:
- _objc_msgSend$mapLogitsToLabels:queryString:intentHint:tokens:subtokenLenForTokens:subtokens:
Functions:
~ -[U2HeadWrapper mapLogitsToLabels:queryString:intentHint:tokens:subtokenLenForTokens:subtokens:] -> -[U2HeadWrapper mapLogitsToLabels:queryString:queryID:intentHint:tokens:subtokenLenForTokens:subtokens:] : 2288 -> 2324
~ -[U2HeadWrapper getU2PredictionsForEmbedding:queryString:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:intentHint:error:] -> -[U2HeadWrapper getU2PredictionsForEmbedding:queryString:queryID:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:intentHint:error:] : 2144 -> 2176
~ -[U2OwlModel getUnderstandingForQueryString:spans:intentHint:withCompletionHandler:] -> -[U2OwlModel getUnderstandingForQueryString:queryID:spans:intentHint:withCompletionHandler:] : 284 -> 300
CStrings:
+ "@72@0:8@16@24q32@40@48@56@64"
+ "@96@0:8@16@24q32@40@48@56@64@72@80^@88"
+ "[QPNLU] QU model released"
+ "[QPNLU][qid=%ld] Intent Hint Value was supplied as %d"
+ "[QPNLU][qid=%ld] U2Head prediction error: %@"
+ "[QPNLU][qid=%ld] got U2output-> intentScores: %@; topArgIds: %@; argConfidenceScores: %@"
+ "[QPNLU][qid=%ld] the supplied intent hint value is out of range and doesnt represent a valid intent. Defaulting back to model predicted intent"
+ "getU2PredictionsForEmbedding:queryString:queryID:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:intentHint:error:"
+ "getUnderstandingForQueryString:queryID:spans:intentHint:withCompletionHandler:"
+ "mapLogitsToLabels:queryString:queryID:intentHint:tokens:subtokenLenForTokens:subtokens:"
+ "v56@0:8@\"NSString\"16q24@\"QUSpans\"32@\"NSNumber\"40@?<v@?@\"<QUUnderstandingOutput>\"@\"NSError\">48"
+ "v56@0:8@16q24@32@40@?48"
- "@64@0:8@16@24@32@40@48@56"
- "@88@0:8@16@24@32@40@48@56@64@72^@80"
- "[QPNLU] Intent Hint Value was supplied as %d"
- "[QPNLU] QU model released."
- "[QPNLU] U2Head prediction error: %@"
- "[QPNLU] got U2output-> intentScores: %@; topArgIds: %@; argConfidenceScores: %@"
- "[QPNLU] the supplied intent hint value is out of range and doesnt represent a valid intent. Defaulting back to model predicted intent"
- "getU2PredictionsForEmbedding:queryString:spans:tokens:tokenRanges:subtokenLenForTokens:subtokens:intentHint:error:"
- "getUnderstandingForQueryString:spans:intentHint:withCompletionHandler:"
- "mapLogitsToLabels:queryString:intentHint:tokens:subtokenLenForTokens:subtokens:"
- "v48@0:8@\"NSString\"16@\"QUSpans\"24@\"NSNumber\"32@?<v@?@\"<QUUnderstandingOutput>\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"

```
