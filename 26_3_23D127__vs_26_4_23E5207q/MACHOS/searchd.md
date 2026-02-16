## searchd

> `/System/Library/PrivateFrameworks/Search.framework/searchd`

```diff

-2400.22.0.0.0
-  __TEXT.__text: 0x61dd4
-  __TEXT.__auth_stubs: 0x1870
-  __TEXT.__objc_stubs: 0xa7a0
-  __TEXT.__objc_methlist: 0x2af4
-  __TEXT.__const: 0x21c
-  __TEXT.__cstring: 0x50ea
-  __TEXT.__objc_methname: 0xaea1
-  __TEXT.__objc_classname: 0x46b
-  __TEXT.__objc_methtype: 0x1818
-  __TEXT.__oslogstring: 0x35a3
-  __TEXT.__gcc_except_tab: 0x5428
-  __TEXT.__unwind_info: 0xea0
-  __DATA_CONST.__auth_got: 0xc50
-  __DATA_CONST.__got: 0x1180
+2418.4.8.2.100
+  __TEXT.__text: 0x65e0c
+  __TEXT.__auth_stubs: 0x1860
+  __TEXT.__objc_stubs: 0xa7c0
+  __TEXT.__objc_methlist: 0x2b1c
+  __TEXT.__const: 0x23c
+  __TEXT.__cstring: 0x51ad
+  __TEXT.__objc_methname: 0xae9a
+  __TEXT.__objc_classname: 0x47c
+  __TEXT.__objc_methtype: 0x1811
+  __TEXT.__oslogstring: 0x363a
+  __TEXT.__gcc_except_tab: 0x5438
+  __TEXT.__unwind_info: 0xfe0
+  __DATA_CONST.__auth_got: 0xc48
+  __DATA_CONST.__got: 0x1198
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x1f60
-  __DATA_CONST.__cfstring: 0x49c0
-  __DATA_CONST.__objc_classlist: 0x120
+  __DATA_CONST.__const: 0x1f88
+  __DATA_CONST.__cfstring: 0x4aa0
+  __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_arrayobj: 0x120
-  __DATA.__objc_const: 0x7ca0
+  __DATA.__objc_const: 0x7d08
   __DATA.__objc_selrefs: 0x3008
-  __DATA.__objc_ivar: 0x388
-  __DATA.__objc_data: 0xb40
+  __DATA.__objc_ivar: 0x384
+  __DATA.__objc_data: 0xb90
   __DATA.__data: 0x670
-  __DATA.__bss: 0x778
+  __DATA.__bss: 0x788
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/MetadataUtilities.framework/MetadataUtilities
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
-  - /System/Library/PrivateFrameworks/MobileSpotlightIndex.framework/MobileSpotlightIndex
   - /System/Library/PrivateFrameworks/People.framework/People
   - /System/Library/PrivateFrameworks/PersonalizationPortrait.framework/PersonalizationPortrait
   - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore

   - /System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SpotlightDaemon.framework/SpotlightDaemon
+  - /System/Library/PrivateFrameworks/SpotlightIndex.framework/SpotlightIndex
   - /System/Library/PrivateFrameworks/SpotlightRecommendation.framework/SpotlightRecommendation
   - /System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources
   - /System/Library/PrivateFrameworks/SpotlightServices.framework/SpotlightServices

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AA693949-E192-37F0-B167-B9325EDC8569
-  Functions: 1218
+  UUID: D353F430-037C-3A00-B089-CDA880B4D942
+  Functions: 1239
   Symbols:   968
-  CStrings:  3934
+  CStrings:  3948
 
Symbols:
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_SSSearchToolRankingManager
+ _SSEnableSearchToolCerberus
+ _SSQueryParseResultsForCerberusQuery
+ _UTTypeAudio
+ _UTTypeAudiovisualContent
+ _UTTypeCalendarEvent
+ _UTTypeContact
+ _UTTypeContent
+ _UTTypeImage
+ _UTTypeMessage
+ _UTTypeMovie
+ _UTTypePlaylist
+ _UTTypeToDoItem
+ _UTTypeVideo
+ _getenv
+ _objc_retain_x11
- _kUTTypeAudio
- _kUTTypeAudiovisualContent
- _kUTTypeCalendarEvent
- _kUTTypeContact
- _kUTTypeContent
- _kUTTypeImage
- _kUTTypeMessage
- _kUTTypeMovie
- _kUTTypePlaylist
- _kUTTypeToDoItem
- _kUTTypeVideo
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x4
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "@52@0:8d16@24@32B40^@44"
+ "CS_INDEX_PATH"
+ "CoreSpotlight"
+ "NSUserActivity from DocumentManager"
+ "No title for (non-Photos) CoreSpotlight result"
+ "TestSDController"
+ "[ParsecQuery] failed to create a local copy for %{private}@ because of \"%@\""
+ "[SpotlightRanking] Skipping (nil) item %{private}@ from %@ because of \"%@\""
+ "app result disabled"
+ "com.apple.searchtoold"
+ "failed to create a CoreSpotlight result"
+ "isEventIntentForQueryUnderstandingOutput:isSearchToolClient:isSearchToolCerberus:"
+ "isInstantAnswerTriggerQuery:isCJK:isSearchToolClient:"
+ "missing ClientData"
+ "processSections:queryContext:"
+ "resultWithTime:queryContext:searchString:isCorrectedQuery:error:"
+ "supportsApplicationIndexing"
+ "testIndex"
- "@44@0:8d16@24B32@36"
- "ClientTopHitRank"
- "Tq,N,V_startedOnce"
- "_startedOnce"
- "isInstantAnswerTriggerQuery:isCJK:isSearchTool:"
- "personalAnswersEventIntentForQUOutput:isDebugLoggingEnabled:"
- "processSearchToolFinalResults:queryContext:"
- "resultWithTime:searchString:isCorrectedQuery:withQueryContext:"
- "setStartedOnce:"
- "startedOnce"
- "v24@0:8q16"

```
