## CoreDuet

> `/System/Library/PrivateFrameworks/CoreDuet.framework/Versions/A/CoreDuet`

```diff

-1880.0.1.0.0
-  __TEXT.__text: 0x19da38
-  __TEXT.__auth_stubs: 0x1280
-  __TEXT.__objc_methlist: 0xfdc8
-  __TEXT.__cstring: 0x14e01
+1882.0.0.0.0
+  __TEXT.__text: 0x19f1e8
+  __TEXT.__auth_stubs: 0x12a0
+  __TEXT.__objc_methlist: 0xfdb8
+  __TEXT.__cstring: 0x14d9c
   __TEXT.__const: 0x590
-  __TEXT.__oslogstring: 0x16b6c
-  __TEXT.__gcc_except_tab: 0x72fc
+  __TEXT.__oslogstring: 0x16d95
+  __TEXT.__gcc_except_tab: 0x7530
   __TEXT.__dlopen_cstrs: 0xb6
-  __TEXT.__unwind_info: 0x5168
+  __TEXT.__unwind_info: 0x51a0
   __TEXT.__objc_classname: 0x2b1f
-  __TEXT.__objc_methname: 0x24e5f
+  __TEXT.__objc_methname: 0x24e70
   __TEXT.__objc_methtype: 0x5fdc
-  __TEXT.__objc_stubs: 0x15fc0
-  __DATA_CONST.__got: 0x10c8
+  __TEXT.__objc_stubs: 0x16020
+  __DATA_CONST.__got: 0x10d0
   __DATA_CONST.__const: 0xd90
   __DATA_CONST.__objc_classlist: 0xbe8
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7ac0
+  __DATA_CONST.__objc_selrefs: 0x7ad0
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x650
   __DATA_CONST.__objc_arraydata: 0x658
-  __AUTH_CONST.__auth_got: 0x950
+  __AUTH_CONST.__auth_got: 0x960
   __AUTH_CONST.__auth_ptr: 0x18
-  __AUTH_CONST.__const: 0x4870
-  __AUTH_CONST.__cfstring: 0x12dc0
+  __AUTH_CONST.__const: 0x49a0
+  __AUTH_CONST.__cfstring: 0x12e00
   __AUTH_CONST.__objc_const: 0x243b8
   __AUTH_CONST.__objc_intobj: 0x2118
   __AUTH_CONST.__objc_doubleobj: 0x40

   __AUTH.__objc_data: 0x4fb0
   __DATA.__objc_ivar: 0x1690
   __DATA.__data: 0x19e8
-  __DATA.__bss: 0xd58
+  __DATA.__bss: 0xd78
   __DATA.__common: 0x31
   __DATA_DIRTY.__objc_data: 0x2760
   __DATA_DIRTY.__bss: 0x98

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8211
-  Symbols:   17829
-  CStrings:  2909
+  Functions: 8225
+  Symbols:   17860
+  CStrings:  2911
 
Symbols:
+ -[_CDInteraction metadataFromFeedbackEvent:]
+ -[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:].cold.1
+ GCC_except_table61
+ GCC_except_table71
+ _NSStringFromRange
+ _OBJC_CLASS_$_BMShareSheetFeedback
+ __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.12
+ __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.15
+ __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.17
+ __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.22
+ __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.24
+ __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.25
+ __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.25.cold.1
+ __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke_2.18
+ __78-[_CDInteraction fetchAndAddShareSheetContentToInteractionWithKnowledgeStore:]_block_invoke.728
+ __78-[_CDInteraction fetchAndAddShareSheetContentToInteractionWithKnowledgeStore:]_block_invoke.cold.1
+ ___75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e20_v20?0B8"NSError"12l
+ ___block_descriptor_40_e8_32r_e8_v12?0B8l
+ ___block_descriptor_56_e8_32s40s48r_e21_v24?0"NSArray"8^B16l
+ ___block_descriptor_56_e8_32s40s48r_e22_v16?0"BMStoreEvent"8l
+ ___block_descriptor_64_e8_32s40s48bs56r_e5_v8?0l
+ ___block_descriptor_82_e8_32s40s48bs_e8_v12?0B8l
+ ___recordInteractionsAsync_block_invoke
+ __block_literal_global.727
+ __block_literal_global.901
+ __recordInteractionsAsync_block_invoke.cold.1
+ _dispatch_group_notify
+ _objc_msgSend$Feedback
+ _objc_msgSend$ShareSheet
+ _objc_msgSend$metadataFromFeedbackEvent:
+ _objc_msgSend$publisherWithUseCase:
+ _recordInteractionsAsync
+ recordInteractions:synchronous:completionHandler:._pasOnceToken5
+ recordInteractions:synchronous:completionHandler:.flag
+ recordInteractions:synchronous:completionHandler:.group
+ recordInteractions:synchronous:completionHandler:.queue
- +[_DKSystemEventStreams mapsShareEtaFeedbackStream]
- +[_DKSystemEventStreams shareSheetFeedbackStream]
- -[_CDInteraction fetchAndAddShareSheetContentToInteractionWithKnowledgeStore:].cold.5
- __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.8
- __75-[_CDInteractionRecorder recordInteractions:synchronous:completionHandler:]_block_invoke.cold.1
- ___block_descriptor_49_e8_32bs40r_e8_v12?0B8l
- __block_literal_global.729
- __block_literal_global.890
- _objc_msgSend$shareSheetFeedbackStream
CStrings:
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/CDMonitorManager.m:339"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Data Collection/CrashReporter/_CDDataCollection.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Query/_DKHistogramQuery.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Syncing/_DKSyncLocalKnowledgeStorage.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKStandingQuery.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Sleep/_CDInBedDetector.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Sleep/_CDSleepPredictor.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightContactResolver.m:92"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightEventIndexerDataSource.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightRecorder.m:575"
+ "/dummyStream/tempStream"
+ "ShareSheetFeedback"
+ "recordInteractions:synchronous:completionHandler:"
+ "sharesheet"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/CDMonitorManager.m:339"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Data Collection/CrashReporter/_CDDataCollection.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Interaction/_CDInteraction.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Query/_DKHistogramQuery.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/Syncing/_DKSyncLocalKnowledgeStorage.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Knowledge/_DKStandingQuery.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Sleep/_CDInBedDetector.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/Sleep/_CDSleepPredictor.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightContactResolver.m:92"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightEventIndexerDataSource.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightRecorder.m:575"
- "/mapsShareEta/feedback"

```
