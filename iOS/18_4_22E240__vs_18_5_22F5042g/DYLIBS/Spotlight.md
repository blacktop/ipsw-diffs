## Spotlight

> `/System/Library/PrivateFrameworks/Spotlight.framework/Spotlight`

```diff

-2333.22.13.0.3
-  __TEXT.__text: 0x4f6dc
-  __TEXT.__auth_stubs: 0x1040
-  __TEXT.__objc_methlist: 0x1fcc
-  __TEXT.__const: 0x170
-  __TEXT.__gcc_except_tab: 0x46cc
-  __TEXT.__oslogstring: 0x2197
-  __TEXT.__cstring: 0x284b
-  __TEXT.__unwind_info: 0xbf0
+2333.41.0.1.0
+  __TEXT.__text: 0x516ec
+  __TEXT.__auth_stubs: 0x1050
+  __TEXT.__objc_methlist: 0x1fec
+  __TEXT.__const: 0x180
+  __TEXT.__gcc_except_tab: 0x4b20
+  __TEXT.__cstring: 0x294f
+  __TEXT.__oslogstring: 0x2526
+  __TEXT.__unwind_info: 0xc18
   __TEXT.__eh_frame: 0x60
   __TEXT.__objc_classname: 0x231
-  __TEXT.__objc_methname: 0x9255
-  __TEXT.__objc_methtype: 0x1e27
-  __TEXT.__objc_stubs: 0x8880
-  __DATA_CONST.__got: 0x12d0
-  __DATA_CONST.__const: 0xb70
+  __TEXT.__objc_methname: 0x930b
+  __TEXT.__objc_methtype: 0x1e35
+  __TEXT.__objc_stubs: 0x8900
+  __DATA_CONST.__got: 0x12f0
+  __DATA_CONST.__const: 0xbc0
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2798
+  __DATA_CONST.__objc_selrefs: 0x27b8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x3c8
-  __AUTH_CONST.__auth_got: 0x838
-  __AUTH_CONST.__const: 0x6c8
-  __AUTH_CONST.__cfstring: 0x2960
-  __AUTH_CONST.__objc_const: 0x3730
+  __AUTH_CONST.__auth_got: 0x840
+  __AUTH_CONST.__const: 0x688
+  __AUTH_CONST.__cfstring: 0x2b00
+  __AUTH_CONST.__objc_const: 0x3750
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH.__objc_data: 0xa0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x394
-  __DATA.__data: 0x298
-  __DATA.__bss: 0xa8
+  __DATA.__objc_ivar: 0x398
+  __DATA.__data: 0x280
+  __DATA.__bss: 0xf8
   __DATA_DIRTY.__objc_data: 0x640
-  __DATA_DIRTY.__data: 0x21
-  __DATA_DIRTY.__bss: 0x428
+  __DATA_DIRTY.__data: 0x11
+  __DATA_DIRTY.__bss: 0x408
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 934
-  Symbols:   1870
-  CStrings:  2445
+  Functions: 939
+  Symbols:   1881
+  CStrings:  2470
 
Symbols:
+ _LLMQUIntentDocument
+ _MDItemAppEntityTypeDisplayRepresentationName
+ _MDItemIsFromMe
+ _OBJC_CLASS_$_SFFormattedText
+ _SSEnableSearchToolDebugMode
+ __Z13printHeapInfoyRKNSt3__16vectorI17SPResultValueItemNS_9allocatorIS1_EEEEiP8NSStringb
+ __Z23isSearchToolDebugModeOnv
+ __Z25canLogIdentifierForBundleP8NSString
+ _rankingAttributeIndexForName
- _SSEnableSearchToolCleanSlate
- __Z13printHeapInfoyRKNSt3__16vectorI17SPResultValueItemNS_9allocatorIS1_EEEEP8NSStringb
CStrings:
+ "\x03\x11\x11\xf0*\x11\x142\x111!"
+ " %@"
+ "(kMDItemDisableSearchInSpotlight!=1 || _kMDItemBundleID=%@)"
+ "B28@0:8@16B24"
+ "Timeout fetching additional attributes for %@ in %@."
+ "[Mail Attachment] could not fetch all attributes. Related items: %lu. Attributes fetched: %lu"
+ "[Mail Attachment] removed result:%@"
+ "[Mail Attachment] timed out fetching attributes for pc:%@."
+ "[SpotlightRanking]<_resultHeaps>: %@ queue: %p, bundle = %@, item = %@, retrievalType = %@ containerId = %@, score: (sparseScore: %f denseScore: %f, hybridScore: %f, timestamp: %f)"
+ "[SpotlightRanking]<_resultHeaps>: %@ queue: %p, bundle = %@, item = %@, retrievalType = %@ containerId = (%@, %lu), score: (sparseScore: %f denseScore: %f, hybridScore: %f, timestamp: %f)"
+ "[SpotlightRanking]<_resultHeaps>: %@ queue: %p, bundle = %@, item = %lu, retrievalType = %@ containerId = %@, score: (sparseScore: %f denseScore: %f, hybridScore: %f, timestamp: %f)"
+ "[SpotlightRanking]<_resultHeaps>: %@ queue: %p, bundle = %@, item = %lu, retrievalType = %@ containerId = (%@, %lu), score: (sparseScore: %f denseScore: %f, hybridScore: %f, timestamp: %f)"
+ "[SpotlightRanking]<_resultHeaps>: queue: %p, bundle = %@, item = %lu has nil container id"
+ "_makeUniqueFetchAttributesWithAttributes:extraAttributes:slowFetchAttributeSet:"
+ "_slowFetchAttrs"
+ "add item"
+ "add to hashtable"
+ "attrHasPhotosAlbumMemoryResult:isSearchToolClient:"
+ "cannot put newEntry to RecencyTables "
+ "cannot put oldEntry to RecencyTables"
+ "descriptionFromEntityType:displayName:"
+ "ignoreFutureDates"
+ "ignorePastDates"
+ "inferredLlmQUIntentType"
+ "logSections:prefix:queryId:query:isSearchToolClient:"
+ "memories"
+ "personalAnswersEventIntentForQUOutput:isDebugLoggingEnabled:"
+ "photo"
+ "rectangle.stack.fill"
+ "resolveDatesInFuture"
+ "resolveDatesInPast"
+ "sendTTRLogsWithSections:queryContext:isCommittedSearch:parsecCameLaterThanSRT:"
+ "setFormattedTextPieces:"
+ "setGlyph:"
+ "slowFetchAttributes:"
+ "updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:isDocumentSearch:"
+ "v32@?0@\"SPSearchTopHitResult\"8Q16^B24"
- "\x03\x11\x11\xf0*\x11\x13B\x111!"
- "*warn* Could not fetch all related item attributes for mail attachments. Related items: %lu. Attributes fetched: %lu"
- "===^^ RANKING 4 Mail higher ranked replaced"
- "SearchToolCleanSlateDenseRetrieval"
- "SearchToolRanking"
- "_makeUniqueFetchAttributesWithAttributes:extraAttributes:"
- "allBundleIDsUsingPommesRankingSearchTool"
- "attrHasPhotosAlbumMemoryResult:"
- "logSections:prefix:queryId:query:"
- "personalAnswersEventIntentForQUOutput:"
- "sendTTRLogsWithSections:searchString:queryKind:isCommittedSearch:parsecCameLaterThanSRT:"
- "updateScoresForPreparedItems:isCJK:clientBundleID:thresholdValue:queryNodeMatchInfo:collectL2Signals:isCardSearch:"

```
