## CoreSpotlight

> `/System/Library/Frameworks/CoreSpotlight.framework/Versions/A/CoreSpotlight`

```diff

-2333.22.13.7.0
-  __TEXT.__text: 0xe08f0
+2333.41.1.3.0
+  __TEXT.__text: 0xe1010
   __TEXT.__auth_stubs: 0x1ee0
-  __TEXT.__objc_methlist: 0xc870
+  __TEXT.__objc_methlist: 0xc868
   __TEXT.__const: 0xbb2
-  __TEXT.__gcc_except_tab: 0x2f9c
-  __TEXT.__cstring: 0x11fe2
-  __TEXT.__oslogstring: 0x6cd7
+  __TEXT.__gcc_except_tab: 0x2ff8
+  __TEXT.__cstring: 0x12092
+  __TEXT.__oslogstring: 0x6d05
   __TEXT.__dlopen_cstrs: 0x365
-  __TEXT.__ustring: 0x2c
+  __TEXT.__ustring: 0x3c
   __TEXT.__swift5_typeref: 0x2a0
   __TEXT.__swift5_reflstr: 0x77
   __TEXT.__swift5_assocty: 0x138

   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x34e8
+  __TEXT.__unwind_info: 0x3508
   __TEXT.__eh_frame: 0x1e8
   __TEXT.__objc_classname: 0x100d
-  __TEXT.__objc_methname: 0x1d4be
-  __TEXT.__objc_methtype: 0x20ea
-  __TEXT.__objc_stubs: 0xfe60
-  __DATA_CONST.__got: 0x7a8
-  __DATA_CONST.__const: 0x3578
+  __TEXT.__objc_methname: 0x1d511
+  __TEXT.__objc_methtype: 0x20fa
+  __TEXT.__objc_stubs: 0xfe80
+  __DATA_CONST.__got: 0x7b8
+  __DATA_CONST.__const: 0x3598
   __DATA_CONST.__objc_classlist: 0x468
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7610
+  __DATA_CONST.__objc_selrefs: 0x7620
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x340
-  __DATA_CONST.__objc_arraydata: 0xb88
+  __DATA_CONST.__objc_arraydata: 0xb98
   __AUTH_CONST.__auth_got: 0xf80
   __AUTH_CONST.__auth_ptr: 0x128
-  __AUTH_CONST.__const: 0x36b8
-  __AUTH_CONST.__cfstring: 0x11340
-  __AUTH_CONST.__objc_const: 0x12660
-  __AUTH_CONST.__objc_intobj: 0x750
+  __AUTH_CONST.__const: 0x36e8
+  __AUTH_CONST.__cfstring: 0x11420
+  __AUTH_CONST.__objc_const: 0x12648
+  __AUTH_CONST.__objc_intobj: 0x768
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__objc_arrayobj: 0x9c0
+  __AUTH_CONST.__objc_arrayobj: 0x9d8
   __AUTH.__objc_data: 0x1590
   __AUTH.__data: 0x3a0
   __DATA.__objc_ivar: 0xbb0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5537
-  Symbols:   12148
-  CStrings:  9510
+  Functions: 5541
+  Symbols:   12159
+  CStrings:  9518
 
Symbols:
+ +[CSPersonalAnswers personalAnswersEventIntentForQUOutput:isDebugLoggingEnabled:]
+ +[CSPersonalAnswers personalAnswersEventIntentForQUOutput:isDebugLoggingEnabled:].cold.1
+ -[CSGenerativeModelsAvailabilityManager _handleLocaleChange]
+ -[CSGenerativeModelsAvailabilityManager _statusForUseCase:]
+ -[CSSearchableIndex embeddingCompletenessForBundle:completion:]
+ -[NSMutableAttributedString(UserAttributedQueryString) _expandedDateFilter:withLocale:]
+ GCC_except_table355
+ GCC_except_table368
+ OBJC_IVAR_$_CSGenerativeModelsAvailabilityManager._cacheLock
+ OBJC_IVAR_$_CSGenerativeModelsAvailabilityManager._cachedStatuses
+ _CSGMUseCaseIdentifiers
+ _MDItemAppEntityTypeDisplayRepresentationName
+ _NSCurrentLocaleDidChangeNotification
+ _NSLocaleLanguageCode
+ __64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.488
+ __64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.728
+ __73-[CSSearchableIndex(SpotlightCache) issueCacheCommand:completionHandler:]_block_invoke.780
+ __94-[CSUserQuery filterContactPeopleSuggestions:cachedSuggestionsEmailToScope:completionHandler:]_block_invoke.775
+ ___63-[CSSearchableIndex embeddingCompletenessForBundle:completion:]_block_invoke
+ ___87-[NSMutableAttributedString(UserAttributedQueryString) _expandedDateFilter:withLocale:]_block_invoke
+ ___block_descriptor_56_e8_32s40r48r_e15_v32?08Q16^B24l
+ __block_literal_global.490
+ __block_literal_global.612
+ __block_literal_global.641
+ __block_literal_global.730
+ __block_literal_global.771
+ __block_literal_global.790
+ _objc_msgSend$_expandedDateFilter:withLocale:
+ _objc_msgSend$_statusForUseCase:
+ _objc_msgSend$autoupdatingCurrentLocale
+ _objc_msgSend$currentWithUseCaseIdentifiers:language:
+ _objc_msgSend$prepare
+ _objc_msgSend$updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:
+ _sIsColdStart
+ defaultSearchableIndex.onceToken.864
+ defaultSearchableIndex.sDefaultInstance.863
+ queryStringWithQueryContext:searchString:options:.onceAttributesToken.727
- +[CSPersonalAnswers personalAnswersEventIntentForQUOutput:]
- +[CSPersonalAnswers personalAnswersEventIntentForQUOutput:].cold.1
- -[CSGenerativeModelsAvailabilityManager .cxx_destruct]
- -[CSGenerativeModelsAvailabilityManager _isAvailableForUseCaseIdentifiers:]
- -[CSGenerativeModelsAvailabilityManager setUseCaseStatus:]
- -[CSGenerativeModelsAvailabilityManager useCaseStatus]
- GCC_except_table352
- GCC_except_table353
- OBJC_IVAR_$_CSGenerativeModelsAvailabilityManager._gmStatusQueue
- OBJC_IVAR_$_CSGenerativeModelsAvailabilityManager._useCaseStatus
- __64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.480
- __64-[CSUserQuery queryStringWithQueryContext:searchString:options:]_block_invoke.720
- __73-[CSSearchableIndex(SpotlightCache) issueCacheCommand:completionHandler:]_block_invoke.773
- __94-[CSUserQuery filterContactPeopleSuggestions:cachedSuggestionsEmailToScope:completionHandler:]_block_invoke.767
- __OBJC_$_PROP_LIST_CSGenerativeModelsAvailabilityManager
- __block_literal_global.482
- __block_literal_global.604
- __block_literal_global.633
- __block_literal_global.722
- __block_literal_global.764
- __block_literal_global.783
- _objc_msgSend$_isAvailableForUseCaseIdentifiers:
- _objc_msgSend$currentWithUseCaseIdentifiers:
- _objc_msgSend$setUseCaseStatus:
- _objc_msgSend$updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:
- _objc_msgSend$useCaseStatus
- defaultSearchableIndex.onceToken.850
- defaultSearchableIndex.sDefaultInstance.849
- queryStringWithQueryContext:searchString:options:.onceAttributesToken.719
CStrings:
+ "(_kMDItemContentCreationDateDay=%ld)"
+ "(_kMDItemContentCreationDateMonth=%ld && _kMDItemContentCreationDateDay=%ld)"
+ "[3i]"
+ "[GMS] received locale did change notification"
+ "_cacheLock"
+ "_cachedStatuses"
+ "_expandedDateFilter:withLocale:"
+ "_handleLocaleChange"
+ "_kMDItemAppEntityTypeDisplayRepresentationName"
+ "_statusForUseCase:"
+ "autoupdatingCurrentLocale"
+ "com.apple.Settings.AppleIntelligence"
+ "currentWithUseCaseIdentifiers:language:"
+ "embeddingCompleteness"
+ "embeddingCompletenessForBundle:completion:"
+ "kMDQueryOptionColdStartPhotosECRTimeout"
+ "personalAnswersEventIntentForQUOutput:isDebugLoggingEnabled:"
+ "q24@0:8Q16"
+ "u2Enabled"
+ "updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:isDocumentSearch:"
+ "useLLMParse"
- "SearchToolDebugMode"
- "T@\"NSDictionary\",&,V_useCaseStatus"
- "_gmStatusQueue"
- "_isAvailableForUseCaseIdentifiers:"
- "_useCaseStatus"
- "com.apple.spotlight.semanticSearch"
- "currentWithUseCaseIdentifiers:"
- "kMDMDItemKeyphraseVersion"
- "kMDQueryOptionU2EnabledKey"
- "personalAnswersEventIntentForQUOutput:"
- "setUseCaseStatus:"
- "updateScoresForItems:withSectionBundle:userQuery:queryID:currentTime:collectL2Signals:keyboardLanguage:onlyEmbeddingResults:isCardSearch:"
- "useCaseStatus"

```
