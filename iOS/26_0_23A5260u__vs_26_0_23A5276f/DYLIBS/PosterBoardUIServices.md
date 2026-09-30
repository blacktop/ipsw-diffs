## PosterBoardUIServices

> `/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices`

```diff

-276.105.0.0.0
-  __TEXT.__text: 0x8bf94
-  __TEXT.__auth_stubs: 0x1f30
-  __TEXT.__objc_methlist: 0x6648
-  __TEXT.__const: 0x24f8
-  __TEXT.__cstring: 0x502f
-  __TEXT.__gcc_except_tab: 0xe5c
-  __TEXT.__oslogstring: 0x38af
+280.101.0.0.0
+  __TEXT.__text: 0x8cd30
+  __TEXT.__auth_stubs: 0x1f40
+  __TEXT.__objc_methlist: 0x6780
+  __TEXT.__const: 0x2518
+  __TEXT.__cstring: 0x524f
+  __TEXT.__gcc_except_tab: 0xe84
+  __TEXT.__oslogstring: 0x3b1f
   __TEXT.__swift5_typeref: 0x58ef
   __TEXT.__constg_swiftt: 0xbcc
-  __TEXT.__swift5_reflstr: 0x8e3
-  __TEXT.__swift5_fieldmd: 0x73c
+  __TEXT.__swift5_reflstr: 0x903
+  __TEXT.__swift5_fieldmd: 0x748
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_assocty: 0x288
   __TEXT.__swift5_proto: 0x10c
   __TEXT.__swift5_types: 0x84
-  __TEXT.__swift5_capture: 0x274
+  __TEXT.__swift5_capture: 0x264
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift_as_entry: 0x3c
   __TEXT.__swift_as_ret: 0x48
-  __TEXT.__unwind_info: 0x2430
-  __TEXT.__eh_frame: 0x1448
-  __TEXT.__objc_classname: 0x1435
-  __TEXT.__objc_methname: 0x12d8e
-  __TEXT.__objc_methtype: 0x313f
-  __TEXT.__objc_stubs: 0xb400
-  __DATA_CONST.__got: 0xce0
-  __DATA_CONST.__const: 0x1ef0
+  __TEXT.__unwind_info: 0x24a8
+  __TEXT.__eh_frame: 0x1478
+  __TEXT.__objc_classname: 0x144d
+  __TEXT.__objc_methname: 0x1315f
+  __TEXT.__objc_methtype: 0x31d1
+  __TEXT.__objc_stubs: 0xb6e0
+  __DATA_CONST.__got: 0xce8
+  __DATA_CONST.__const: 0x1fb8
   __DATA_CONST.__objc_classlist: 0x328
-  __DATA_CONST.__objc_catlist: 0x38
+  __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x268
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b70
+  __DATA_CONST.__objc_selrefs: 0x3c20
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x218
-  __AUTH_CONST.__auth_got: 0xfa8
-  __AUTH_CONST.__const: 0x1620
-  __AUTH_CONST.__cfstring: 0x3220
-  __AUTH_CONST.__objc_const: 0x13ed0
+  __AUTH_CONST.__auth_got: 0xfb0
+  __AUTH_CONST.__const: 0x15f8
+  __AUTH_CONST.__cfstring: 0x32e0
+  __AUTH_CONST.__objc_const: 0x140a8
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0x1730
+  __AUTH.__objc_data: 0x1738
   __AUTH.__data: 0x5d0
-  __DATA.__objc_ivar: 0x764
+  __DATA.__objc_ivar: 0x77c
   __DATA.__data: 0x2770
   __DATA.__bss: 0x2420
-  __DATA.__common: 0x90
+  __DATA.__common: 0x98
   __DATA_DIRTY.__objc_data: 0x11a8
   __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 53B73E6F-BA2A-3D48-9F19-CB79A138E127
-  Functions: 3348
-  Symbols:   9181
-  CStrings:  4556
+  UUID: 67BF07E7-1DE1-3CFF-B863-983D09C0F81A
+  Functions: 3385
+  Symbols:   9282
+  CStrings:  4619
 
Symbols:
+ -[PRUISDeviceMotionController deviceMotionActivityLevel]
+ -[PRUISDeviceMotionController motionProvider:motionActivityLevelDidUpdate:]
+ -[PRUISDeviceMotionController setDeviceMotionActivityLevel:]
+ -[PRUISDeviceMotionProvider __lock_lightSourceSubscription]
+ -[PRUISDeviceMotionProvider _lightSourceSubscription]
+ -[PRUISDeviceMotionProvider _lock_invalidateLightSourceSubscription]
+ -[PRUISDeviceMotionProvider _lock_setLightSourceSubscriptionActive:]
+ -[PRUISDeviceMotionProvider _motionActivityLevel]
+ -[PRUISDeviceMotionProvider _motionGenerationQueue_pauseGeneratingMotionEvents]
+ -[PRUISDeviceMotionProvider _motionGenerationQueue_startGeneratingMotionEvents]
+ -[PRUISDeviceMotionProvider _motionGenerationQueue_stopGeneratingMotionEvents]
+ -[PRUISDeviceMotionProvider _motionProvider:motionActivityLevelDidUpdate:]
+ -[PRUISDeviceMotionProvider _queue_motionProvider:motionActivityLevelDidUpdate:]
+ -[PRUISDeviceMotionProvider _setMotionActivityLevel:]
+ -[PRUISDeviceMotionProvider motionActivityLevel]
+ -[PRUISDeviceMotionProvider pauseGeneratingMotionEvents]
+ -[PRUISPosterChannelViewController _purgeSnapshotBundleFuture:]
+ -[PRUISPosterChannelViewController _purgeSnapshotBundlesFuture:]
+ -[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]
+ -[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:].cold.1
+ -[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:].cold.2
+ -[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:].cold.3
+ -[PRUISTestingDeviceMotionProvider motionActivityLevel]
+ -[PRUISTestingDeviceMotionProvider pauseGeneratingMotionEvents]
+ -[UIViewController(PosterBoardUIServices) pruis_snapshotRequestForDefinition:interfaceOrientation:bounds:screen:posterContents:]
+ -[UIViewController(PosterBoardUIServices) pruis_snapshotRequestForDefinition:interfaceOrientation:bounds:screen:posterContents:].cold.1
+ -[UIViewController(PosterBoardUIServices) pruis_snapshotRequestForDefinition:interfaceOrientation:bounds:screen:posterContents:].cold.2
+ GCC_except_table146
+ GCC_except_table32
+ GCC_except_table48
+ GCC_except_table54
+ GCC_except_table69
+ GCC_except_table70
+ GCC_except_table75
+ GCC_except_table80
+ _CGRectNull
+ _OBJC_CLASS_$_PFDebounceFilter
+ _OBJC_IVAR_$_PRUISDeviceMotionController._lock
+ _OBJC_IVAR_$_PRUISDeviceMotionController._lock_deviceMotionActivityLevel
+ _OBJC_IVAR_$_PRUISDeviceMotionProvider._lock_lightSourceSubscription
+ _OBJC_IVAR_$_PRUISDeviceMotionProvider._lock_lightSourceSubscriptionQueue
+ _OBJC_IVAR_$_PRUISDeviceMotionProvider._lock_motionActivityLevel
+ _OBJC_IVAR_$_PRUISDeviceMotionProvider._motionGenerationQueue
+ _OBJC_IVAR_$_PRUISPosterRenderingViewController._initialSnapshotBundle
+ _OBJC_IVAR_$_PRUISPosterRenderingViewController._jetsamDebounceFilter
+ _OBJC_IVAR_$_PRUISTestingDeviceMotionProvider._motionActivityLevel
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _PRUISStringFromDeviceMotionActivityLevel
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UIViewController_$_PosterBoardUIServices
+ __OBJC_$_CATEGORY_UIViewController_$_PosterBoardUIServices
+ ___55-[PRUISDeviceMotionProvider stopGeneratingMotionEvents]_block_invoke
+ ___56-[PRUISDeviceMotionProvider pauseGeneratingMotionEvents]_block_invoke
+ ___56-[PRUISPosterRenderingViewController applyVisualEffect:]_block_invoke.107
+ ___56-[PRUISPosterRenderingViewController applyVisualEffect:]_block_invoke.107.cold.1
+ ___59-[PRUISDeviceMotionProvider __lock_lightSourceSubscription]_block_invoke
+ ___63-[PRUISPosterChannelViewController _purgeSnapshotBundleFuture:]_block_invoke
+ ___64-[PRUISPosterChannelViewController _purgeSnapshotBundlesFuture:]_block_invoke
+ ___64-[PRUISPosterChannelViewController _purgeSnapshotBundlesFuture:]_block_invoke_2
+ ___67-[PRUISPosterChannelViewController _createViewControllerForPoster:]_block_invoke.110
+ ___67-[PRUISPosterChannelViewController _createViewControllerForPoster:]_block_invoke.114
+ ___67-[PRUISPosterChannelViewController _createViewControllerForPoster:]_block_invoke_2.113
+ ___74-[PRUISDeviceMotionProvider _motionProvider:motionActivityLevelDidUpdate:]_block_invoke
+ ___79-[PRUISDeviceMotionProvider _motionGenerationQueue_startGeneratingMotionEvents]_block_invoke
+ ___79-[PRUISDeviceMotionProvider _motionGenerationQueue_startGeneratingMotionEvents]_block_invoke.cold.1
+ ___79-[PRUISDeviceMotionProvider _motionGenerationQueue_startGeneratingMotionEvents]_block_invoke.cold.2
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.100
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.86
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.86.cold.1
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.91
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.96
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.96.cold.1
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.99
+ ___block_descriptor_40_e8_32s_e40_v32?0"PUIPosterSnapshotBundle"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSArray"8lw32l8
+ ___block_descriptor_40_e8_32w_e5_8?0lw32l8
+ ___block_descriptor_48_e8_32s40bs_e35_v16?0"PRUISPosterSnapshotBundle"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e90_v40?0"PRUISPosterSnapshotRequest"8"PRUISPosterSnapshotResult"16"NSError"24"NSError"32ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e46_B24?0"PUIPosterSnapshotBundle"8"NSString"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.144
+ ___block_literal_global.167
+ ___block_literal_global.172
+ _objc_msgSend$__lock_lightSourceSubscription
+ _objc_msgSend$_lightSourceSubscription
+ _objc_msgSend$_lock_invalidateLightSourceSubscription
+ _objc_msgSend$_lock_setLightSourceSubscriptionActive:
+ _objc_msgSend$_motionActivityLevel
+ _objc_msgSend$_motionGenerationQueue_pauseGeneratingMotionEvents
+ _objc_msgSend$_motionGenerationQueue_startGeneratingMotionEvents
+ _objc_msgSend$_motionGenerationQueue_stopGeneratingMotionEvents
+ _objc_msgSend$_motionProvider:motionActivityLevelDidUpdate:
+ _objc_msgSend$_purgeSnapshotBundleFuture:
+ _objc_msgSend$_purgeSnapshotBundlesFuture:
+ _objc_msgSend$_queue_motionProvider:motionActivityLevelDidUpdate:
+ _objc_msgSend$_setMotionActivityLevel:
+ _objc_msgSend$_setRenderingMode:canUseInitialSnapshotBundle:
+ _objc_msgSend$allowEvent
+ _objc_msgSend$initWithDebounceAfterEvents:withinTimeInterval:
+ _objc_msgSend$motionProvider:motionActivityLevelDidUpdate:
+ _objc_msgSend$pauseGeneratingMotionEvents
+ _objc_msgSend$pf_jetsamReason
+ _objc_msgSend$pr_posterUUID
+ _objc_msgSend$pruis_snapshotRequestForDefinition:interfaceOrientation:bounds:screen:posterContents:
+ _objc_msgSend$setDeviceMotionActivityLevel:
+ _objc_msgSend$setPosterUUID:
+ _objc_msgSend$setSnapshotDefinitionIdentifier:
- -[PRUISDeviceMotionProvider _createLightSourceSubscriptionIfNeeded]
- -[PRUISPosterChannelViewController _waitingForLiveRenderingSceneSnapshotRequestForPosterConfiguration:].cold.2
- -[PRUISPosterRenderingViewController setRenderingMode:].cold.1
- -[PRUISPosterRenderingViewController setRenderingMode:].cold.2
- GCC_except_table142
- GCC_except_table50
- GCC_except_table65
- GCC_except_table66
- GCC_except_table76
- _OBJC_CLASS_$_PRSMutablePosterDescriptor
- _OBJC_IVAR_$_PRUISDeviceMotionController._significantMotionLock
- _OBJC_IVAR_$_PRUISDeviceMotionProvider._lightSourceSubscription
- _OBJC_IVAR_$_PRUISDeviceMotionProvider._lightSourceSubscriptionQueue
- ___55-[PRUISPosterRenderingViewController setRenderingMode:]_block_invoke
- ___55-[PRUISPosterRenderingViewController setRenderingMode:]_block_invoke.85
- ___55-[PRUISPosterRenderingViewController setRenderingMode:]_block_invoke.85.cold.1
- ___55-[PRUISPosterRenderingViewController setRenderingMode:]_block_invoke.87
- ___55-[PRUISPosterRenderingViewController setRenderingMode:]_block_invoke.87.cold.1
- ___56-[PRUISDeviceMotionProvider startGeneratingMotionEvents]_block_invoke.cold.1
- ___56-[PRUISDeviceMotionProvider startGeneratingMotionEvents]_block_invoke.cold.2
- ___56-[PRUISPosterRenderingViewController applyVisualEffect:]_block_invoke.95
- ___56-[PRUISPosterRenderingViewController applyVisualEffect:]_block_invoke.95.cold.1
- ___57-[PRUISPosterChannelViewController _purgeSnapshotBundle:]_block_invoke.109
- ___67-[PRUISDeviceMotionProvider _createLightSourceSubscriptionIfNeeded]_block_invoke
- ___67-[PRUISPosterChannelViewController _createViewControllerForPoster:]_block_invoke.120
- ___67-[PRUISPosterChannelViewController _createViewControllerForPoster:]_block_invoke.124
- ___67-[PRUISPosterChannelViewController _createViewControllerForPoster:]_block_invoke_2.123
- ___block_descriptor_48_e8_32s40w_e5_8?0lw40l8s32l8
- ___block_descriptor_56_e8_32s40bs_e35_v16?0"PRUISPosterSnapshotBundle"8ls32l8s40l8
- ___block_literal_global.126
- ___block_literal_global.132
- ___block_literal_global.155
- ___block_literal_global.160
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_PosterBoardUIServices
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_PosterBoardUIServices
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_PosterBoardUIServices
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_PosterBoardUIServices
- _objc_msgSend$_createLightSourceSubscriptionIfNeeded
CStrings:
+ "%{public}@ Purging snapshot bundle (%{public}lu)..."
+ "<%{public}@:%{public}p> Cannot capture snapshot. Scene content was not ready and there is no snapshotController. Not updating rendering mode. Keeping mode as '%{public}@'"
+ "<%{public}@:%{public}p> Capturing snapshot using the content-ready scene."
+ "<%{public}@:%{public}p> Capturing snapshot using the snapshot controller."
+ "<%{public}@:%{public}p> Failed to capture snapshot with error: %{public}@. Not updating rendering mode. Keeping mode as '%{public}@'"
+ "<%{public}@:%{public}p> Failed to capture snapshot with resultError: %{public}@, cacheError: %{public}@. Not updating rendering mode. Keeping mode as '%{public}@'"
+ "<%{public}@:%{public}p> Snapshot bundle insufficient for setting up snapshot image views. %{public}@"
+ "<%{public}@:%{public}p> scene %@ did activate"
+ "<%{public}@:%{public}p> scene %@ did change content state to %@"
+ "<%{public}@:%{public}p> scene %@ did deactivate with fatal error %@"
+ "<%{public}@:%{public}p> scene %@ did deactivate with jetsam error with reason %@. Transitioning to snapshot."
+ "<%{public}@:%{public}p> scene %@ did deactivate with jetsam error with reason %@. Trying to activate live again."
+ "<%{public}@:%{public}p> scene %@ did deactivate with transient error %@"
+ "<%{public}@:%{public}p> scene %@ did receive actions %@"
+ "<%{public}@:%{public}p> scene %@ did update client settings with diff %@, transition %@"
+ "@\"PFDebounceFilter\""
+ "@80@0:8@16q24{CGRect={CGPoint=dd}{CGSize=dd}}32@64@72"
+ "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
+ "B24@?0@\"PUIPosterSnapshotBundle\"8@\"NSString\"16"
+ "Device motion activity level updated from %@ to %@"
+ "Ignoring light source orientation because light source timestamp (%f) is not close enough to the interpolated time (%f)"
+ "Motion activity level changed: %@"
+ "Not updating rendering mode. Keeping mode as '%@'"
+ "Pausing motion updates"
+ "PosterBoardUIServices"
+ "TB,N,R,VdescriptorsUpdated"
+ "Tq,N,V_lock_deviceMotionActivityLevel"
+ "Tq,R,N,V_motionActivityLevel"
+ "UIViewController+PosterBoardUIServices.m"
+ "Will continue by trying to take a snapshot..."
+ "__lock_lightSourceSubscription"
+ "_initialSnapshotBundle"
+ "_jetsamDebounceFilter"
+ "_lock_deviceMotionActivityLevel"
+ "_lock_invalidateLightSourceSubscription"
+ "_lock_lightSourceSubscription"
+ "_lock_lightSourceSubscriptionQueue"
+ "_lock_motionActivityLevel"
+ "_lock_setLightSourceSubscriptionActive:"
+ "_motionActivityLevel"
+ "_motionGenerationQueue"
+ "_motionGenerationQueue_pauseGeneratingMotionEvents"
+ "_motionGenerationQueue_startGeneratingMotionEvents"
+ "_motionGenerationQueue_stopGeneratingMotionEvents"
+ "_motionProvider:motionActivityLevelDidUpdate:"
+ "_purgeSnapshotBundleFuture:"
+ "_purgeSnapshotBundlesFuture:"
+ "_queue_motionProvider:motionActivityLevelDidUpdate:"
+ "_setMotionActivityLevel:"
+ "_setRenderingMode:canUseInitialSnapshotBundle:"
+ "allowEvent"
+ "com.apple.PosterBoardUIServices.PRUISDeviceMotionProvider.motionGenerationQueue"
+ "descriptorsUpdated"
+ "deviceMotionActivityLevel"
+ "idle"
+ "initWithDebounceAfterEvents:withinTimeInterval:"
+ "motionActivityLevel"
+ "motionProvider:motionActivityLevelDidUpdate:"
+ "none"
+ "pauseGeneratingMotionEvents"
+ "pf_jetsamReason"
+ "pruis_snapshotRequestForDefinition:interfaceOrientation:bounds:screen:posterContents:"
+ "setDeviceMotionActivityLevel:"
+ "unknown"
+ "v16@?0@\"NSArray\"8"
+ "v28@0:8Q16B24"
+ "v32@0:8@\"<PRUISDeviceMotionProviding>\"16q24"
+ "v32@0:8@16q24"
+ "v32@?0@\"PUIPosterSnapshotBundle\"8Q16^B24"
+ "\xd1"
+ "\xf0\xf0R"
- "<%{public}@:%{public}p> Failed to capture snapshot. Not updating rendering mode. Keeping mode as '%{public}@'"
- "<%{public}@:%{public}p> Snapshot bundle insufficient for setting up snapshot image views. Not updating rendering mode. Keeping mode as '%{public}@'"
- "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
- "Ignoring light source orientation because light source timestamp (%f) is not close enough to the current time (%f)"
- "SceneViewController-%p: scene %@ did activate"
- "SceneViewController-%p: scene %@ did change content state to %@"
- "SceneViewController-%p: scene %@ did deactivate with error %@"
- "SceneViewController-%p: scene %@ did deactivate with fatal error %@"
- "SceneViewController-%p: scene %@ did deactivate with transient error %@"
- "SceneViewController-%p: scene %@ did receive actions %@"
- "SceneViewController-%p: scene %@ did update client settings with diff %@, transition %@"
- "_createLightSourceSubscriptionIfNeeded"
- "_lightSourceSubscriptionQueue"
- "_significantMotionLock"
- "pf_replaceURL:withURL:error:"
- "\xf0\xf02"

```
