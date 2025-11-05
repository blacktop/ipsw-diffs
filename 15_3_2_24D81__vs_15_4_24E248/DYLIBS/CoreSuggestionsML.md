## CoreSuggestionsML

> `/System/Library/PrivateFrameworks/CoreSuggestionsML.framework/Versions/A/CoreSuggestionsML`

```diff

-1271.10.0.0.0
-  __TEXT.__text: 0x37db4
+1276.10.4.0.0
+  __TEXT.__text: 0x37aa4
   __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x2438
+  __TEXT.__objc_methlist: 0x25fc
   __TEXT.__const: 0x128
+  __TEXT.__cstring: 0x44e6
+  __TEXT.__dlopen_cstrs: 0x132
   __TEXT.__gcc_except_tab: 0x968
   __TEXT.__oslogstring: 0x400d
-  __TEXT.__cstring: 0x44e6
   __TEXT.__ustring: 0x11a
-  __TEXT.__dlopen_cstrs: 0x132
-  __TEXT.__unwind_info: 0xcc8
+  __TEXT.__unwind_info: 0xcb8
   __TEXT.__objc_classname: 0x713
   __TEXT.__objc_methname: 0x7d9f
   __TEXT.__objc_methtype: 0xe09

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18f0
+  __DATA_CONST.__objc_selrefs: 0x1978
   __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0x3b8
   __AUTH_CONST.__const: 0x1770
   __AUTH_CONST.__cfstring: 0x3000
-  __AUTH_CONST.__objc_const: 0x55c8
+  __AUTH_CONST.__objc_const: 0x52a0
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x1310

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 996EEB2C-B4C2-3B7A-80A8-8CFB020ED3E1
-  Functions: 1004
+  UUID: D62E407A-D3CA-32F1-A125-FF6E15590FBA
+  Functions: 1002
   Symbols:   2859
   CStrings:  2585
 
Symbols:
+ CoreSuggestionsInternalsLibraryCore.frameworkLibrary.448
+ __112-[SGQuickResponsesStore _addCustomResponseToDb:reply:language:embedding:sentAt:recipient:messagesRowId:onError:]_block_invoke.100
+ __112-[SGQuickResponsesStore _addCustomResponseToDb:reply:language:embedding:sentAt:recipient:messagesRowId:onError:]_block_invoke.96
+ __114-[SGQuickResponsesStore addingMessageExceedsBatchLimit:tableLimit:message:language:prompt:recipientHandle:sentAt:]_block_invoke.118
+ __114-[SGQuickResponsesStore addingMessageExceedsBatchLimit:tableLimit:message:language:prompt:recipientHandle:sentAt:]_block_invoke.126
+ __114-[SGQuickResponsesStore addingMessageExceedsBatchLimit:tableLimit:message:language:prompt:recipientHandle:sentAt:]_block_invoke_2.119
+ __114-[SGQuickResponsesStore addingMessageExceedsBatchLimit:tableLimit:message:language:prompt:recipientHandle:sentAt:]_block_invoke_2.127
+ __237-[SGQuickResponsesStore nearestCustomResponsesAndScoresToPromptEmbedding:recipient:limit:withinRadius:responseCountExponent:minimumDecayedCount:compatibilityVersion:language:locale:allowProfanity:minimumTimeInterval:usageSpreadExponent:]_block_invoke.257
+ __237-[SGQuickResponsesStore nearestCustomResponsesAndScoresToPromptEmbedding:recipient:limit:withinRadius:responseCountExponent:minimumDecayedCount:compatibilityVersion:language:locale:allowProfanity:minimumTimeInterval:usageSpreadExponent:]_block_invoke.262
+ __237-[SGQuickResponsesStore nearestCustomResponsesAndScoresToPromptEmbedding:recipient:limit:withinRadius:responseCountExponent:minimumDecayedCount:compatibilityVersion:language:locale:allowProfanity:minimumTimeInterval:usageSpreadExponent:]_block_invoke.267
+ __237-[SGQuickResponsesStore nearestCustomResponsesAndScoresToPromptEmbedding:recipient:limit:withinRadius:responseCountExponent:minimumDecayedCount:compatibilityVersion:language:locale:allowProfanity:minimumTimeInterval:usageSpreadExponent:]_block_invoke_2.272
+ __55-[SGQuickResponsesStore _recordsForResponses:language:]_block_invoke.41
+ __55-[SGQuickResponsesStore _recordsForResponses:language:]_block_invoke.46
+ __55-[SGQuickResponsesStore _recordsForResponses:language:]_block_invoke.54
+ __60-[SGQuickResponsesStore setProfanityLocale:andModelVersion:]_block_invoke.195
+ __61+[SGQuickResponsesScoring sortedWithUnweightedScores:config:]_block_invoke.41
+ __61+[SGQuickResponsesScoring sortedWithUnweightedScores:config:]_block_invoke.45
+ __62+[SGQuickResponsesRepliesNested indexedArraysFromNestedArray:]_block_invoke.472
+ __66+[SGQuickResponsesInference dynamicIndicesAndTopIsDynamic:config:]_block_invoke.172
+ __73-[SGQuickResponsesStore initInDirectory:inMemory:withMigration:forTools:]_block_invoke.22
+ __83-[SGQuickResponsesStore decayAllCustomResponsesWithDecayFactor:filteringBatchSize:]_block_invoke.290
+ __83-[SGQuickResponsesStore decayAllCustomResponsesWithDecayFactor:filteringBatchSize:]_block_invoke_2.291
+ __89-[SGQuickResponsesStore filterBatchWithMinimumDistinctRecipients:minimumReplyOccurences:]_block_invoke.165
+ __89-[SGQuickResponsesStore filterBatchWithMinimumDistinctRecipients:minimumReplyOccurences:]_block_invoke.175
+ __89-[SGQuickResponsesStore filterBatchWithMinimumDistinctRecipients:minimumReplyOccurences:]_block_invoke_2.166
+ __89-[SGQuickResponsesStore filterBatchWithMinimumDistinctRecipients:minimumReplyOccurences:]_block_invoke_2.176
+ __Block_byref_object_copy_.1140
+ __Block_byref_object_copy_.1460
+ __Block_byref_object_copy_.1663
+ __Block_byref_object_copy_.239
+ __Block_byref_object_copy_.270
+ __Block_byref_object_copy_.441
+ __Block_byref_object_copy_.521
+ __Block_byref_object_copy_.625
+ __Block_byref_object_copy_.63
+ __Block_byref_object_dispose_.1141
+ __Block_byref_object_dispose_.1461
+ __Block_byref_object_dispose_.1664
+ __Block_byref_object_dispose_.240
+ __Block_byref_object_dispose_.271
+ __Block_byref_object_dispose_.442
+ __Block_byref_object_dispose_.522
+ __Block_byref_object_dispose_.626
+ __Block_byref_object_dispose_.64
+ __CoreSuggestionsInternalsLibraryCore_block_invoke.449
+ __block_literal_global.1006
+ __block_literal_global.110
+ __block_literal_global.1120
+ __block_literal_global.1165
+ __block_literal_global.15
+ __block_literal_global.150
+ __block_literal_global.154
+ __block_literal_global.157
+ __block_literal_global.1615
+ __block_literal_global.1681
+ __block_literal_global.17
+ __block_literal_global.175
+ __block_literal_global.18
+ __block_literal_global.2151
+ __block_literal_global.25
+ __block_literal_global.265
+ __block_literal_global.270
+ __block_literal_global.275
+ __block_literal_global.30
+ __block_literal_global.33
+ __block_literal_global.427
+ __block_literal_global.512
+ __block_literal_global.61
+ __block_literal_global.68
+ __block_literal_global.73
+ __block_literal_global.733
+ __block_literal_global.740
+ __block_literal_global.747
+ __block_literal_global.755
+ __block_literal_global.76
+ __block_literal_global.77
+ __block_literal_global.792
+ __block_literal_global.81
+ __getSGNameDetectorClass_block_invoke.447
+ _addModelAssetUpdateHandler.onceToken.510
+ audit_stringCoreSuggestionsInternals.453
+ getSGNameDetectorClass.softClass.446
+ sharedInstance._pasExprOnceResult.1682
+ sharedInstance._pasExprOnceResult.790
+ sharedInstance._pasOnceToken2.1680
- CoreSuggestionsInternalsLibraryCore.frameworkLibrary.443
- __112-[SGQuickResponsesStore _addCustomResponseToDb:reply:language:embedding:sentAt:recipient:messagesRowId:onError:]_block_invoke.90
- __112-[SGQuickResponsesStore _addCustomResponseToDb:reply:language:embedding:sentAt:recipient:messagesRowId:onError:]_block_invoke.94
- __114-[SGQuickResponsesStore addingMessageExceedsBatchLimit:tableLimit:message:language:prompt:recipientHandle:sentAt:]_block_invoke.112
- __114-[SGQuickResponsesStore addingMessageExceedsBatchLimit:tableLimit:message:language:prompt:recipientHandle:sentAt:]_block_invoke.120
- __114-[SGQuickResponsesStore addingMessageExceedsBatchLimit:tableLimit:message:language:prompt:recipientHandle:sentAt:]_block_invoke_2.113
- __114-[SGQuickResponsesStore addingMessageExceedsBatchLimit:tableLimit:message:language:prompt:recipientHandle:sentAt:]_block_invoke_2.121
- __237-[SGQuickResponsesStore nearestCustomResponsesAndScoresToPromptEmbedding:recipient:limit:withinRadius:responseCountExponent:minimumDecayedCount:compatibilityVersion:language:locale:allowProfanity:minimumTimeInterval:usageSpreadExponent:]_block_invoke.251
- __237-[SGQuickResponsesStore nearestCustomResponsesAndScoresToPromptEmbedding:recipient:limit:withinRadius:responseCountExponent:minimumDecayedCount:compatibilityVersion:language:locale:allowProfanity:minimumTimeInterval:usageSpreadExponent:]_block_invoke.256
- __237-[SGQuickResponsesStore nearestCustomResponsesAndScoresToPromptEmbedding:recipient:limit:withinRadius:responseCountExponent:minimumDecayedCount:compatibilityVersion:language:locale:allowProfanity:minimumTimeInterval:usageSpreadExponent:]_block_invoke.261
- __237-[SGQuickResponsesStore nearestCustomResponsesAndScoresToPromptEmbedding:recipient:limit:withinRadius:responseCountExponent:minimumDecayedCount:compatibilityVersion:language:locale:allowProfanity:minimumTimeInterval:usageSpreadExponent:]_block_invoke_2.266
- __55-[SGQuickResponsesStore _recordsForResponses:language:]_block_invoke.35
- __55-[SGQuickResponsesStore _recordsForResponses:language:]_block_invoke.40
- __55-[SGQuickResponsesStore _recordsForResponses:language:]_block_invoke.48
- __60-[SGQuickResponsesStore setProfanityLocale:andModelVersion:]_block_invoke.189
- __61+[SGQuickResponsesScoring sortedWithUnweightedScores:config:]_block_invoke.35
- __61+[SGQuickResponsesScoring sortedWithUnweightedScores:config:]_block_invoke.39
- __62+[SGQuickResponsesRepliesNested indexedArraysFromNestedArray:]_block_invoke.466
- __66+[SGQuickResponsesInference dynamicIndicesAndTopIsDynamic:config:]_block_invoke.166
- __73-[SGQuickResponsesStore initInDirectory:inMemory:withMigration:forTools:]_block_invoke.16
- __83-[SGQuickResponsesStore decayAllCustomResponsesWithDecayFactor:filteringBatchSize:]_block_invoke.284
- __83-[SGQuickResponsesStore decayAllCustomResponsesWithDecayFactor:filteringBatchSize:]_block_invoke_2.285
- __89-[SGQuickResponsesStore filterBatchWithMinimumDistinctRecipients:minimumReplyOccurences:]_block_invoke.159
- __89-[SGQuickResponsesStore filterBatchWithMinimumDistinctRecipients:minimumReplyOccurences:]_block_invoke.169
- __89-[SGQuickResponsesStore filterBatchWithMinimumDistinctRecipients:minimumReplyOccurences:]_block_invoke_2.160
- __89-[SGQuickResponsesStore filterBatchWithMinimumDistinctRecipients:minimumReplyOccurences:]_block_invoke_2.170
- __Block_byref_object_copy_.1137
- __Block_byref_object_copy_.1456
- __Block_byref_object_copy_.1662
- __Block_byref_object_copy_.233
- __Block_byref_object_copy_.264
- __Block_byref_object_copy_.436
- __Block_byref_object_copy_.518
- __Block_byref_object_copy_.621
- __Block_byref_object_copy_.65
- __Block_byref_object_dispose_.1138
- __Block_byref_object_dispose_.1457
- __Block_byref_object_dispose_.1663
- __Block_byref_object_dispose_.234
- __Block_byref_object_dispose_.265
- __Block_byref_object_dispose_.437
- __Block_byref_object_dispose_.519
- __Block_byref_object_dispose_.622
- __Block_byref_object_dispose_.66
- __CoreSuggestionsInternalsLibraryCore_block_invoke.444
- __block_literal_global.11
- __block_literal_global.11.786
- __block_literal_global.1116
- __block_literal_global.1161
- __block_literal_global.118
- __block_literal_global.12
- __block_literal_global.144
- __block_literal_global.148
- __block_literal_global.151
- __block_literal_global.1614
- __block_literal_global.1680
- __block_literal_global.169
- __block_literal_global.19
- __block_literal_global.2157
- __block_literal_global.24
- __block_literal_global.259
- __block_literal_global.264
- __block_literal_global.269
- __block_literal_global.27
- __block_literal_global.422
- __block_literal_global.510
- __block_literal_global.55
- __block_literal_global.64
- __block_literal_global.67
- __block_literal_global.70.508
- __block_literal_global.71
- __block_literal_global.727
- __block_literal_global.731
- __block_literal_global.734
- __block_literal_global.741
- __block_literal_global.75
- __block_literal_global.789
- __block_literal_global.998
- __getSGNameDetectorClass_block_invoke.442
- _addModelAssetUpdateHandler.onceToken.506
- audit_stringCoreSuggestionsInternals.448
- getSGNameDetectorClass.softClass.441
- sharedInstance._pasExprOnceResult.1681
- sharedInstance._pasExprOnceResult.787
- sharedInstance._pasOnceToken2.1679

```
