## PosterBoardUIServices

> `/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices`

```diff

-296.100.0.0.0
-  __TEXT.__text: 0x8fe10
-  __TEXT.__auth_stubs: 0x1f90
-  __TEXT.__objc_methlist: 0x67d0
-  __TEXT.__const: 0x2528
-  __TEXT.__cstring: 0x53ff
-  __TEXT.__gcc_except_tab: 0xe2c
-  __TEXT.__oslogstring: 0x413f
-  __TEXT.__swift5_typeref: 0x58ef
-  __TEXT.__constg_swiftt: 0xbcc
+302.100.0.0.0
+  __TEXT.__text: 0x938c4
+  __TEXT.__auth_stubs: 0x2000
+  __TEXT.__objc_methlist: 0x68a8
+  __TEXT.__const: 0x2548
+  __TEXT.__cstring: 0x553f
+  __TEXT.__gcc_except_tab: 0xe7c
+  __TEXT.__oslogstring: 0x42df
+  __TEXT.__swift5_typeref: 0x5a13
+  __TEXT.__constg_swiftt: 0xc30
   __TEXT.__swift5_reflstr: 0x903
-  __TEXT.__swift5_fieldmd: 0x748
-  __TEXT.__swift5_builtin: 0xdc
+  __TEXT.__swift5_fieldmd: 0x764
+  __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_assocty: 0x288
   __TEXT.__swift5_proto: 0x10c
-  __TEXT.__swift5_types: 0x84
-  __TEXT.__swift5_capture: 0x274
+  __TEXT.__swift5_types: 0x8c
+  __TEXT.__swift5_capture: 0x314
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift_as_entry: 0x3c
   __TEXT.__swift_as_ret: 0x48
-  __TEXT.__unwind_info: 0x24e8
-  __TEXT.__eh_frame: 0x1478
-  __TEXT.__objc_classname: 0x1472
-  __TEXT.__objc_methname: 0x13616
-  __TEXT.__objc_methtype: 0x32f4
-  __TEXT.__objc_stubs: 0xb920
+  __TEXT.__unwind_info: 0x25b8
+  __TEXT.__eh_frame: 0x1590
+  __TEXT.__objc_classname: 0x1474
+  __TEXT.__objc_methname: 0x13859
+  __TEXT.__objc_methtype: 0x3305
+  __TEXT.__objc_stubs: 0xbaa0
   __DATA_CONST.__got: 0xcd8
-  __DATA_CONST.__const: 0x1fb0
-  __DATA_CONST.__objc_classlist: 0x328
+  __DATA_CONST.__const: 0x2048
+  __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ca8
+  __DATA_CONST.__objc_selrefs: 0x3d38
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x218
-  __AUTH_CONST.__auth_got: 0xfd8
-  __AUTH_CONST.__const: 0x16e8
+  __AUTH_CONST.__auth_got: 0x1010
+  __AUTH_CONST.__const: 0x1950
   __AUTH_CONST.__cfstring: 0x34e0
-  __AUTH_CONST.__objc_const: 0x14238
+  __AUTH_CONST.__objc_const: 0x14430
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0x15f8
-  __AUTH.__data: 0x5d0
-  __DATA.__objc_ivar: 0x79c
-  __DATA.__data: 0x27d0
-  __DATA.__bss: 0x23e0
-  __DATA.__common: 0x98
-  __DATA_DIRTY.__objc_data: 0x12e8
-  __DATA_DIRTY.__bss: 0x148
+  __AUTH.__objc_data: 0xfd8
+  __AUTH.__data: 0x5c0
+  __DATA.__objc_ivar: 0x7a8
+  __DATA.__data: 0x26d0
+  __DATA.__bss: 0x22d0
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__objc_data: 0x1908
+  __DATA_DIRTY.__data: 0x298
+  __DATA_DIRTY.__bss: 0x260
+  __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: AD189139-8C41-3881-BE0F-2DEEFFADEDDC
-  Functions: 3417
-  Symbols:   9361
-  CStrings:  4705
+  UUID: F01CBCE4-CCCF-376D-9592-287E41A468A4
+  Functions: 3492
+  Symbols:   9489
+  CStrings:  4735
 
Symbols:
+ +[PRUISDeviceMotionProvider new]
+ +[PRUISPosterRenderingViewController _defaultExtensionProvider]
+ -[PRUISDeviceMotionController _queue_pauseGeneratingMotionEvents]
+ -[PRUISDeviceMotionController _queue_setDeviceMotionActivityLevel:]
+ -[PRUISDeviceMotionController _queue_startGeneratingMotionEvents]
+ -[PRUISDeviceMotionController _queue_stopGeneratingMotionEvents]
+ -[PRUISDeviceMotionController deviceMotionMode]
+ -[PRUISDeviceMotionController invalidate]
+ -[PRUISDeviceMotionController setDeviceMotionMode:]
+ -[PRUISDeviceMotionProvider _stopGeneratingMotionEventsRightNow]
+ -[PRUISDeviceMotionProvider init]
+ -[PRUISDeviceMotionProvider invalidate]
+ -[PRUISDeviceMotionProvider motionSource]
+ -[PRUISDeviceMotionSettings deviceMotionMode]
+ -[PRUISDeviceMotionSettings setDeviceMotionMode:]
+ -[PRUISDeviceMotionSettings shouldIgnoreReducedMotionChange]
+ -[PRUISPosterChannel _lock_currentGallery]
+ -[PRUISPosterChannel _lock_currentPosterConfiguration]
+ -[PRUISPosterChannel ingestUpdatedDescriptors:forState:policy:error:]
+ -[PRUISPosterChannelViewController _fetchWaitingForLiveRenderingSnapshotBundlesForPoster:]
+ -[PRUISPosterChannelViewController _purgeSnapshotBundles:]
+ -[PRUISPosterRenderingViewController _extensionProvider]
+ -[PRUISPosterRenderingViewController _setSceneContentHidden:animated:completion:]
+ -[PRUISPosterRenderingViewController _setSceneContentHidden:animationSettings:completion:]
+ -[PRUISPosterSnapshotController extensionProvider]
+ -[_PRUISPosterSnapshotControllerImpl extensionProvider]
+ GCC_except_table155
+ GCC_except_table164
+ GCC_except_table48
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table8
+ GCC_except_table81
+ GCC_except_table82
+ GCC_except_table90
+ _BSDispatchQueueAssertNot
+ _OBJC_IVAR_$_PRUISDeviceMotionController._invalidationSignal
+ _OBJC_IVAR_$_PRUISDeviceMotionController._motionControlQueue
+ _OBJC_IVAR_$_PRUISDeviceMotionController._queue_isGeneratingMotionEvents
+ _OBJC_IVAR_$_PRUISDeviceMotionProvider._invalidationSignal
+ _OBJC_IVAR_$_PRUISDeviceMotionProvider._motionGenerationQueue_deallocating
+ _OBJC_IVAR_$_PRUISDeviceMotionSettings._deviceMotionMode
+ _OBJC_IVAR_$_PRUISDeviceMotionSettings._shouldIgnoreReducedMotionChange
+ _OBJC_IVAR_$_PRUISPosterRenderingViewController._sceneContentHidden
+ __Block_copy
+ __Block_release
+ __DATA__TtCC21PosterBoardUIServices24PRUISPosterChannelReaperP33_FB148EC8685A74C4942C9852D80DCC0323OptionalSQLitePredicate
+ __IVARS__TtCC21PosterBoardUIServices24PRUISPosterChannelReaperP33_FB148EC8685A74C4942C9852D80DCC0323OptionalSQLitePredicate
+ __METACLASS_DATA__TtCC21PosterBoardUIServices24PRUISPosterChannelReaperP33_FB148EC8685A74C4942C9852D80DCC0323OptionalSQLitePredicate
+ ___130-[PRUISDeviceMotionProvider _motionGenerationQueue_stopGeneratingMotionEventsWithActivityLevel:invalidateLightSourceSubscription:]_block_invoke
+ ___55-[PRUISDeviceMotionController isGeneratingMotionEvents]_block_invoke
+ ___57-[PRUISDeviceMotionController stopGeneratingMotionEvents]_block_invoke
+ ___58-[PRUISDeviceMotionController startGeneratingMotionEvents]_block_invoke
+ ___58-[PRUISPosterChannelViewController _purgeSnapshotBundles:]_block_invoke
+ ___60-[PRUISDeviceMotionController setDeviceMotionActivityLevel:]_block_invoke
+ ___63+[PRUISPosterRenderingViewController _defaultExtensionProvider]_block_invoke
+ ___64-[PRUISDeviceMotionProvider _stopGeneratingMotionEventsRightNow]_block_invoke
+ ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke.100
+ ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke.103
+ ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke.103.cold.1
+ ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke.95
+ ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke_2.97
+ ___90-[PRUISPosterRenderingViewController _setSceneContentHidden:animationSettings:completion:]_block_invoke
+ ___90-[PRUISPosterRenderingViewController _setSceneContentHidden:animationSettings:completion:]_block_invoke_2
+ ___90-[PRUISPosterRenderingViewController _setSceneContentHidden:animationSettings:completion:]_block_invoke_3
+ ___90-[PRUISPosterRenderingViewController _setSceneContentHidden:animationSettings:completion:]_block_invoke_4
+ ___block_descriptor_32_e16_v16?0"UIView"8l
+ ___block_descriptor_40_e8_32s_e50_B24?0"PUIPosterSnapshotBundle"8"NSDictionary"16ls32l8
+ ___block_descriptor_41_e8_32w_e8_v12?0B8lw32l8
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0B8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSArray"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64w_e33_v16?0"PUIPosterSnapshotBundle"8lw64l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.165
+ ___block_literal_global.167
+ ___block_literal_global.169
+ ___block_literal_global.192
+ ___block_literal_global.197
+ __defaultExtensionProvider.__extensionProvider
+ __defaultExtensionProvider.onceToken
+ _block_copy_helper.20
+ _block_copy_helper.26
+ _block_copy_helper.32
+ _block_copy_helper.38
+ _block_descriptor.22
+ _block_descriptor.28
+ _block_descriptor.34
+ _block_descriptor.40
+ _block_destroy_helper.21
+ _block_destroy_helper.27
+ _block_destroy_helper.33
+ _block_destroy_helper.39
+ _objc_getProperty
+ _objc_msgSend$_defaultExtensionProvider
+ _objc_msgSend$_fetchWaitingForLiveRenderingSnapshotBundlesForPoster:
+ _objc_msgSend$_lock_currentGallery
+ _objc_msgSend$_lock_currentPosterConfiguration
+ _objc_msgSend$_purgeSnapshotBundles:
+ _objc_msgSend$_queue_pauseGeneratingMotionEvents
+ _objc_msgSend$_queue_setDeviceMotionActivityLevel:
+ _objc_msgSend$_queue_startGeneratingMotionEvents
+ _objc_msgSend$_queue_stopGeneratingMotionEvents
+ _objc_msgSend$_setSceneContentHidden:animated:completion:
+ _objc_msgSend$_setSceneContentHidden:animationSettings:completion:
+ _objc_msgSend$_stopGeneratingMotionEventsRightNow
+ _objc_msgSend$bs_safeAddObject:
+ _objc_msgSend$deviceMotionMode
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$minusSet:
+ _objc_msgSend$pr_deviceMotionMode
+ _objc_msgSend$setDeviceMotionMode:
+ _objc_msgSend$setWithCapacity:
+ _swift_initStaticObject
+ _symbolic SaySo23PUIPosterSnapshotBundleCG
+ _symbolic So10PFTPromiseCySo5NSSetCG
+ _symbolic So10PFTPromiseCy_____G 21PosterBoardUIServices24PRUISPosterChannelReaperC23OptionalSQLitePredicate33_FB148EC8685A74C4942C9852D80DCC03LLC
+ _symbolic So17PFSQLitePredicateC
+ _symbolic So17PFSQLitePredicateCSg
+ _symbolic So17PFSQLitePredicateCSgIegg_
+ _symbolic So17PFSQLitePredicateCz_Xx
+ _symbolic So28PUIPosterSnapshotSQLiteCacheC
+ _symbolic So32PUIPosterSnapshotBundlePredicateC
+ _symbolic _____ 21PosterBoardUIServices24PRUISPosterChannelReaperC23OptionalSQLitePredicate33_FB148EC8685A74C4942C9852D80DCC03LLC
+ _symbolic _____ So32PRUISPosterChannelOperationPhaseV
+ _symbolic _____SSIegyo_ So32PRUISPosterChannelOperationPhaseV
- +[PRUISPosterRenderingViewController _instancePool]
- -[PRUISDeviceMotionController _checkForSignificantMotionUpdateWithRotation:]
- -[PRUISDeviceMotionController _hasSignificantMotionForLatestRotation:]
- -[PRUISDeviceMotionController _resetSignificantMotionState]
- -[PRUISDeviceMotionController setIsGeneratingMotionEvents:]
- -[PRUISDeviceMotionController setSignificantMotion:]
- -[PRUISPosterRenderingViewController _setContentHidden:animated:completion:]
- -[PRUISPosterRenderingViewController _setContentHidden:animationSettings:completion:]
- GCC_except_table152
- GCC_except_table161
- GCC_except_table37
- GCC_except_table77
- GCC_except_table78
- GCC_except_table89
- _OBJC_IVAR_$_PRUISDeviceMotionController._isGeneratingMotionEvents
- _OBJC_IVAR_$_PRUISDeviceMotionController._lock_lastSignificantRotationData
- _OBJC_IVAR_$_PRUISDeviceMotionController._lock_significantMotion
- _OBJC_IVAR_$_PRUISDeviceMotionController._lock_significantMotionCounter
- _OBJC_IVAR_$_PRUISPosterRenderingViewController._contentHidden
- _SPRotation3DIdentity
- ___51+[PRUISPosterRenderingViewController _instancePool]_block_invoke
- ___57-[PRUISPosterChannelViewController _purgeSnapshotBundle:]_block_invoke
- ___64-[PRUISPosterChannelViewController _purgeSnapshotBundlesFuture:]_block_invoke_2
- ___69-[PRUISPosterRenderingViewController _sceneContentReadinessDidChange]_block_invoke_2
- ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke.96
- ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke.96.cold.1
- ___85-[PRUISPosterRenderingViewController _setContentHidden:animationSettings:completion:]_block_invoke
- ___block_descriptor_40_e8_32s_e40_v32?0"PUIPosterSnapshotBundle"8Q16^B24ls32l8
- ___block_descriptor_49_e8_32bs40w_e8_v12?0B8lw40l8s32l8
- ___block_descriptor_64_e8_32s40s48s56w_e33_v16?0"PUIPosterSnapshotBundle"8lw56l8s32l8s40l8s48l8
- ___block_literal_global.162
- ___block_literal_global.185
- ___block_literal_global.190
- __instancePool.__extensionProvider
- __instancePool.onceToken
- _objc_msgSend$_cancelDampeningTimer
- _objc_msgSend$_checkForSignificantMotionUpdateWithRotation:
- _objc_msgSend$_hasSignificantMotionForLatestRotation:
- _objc_msgSend$_instancePool
- _objc_msgSend$_resetSignificantMotionState
- _objc_msgSend$_setContentHidden:animated:completion:
- _objc_msgSend$_setContentHidden:animationSettings:completion:
CStrings:
+ "%s Found %ld 'waitingForLiveRenderingScene' snapshots for poster %s, keeping only the latest"
+ "%s failed to build duplicate 'waitingForLiveRendering' snapshots predicate: %s, continuing without it"
+ "%{public}@ Failed to fetch waitingForLiveRenderingScene snapshot bundles for cleanup: %{public}@, falling back to naive cleanup"
+ "%{public}@ Purging %lu old waitingForLiveRenderingScene snapshots"
+ "<%{public}@:%{public}p> Snapshot controller was nil or did not have an extensionProvider. Falling back to default extensionProvider."
+ "@\"<PRUISDeviceMotionProviding><BSInvalidatable>\""
+ "B24@?0@\"PUIPosterSnapshotBundle\"8@\"NSDictionary\"16"
+ "B48@0:8@16@24Q32o^@40"
+ "T@\"CMMotionManager\",R,V_motionSource"
+ "T@\"PFPosterExtensionProvider\",R,N"
+ "TB,R,N,V_shouldIgnoreReducedMotionChange"
+ "TQ,R,N,V_deviceMotionMode"
+ "_TtCC21PosterBoardUIServices24PRUISPosterChannelReaperP33_FB148EC8685A74C4942C9852D80DCC0323OptionalSQLitePredicate"
+ "_defaultExtensionProvider"
+ "_deviceMotionMode"
+ "_fetchWaitingForLiveRenderingSnapshotBundlesForPoster:"
+ "_motionControlQueue"
+ "_motionGenerationQueue_deallocating"
+ "_purgeSnapshotBundles:"
+ "_queue_isGeneratingMotionEvents"
+ "_queue_pauseGeneratingMotionEvents"
+ "_queue_setDeviceMotionActivityLevel:"
+ "_queue_startGeneratingMotionEvents"
+ "_queue_stopGeneratingMotionEvents"
+ "_sceneContentHidden"
+ "_setSceneContentHidden:animated:completion:"
+ "_setSceneContentHidden:animationSettings:completion:"
+ "_shouldIgnoreReducedMotionChange"
+ "_stopGeneratingMotionEventsRightNow"
+ "bs_safeAddObject:"
+ "channel was updated before descriptors were ingested."
+ "com.apple.PosterBoardUIServices.PRUISDeviceMotionController"
+ "deviceMotionMode"
+ "filteredArrayUsingPredicate:"
+ "finishWithResult:"
+ "ingestUpdatedDescriptors:forState:policy:error:"
+ "minusSet:"
+ "motionSource"
+ "pr_deviceMotionMode"
+ "predicate"
+ "setDeviceMotionMode:"
+ "setSnapshotBundleUUID:"
+ "setWithCapacity:"
+ "shouldIgnoreReducedMotionChange"
+ "snapshotBundleUUID"
+ "v16@?0@\"NSSet\"8"
+ "v16@?0@\"UIView\"8"
+ "v24@?0@8@\"NSError\"16"
- "%{public}@ Purging snapshot bundle (%{public}lu)..."
- "@\"<PRUISDeviceMotionProviding>\""
- "B48@0:8(?={?=}{?=})16"
- "Significant motion state changed; hasSignificantMotion: %{BOOL}u"
- "TB,N,V_isGeneratingMotionEvents"
- "_checkForSignificantMotionUpdateWithRotation:"
- "_contentHidden"
- "_hasSignificantMotionForLatestRotation:"
- "_instancePool"
- "_lock_lastSignificantRotationData"
- "_lock_significantMotion"
- "_lock_significantMotionCounter"
- "_resetSignificantMotionState"
- "_setContentHidden:animated:completion:"
- "_setContentHidden:animationSettings:completion:"
- "channel was updated."
- "setIsGeneratingMotionEvents:"
- "v32@?0@\"PUIPosterSnapshotBundle\"8Q16^B24"
- "\xa1"

```
