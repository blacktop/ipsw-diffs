## PosterBoardUIServices

> `/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices`

```diff

-283.101.0.0.0
-  __TEXT.__text: 0x8d590
+286.101.0.0.0
+  __TEXT.__text: 0x8deac
   __TEXT.__auth_stubs: 0x1f80
-  __TEXT.__objc_methlist: 0x67f8
+  __TEXT.__objc_methlist: 0x6818
   __TEXT.__const: 0x2528
-  __TEXT.__cstring: 0x522f
-  __TEXT.__gcc_except_tab: 0xf08
-  __TEXT.__oslogstring: 0x3c6f
+  __TEXT.__cstring: 0x52bf
+  __TEXT.__gcc_except_tab: 0xeb8
+  __TEXT.__oslogstring: 0x3cff
   __TEXT.__swift5_typeref: 0x58ef
   __TEXT.__constg_swiftt: 0xbcc
   __TEXT.__swift5_reflstr: 0x903

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift_as_entry: 0x3c
   __TEXT.__swift_as_ret: 0x48
-  __TEXT.__unwind_info: 0x24b0
+  __TEXT.__unwind_info: 0x2498
   __TEXT.__eh_frame: 0x1478
-  __TEXT.__objc_classname: 0x1451
-  __TEXT.__objc_methname: 0x1340e
-  __TEXT.__objc_methtype: 0x3257
-  __TEXT.__objc_stubs: 0xb820
+  __TEXT.__objc_classname: 0x1450
+  __TEXT.__objc_methname: 0x13570
+  __TEXT.__objc_methtype: 0x324e
+  __TEXT.__objc_stubs: 0xb8e0
   __DATA_CONST.__got: 0xce0
-  __DATA_CONST.__const: 0x1ec0
+  __DATA_CONST.__const: 0x1f38
   __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c88
+  __DATA_CONST.__objc_selrefs: 0x3cd0
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x218
   __AUTH_CONST.__auth_got: 0xfd0
   __AUTH_CONST.__const: 0x1640
-  __AUTH_CONST.__cfstring: 0x3300
-  __AUTH_CONST.__objc_const: 0x14120
+  __AUTH_CONST.__cfstring: 0x33a0
+  __AUTH_CONST.__objc_const: 0x140c8
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0x1738
   __AUTH.__data: 0x5d0
-  __DATA.__objc_ivar: 0x788
+  __DATA.__objc_ivar: 0x77c
   __DATA.__data: 0x2770
   __DATA.__bss: 0x2420
   __DATA.__common: 0x98

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 69408F9F-0381-3482-A69D-FDC145577AF0
-  Functions: 3394
-  Symbols:   9306
-  CStrings:  4646
+  UUID: ABDA4A69-D309-34B3-ABA1-8F994E188357
+  Functions: 3397
+  Symbols:   9317
+  CStrings:  4667
 
Symbols:
+ -[PRUISPosterChannel _extensionProvider]
+ -[PRUISPosterChannel pooledExtensionInstanceWithError:]
+ -[PRUISPosterChannel relinquishExtensionInstanceForReason:]
+ -[PRUISPosterChannel relinquishExtensionInstanceForReason:].cold.1
+ -[PRUISPosterChannel relinquishExtensionInstanceForReason:].cold.2
+ -[PRUISPosterChannel relinquishPooledExtensionInstance:]
+ -[PRUISPosterChannel relinquishPooledExtensionInstance:].cold.1
+ -[PRUISPosterChannelViewController _relinquishExtensionInstance:]
+ -[PRUISPosterChannelViewController extensionInstance]
+ -[PRUISPosterChannelViewController scene]
+ -[PRUISPosterChannelViewController viewDidDisappear:]
+ -[PRUISPosterRenderingViewController initWithPosterContents:context:boundingShape:extensionInstance:snapshotController:initialSnapshotBundle:renderingMode:snapshotDefinition:]
+ -[PRUISPosterRenderingViewController initWithPosterContents:context:boundingShape:extensionInstance:snapshotController:initialSnapshotBundle:renderingMode:snapshotDefinition:].cold.1
+ -[PRUISPosterRenderingViewController initWithPosterContents:context:boundingShape:extensionInstance:snapshotController:initialSnapshotBundle:renderingMode:snapshotDefinition:].cold.2
+ -[PRUISPosterRenderingViewController initWithPosterContents:context:boundingShape:extensionInstance:snapshotController:initialSnapshotBundle:renderingMode:snapshotDefinition:].cold.3
+ -[PRUISPosterSnapshotSQLiteCache _buildOptionsForRequest:]
+ -[PRUISPosterSnapshotSQLiteCache cacheSnapshotBundle:forRequest:error:]
+ GCC_except_table14
+ GCC_except_table157
+ GCC_except_table20
+ GCC_except_table31
+ GCC_except_table46
+ GCC_except_table70
+ GCC_except_table71
+ GCC_except_table86
+ _OBJC_IVAR_$_PRUISPosterChannelViewController._extensionInstance
+ ___175-[PRUISPosterRenderingViewController initWithPosterContents:context:boundingShape:extensionInstance:snapshotController:initialSnapshotBundle:renderingMode:snapshotDefinition:]_block_invoke
+ ___56-[PRUISPosterRenderingViewController applyVisualEffect:]_block_invoke.124
+ ___56-[PRUISPosterRenderingViewController applyVisualEffect:]_block_invoke.124.cold.1
+ ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke.91
+ ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke.91.cold.1
+ ___80-[PRUISPosterSnapshotFilesystemCache cacheSnapshotBundle:forRequest:completion:]_block_invoke
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.105
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.105.cold.1
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.110
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.114
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.88
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.97
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e45_v24?0"PUIPosterSnapshotBundle"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e18_v16?0"NSString"8ls32l8
+ ___block_descriptor_40_e8_32w_e98_v32?0"PRUISPosterRenderingViewController"8"PFPosterExtensionInstance"16"BSAnimationSettings"24lw32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e44_v16?0"PRUISPosterRenderingViewController"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48bs_e35_v16?0"PRUISPosterSnapshotBundle"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40bs48bs_e90_v40?0"PRUISPosterSnapshotRequest"8"PRUISPosterSnapshotResult"16"NSError"24"NSError"32ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e5_v8?0ls48l8s32l8s40l8s56l8
+ ___block_literal_global.152
+ ___block_literal_global.158
+ ___block_literal_global.164
+ ___block_literal_global.187
+ ___block_literal_global.192
+ _objc_msgSend$_buildOptionsForRequest:
+ _objc_msgSend$_extensionProvider
+ _objc_msgSend$_relinquishExtensionInstance:
+ _objc_msgSend$addCompletionBlock:
+ _objc_msgSend$cacheSnapshotBundle:options:outError:
+ _objc_msgSend$currentRunLoop
+ _objc_msgSend$initWithPosterContents:context:boundingShape:extensionInstance:snapshotController:initialSnapshotBundle:renderingMode:snapshotDefinition:
+ _objc_msgSend$pooledExtensionInstanceWithError:
+ _objc_msgSend$relinquishExtensionInstanceWithIdentifier:reason:
+ _objc_msgSend$relinquishPooledExtensionInstance:
- -[PRUISPosterEditingViewController _queue_deviceMotionEventGenerationDidStop]
- -[PRUISPosterEditingViewController _queue_deviceMotionEventGenerationWillStart]
- -[PRUISPosterRenderingViewController _queue_deviceMotionEventGenerationDidStop]
- -[PRUISPosterRenderingViewController _queue_deviceMotionEventGenerationWillStart]
- -[PRUISPosterRenderingViewController dealloc].cold.1
- -[PRUISPosterRenderingViewController dealloc].cold.2
- -[PRUISPosterRenderingViewController initWithPosterContents:context:boundingShape:extensionInstance:snapshotController:initialSnapshotBundle:renderingMode:].cold.1
- -[PRUISPosterRenderingViewController initWithPosterContents:context:boundingShape:extensionInstance:snapshotController:initialSnapshotBundle:renderingMode:].cold.2
- -[PRUISPosterRenderingViewController initWithPosterContents:context:boundingShape:extensionInstance:snapshotController:initialSnapshotBundle:renderingMode:].cold.3
- -[PRUISPosterSnapshotFilesystemCache cacheSnapshotBundle:forRequest:]
- -[PRUISPosterSnapshotSQLiteCache cacheSnapshotBundle:forRequest:]
- GCC_except_table159
- GCC_except_table28
- GCC_except_table56
- GCC_except_table66
- GCC_except_table67
- GCC_except_table82
- _OBJC_IVAR_$_PRUISPosterChannelViewController._mainThreadScheduler
- _OBJC_IVAR_$_PRUISPosterEditingViewController._deviceMotionEventQueue
- _OBJC_IVAR_$_PRUISPosterRenderingViewController._deviceMotionEventQueue
- _OBJC_IVAR_$_PRUISPosterRenderingViewController._pendTransitionToSnapshotRenderingMode
- _OUTLINED_FUNCTION_15
- ___56-[PRUISPosterRenderingViewController applyVisualEffect:]_block_invoke.107
- ___56-[PRUISPosterRenderingViewController applyVisualEffect:]_block_invoke.107.cold.1
- ___70-[PRUISPosterEditingViewController deviceMotionEventGenerationDidStop]_block_invoke
- ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke.90
- ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke.90.cold.1
- ___72-[PRUISPosterEditingViewController deviceMotionEventGenerationWillStart]_block_invoke
- ___72-[PRUISPosterRenderingViewController deviceMotionEventGenerationDidStop]_block_invoke
- ___74-[PRUISPosterRenderingViewController deviceMotionEventGenerationWillStart]_block_invoke
- ___76-[PRUISPosterSnapshotSQLiteCache cacheSnapshotBundle:forRequest:completion:]_block_invoke_2
- ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.100
- ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.91
- ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.96
- ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.96.cold.1
- ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.99
- ___block_descriptor_40_e8_32bs_e33_v16?0"PUIPosterSnapshotBundle"8ls32l8
- ___block_descriptor_40_e8_32s_e44_v16?0"PRUISPosterRenderingViewController"8ls32l8
- ___block_descriptor_40_e8_32w_e68_v24?0"PRUISPosterRenderingViewController"8"BSAnimationSettings"16lw32l8
- ___block_descriptor_48_e8_32bs40r_e17_v16?0"NSError"8lr40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e35_v16?0"PRUISPosterSnapshotBundle"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e90_v40?0"PRUISPosterSnapshotRequest"8"PRUISPosterSnapshotResult"16"NSError"24"NSError"32ls32l8s40l8
- ___block_literal_global.135
- ___block_literal_global.141
- ___block_literal_global.147
- ___block_literal_global.170
- ___block_literal_global.175
- _objc_msgSend$_queue_deviceMotionEventGenerationDidStop
- _objc_msgSend$_queue_deviceMotionEventGenerationWillStart
- _objc_msgSend$cacheSnapshotBundle:forRequest:
- _objc_msgSend$extensionInstanceForReason:outError:
CStrings:
+ "%{public}@ error capturing snapshot: %{public}@"
+ "%{public}@ relinquishing extension instance: %{public}@"
+ "%{public}@ successfully captured snapshot. Result: %{public}@."
+ "%{public}@ viewDidDisappear..."
+ "%{public}@ viewWillDisappear..."
+ "<%{public}@:%{public}p> Spinning up a live scene because %{public}@"
+ "@80@0:8@16@24q32@40@48@56Q64@72"
+ "Cannot relinquish extension instance for reason %{public}@, because Poster Configuration Extension Identifier was nil"
+ "Scene content was not ready and there is no snapshotController."
+ "T@\"FBScene\",R,N"
+ "T@\"NSURL\",R,N,V_cacheURL"
+ "T@\"PFPosterExtensionInstance\",R,N,V_extensionInstance"
+ "_buildOptionsForRequest:"
+ "_relinquishExtensionInstance:"
+ "addCompletionBlock:"
+ "cacheSnapshotBundle:forRequest:error:"
+ "cacheSnapshotBundle:options:outError:"
+ "currentRunLoop"
+ "failed to build snapshot image views"
+ "failed to capture snapshot from live running scene"
+ "failed to capture snapshot from snapshot controller"
+ "initWithPosterContents:context:boundingShape:extensionInstance:snapshotController:initialSnapshotBundle:renderingMode:snapshotDefinition:"
+ "nil snapshot definition"
+ "pooledExtensionInstance"
+ "pooledExtensionInstanceWithError:"
+ "relinquishExtensionInstanceForReason:"
+ "relinquishExtensionInstanceWithIdentifier:reason:"
+ "relinquishPooledExtensionInstance:"
+ "v16@?0@\"NSString\"8"
+ "v24@?0@\"PUIPosterSnapshotBundle\"8@\"NSError\"16"
+ "v32@?0@\"PRUISPosterRenderingViewController\"8@\"PFPosterExtensionInstance\"16@\"BSAnimationSettings\"24"
+ "v40@0:8@\"PRUISPosterSnapshotBundle\"16@\"PRUISPosterSnapshotRequest\"24@?<v@?@\"PRUISPosterSnapshotBundle\"@\"NSError\">32"
+ "v40@0:8@16@24@?32"
+ "\xf0\xf02"
- "%{public}@ error capturing snapshot in viewDidDisappear: %{public}@"
- "%{public}@ successfully captured snapshot in viewDidDisappear. Result: %{public}@."
- "B32@0:8@\"PRUISPosterSnapshotBundle\"16@\"PRUISPosterSnapshotRequest\"24"
- "B40@0:8@\"PRUISPosterSnapshotBundle\"16@\"PRUISPosterSnapshotRequest\"24@?<v@?@\"NSError\">32"
- "B40@0:8@16@24@?32"
- "Rendering View Controller"
- "_deviceMotionEventQueue"
- "_mainThreadScheduler"
- "_pendTransitionToSnapshotRenderingMode"
- "_queue_deviceMotionEventGenerationDidStop"
- "_queue_deviceMotionEventGenerationWillStart"
- "cacheSnapshotBundle:forRequest:"
- "com.apple.PosterBoardUIServices.PRUISPosterEditingViewController.deviceMotionEventQueue"
- "com.apple.PosterBoardUIServices.PRUISPosterRenderingViewController.deviceMotionEventQueue"
- "invalidating snapshot controller"
- "not invalidating snapshot controller because it's the shared incoming call snapshot controller"
- "v24@?0@\"PRUISPosterRenderingViewController\"8@\"BSAnimationSettings\"16"
- "\xf0\xf0B"

```
