## MailSupport

> `/System/Library/PrivateFrameworks/MailSupport.framework/MailSupport`

```diff

-3853.100.6.2.6
-  __TEXT.__text: 0x1a7e8
+3856.100.4.0.0
+  __TEXT.__text: 0x1b054
   __TEXT.__auth_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x1838
-  __TEXT.__gcc_except_tab: 0x2b00
-  __TEXT.__cstring: 0x49ce
-  __TEXT.__const: 0x39c
+  __TEXT.__objc_methlist: 0x1888
+  __TEXT.__gcc_except_tab: 0x2be0
+  __TEXT.__cstring: 0x4a8e
+  __TEXT.__const: 0x3ac
   __TEXT.__oslogstring: 0x736
-  __TEXT.__dlopen_cstrs: 0xd4
+  __TEXT.__dlopen_cstrs: 0x132
   __TEXT.__ustring: 0x18
   __TEXT.__swift5_typeref: 0x242
   __TEXT.__constg_swiftt: 0x60
-  __TEXT.__swift5_reflstr: 0xe7
-  __TEXT.__swift5_fieldmd: 0xbc
+  __TEXT.__swift5_reflstr: 0xf2
+  __TEXT.__swift5_fieldmd: 0xc8
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_capture: 0x48
-  __TEXT.__unwind_info: 0xd88
-  __TEXT.__objc_classname: 0x650
-  __TEXT.__objc_methname: 0x5710
-  __TEXT.__objc_methtype: 0x85c
-  __TEXT.__objc_stubs: 0x3be0
+  __TEXT.__unwind_info: 0xde8
+  __TEXT.__objc_classname: 0x64d
+  __TEXT.__objc_methname: 0x599b
+  __TEXT.__objc_methtype: 0x8a2
+  __TEXT.__objc_stubs: 0x3d20
   __DATA_CONST.__got: 0x4e0
-  __DATA_CONST.__const: 0x1318
+  __DATA_CONST.__const: 0x12f8
   __DATA_CONST.__objc_classlist: 0x1a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1520
+  __DATA_CONST.__objc_selrefs: 0x1580
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x5c0
   __AUTH_CONST.__const: 0x4d0
   __AUTH_CONST.__cfstring: 0x49c0
-  __AUTH_CONST.__objc_const: 0x3fe0
+  __AUTH_CONST.__objc_const: 0x4058
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x180
-  __DATA.__objc_ivar: 0x1a4
+  __DATA.__objc_ivar: 0x1ac
   __DATA.__data: 0x5d0
-  __DATA.__bss: 0x468
+  __DATA.__bss: 0x478
   __DATA_DIRTY.__objc_data: 0xf00
   __DATA_DIRTY.__data: 0x1b8
   __DATA_DIRTY.__bss: 0x190

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EBBBDEDE-2EA9-3F2E-A946-D79DF3B14176
-  Functions: 665
-  Symbols:   3103
-  CStrings:  2396
+  UUID: 843B1600-BEC8-3EE0-A744-224AA97EB2D5
+  Functions: 675
+  Symbols:   3135
+  CStrings:  2421
 
Symbols:
+ +[MSParsecSearchSessionMessageResult resultWithIdentifier:date:mailRankingSignals:]
+ +[MSParsecSearchSessionMessageResult resultWithIdentifier:mailRankingSignals:]
+ -[MSParsecSearchSession reportLocalSearchEnded:hasEmbeddingResults:hasKeywordResults:]
+ -[MSParsecSearchSession reportMessageListResultsFetched:isSemanticSearchFeedback:hasEmbeddingResults:hasKeywordResults:isFinished:]
+ -[MSParsecSearchSessionMessageResult initResultWithIdentifier:date:mailRankingSignals:]
+ -[MSParsecSearchSessionMessageResult mailRankingSignalForMessageList]
+ -[MSParsecSearchSessionSuggestion mailRankingSignalForMessageList]
+ GCC_except_table51
+ GCC_except_table52
+ GCC_except_table54
+ _OBJC_IVAR_$_MSParsecSearchSessionMessageResult._mailRankingSignalForMessageList
+ _OBJC_IVAR_$_MSParsecSearchSessionSuggestion._mailRankingSignalForMessageList
+ _SearchFoundationLibrary
+ _SearchFoundationLibraryCore.frameworkLibrary
+ ___SearchFoundationLibraryCore_block_invoke
+ ___getSFEmbeddingStateClass_block_invoke
+ ___getSFQueryUnderstandingParseClass_block_invoke
+ _audit_stringSearchFoundation
+ _getSFEmbeddingStateClass.softClass
+ _getSFQueryUnderstandingParseClass.softClass
+ _objc_msgSend$initResultWithIdentifier:date:mailRankingSignals:
+ _objc_msgSend$initWithStartSearch:queryUnderstandingParse:l1ToL2ResultCount:coreSpotlightIndexCount:embeddingState:
+ _objc_msgSend$mailRankingSignalForMessageList
+ _objc_msgSend$reportLocalSearchEnded:hasEmbeddingResults:hasKeywordResults:
+ _objc_msgSend$setHasEmbeddingResults:
+ _objc_msgSend$setHasHybridResults:
+ _objc_msgSend$setHasKeywordResults:
+ _objc_msgSend$setHasQueryEmbedding:
+ _objc_msgSend$setHasResults:
+ _objc_msgSend$setHasSuppressedResults:
+ _objc_msgSend$setIsSemanticSearchEligible:
+ _objc_msgSend$setQueryStatus:
- -[MSParsecSearchSession reportLocalSearchEnded]
- -[MSParsecSearchSession reportMessageListResultsFetched:isFinished:]
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_MailSupport
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_MailSupport
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_MailSupport
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_MailSupport
- _objc_msgSend$initWithStartSearch:
- _objc_msgSend$reportLocalSearchEnded
CStrings:
+ "@\"SFMailRankingSignals\"16@0:8"
+ "Class getSFEmbeddingStateClass(void)_block_invoke"
+ "Class getSFQueryUnderstandingParseClass(void)_block_invoke"
+ "LiveSearch"
+ "SFEmbeddingState"
+ "SFQueryUnderstandingParse"
+ "T@\"SFMailRankingSignals\",R,N"
+ "T@\"SFMailRankingSignals\",R,N,V_mailRankingSignalForMessageList"
+ "_mailRankingSignalForMessageList"
+ "initResultWithIdentifier:date:mailRankingSignals:"
+ "initWithStartSearch:queryUnderstandingParse:l1ToL2ResultCount:coreSpotlightIndexCount:embeddingState:"
+ "mailRankingSignalForMessageList"
+ "reportLocalSearchEnded:hasEmbeddingResults:hasKeywordResults:"
+ "reportMessageListResultsFetched:isSemanticSearchFeedback:hasEmbeddingResults:hasKeywordResults:isFinished:"
+ "resultWithIdentifier:date:mailRankingSignals:"
+ "resultWithIdentifier:mailRankingSignals:"
+ "setHasEmbeddingResults:"
+ "setHasHybridResults:"
+ "setHasKeywordResults:"
+ "setHasQueryEmbedding:"
+ "setHasResults:"
+ "setHasSuppressedResults:"
+ "setIsSemanticSearchEligible:"
+ "setQueryStatus:"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation"
+ "v28@0:8B16B20B24"
+ "v40@0:8@16B24B28B32B36"
+ "void *SearchFoundationLibrary(void)"
- "initWithStartSearch:"
- "reportLocalSearchEnded"
- "reportMessageListResultsFetched:isFinished:"

```
