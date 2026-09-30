## MailSupport

> `/System/Library/PrivateFrameworks/MailSupport.framework/MailSupport`

```diff

-3858.100.10.2.1
-  __TEXT.__text: 0x19440
+3860.100.5.2.1
+  __TEXT.__text: 0x18bdc
   __TEXT.__auth_stubs: 0xb00
-  __TEXT.__objc_methlist: 0x1828
-  __TEXT.__gcc_except_tab: 0x26fc
-  __TEXT.__cstring: 0x486e
+  __TEXT.__objc_methlist: 0x17d8
+  __TEXT.__gcc_except_tab: 0x261c
+  __TEXT.__cstring: 0x47ae
   __TEXT.__const: 0x39c
   __TEXT.__oslogstring: 0x4a6
-  __TEXT.__dlopen_cstrs: 0x132
+  __TEXT.__dlopen_cstrs: 0xd4
   __TEXT.__ustring: 0x18
   __TEXT.__swift5_typeref: 0x242
   __TEXT.__constg_swiftt: 0x60

   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_capture: 0x48
-  __TEXT.__unwind_info: 0xda8
-  __TEXT.__objc_classname: 0x629
-  __TEXT.__objc_methname: 0x56f2
-  __TEXT.__objc_methtype: 0x897
-  __TEXT.__objc_stubs: 0x38a0
+  __TEXT.__unwind_info: 0xd50
+  __TEXT.__objc_classname: 0x62c
+  __TEXT.__objc_methname: 0x5467
+  __TEXT.__objc_methtype: 0x851
+  __TEXT.__objc_stubs: 0x3760
   __DATA_CONST.__got: 0x4b0
   __DATA_CONST.__const: 0x1288
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1460
+  __DATA_CONST.__objc_selrefs: 0x1400
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x590
   __AUTH_CONST.__const: 0x4d0
   __AUTH_CONST.__cfstring: 0x4500
-  __AUTH_CONST.__objc_const: 0x3fc8
+  __AUTH_CONST.__objc_const: 0x3f50
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x180
-  __DATA.__objc_ivar: 0x1ac
+  __DATA.__objc_ivar: 0x1a4
   __DATA.__data: 0x5d0
-  __DATA.__bss: 0x478
+  __DATA.__bss: 0x468
   __DATA_DIRTY.__objc_data: 0xeb0
   __DATA_DIRTY.__data: 0x1b8
   __DATA_DIRTY.__bss: 0x180

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A9D36C16-D44D-3779-A45C-488F5F8C45B8
-  Functions: 664
-  Symbols:   3051
-  CStrings:  2297
+  UUID: AD6FB8B8-686C-3510-9885-8C5B3AD93399
+  Functions: 655
+  Symbols:   3011
+  CStrings:  2273
 
Symbols:
+ -[MSParsecSearchSession reportLocalSearchEnded]
+ -[MSParsecSearchSession reportMessageListResultsFetched:isFinished:]
+ _objc_msgSend$initWithStartSearch:
+ _objc_msgSend$reportLocalSearchEnded
- +[MSParsecSearchSessionMessageResult resultWithIdentifier:date:mailRankingSignals:]
- +[MSParsecSearchSessionMessageResult resultWithIdentifier:mailRankingSignals:]
- -[MSParsecSearchSession reportLocalSearchEnded:hasEmbeddingResults:hasKeywordResults:]
- -[MSParsecSearchSession reportMessageListResultsFetched:isSemanticSearchFeedback:hasEmbeddingResults:hasKeywordResults:isFinished:]
- -[MSParsecSearchSessionMessageResult initResultWithIdentifier:date:mailRankingSignals:]
- -[MSParsecSearchSessionMessageResult mailRankingSignalForMessageList]
- -[MSParsecSearchSessionSuggestion mailRankingSignalForMessageList]
- GCC_except_table51
- GCC_except_table52
- GCC_except_table54
- _OBJC_IVAR_$_MSParsecSearchSessionMessageResult._mailRankingSignalForMessageList
- _OBJC_IVAR_$_MSParsecSearchSessionSuggestion._mailRankingSignalForMessageList
- _SearchFoundationLibrary
- _SearchFoundationLibraryCore.frameworkLibrary
- ___SearchFoundationLibraryCore_block_invoke
- ___getSFEmbeddingStateClass_block_invoke
- ___getSFQueryUnderstandingParseClass_block_invoke
- _audit_stringSearchFoundation
- _getSFEmbeddingStateClass.softClass
- _getSFQueryUnderstandingParseClass.softClass
- _objc_msgSend$initResultWithIdentifier:date:mailRankingSignals:
- _objc_msgSend$initWithStartSearch:queryUnderstandingParse:l1ToL2ResultCount:coreSpotlightIndexCount:embeddingState:
- _objc_msgSend$mailRankingSignalForMessageList
- _objc_msgSend$reportLocalSearchEnded:hasEmbeddingResults:hasKeywordResults:
- _objc_msgSend$setHasEmbeddingResults:
- _objc_msgSend$setHasHybridResults:
- _objc_msgSend$setHasKeywordResults:
- _objc_msgSend$setHasQueryEmbedding:
- _objc_msgSend$setHasResults:
- _objc_msgSend$setHasSuppressedResults:
- _objc_msgSend$setIsSemanticSearchEligible:
- _objc_msgSend$setQueryStatus:
CStrings:
+ "initWithStartSearch:"
+ "reportLocalSearchEnded"
+ "reportMessageListResultsFetched:isFinished:"
- "@\"SFMailRankingSignals\"16@0:8"
- "Class getSFEmbeddingStateClass(void)_block_invoke"
- "Class getSFQueryUnderstandingParseClass(void)_block_invoke"
- "SFEmbeddingState"
- "SFQueryUnderstandingParse"
- "T@\"SFMailRankingSignals\",R,N"
- "T@\"SFMailRankingSignals\",R,N,V_mailRankingSignalForMessageList"
- "_mailRankingSignalForMessageList"
- "initResultWithIdentifier:date:mailRankingSignals:"
- "initWithStartSearch:queryUnderstandingParse:l1ToL2ResultCount:coreSpotlightIndexCount:embeddingState:"
- "mailRankingSignalForMessageList"
- "reportLocalSearchEnded:hasEmbeddingResults:hasKeywordResults:"
- "reportMessageListResultsFetched:isSemanticSearchFeedback:hasEmbeddingResults:hasKeywordResults:isFinished:"
- "resultWithIdentifier:date:mailRankingSignals:"
- "resultWithIdentifier:mailRankingSignals:"
- "setHasEmbeddingResults:"
- "setHasHybridResults:"
- "setHasKeywordResults:"
- "setHasQueryEmbedding:"
- "setHasResults:"
- "setHasSuppressedResults:"
- "setIsSemanticSearchEligible:"
- "setQueryStatus:"
- "softlink:r:path:/System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation"
- "v28@0:8B16B20B24"
- "v40@0:8@16B24B28B32B36"
- "void *SearchFoundationLibrary(void)"

```
