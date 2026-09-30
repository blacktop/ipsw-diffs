## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight`

```diff

-2418.4.8.2.100
-  __TEXT.__text: 0xe8a34
-  __TEXT.__auth_stubs: 0x1d20
-  __TEXT.__objc_methlist: 0xd808
+2418.4.10.1.0
+  __TEXT.__text: 0xe9550
+  __TEXT.__auth_stubs: 0x1d60
+  __TEXT.__objc_methlist: 0xd850
   __TEXT.__const: 0xd00
-  __TEXT.__cstring: 0x147d7
-  __TEXT.__gcc_except_tab: 0x2f90
-  __TEXT.__oslogstring: 0x849e
+  __TEXT.__cstring: 0x148f3
+  __TEXT.__gcc_except_tab: 0x2f94
+  __TEXT.__oslogstring: 0x84be
   __TEXT.__dlopen_cstrs: 0x49b
   __TEXT.__ustring: 0x3c
   __TEXT.__swift5_typeref: 0x2a0

   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x3d30
+  __TEXT.__unwind_info: 0x3d48
   __TEXT.__eh_frame: 0x210
   __TEXT.__objc_classname: 0x1180
-  __TEXT.__objc_methname: 0x20608
+  __TEXT.__objc_methname: 0x206e8
   __TEXT.__objc_methtype: 0x2682
-  __TEXT.__objc_stubs: 0x10ba0
-  __DATA_CONST.__got: 0x838
-  __DATA_CONST.__const: 0x5470
+  __TEXT.__objc_stubs: 0x10c20
+  __DATA_CONST.__got: 0x848
+  __DATA_CONST.__const: 0x54b8
   __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7dd8
+  __DATA_CONST.__objc_selrefs: 0x7df0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0xd90
-  __AUTH_CONST.__auth_got: 0xea8
+  __AUTH_CONST.__auth_got: 0xec8
   __AUTH_CONST.__const: 0x1a50
-  __AUTH_CONST.__cfstring: 0x13c00
-  __AUTH_CONST.__objc_const: 0x11eb8
+  __AUTH_CONST.__cfstring: 0x13e40
+  __AUTH_CONST.__objc_const: 0x11fd8
   __AUTH_CONST.__objc_arrayobj: 0xa80
   __AUTH_CONST.__objc_intobj: 0x7b0
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_doubleobj: 0xd0
   __AUTH.__objc_data: 0x1900
   __AUTH.__data: 0x3a0
-  __DATA.__objc_ivar: 0xc94
+  __DATA.__objc_ivar: 0xcb0
   __DATA.__data: 0xab8
   __DATA.__bss: 0x1320
   __DATA_DIRTY.__objc_data: 0x15e0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: FD962F93-B163-3197-8019-6C29A5DC715F
-  Functions: 5899
-  Symbols:   18652
-  CStrings:  12891
+  UUID: 7E1121EC-F294-3600-9F94-FF719A118C30
+  Functions: 5907
+  Symbols:   18687
+  CStrings:  12940
 
Symbols:
+ -[CSSearchConnection createXPCDictionaryForQuery:queryID:queryContext:needsInitialization:].cold.1
+ -[CSSearchQuery _sendQueryAnalyticsEventWithError:]
+ -[CSSearchQuery _shouldEmitAnalyticsEvent]
+ -[CSSearchQuery(TopHitRanking) rankBatch:withRanker:withBundle:maxCount:heapMaxCount:userQuery:queryID:rankingConfiguration:isCJK:clientBundle:isKeyboardCJK:privateQuery:collectL2Signals:onlyEmbeddingResults:]
+ -[CSSearchQueryContext isUnsafeQuery]
+ -[CSSearchQueryContext ownerToken]
+ -[CSSearchQueryContext setIsUnsafeQuery:]
+ -[CSSearchQueryContext setOwnerToken:]
+ GCC_except_table308
+ GCC_except_table322
+ GCC_except_table330
+ GCC_except_table345
+ GCC_except_table348
+ GCC_except_table353
+ GCC_except_table357
+ GCC_except_table358
+ GCC_except_table361
+ GCC_except_table363
+ GCC_except_table439
+ GCC_except_table440
+ GCC_except_table441
+ GCC_except_table449
+ GCC_except_table486
+ _OBJC_IVAR_$_CSSearchQuery._firstResultTime
+ _OBJC_IVAR_$_CSSearchQuery._hasReceivedFirstResult
+ _OBJC_IVAR_$_CSSearchQuery._l2RankingTime
+ _OBJC_IVAR_$_CSSearchQuery._queryParseEndTime
+ _OBJC_IVAR_$_CSSearchQuery._queryStartTime
+ _OBJC_IVAR_$_CSSearchQueryContext._isUnsafeQuery
+ _OBJC_IVAR_$_CSSearchQueryContext._ownerToken
+ _UTTypeCopyParentIdentifiers
+ ___21-[CSSearchQuery poll]_block_invoke.1170
+ ___34-[CSSearchConnection cancelQuery:]_block_invoke.1605
+ ___34-[CSSearchConnection cancelQuery:]_block_invoke.1605.cold.1
+ ___36-[CSSearchQuery processResultItems:]_block_invoke.1247
+ ___51-[CSSearchQuery _sendQueryAnalyticsEventWithError:]_block_invoke
+ ___54-[CSSearchQuery copyResultsFromPlist:protectionClass:]_block_invoke.1204
+ ___67+[CSSearchQuery fetchDonationProgressForBundles:completionHandler:]_block_invoke.1302
+ ___80-[CSSearchQuery filterMegadomePeopleSuggestions:isShortQuery:completionHandler:]_block_invoke.1216
+ ___assetPathForLocalizedKeywords_block_invoke
+ ___block_descriptor_40_e8_32s_e26_"NSMutableDictionary"8?0ls32l8
+ ___block_literal_global.1018
+ ___block_literal_global.1022
+ ___block_literal_global.1073
+ ___block_literal_global.1173
+ ___block_literal_global.1179
+ ___block_literal_global.1578
+ ___block_literal_global.1580
+ ___block_literal_global.1582
+ ___block_literal_global.1585
+ ___block_literal_global.1588
+ ___block_literal_global.1701
+ _assetPathForLocalizedKeywords
+ _assetPathForLocalizedKeywords.cold.1
+ _kUTTypeDirectory
+ _kUTTypeFolder
+ _kUTTypeItem
+ _mach_port_deallocate
+ _mach_task_self_
+ _objc_msgSend$_sendQueryAnalyticsEventWithError:
+ _objc_msgSend$_shouldEmitAnalyticsEvent
+ _objc_msgSend$isUnsafeQuery
+ _objc_msgSend$ownerToken
+ _objc_msgSend$rankBatch:withRanker:withBundle:maxCount:heapMaxCount:userQuery:queryID:rankingConfiguration:isCJK:clientBundle:isKeyboardCJK:privateQuery:collectL2Signals:onlyEmbeddingResults:
+ _objc_msgSend$setIsUnsafeQuery:
+ _objc_msgSend$setOwnerToken:
+ _objc_msgSend$updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:maxCount:
+ _task_create_identity_token
+ _xpc_dictionary_set_mach_send
- -[CSSearchQuery(TopHitRanking) rankBatch:withRanker:withBundle:maxCount:userQuery:queryID:rankingConfiguration:isCJK:clientBundle:isKeyboardCJK:privateQuery:collectL2Signals:onlyEmbeddingResults:]
- GCC_except_table301
- GCC_except_table315
- GCC_except_table323
- GCC_except_table328
- GCC_except_table337
- GCC_except_table338
- GCC_except_table341
- GCC_except_table350
- GCC_except_table354
- GCC_except_table356
- GCC_except_table432
- GCC_except_table433
- GCC_except_table434
- GCC_except_table435
- GCC_except_table479
- _NSLocaleLanguageCode
- _SSDefaultsGetAssetPathForLocalizedKeywords
- _SSDefaultsGetAssetPathForLocalizedKeywords.cold.1
- _UTTypeDirectory
- ___21-[CSSearchQuery poll]_block_invoke.1101
- ___34-[CSSearchConnection cancelQuery:]_block_invoke.1528
- ___34-[CSSearchConnection cancelQuery:]_block_invoke.1528.cold.1
- ___36-[CSSearchQuery processResultItems:]_block_invoke.1178
- ___54-[CSSearchQuery copyResultsFromPlist:protectionClass:]_block_invoke.1135
- ___67+[CSSearchQuery fetchDonationProgressForBundles:completionHandler:]_block_invoke.1233
- ___80-[CSSearchQuery filterMegadomePeopleSuggestions:isShortQuery:completionHandler:]_block_invoke.1147
- ___SSDefaultsGetAssetPathForLocalizedKeywords_block_invoke
- ___block_literal_global.1004
- ___block_literal_global.1008
- ___block_literal_global.1059
- ___block_literal_global.1104
- ___block_literal_global.1110
- ___block_literal_global.1502
- ___block_literal_global.1504
- ___block_literal_global.1506
- ___block_literal_global.1509
- ___block_literal_global.1512
- _objc_msgSend$_parentTypes
- _objc_msgSend$autoupdatingCurrentLocale
- _objc_msgSend$rankBatch:withRanker:withBundle:maxCount:userQuery:queryID:rankingConfiguration:isCJK:clientBundle:isKeyboardCJK:privateQuery:collectL2Signals:onlyEmbeddingResults:
- _objc_msgSend$updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJIZugATEuOG37tyocnHKROXT_9XKJiQQrSEavg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CJIZugATEuOG37tyocnHKROXT_9XKJiQQrSEavg/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
+ "@\"NSMutableDictionary\"8@?0"
+ "@108@0:8@16@24@32Q40q48@56q64@72B80@84B92B96B100B104"
+ "BundleID"
+ "Cancelled"
+ "Could not create owner token:%d"
+ "ErrorCode"
+ "FilterQueryLength"
+ "FoundDocs"
+ "L2RankingTime"
+ "MaxCount"
+ "MaxRankedCount"
+ "ProcessName"
+ "QoS"
+ "QueryParseTime"
+ "QueryStringLength"
+ "RankingQueryLength"
+ "T@\"NSNumber\",&,N,V_isUnsafeQuery"
+ "TimeToFinish"
+ "TimeToFirstResult"
+ "UserQueryLength"
+ "_firstResultTime"
+ "_hasReceivedFirstResult"
+ "_l2RankingTime"
+ "_ownerToken"
+ "_queryParseEndTime"
+ "_queryStartTime"
+ "_sendQueryAnalyticsEventWithError:"
+ "_shouldEmitAnalyticsEvent"
+ "com.apple.corespotlight.query"
+ "kCIMatchArray"
+ "ot"
+ "ownerToken"
+ "rankBatch:withRanker:withBundle:maxCount:heapMaxCount:userQuery:queryID:rankingConfiguration:isCJK:clientBundle:isKeyboardCJK:privateQuery:collectL2Signals:onlyEmbeddingResults:"
+ "setIsUnsafeQuery:"
+ "setOwnerToken:"
+ "updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:maxCount:"
- "/AppleInternal/Library/BuildRoots/4~CIU-ugDPXOyvdfYB_QAU87F_Ti_htSLbt3NKGrY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:429: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
- "/AppleInternal/Library/BuildRoots/4~CIU-ugDPXOyvdfYB_QAU87F_Ti_htSLbt3NKGrY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:486: libc++ Hardening assertion !empty() failed: vector::pop_back called on an empty vector\n"
- "@100@0:8@16@24@32Q40@48q56@64B72@76B84B88B92B96"
- "_parentTypes"
- "autoupdatingCurrentLocale"
- "rankBatch:withRanker:withBundle:maxCount:userQuery:queryID:rankingConfiguration:isCJK:clientBundle:isKeyboardCJK:privateQuery:collectL2Signals:onlyEmbeddingResults:"
- "updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:"

```
