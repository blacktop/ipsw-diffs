## PosterBoardUIServices

> `/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices`

```diff

-286.101.0.0.0
-  __TEXT.__text: 0x8deac
-  __TEXT.__auth_stubs: 0x1f80
-  __TEXT.__objc_methlist: 0x6818
+289.103.0.0.0
+  __TEXT.__text: 0x8e8b8
+  __TEXT.__auth_stubs: 0x1f90
+  __TEXT.__objc_methlist: 0x67a8
   __TEXT.__const: 0x2528
-  __TEXT.__cstring: 0x52bf
-  __TEXT.__gcc_except_tab: 0xeb8
-  __TEXT.__oslogstring: 0x3cff
+  __TEXT.__cstring: 0x53af
+  __TEXT.__gcc_except_tab: 0xe2c
+  __TEXT.__oslogstring: 0x3e8f
   __TEXT.__swift5_typeref: 0x58ef
   __TEXT.__constg_swiftt: 0xbcc
   __TEXT.__swift5_reflstr: 0x903

   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift_as_entry: 0x3c
   __TEXT.__swift_as_ret: 0x48
-  __TEXT.__unwind_info: 0x2498
+  __TEXT.__unwind_info: 0x24b8
   __TEXT.__eh_frame: 0x1478
-  __TEXT.__objc_classname: 0x1450
-  __TEXT.__objc_methname: 0x13570
-  __TEXT.__objc_methtype: 0x324e
-  __TEXT.__objc_stubs: 0xb8e0
-  __DATA_CONST.__got: 0xce0
+  __TEXT.__objc_classname: 0x1470
+  __TEXT.__objc_methname: 0x13517
+  __TEXT.__objc_methtype: 0x32d2
+  __TEXT.__objc_stubs: 0xb8c0
+  __DATA_CONST.__got: 0xcd8
   __DATA_CONST.__const: 0x1f38
   __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x268
+  __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3cd0
+  __DATA_CONST.__objc_selrefs: 0x3c80
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x218
-  __AUTH_CONST.__auth_got: 0xfd0
-  __AUTH_CONST.__const: 0x1640
-  __AUTH_CONST.__cfstring: 0x33a0
-  __AUTH_CONST.__objc_const: 0x140c8
-  __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0x1738
+  __AUTH_CONST.__auth_got: 0xfd8
+  __AUTH_CONST.__const: 0x16b0
+  __AUTH_CONST.__cfstring: 0x34a0
+  __AUTH_CONST.__objc_const: 0x141a8
+  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH.__objc_data: 0x15f8
   __AUTH.__data: 0x5d0
-  __DATA.__objc_ivar: 0x77c
-  __DATA.__data: 0x2770
-  __DATA.__bss: 0x2420
+  __DATA.__objc_ivar: 0x794
+  __DATA.__data: 0x27d0
+  __DATA.__bss: 0x23e0
   __DATA.__common: 0x98
-  __DATA_DIRTY.__objc_data: 0x11a8
-  __DATA_DIRTY.__bss: 0x110
+  __DATA_DIRTY.__objc_data: 0x12e8
+  __DATA_DIRTY.__bss: 0x148
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: ABDA4A69-D309-34B3-ABA1-8F994E188357
+  UUID: 2698557F-D0EC-343C-8F09-FC643FC53A25
   Functions: 3397
-  Symbols:   9317
-  CStrings:  4667
+  Symbols:   9316
+  CStrings:  4689
 
Symbols:
+ -[PRUISDeviceMotionProvider _cancelDampeningTimer]
+ -[PRUISDeviceMotionProvider _motionGenerationQueue_cancelDampeningTimer]
+ -[PRUISDeviceMotionProvider _motionGenerationQueue_motionProvider:motionActivityLevelDidUpdate:]
+ -[PRUISDeviceMotionProvider _motionGenerationQueue_motionProvider:motionDidUpdateWithRotation:]
+ -[PRUISDeviceMotionProvider _motionGenerationQueue_motionProvider:motionDidUpdateWithRotation:].cold.1
+ -[PRUISDeviceMotionProvider _motionGenerationQueue_processDampeningStep:]
+ -[PRUISDeviceMotionProvider _motionGenerationQueue_processDeviceMotion:]
+ -[PRUISDeviceMotionProvider _motionGenerationQueue_processDeviceMotion:].cold.1
+ -[PRUISDeviceMotionProvider _motionGenerationQueue_processDeviceMotion:].cold.2
+ -[PRUISDeviceMotionProvider _motionGenerationQueue_startDampeningToZeroFromRotation:]
+ -[PRUISDeviceMotionProvider _motionGenerationQueue_stopGeneratingMotionEventsWithActivityLevel:invalidateLightSourceSubscription:]
+ -[PRUISDeviceMotionProvider _scaleRotation:byFactor:]
+ -[PRUISMutablePosterSnapshotRequest(Deprecated) setRetryCount:]
+ -[PRUISPosterChannelController handleDidAddChannel:]
+ -[PRUISPosterChannelController handleDidRemoveChannel:]
+ -[PRUISPosterChannelController handleDidUpdateChannel:]
+ -[PRUISPosterChannelController handleWillAddChannel:]
+ -[PRUISPosterChannelController handleWillRemoveChannel:]
+ -[PRUISPosterChannelController handleWillUpdateChannel:]
+ -[PRUISPosterChannelController removeChannel:completion:]
+ -[PRUISPosterChannelModelCoordinator extensionProvider]
+ -[PRUISPosterChannelModelCoordinator initWithChannelConfiguration:extensionProvider:]
+ -[PRUISPosterChannelModelCoordinator initWithChannelConfiguration:extensionProvider:].cold.1
+ -[PRUISPosterChannelModelCoordinator initWithChannelConfiguration:extensionProvider:].cold.2
+ -[PRUISPosterChannelModelCoordinator initWithChannelConfiguration:extensionProvider:].cold.3
+ -[PRUISPosterChannelViewController viewDidAppear:]
+ -[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:].cold.4
+ -[PRUISPosterRenderingViewController extensionInstance]
+ -[PRUISPosterSnapshotRequest retryCount]
+ -[PRUISPosterSnapshotRequest setRetryCount:]
+ -[_PRUISPosterSnapshotControllerImpl snapshotterDidInvalidateScene:didWaitForSceneInvalidation:forRequest:]
+ GCC_except_table146
+ GCC_except_table155
+ GCC_except_table32
+ GCC_except_table47
+ GCC_except_table50
+ GCC_except_table52
+ GCC_except_table59
+ GCC_except_table73
+ GCC_except_table75
+ GCC_except_table85
+ OBJC_IVAR_$_PRUISPosterSnapshotRequest._retryCount
+ _OBJC_IVAR_$_PRUISDeviceMotionProvider._dampeningDuration
+ _OBJC_IVAR_$_PRUISDeviceMotionProvider._dampeningMultiplier
+ _OBJC_IVAR_$_PRUISDeviceMotionProvider._dampeningTimer
+ _OBJC_IVAR_$_PRUISDeviceMotionProvider._lock_isDampening
+ _OBJC_IVAR_$_PRUISDeviceMotionProvider._lock_lastKnownRotation
+ _OBJC_IVAR_$_PRUISPosterChannel._completionScheduler
+ _OBJC_IVAR_$_PRUISPosterChannel._observerQueue
+ _OBJC_IVAR_$_PRUISPosterChannelController._completionScheduler
+ _OBJC_IVAR_$_PRUISPosterChannelController._extensionProvider
+ _OBJC_IVAR_$_PRUISPosterChannelController._modelCoordinatorScheduler
+ _OBJC_IVAR_$_PRUISPosterChannelController._modelCoordinatorScheduler_channelForUUID
+ _OBJC_IVAR_$_PRUISPosterChannelController._observerQueue
+ _OBJC_IVAR_$_PRUISPosterChannelController._reapScheduler
+ _OBJC_IVAR_$_PRUISPosterChannelModelCoordinator._extensionProvider
+ _OBJC_IVAR_$_PRUISPosterRenderingViewController._pendTransitionToRenderingModeOnViewDidAppear
+ _OUTLINED_FUNCTION_15
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PUIPosterSnapshotterDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PUIPosterSnapshotterDelegate
+ __OBJC_$_PROTOCOL_REFS_PRRenderingEventSupporting
+ __OBJC_$_PROTOCOL_REFS_PUIPosterSnapshotterDelegate
+ __OBJC_LABEL_PROTOCOL_$_PUIPosterSnapshotterDelegate
+ __OBJC_PROTOCOL_$_PUIPosterSnapshotterDelegate
+ __ZL10simd_slerp10simd_quatdS_d
+ ___50-[PRUISDeviceMotionProvider _cancelDampeningTimer]_block_invoke
+ ___51-[PRUISPosterChannel _notifyObserversDidInvalidate]_block_invoke_2
+ ___52-[PRUISPosterChannel _notifyObserversWillInvalidate]_block_invoke_2
+ ___52-[PRUISPosterChannelController handleDidAddChannel:]_block_invoke
+ ___52-[PRUISPosterRenderingViewController viewDidAppear:]_block_invoke
+ ___53-[PRUISPosterChannelController handleWillAddChannel:]_block_invoke
+ ___54-[PRUISPosterChannel _notifyObserversDidUpdatePoster:]_block_invoke_2
+ ___54-[PRUISPosterChannel _notifyObserversWillUpdatePoster]_block_invoke_2
+ ___54-[PRUISPosterChannelController initWithConfiguration:]_block_invoke.101
+ ___54-[PRUISPosterChannelController initWithConfiguration:]_block_invoke_2.108
+ ___55-[PRUISPosterChannel _notifyObserversDidUpdateContext:]_block_invoke_2
+ ___55-[PRUISPosterChannel _notifyObserversDidUpdateGallery:]_block_invoke_2
+ ___55-[PRUISPosterChannel _notifyObserversWillUpdateContext]_block_invoke_2
+ ___55-[PRUISPosterChannel _notifyObserversWillUpdateGallery]_block_invoke_2
+ ___55-[PRUISPosterChannelController handleDidRemoveChannel:]_block_invoke
+ ___55-[PRUISPosterChannelController handleDidUpdateChannel:]_block_invoke
+ ___56-[PRUISPosterChannelController handleWillRemoveChannel:]_block_invoke
+ ___56-[PRUISPosterChannelController handleWillUpdateChannel:]_block_invoke
+ ___56-[PRUISPosterRenderingViewController applyVisualEffect:]_block_invoke.125
+ ___56-[PRUISPosterRenderingViewController applyVisualEffect:]_block_invoke.125.cold.1
+ ___57-[PRUISPosterChannelController removeChannel:completion:]_block_invoke
+ ___60-[PRUISPosterChannel fetchSnapshotForDescriptor:completion:]_block_invoke_3
+ ___60-[PRUISPosterChannel fetchSnapshotForDescriptor:completion:]_block_invoke_4
+ ___60-[PRUISPosterChannel fetchSnapshotForDescriptor:completion:]_block_invoke_5
+ ___60-[PRUISPosterChannel fetchSnapshotForDescriptor:completion:]_block_invoke_5.cold.1
+ ___60-[PRUISPosterChannel fetchSnapshotForDescriptor:completion:]_block_invoke_5.cold.2
+ ___60-[PRUISPosterChannelViewController channel:didUpdatePoster:]_block_invoke_7
+ ___66-[PRUISPosterChannelViewController _teardownPosterViewController:]_block_invoke.116
+ ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke.93
+ ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke.93.cold.1
+ ___75-[PRUISPosterChannelController _fireObserversRespondingToSelector:handler:]_block_invoke_2
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.106
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.106.cold.1
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.111
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.115
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.87
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.87.cold.1
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.89
+ ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.98
+ ___85-[PRUISDeviceMotionProvider _motionGenerationQueue_startDampeningToZeroFromRotation:]_block_invoke
+ ___85-[PRUISPosterChannelModelCoordinator initWithChannelConfiguration:extensionProvider:]_block_invoke
+ ___85-[PRUISPosterChannelModelCoordinator initWithChannelConfiguration:extensionProvider:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSNull"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e40_v24?0"PRUISPosterChannel"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e40_v24?0"PRUISPosterGallery"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e35_"<PFTFuture>"16?0"NSDictionary"8ls32l8
+ ___block_descriptor_40_e8_32s_e44_v16?0"PRUISPosterRenderingViewController"8ls32l8
+ ___block_descriptor_40_e8_32w_e68_v24?0"PRUISPosterRenderingViewController"8"BSAnimationSettings"16lw32l8
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e47_v24?0"PRUISPosterSnapshotBundle"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e5_v8?0lw56l8s32l8s48l8s40l8
+ ___block_descriptor_72_e16_64w_e29_v16?0"BSAbsoluteMachTimer"8lw64l8
+ ___swift_memcpy0_1
+ _get_witness_table 7SwiftUI15ModifiedContentVyACyAA6SliderVyAA4TextVAA9EmptyViewVGAA14_PaddingLayoutVGAA19_BackgroundModifierVyACyAA06_ShapeH0VyAA16RoundedRectangleVAA5ColorVGALGGGSgAA0H0HpAyAA_HPAmAA_HPAjAA_HPyHC_AlA0hL0HPyHCHC_AxAA0_HPyHCHC_HC.57
+ _get_witness_table qd0__7SwiftUI4ViewHD3_AaBPAAE8onChange2of7initial_Qrqd___SbyyctSQRd__lFQOyAcAE0D10TapGesture5count7performQrSi_yyctFQOyAcAEAgH15coordinateSpaceAIQrSi_qd__ySo7CGPointVctAA010CoordinateM8ProtocolRd__lFQOyAA01_C16Modifier_ContentVy21PosterBoardUIServices36RenderingEventsAndTransitionsSupportO011CoordinatorQ0VG_AA05LocaloM0VQo__Qo__12CoreGraphics7CGFloatVQo_HO.56
+ _initWithChannelConfiguration:extensionProvider:.onceToken
+ _objc_msgSend$_cancelDampeningTimer
+ _objc_msgSend$_motionGenerationQueue_cancelDampeningTimer
+ _objc_msgSend$_motionGenerationQueue_motionProvider:motionActivityLevelDidUpdate:
+ _objc_msgSend$_motionGenerationQueue_motionProvider:motionDidUpdateWithRotation:
+ _objc_msgSend$_motionGenerationQueue_processDampeningStep:
+ _objc_msgSend$_motionGenerationQueue_processDeviceMotion:
+ _objc_msgSend$_motionGenerationQueue_startDampeningToZeroFromRotation:
+ _objc_msgSend$_motionGenerationQueue_stopGeneratingMotionEventsWithActivityLevel:invalidateLightSourceSubscription:
+ _objc_msgSend$_scaleRotation:byFactor:
+ _objc_msgSend$addCompletionBlock:scheduler:
+ _objc_msgSend$flatMap:continuationScheduler:
+ _objc_msgSend$handleDidAddChannel:
+ _objc_msgSend$handleDidRemoveChannel:
+ _objc_msgSend$handleDidUpdateChannel:
+ _objc_msgSend$handleWillAddChannel:
+ _objc_msgSend$handleWillRemoveChannel:
+ _objc_msgSend$handleWillUpdateChannel:
+ _objc_msgSend$initWithChannelConfiguration:extensionProvider:
+ _objc_msgSend$initWithPath:sceneSettingsApplicator:priority:snapshotDescriptor:retryCount:timeout:
+ _objc_msgSend$initWithScene:
+ _objc_msgSend$isDeviceMotionDisabled
+ _objc_msgSend$removeChannel:completion:
+ _objc_msgSend$retryCount
+ _objc_msgSend$serialDispatchQueueSchedulerWithName:qualityOfService:
+ _objc_msgSend$setRetryCount:
+ _objc_msgSend$startWithImmediateQueryExecution:
+ _pow
- -[PRUISDeviceMotionController _createDampeningTimerWithDuration:]
- -[PRUISDeviceMotionController _dampenRotationData]
- -[PRUISDeviceMotionController _dampenRotationData].cold.1
- -[PRUISDeviceMotionController _resetDampening]
- -[PRUISDeviceMotionController _stopDampeningIfNeeded]
- -[PRUISDeviceMotionController dampeningDuration]
- -[PRUISDeviceMotionController dampeningTimer]
- -[PRUISDeviceMotionController decrementInterval]
- -[PRUISDeviceMotionController isDampening]
- -[PRUISDeviceMotionController multiplier]
- -[PRUISDeviceMotionController setDampeningDuration:]
- -[PRUISDeviceMotionController setDampeningTimer:]
- -[PRUISDeviceMotionController setDecrementInterval:]
- -[PRUISDeviceMotionController setIsDampening:]
- -[PRUISDeviceMotionController setMultiplier:]
- -[PRUISDeviceMotionController stopGeneratingMotionEventsWithDampeningDuration:]
- -[PRUISDeviceMotionProvider _motionGenerationQueue_pauseGeneratingMotionEvents]
- -[PRUISDeviceMotionProvider _motionGenerationQueue_stopGeneratingMotionEvents]
- -[PRUISDeviceMotionProvider _queue_motionProvider:motionActivityLevelDidUpdate:]
- -[PRUISDeviceMotionProvider _queue_motionProvider:motionDidUpdateWithRotation:]
- -[PRUISDeviceMotionProvider _queue_processDeviceMotion:]
- -[PRUISDeviceMotionProvider _queue_processDeviceMotion:].cold.1
- -[PRUISDeviceMotionProvider _queue_processDeviceMotion:].cold.2
- -[PRUISDeviceMotionProvider _queue_processDeviceMotion:].cold.3
- -[PRUISPosterChannelController _handleDidAddChannel:]
- -[PRUISPosterChannelController _handleDidRemoveChannel:]
- -[PRUISPosterChannelController _handleDidUpdateChannel:]
- -[PRUISPosterChannelController _handleWillAddChannel:]
- -[PRUISPosterChannelController _handleWillRemoveChannel:]
- -[PRUISPosterChannelController _handleWillUpdateChannel:]
- -[PRUISPosterChannelModelCoordinator initWithChannelConfiguration:]
- -[PRUISPosterChannelModelCoordinator initWithChannelConfiguration:].cold.1
- -[PRUISPosterChannelModelCoordinator initWithChannelConfiguration:].cold.2
- -[PRUISPosterChannelModelCoordinator initWithChannelConfiguration:].cold.3
- -[PRUISPosterChannelViewController _relinquishExtensionInstance:]
- -[PRUISPosterEditingViewController deviceMotionEventGenerationDidStop]
- -[PRUISPosterEditingViewController deviceMotionEventGenerationWillStart]
- -[PRUISPosterEditingViewController stopSendingMotionEventsWithDampeningDuration:]
- -[PRUISPosterRenderingViewController deviceMotionEventGenerationDidStop]
- -[PRUISPosterRenderingViewController deviceMotionEventGenerationWillStart]
- -[PRUISPosterRenderingViewController stopSendingMotionEventsWithDampeningDuration:]
- GCC_except_table148
- GCC_except_table157
- GCC_except_table20
- GCC_except_table27
- GCC_except_table31
- GCC_except_table33
- GCC_except_table37
- GCC_except_table46
- GCC_except_table57
- GCC_except_table6
- GCC_except_table70
- GCC_except_table71
- GCC_except_table83
- GCC_except_table86
- _OBJC_CLASS_$_PRRenderingServiceServerKeepAliveAssertionManager
- _OBJC_IVAR_$_PRUISDeviceMotionController._dampeningDuration
- _OBJC_IVAR_$_PRUISDeviceMotionController._dampeningTimer
- _OBJC_IVAR_$_PRUISDeviceMotionController._decrementInterval
- _OBJC_IVAR_$_PRUISDeviceMotionController._isDampening
- _OBJC_IVAR_$_PRUISDeviceMotionController._multiplier
- _OBJC_IVAR_$_PRUISDeviceMotionProvider._motionProviderQueue
- _OBJC_IVAR_$_PRUISPosterChannel._extensionProvider
- _OBJC_IVAR_$_PRUISPosterChannelController._automaticReapScheduler
- _OBJC_IVAR_$_PRUISPosterChannelController._scheduler
- _OBJC_IVAR_$_PRUISPosterChannelController._scheduler_channelForUUID
- ___104-[PRUISPosterChannel updateGalleryWithUpdateSessionInfoProvider:extensionIdentifiers:policy:completion:]_block_invoke_2
- ___175-[PRUISPosterRenderingViewController initWithPosterContents:context:boundingShape:extensionInstance:snapshotController:initialSnapshotBundle:renderingMode:snapshotDefinition:]_block_invoke
- ___53-[PRUISPosterChannelController _handleDidAddChannel:]_block_invoke
- ___54-[PRUISPosterChannelController _handleWillAddChannel:]_block_invoke
- ___54-[PRUISPosterChannelController initWithConfiguration:]_block_invoke.86
- ___54-[PRUISPosterChannelController initWithConfiguration:]_block_invoke_4
- ___56-[PRUISPosterChannelController _handleDidRemoveChannel:]_block_invoke
- ___56-[PRUISPosterChannelController _handleDidUpdateChannel:]_block_invoke
- ___56-[PRUISPosterChannelController _handleDidUpdateChannel:]_block_invoke.161
- ___56-[PRUISPosterRenderingViewController applyVisualEffect:]_block_invoke.124
- ___56-[PRUISPosterRenderingViewController applyVisualEffect:]_block_invoke.124.cold.1
- ___57-[PRUISPosterChannelController _handleWillRemoveChannel:]_block_invoke
- ___57-[PRUISPosterChannelController _handleWillUpdateChannel:]_block_invoke
- ___60-[PRUISPosterChannel fetchSnapshotForDescriptor:completion:]_block_invoke_2.cold.1
- ___60-[PRUISPosterChannel fetchSnapshotForDescriptor:completion:]_block_invoke_2.cold.2
- ___65-[PRUISDeviceMotionController _createDampeningTimerWithDuration:]_block_invoke
- ___65-[PRUISPosterChannelController updateChannel:updater:completion:]_block_invoke_2
- ___67-[PRUISPosterChannelModelCoordinator initWithChannelConfiguration:]_block_invoke
- ___67-[PRUISPosterChannelModelCoordinator initWithChannelConfiguration:]_block_invoke_2
- ___68-[PRUISPosterChannelController reapEverythingForChannel:completion:]_block_invoke_2
- ___68-[PRUISPosterChannelController reapEverythingForChannel:completion:]_block_invoke_3
- ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke.91
- ___71-[PRUISPosterChannelViewController _snapshotCurrentPosterConfiguration]_block_invoke.91.cold.1
- ___72-[PRUISPosterChannelController reapStaleSnapshotsForChannel:completion:]_block_invoke_2
- ___72-[PRUISPosterChannelController reapStaleSnapshotsForChannel:completion:]_block_invoke_3
- ___79-[PRUISPosterChannelController createChannelWithIdentifier:updater:completion:]_block_invoke_2
- ___81-[PRUISPosterChannelController reapStaleStateForChannel:omittingLast:completion:]_block_invoke_2
- ___81-[PRUISPosterChannelController reapStaleStateForChannel:omittingLast:completion:]_block_invoke_3
- ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.105
- ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.105.cold.1
- ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.110
- ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.114
- ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.86
- ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.86.cold.1
- ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.88
- ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke.97
- ___Block_byref_object_copy_.99
- ___Block_byref_object_dispose_.100
- ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_40_e8_32bs_e28_v16?0"PRUISPosterChannel"8ls32l8
- ___block_descriptor_40_e8_32bs_e28_v16?0"PRUISPosterGallery"8ls32l8
- ___block_descriptor_40_e8_32r_e16_v16?0"NSNull"8lr32l8
- ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8lr32l8
- ___block_descriptor_40_e8_32w_e29_v16?0"BSAbsoluteMachTimer"8lw32l8
- ___block_descriptor_40_e8_32w_e98_v32?0"PRUISPosterRenderingViewController"8"PFPosterExtensionInstance"16"BSAnimationSettings"24lw32l8
- ___block_descriptor_48_e8_32s40bs_e47_v24?0"PRUISPosterSnapshotBundle"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e44_v16?0"PRUISPosterRenderingViewController"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e35_"<PFTFuture>"16?0"NSDictionary"8ls32l8w40l8
- ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls48l8s32l8s40l8
- _get_witness_table 7SwiftUI15ModifiedContentVyACyAA6SliderVyAA4TextVAA9EmptyViewVGAA14_PaddingLayoutVGAA19_BackgroundModifierVyACyAA06_ShapeH0VyAA16RoundedRectangleVAA5ColorVGALGGGSgAA0H0HpAyAA_HPAmAA_HPAjAA_HPyHC_AlA0hL0HPyHCHC_AxAA0_HPyHCHC_HC.53
- _get_witness_table qd0__7SwiftUI4ViewHD3_AaBPAAE8onChange2of7initial_Qrqd___SbyyctSQRd__lFQOyAcAE0D10TapGesture5count7performQrSi_yyctFQOyAcAEAgH15coordinateSpaceAIQrSi_qd__ySo7CGPointVctAA010CoordinateM8ProtocolRd__lFQOyAA01_C16Modifier_ContentVy21PosterBoardUIServices36RenderingEventsAndTransitionsSupportO011CoordinatorQ0VG_AA05LocaloM0VQo__Qo__12CoreGraphics7CGFloatVQo_HO.52
- _initWithChannelConfiguration:.onceToken
- _objc_msgSend$_createDampeningTimerWithDuration:
- _objc_msgSend$_dampenRotationData
- _objc_msgSend$_handleDidAddChannel:
- _objc_msgSend$_handleDidRemoveChannel:
- _objc_msgSend$_handleDidUpdateChannel:
- _objc_msgSend$_handleWillAddChannel:
- _objc_msgSend$_handleWillRemoveChannel:
- _objc_msgSend$_handleWillUpdateChannel:
- _objc_msgSend$_motionGenerationQueue_pauseGeneratingMotionEvents
- _objc_msgSend$_motionGenerationQueue_stopGeneratingMotionEvents
- _objc_msgSend$_motionProvider:motionDidUpdateWithRotation:
- _objc_msgSend$_queue_motionProvider:motionActivityLevelDidUpdate:
- _objc_msgSend$_queue_motionProvider:motionDidUpdateWithRotation:
- _objc_msgSend$_queue_processDeviceMotion:
- _objc_msgSend$_relinquishExtensionInstance:
- _objc_msgSend$_resetDampening
- _objc_msgSend$_stopDampeningIfNeeded
- _objc_msgSend$deviceMotionEventGenerationDidStop
- _objc_msgSend$deviceMotionEventGenerationWillStart
- _objc_msgSend$initWithChannelConfiguration:
- _objc_msgSend$initWithPath:sceneSettingsApplicator:priority:snapshotDescriptor:timeout:
- _objc_msgSend$initWithScene:renderingServiceServerKeepAliveAssertionManager:
- _objc_msgSend$renderingServiceServer
- _objc_msgSend$scheduleWithFireInterval:leewayInterval:queue:handler:
- _objc_msgSend$serialDispatchQueueSchedulerWithName:
- _objc_msgSend$stopGeneratingMotionEventsWithDampeningDuration:
- _objc_msgSend$stopSendingMotionEventsWithDampeningDuration:
CStrings:
+ "\f"
+ "#P"
+ "%@ motion updates"
+ "%@-%@"
+ "%@-CompletionQueue"
+ "%@-ModelCoordinatorQueue"
+ "%@-ObserverQueue"
+ "%@:%@-CompletionQueue"
+ "%@:%@-ObserverQueue"
+ "%{public}@ viewDidAppear..."
+ "(?={?=}{?=})56@0:8(?={?=}{?=})16d48"
+ "<%{public}@:%{public}p> In the middle of pending transition to rendering mode %@, bailing"
+ "?"
+ "@\"PFServerPosterIdentity\""
+ "Can't start motion generation because device motion updates are currently disabled."
+ "Dampening complete - reached zero rotation"
+ "PRUISDeviceMotionProvider.dampening"
+ "PUIPosterSnapshotterDelegate"
+ "Pausing"
+ "Rotation data: x: %f, y: %f, z: %f, w: %f"
+ "Starting dampening motion to zero over %f seconds"
+ "Stopping"
+ "T@\"PRUISPosterSnapshotDescriptor\",&,N,V_snapshotDescriptor"
+ "TQ,N,V_retryCount"
+ "[%{public}@]: %{public}@, but we're still expecting more work from this snapshotter"
+ "[%{public}@]: %{public}@, remaining running snapshotters: %{public}lu, request: %{public}@"
+ "_cancelDampeningTimer"
+ "_completionScheduler"
+ "_dampeningMultiplier"
+ "_lock_isDampening"
+ "_lock_lastKnownRotation"
+ "_modelCoordinatorScheduler"
+ "_modelCoordinatorScheduler_channelForUUID"
+ "_motionGenerationQueue_cancelDampeningTimer"
+ "_motionGenerationQueue_motionProvider:motionActivityLevelDidUpdate:"
+ "_motionGenerationQueue_motionProvider:motionDidUpdateWithRotation:"
+ "_motionGenerationQueue_processDampeningStep:"
+ "_motionGenerationQueue_processDeviceMotion:"
+ "_motionGenerationQueue_startDampeningToZeroFromRotation:"
+ "_motionGenerationQueue_stopGeneratingMotionEventsWithActivityLevel:invalidateLightSourceSubscription:"
+ "_pendTransitionToRenderingModeOnViewDidAppear"
+ "_reapScheduler"
+ "_retryCount"
+ "_scaleRotation:byFactor:"
+ "addCompletionBlock:scheduler:"
+ "flatMap:continuationScheduler:"
+ "handleDidAddChannel:"
+ "handleDidRemoveChannel:"
+ "handleDidUpdateChannel:"
+ "handleWillAddChannel:"
+ "handleWillRemoveChannel:"
+ "handleWillUpdateChannel:"
+ "initWithChannelConfiguration:extensionProvider:"
+ "initWithPath:sceneSettingsApplicator:priority:snapshotDescriptor:retryCount:timeout:"
+ "initWithScene:"
+ "removeChannel:completion:"
+ "retryCount"
+ "serialDispatchQueueSchedulerWithName:qualityOfService:"
+ "setRetryCount:"
+ "snapshotterDidInvalidateScene:didWaitForSceneInvalidation:forRequest:"
+ "startWithImmediateQueryExecution:"
+ "v24@?0@\"NSNull\"8@\"NSError\"16"
+ "v24@?0@\"PRUISPosterChannel\"8@\"NSError\"16"
+ "v24@?0@\"PRUISPosterGallery\"8@\"NSError\"16"
+ "v24@?0@\"PRUISPosterRenderingViewController\"8@\"BSAnimationSettings\"16"
+ "v28@0:8q16B24"
+ "v36@0:8@\"PUIPosterSnapshotter\"16B24@\"PUIPosterSnapshotRequest\"28"
+ "v36@0:8@16B24@28"
+ "\xf0\xc1"
+ "\xf0\xf0B"
- "\v"
- "PRUISDeviceMotionController.dampeningTimer"
- "Pausing motion updates"
- "Relative rotation data: x: %f, y: %f, z: %f, w: %f"
- "Stopping motion updates"
- "T@\"BSAbsoluteMachTimer\",&,N,V_dampeningTimer"
- "T@\"PRUISPosterSnapshotDescriptor\",R,N,V_snapshotDescriptor"
- "TB,N,V_isDampening"
- "Td,N,V_dampeningDuration"
- "Td,N,V_decrementInterval"
- "Td,N,V_multiplier"
- "Updated dampening multiplier to %.03f"
- "_automaticReapScheduler"
- "_createDampeningTimerWithDuration:"
- "_dampenRotationData"
- "_decrementInterval"
- "_handleDidAddChannel:"
- "_handleDidRemoveChannel:"
- "_handleDidUpdateChannel:"
- "_handleWillAddChannel:"
- "_handleWillRemoveChannel:"
- "_handleWillUpdateChannel:"
- "_isDampening"
- "_motionGenerationQueue_pauseGeneratingMotionEvents"
- "_motionGenerationQueue_stopGeneratingMotionEvents"
- "_motionProviderQueue"
- "_multiplier"
- "_queue_motionProvider:motionActivityLevelDidUpdate:"
- "_queue_motionProvider:motionDidUpdateWithRotation:"
- "_queue_processDeviceMotion:"
- "_relinquishExtensionInstance:"
- "_resetDampening"
- "_scheduler_channelForUUID"
- "_stopDampeningIfNeeded"
- "com.apple.PosterBoardUIServices.PRUISDeviceMotionProvider.motionProviderQueue"
- "dampeningDuration"
- "dampeningTimer"
- "decrementInterval"
- "deviceMotionEventGenerationDidStop"
- "deviceMotionEventGenerationWillStart"
- "initWithChannelConfiguration:"
- "initWithPath:sceneSettingsApplicator:priority:snapshotDescriptor:timeout:"
- "initWithScene:renderingServiceServerKeepAliveAssertionManager:"
- "isDampening"
- "multiplier"
- "renderingServiceServer"
- "scheduleWithFireInterval:leewayInterval:queue:handler:"
- "serialDispatchQueueSchedulerWithName:"
- "setDampeningDuration:"
- "setDampeningTimer:"
- "setDecrementInterval:"
- "setIsDampening:"
- "setMultiplier:"
- "stopGeneratingMotionEventsWithDampeningDuration:"
- "stopSendingMotionEventsWithDampeningDuration:"
- "v16@?0@\"NSNull\"8"
- "v32@?0@\"PRUISPosterRenderingViewController\"8@\"PFPosterExtensionInstance\"16@\"BSAnimationSettings\"24"
- "\xd1"
- "\xf01"
- "\xf0\xf02"

```
