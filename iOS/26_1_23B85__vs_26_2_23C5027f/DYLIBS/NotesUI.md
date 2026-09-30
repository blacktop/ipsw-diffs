## NotesUI

> `/System/Library/PrivateFrameworks/NotesUI.framework/NotesUI`

```diff

-2952.40.13.0.0
-  __TEXT.__text: 0x2a1724
-  __TEXT.__auth_stubs: 0x6110
+2952.60.3.0.0
+  __TEXT.__text: 0x2a23b0
+  __TEXT.__auth_stubs: 0x6130
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0x598
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x16b18
+  __TEXT.__objc_methlist: 0x16be8
   __TEXT.__const: 0xa004
-  __TEXT.__cstring: 0x16aa9
-  __TEXT.__oslogstring: 0x957c
-  __TEXT.__gcc_except_tab: 0x4ab0
+  __TEXT.__cstring: 0x16b19
+  __TEXT.__oslogstring: 0x958c
+  __TEXT.__gcc_except_tab: 0x4b00
   __TEXT.__ustring: 0x139be
   __TEXT.__constg_swiftt: 0x3870
   __TEXT.__swift5_typeref: 0xcd2a

   __TEXT.__swift_as_ret: 0x108
   __TEXT.__swift5_protos: 0x24
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x9818
+  __TEXT.__unwind_info: 0x9860
   __TEXT.__eh_frame: 0x47b8
   __TEXT.__objc_classname: 0x2940
-  __TEXT.__objc_methname: 0x47d32
-  __TEXT.__objc_methtype: 0x9380
-  __TEXT.__objc_stubs: 0x2ce40
+  __TEXT.__objc_methname: 0x48020
+  __TEXT.__objc_methtype: 0x93e4
+  __TEXT.__objc_stubs: 0x2d0c0
   __DATA_CONST.__got: 0x2d98
-  __DATA_CONST.__const: 0x6310
+  __DATA_CONST.__const: 0x6318
   __DATA_CONST.__objc_classlist: 0xa90
   __DATA_CONST.__objc_catlist: 0x2b0
   __DATA_CONST.__objc_catlist2: 0x10
   __DATA_CONST.__objc_protolist: 0x3b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfa98
+  __DATA_CONST.__objc_selrefs: 0xfb60
   __DATA_CONST.__objc_protorefs: 0x168
   __DATA_CONST.__objc_superrefs: 0x688
   __DATA_CONST.__objc_arraydata: 0x318
-  __AUTH_CONST.__auth_got: 0x30a8
-  __AUTH_CONST.__const: 0x9b00
-  __AUTH_CONST.__cfstring: 0xbd60
-  __AUTH_CONST.__objc_const: 0x239f8
+  __AUTH_CONST.__auth_got: 0x30b8
+  __AUTH_CONST.__const: 0x9b40
+  __AUTH_CONST.__cfstring: 0xbda0
+  __AUTH_CONST.__objc_const: 0x23ac8
   __AUTH_CONST.__objc_arrayobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x660
   __AUTH_CONST.__objc_doubleobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x3de8
   __AUTH.__data: 0x19c8
-  __DATA.__objc_ivar: 0x11ec
-  __DATA.__data: 0x58ec
+  __DATA.__objc_ivar: 0x11f8
+  __DATA.__data: 0x58fc
   __DATA.__objc_stublist: 0x28
-  __DATA.__bss: 0x48e0
+  __DATA.__bss: 0x4920
   __DATA.__common: 0x50
   __DATA_DIRTY.__objc_data: 0x3fb8
   __DATA_DIRTY.__data: 0x2140

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CBED7EA6-7255-347D-A6E0-6E7BF3518AD9
-  Functions: 14387
-  Symbols:   31499
-  CStrings:  16691
+  UUID: DEA90D4B-5C80-3C95-B0BA-B5583C443192
+  Functions: 14411
+  Symbols:   31590
+  CStrings:  16731
 
Symbols:
+ +[ICCoreDataIndexer indexerCount]
+ -[ICAttachmentBrickView inDidFailFetchingMetadataNotification]
+ -[ICAttachmentBrickView setInDidFailFetchingMetadataNotification:]
+ -[ICCoreDataIndexer dealloc]
+ -[ICCoreDataIndexer setStopIndexing:]
+ -[ICCoreDataIndexer setStopIndexingToken:]
+ -[ICCoreDataIndexer stopIndexingToken]
+ -[ICCoreDataIndexer stopIndexing]
+ -[ICNote(UI) _delayedSave]
+ -[ICNote(UI) lastSaveDuration]
+ -[ICNote(UI) saveDelayDebounceTime]
+ -[ICNote(UI) saveDelayDebounceTime].cold.1
+ -[ICNote(UI) saveDelayMaxTime]
+ -[ICNote(UI) saveDelayMaxTime].cold.1
+ -[ICNote(UI) saveDelayerNoCreate]
+ -[ICNote(UI) saveDelayer]
+ -[ICNote(UI) save].cold.3
+ -[ICNote(UI) setLastSaveDuration:]
+ -[ICTTTextContentStorage rangeForParagraphID:]
+ GCC_except_table115
+ GCC_except_table117
+ GCC_except_table119
+ GCC_except_table126
+ GCC_except_table128
+ GCC_except_table132
+ GCC_except_table147
+ GCC_except_table172
+ GCC_except_table173
+ GCC_except_table174
+ _ICCoreDataIndexerStopIndexingNotification
+ _ICMachTimeToSeconds
+ _OBJC_IVAR_$_ICAttachmentBrickView._inDidFailFetchingMetadataNotification
+ _OBJC_IVAR_$_ICCoreDataIndexer._stopIndexing
+ _OBJC_IVAR_$_ICCoreDataIndexer._stopIndexingToken
+ __OBJC_$_CLASS_METHODS_ICCoreDataIndexer
+ __OBJC_$_CLASS_PROP_LIST_ICCoreDataIndexer
+ ___26-[ICNote(UI) _delayedSave]_block_invoke
+ ___30-[ICNote(UI) saveDelayMaxTime]_block_invoke
+ ___35-[ICNote(UI) saveDelayDebounceTime]_block_invoke
+ ___39-[ICNote(UI) airDropActivityItemSource]_block_invoke.82
+ ___46-[ICTTTextContentStorage rangeForParagraphID:]_block_invoke
+ ___51-[ICNote(UI) filterAttachmentsInTextStorage:range:]_block_invoke.281
+ ___83-[ICCoreDataIndexer initWithLegacyManagedObjectContext:modernManagedObjectContext:]_block_invoke
+ ___block_literal_global.1023
+ ___block_literal_global.243
+ ___block_literal_global.263
+ ___block_literal_global.270
+ ___block_literal_global.382
+ _kICLastSaveDurationKey
+ _kICSaveDelayerKey
+ _objc_msgSend$inDidFailFetchingMetadataNotification
+ _objc_msgSend$initWithTarget:selector:delay:maximumDelay:callOnMainThread:
+ _objc_msgSend$isDeviceHot
+ _objc_msgSend$isLowPowerModeEnabled
+ _objc_msgSend$lastSaveDuration
+ _objc_msgSend$saveDelayDebounceTime
+ _objc_msgSend$saveDelayFastSyncMaxDebounceTime
+ _objc_msgSend$saveDelayFastSyncMaxTime
+ _objc_msgSend$saveDelayFastSyncMinDebounceTime
+ _objc_msgSend$saveDelayMaxDebounceTime
+ _objc_msgSend$saveDelayMaxTime
+ _objc_msgSend$saveDelayMinDebounceTime
+ _objc_msgSend$saveDelayer
+ _objc_msgSend$saveDelayerNoCreate
+ _objc_msgSend$setInDidFailFetchingMetadataNotification:
+ _objc_msgSend$setLastSaveDuration:
+ _objc_msgSend$setMaximumDelay:
+ _objc_msgSend$setStopIndexing:
+ _objc_msgSend$stopIndexing
+ _objc_msgSend$stopIndexingToken
+ _sIndexerCount
+ _saveDelayDebounceTime.onceToken
+ _saveDelayDebounceTime.sSaveDelayFastSyncMaxDebounceTime
+ _saveDelayDebounceTime.sSaveDelayFastSyncMinDebounceTime
+ _saveDelayDebounceTime.sSaveDelayMaxDebounceTime
+ _saveDelayDebounceTime.sSaveDelayMinDebounceTime
+ _saveDelayMaxTime.onceToken
+ _saveDelayMaxTime.sSaveDelayFastSyncMaxTime
+ _saveDelayMaxTime.sSaveDelayMaxTime
- GCC_except_table107
- GCC_except_table109
- GCC_except_table118
- GCC_except_table122
- GCC_except_table127
- GCC_except_table162
- GCC_except_table163
- GCC_except_table27
- GCC_except_table86
- ___39-[ICNote(UI) airDropActivityItemSource]_block_invoke.85
- ___51-[ICNote(UI) filterAttachmentsInTextStorage:range:]_block_invoke.272
- ___block_literal_global.1021
- ___block_literal_global.246
- ___block_literal_global.373
CStrings:
+ "-[ICNote(UI) saveDelayDebounceTime]"
+ "ICCoreDataIndexerStopIndexingNotification"
+ "Invalid save delay time"
+ "Note save took %.2fs"
+ "T@\"ICSelectorDelayer\",R,N"
+ "T@,&,N,V_stopIndexingToken"
+ "TB,N,V_inDidFailFetchingMetadataNotification"
+ "TB,V_stopIndexing"
+ "_delayedSave"
+ "_inDidFailFetchingMetadataNotification"
+ "_stopIndexing"
+ "_stopIndexingToken"
+ "_webView:didReceiveConsoleLogForTesting:"
+ "_webView:startXRSessionWithFeatures:colorFormat:depthFormat:completionHandler:"
+ "_webView:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:submissionHandler:"
+ "delayTime > 0"
+ "inDidFailFetchingMetadataNotification"
+ "indexerCount"
+ "isDeviceHot"
+ "isLowPowerModeEnabled"
+ "lastSaveDuration"
+ "rangeForParagraphID:"
+ "saveDelayDebounceTime"
+ "saveDelayFastSyncMaxDebounceTime"
+ "saveDelayFastSyncMaxTime"
+ "saveDelayFastSyncMinDebounceTime"
+ "saveDelayMaxDebounceTime"
+ "saveDelayMaxTime"
+ "saveDelayMinDebounceTime"
+ "saveDelayer"
+ "saveDelayerNoCreate"
+ "setInDidFailFetchingMetadataNotification:"
+ "setLastSaveDuration:"
+ "setMaximumDelay:"
+ "setPaperHasMath:"
+ "setStopIndexing:"
+ "setStopIndexingToken:"
+ "stopIndexing"
+ "stopIndexingToken"
+ "v32@0:8@\"WKWebView\"16@\"NSString\"24"
+ "v56@0:8@\"WKWebView\"16Q24Q32Q40@?<v@?@@\"UIViewController\">48"
+ "v56@0:8@16Q24Q32Q40@?48"
+ "v64@0:8@\"WKWebView\"16@\"NSDictionary\"24@\"WKFrameInfo\"32@\"WKFrameInfo\"40@\"NSObject<NSSecureCoding>\"48@?<v@?>56"
+ "v64@0:8@16@24@32@40@48@?56"
- "_webView:decideWebApplicationCacheQuotaForSecurityOrigin:currentQuota:totalBytesNeeded:decisionHandler:"
- "_webView:startXRSessionWithFeatures:completionHandler:"
- "v40@0:8@\"WKWebView\"16Q24@?<v@?@@\"UIViewController\">32"
- "v40@0:8@16Q24@?32"
- "v56@0:8@\"WKWebView\"16@\"WKSecurityOrigin\"24Q32Q40@?<v@?Q>48"
- "v56@0:8@16@24Q32Q40@?48"

```
