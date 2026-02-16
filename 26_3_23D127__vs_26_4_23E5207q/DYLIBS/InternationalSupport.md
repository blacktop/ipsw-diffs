## InternationalSupport

> `/System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport`

```diff

-114.0.0.0.0
-  __TEXT.__text: 0x8aa8
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_methlist: 0x634
-  __TEXT.__const: 0x182
-  __TEXT.__cstring: 0x1fbd
+114.4.1.0.0
+  __TEXT.__text: 0xae80
+  __TEXT.__auth_stubs: 0x720
+  __TEXT.__objc_methlist: 0x724
+  __TEXT.__const: 0x192
+  __TEXT.__cstring: 0x2107
   __TEXT.__ustring: 0x2f9ab8
-  __TEXT.__gcc_except_tab: 0xb4
+  __TEXT.__gcc_except_tab: 0xd4
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__oslogstring: 0x2f0
+  __TEXT.__oslogstring: 0x46f
   __TEXT.__swift5_typeref: 0x29
   __TEXT.__constg_swiftt: 0x2c
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x278
-  __TEXT.__objc_classname: 0x6e
-  __TEXT.__objc_methname: 0x17a0
-  __TEXT.__objc_methtype: 0x22b
-  __TEXT.__objc_stubs: 0x14a0
-  __DATA_CONST.__got: 0x120
-  __DATA_CONST.__const: 0x1e8
+  __TEXT.__unwind_info: 0x348
+  __TEXT.__objc_classname: 0x85
+  __TEXT.__objc_methname: 0x1b98
+  __TEXT.__objc_methtype: 0x27f
+  __TEXT.__objc_stubs: 0x1480
+  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__const: 0x308
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b8
+  __DATA_CONST.__objc_selrefs: 0x770
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__objc_arraydata: 0x1aa2d0
-  __AUTH_CONST.__auth_got: 0x388
+  __AUTH_CONST.__auth_got: 0x3a0
   __AUTH_CONST.__const: 0xe8
   __AUTH_CONST.__cfstring: 0x68f680
-  __AUTH_CONST.__objc_const: 0x6e8
+  __AUTH_CONST.__objc_const: 0x838
   __AUTH_CONST.__objc_dictobj: 0x2cd8
   __AUTH_CONST.__objc_arrayobj: 0x1d40
   __AUTH_CONST.__objc_doubleobj: 0x350
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x50
+  __DATA.__objc_ivar: 0x6c
   __DATA.__data: 0x18
   __DATA.__bss: 0x240
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 7CBDF737-ECD2-3736-BEEF-E61C293BC9AB
-  Functions: 173
-  Symbols:   779
-  CStrings:  216499
+  UUID: 7D6925D2-02EB-3E86-96CC-8D5D26B17C84
+  Functions: 224
+  Symbols:   900
+  CStrings:  216556
 
Symbols:
+ -[ISLanguageCarousel _callRegionDetectionCompletionHandler]
+ -[ISLanguageCarousel _guessedRegion]
+ -[ISLanguageCarousel _rankedItems:usePreferredLanguages:guessedRegion:]
+ -[ISLanguageCarousel _regionDetectionDidComplete]
+ -[ISLanguageCarousel _reloadQueue]
+ -[ISLanguageCarousel _startRegionDetectionIfNeeded]
+ -[ISLanguageCarousel dealloc]
+ -[ISLanguageCarousel dispatchQueue]
+ -[ISLanguageCarousel guessedRegionOverride]
+ -[ISLanguageCarousel initWithItems:regionDetectionCompletionHandler:]
+ -[ISLanguageCarousel regionDetectionComplete]
+ -[ISLanguageCarousel regionDetectionCompletionHandler]
+ -[ISLanguageCarousel regionDetectionObserver]
+ -[ISLanguageCarousel regionDetectionStarted]
+ -[ISLanguageCarousel serialQueue]
+ -[ISLanguageCarousel setDispatchQueue:]
+ -[ISLanguageCarousel setGuessedRegionOverride:]
+ -[ISLanguageCarousel setRegionDetectionComplete:]
+ -[ISLanguageCarousel setRegionDetectionCompletionHandler:]
+ -[ISLanguageCarousel setRegionDetectionObserver:]
+ -[ISLanguageCarousel setRegionDetectionStarted:]
+ -[ISLanguageCarousel setSerialQueue:]
+ GCC_except_table0
+ _ISRegionDetectorCountryScanCompletedNotification
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_IVAR_$_ISLanguageCarousel._dispatchQueue
+ _OBJC_IVAR_$_ISLanguageCarousel._guessedRegionOverride
+ _OBJC_IVAR_$_ISLanguageCarousel._regionDetectionComplete
+ _OBJC_IVAR_$_ISLanguageCarousel._regionDetectionCompletionHandler
+ _OBJC_IVAR_$_ISLanguageCarousel._regionDetectionObserver
+ _OBJC_IVAR_$_ISLanguageCarousel._regionDetectionStarted
+ _OBJC_IVAR_$_ISLanguageCarousel._serialQueue
+ _OUTLINED_FUNCTION_0
+ ___27-[ISLanguageCarousel cycle]_block_invoke
+ ___27-[ISLanguageCarousel items]_block_invoke
+ ___30-[ISLanguageCarousel allItems]_block_invoke
+ ___30-[ISLanguageCarousel nextItem]_block_invoke
+ ___31-[ISLanguageCarousel randomize]_block_invoke
+ ___31-[ISLanguageCarousel setCycle:]_block_invoke
+ ___31-[ISLanguageCarousel setItems:]_block_invoke
+ ___33-[ISLanguageCarousel reloadQueue]_block_invoke
+ ___35-[ISLanguageCarousel dispatchQueue]_block_invoke
+ ___35-[ISLanguageCarousel setRandomize:]_block_invoke
+ ___36-[ISLanguageCarousel initWithItems:]_block_invoke
+ ___36-[ISLanguageCarousel initWithItems:]_block_invoke_2
+ ___37-[ISLanguageCarousel mergeDuplicates]_block_invoke
+ ___39-[ISLanguageCarousel setDispatchQueue:]_block_invoke
+ ___40-[ISLanguageCarousel weightedRepetition]_block_invoke
+ ___41-[ISLanguageCarousel setMergeDuplicates:]_block_invoke
+ ___43-[ISLanguageCarousel guessedRegionOverride]_block_invoke
+ ___44-[ISLanguageCarousel setWeightedRepetition:]_block_invoke
+ ___46-[ISLanguageCarousel rankingUsesGuessedRegion]_block_invoke
+ ___47-[ISLanguageCarousel setGuessedRegionOverride:]_block_invoke
+ ___50-[ISLanguageCarousel setRankingUsesGuessedRegion:]_block_invoke
+ ___51-[ISLanguageCarousel rankingUsesPreferredLanguages]_block_invoke
+ ___54-[ISLanguageCarousel regionDetectionCompletionHandler]_block_invoke
+ ___55-[ISLanguageCarousel setRankingUsesPreferredLanguages:]_block_invoke
+ ___58-[ISLanguageCarousel setRegionDetectionCompletionHandler:]_block_invoke
+ ___59-[ISLanguageCarousel _callRegionDetectionCompletionHandler]_block_invoke
+ ___Block_byref_object_copy_
+ ___Block_byref_object_copy_.17
+ ___Block_byref_object_dispose_
+ ___Block_byref_object_dispose_.18
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32w_e24_v16?0"NSNotification"8lw32l8
+ ___block_descriptor_41_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ _dispatch_assert_queue$V2
+ _dispatch_async
+ _dispatch_queue_create
+ _dispatch_sync
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$_callRegionDetectionCompletionHandler
+ _objc_msgSend$_guessedRegion
+ _objc_msgSend$_regionDetectionDidComplete
+ _objc_msgSend$_reloadQueue
+ _objc_msgSend$_startRegionDetectionIfNeeded
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$copy
+ _objc_msgSend$initWithItems:
+ _objc_msgSend$mainQueue
+ _objc_msgSend$removeObserver:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retainBlock
- +[ISLanguageCarousel _rankedItems:usePreferredLanguages:guessedRegion:]
- +[ISLanguageCarousel guessedRegion]
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$cycle
- _objc_msgSend$guessedRegion
- _objc_msgSend$items
- _objc_msgSend$mergeDuplicates
- _objc_msgSend$randomize
- _objc_msgSend$rankingUsesGuessedRegion
- _objc_msgSend$rankingUsesPreferredLanguages
- _objc_msgSend$setCycle:
- _objc_msgSend$setItems:
- _objc_msgSend$setWeightedRepetition:
- _objc_msgSend$weightedRepetition
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "%s: Calling completion handler"
+ "%s: Client set regionOverride: %{public}@"
+ "%s: Ignoring detection result - client provided region"
+ "%s: Region detection already complete"
+ "%s: Region detection already finished when handler set"
+ "%s: Region detection completed. guessedRegion = %{public}@."
+ "%s: Skipping completion handler - client provided region"
+ "%s: Waiting for region detection to complete"
+ "-[ISLanguageCarousel _callRegionDetectionCompletionHandler]"
+ "-[ISLanguageCarousel _regionDetectionDidComplete]"
+ "-[ISLanguageCarousel _reloadQueue]"
+ "-[ISLanguageCarousel _startRegionDetectionIfNeeded]"
+ "-[ISLanguageCarousel setGuessedRegionOverride:]_block_invoke"
+ "-[ISLanguageCarousel setRegionDetectionCompletionHandler:]_block_invoke"
+ "@\"<NSObject>\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@32@0:8@16@?24"
+ "@?"
+ "@?16@0:8"
+ "ISCountryScanCompletedNotification"
+ "T@\"<NSObject>\",&,N,V_regionDetectionObserver"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_dispatchQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_serialQueue"
+ "T@\"NSString\",C,N,V_guessedRegionOverride"
+ "T@?,C,N,V_regionDetectionCompletionHandler"
+ "TB,N,V_regionDetectionComplete"
+ "TB,N,V_regionDetectionStarted"
+ "_callRegionDetectionCompletionHandler"
+ "_dispatchQueue"
+ "_guessedRegion"
+ "_guessedRegionOverride"
+ "_regionDetectionComplete"
+ "_regionDetectionCompletionHandler"
+ "_regionDetectionDidComplete"
+ "_regionDetectionObserver"
+ "_regionDetectionStarted"
+ "_reloadQueue"
+ "_serialQueue"
+ "_startRegionDetectionIfNeeded"
+ "addObserverForName:object:queue:usingBlock:"
+ "com.apple.InternationalSupport.ISLanguageCarousel"
+ "copy"
+ "dispatchQueue"
+ "guessedRegionOverride"
+ "initWithItems:regionDetectionCompletionHandler:"
+ "mainQueue"
+ "regionDetectionComplete"
+ "regionDetectionCompletionHandler"
+ "regionDetectionObserver"
+ "regionDetectionStarted"
+ "removeObserver:"
+ "serialQueue"
+ "setDispatchQueue:"
+ "setGuessedRegionOverride:"
+ "setRegionDetectionComplete:"
+ "setRegionDetectionCompletionHandler:"
+ "setRegionDetectionObserver:"
+ "setRegionDetectionStarted:"
+ "setSerialQueue:"
+ "v16@?0@\"NSNotification\"8"
+ "v24@0:8@?16"
- "-[ISLanguageCarousel reloadQueue]"
- "BYCountryScanCompletedNotification"
- "guessedRegion"

```
