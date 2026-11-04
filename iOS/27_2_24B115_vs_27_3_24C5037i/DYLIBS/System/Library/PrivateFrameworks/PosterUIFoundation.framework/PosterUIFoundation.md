## PosterUIFoundation

> `/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation`

```diff

-355.2.12.101.0
-  __TEXT.__text: 0x92f34
-  __TEXT.__objc_methlist: 0xac14
-  __TEXT.__const: 0xde4
-  __TEXT.__oslogstring: 0x40c1
-  __TEXT.__cstring: 0x6913
-  __TEXT.__gcc_except_tab: 0x1898
-  __TEXT.__dlopen_cstrs: 0x216
+355.3.7.0.0
+  __TEXT.__text: 0x96008
+  __TEXT.__objc_methlist: 0xafe4
+  __TEXT.__const: 0xe34
+  __TEXT.__cstring: 0x6b53
+  __TEXT.__oslogstring: 0x4141
+  __TEXT.__gcc_except_tab: 0x1920
+  __TEXT.__dlopen_cstrs: 0x272
   __TEXT.__swift5_typeref: 0x80a
   __TEXT.__constg_swiftt: 0x708
   __TEXT.__swift5_reflstr: 0x113

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x2c
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x3418
+  __TEXT.__unwind_info: 0x3568
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2778
-  __DATA_CONST.__objc_classlist: 0x518
-  __DATA_CONST.__objc_catlist: 0xe0
-  __DATA_CONST.__objc_protolist: 0x1c0
+  __DATA_CONST.__const: 0x2888
+  __DATA_CONST.__objc_classlist: 0x550
+  __DATA_CONST.__objc_catlist: 0xe8
+  __DATA_CONST.__objc_protolist: 0x1d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5980
+  __DATA_CONST.__objc_selrefs: 0x5be0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x410
-  __DATA_CONST.__objc_arraydata: 0x19d0
-  __DATA_CONST.__got: 0xff8
-  __AUTH_CONST.__const: 0x1100
-  __AUTH_CONST.__cfstring: 0x8180
-  __AUTH_CONST.__objc_const: 0x1f228
-  __AUTH_CONST.__objc_dictobj: 0xd70
-  __AUTH_CONST.__objc_intobj: 0xe10
+  __DATA_CONST.__objc_superrefs: 0x428
+  __DATA_CONST.__objc_arraydata: 0x1a60
+  __DATA_CONST.__got: 0x1090
+  __AUTH_CONST.__const: 0x1140
+  __AUTH_CONST.__cfstring: 0x8400
+  __AUTH_CONST.__objc_const: 0x201f0
+  __AUTH_CONST.__objc_dictobj: 0xde8
+  __AUTH_CONST.__objc_intobj: 0xe70
   __AUTH_CONST.__objc_doubleobj: 0x2b0
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_floatobj: 0x10
-  __AUTH_CONST.__auth_got: 0x1110
-  __AUTH.__objc_data: 0x2500
+  __AUTH_CONST.__auth_got: 0x1138
+  __AUTH.__objc_data: 0x2730
   __AUTH.__data: 0x1a0
-  __DATA.__objc_ivar: 0xbec
-  __DATA.__data: 0x17e0
+  __DATA.__objc_ivar: 0xc18
+  __DATA.__data: 0x18b0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xdc0
-  __DATA_DIRTY.__bss: 0xe0
+  __DATA_DIRTY.__bss: 0xd0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4180
-  Symbols:   7471
-  CStrings:  1543
+  Functions: 4262
+  Symbols:   7667
+  CStrings:  1566
 
Symbols:
+ +[PUIHingeState supportsSecureCoding]
+ +[PUIPosterSnapshotDeadline deadlineAtContinuousTime:]
+ +[PUIPosterSnapshotDeadline deadlineWithBudget:]
+ +[PUIPosterSnapshotDeadline supportsSecureCoding]
+ +[PUISceneResolverBridgeExtension hostComponents]
+ -[FBSMutableSceneSettings(PosterUIFoundation) pui_setComplicationColumnConfigured:]
+ -[FBSMutableSceneSettings(PosterUIFoundation) pui_setSnapshotDeadlineContinuousTime:]
+ -[FBSMutableSceneSettings(PosterUIFoundation) pui_setSuppressesPresentationGraces:]
+ -[FBSSceneSettings(PosterUIFoundation) pui_isComplicationColumnConfigured]
+ -[FBSSceneSettings(PosterUIFoundation) pui_snapshotDeadlineContinuousTime]
+ -[FBSSceneSettings(PosterUIFoundation) pui_suppressesPresentationGraces]
+ -[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:invalidateSnapshottingAssertion:]
+ -[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:invalidateSnapshottingAssertion:]
+ -[FBScene(PosterUIFoundation) _pui_executeOutOfProcessSnapshotWithPromise:descriptor:outputDestination:snapshottingAssertion:invalidateSnapshottingAssertion:]
+ -[FBScene(PosterUIFoundation) _pui_finishAndCleanupSnapshottingPromise:bundle:outputDestination:snapshottingAssertion:error:invalidateSnapshottingAssertion:]
+ -[PUIHingeState angleDegrees]
+ -[PUIHingeState copyWithZone:]
+ -[PUIHingeState description]
+ -[PUIHingeState encodeWithCoder:]
+ -[PUIHingeState hash]
+ -[PUIHingeState hingeProgress]
+ -[PUIHingeState initWithCoder:]
+ -[PUIHingeState initWithStatus:angleDegrees:]
+ -[PUIHingeState isEqual:]
+ -[PUIHingeState isEqualToHingeState:]
+ -[PUIHingeState status]
+ -[PUIMainDisplayTransformer transformDisplayConfiguration:]
+ -[PUIMappedImageCacheManager _cacheLock_scheduleManifestWrite]
+ -[PUIMappedImageCacheManager manifestIOQueue]
+ -[PUIMappedImageCacheManager manifestURL]
+ -[PUIPosterSnapshotDeadline _initWithContinuousTime:]
+ -[PUIPosterSnapshotDeadline continuousTime]
+ -[PUIPosterSnapshotDeadline copyWithZone:]
+ -[PUIPosterSnapshotDeadline description]
+ -[PUIPosterSnapshotDeadline encodeWithCoder:]
+ -[PUIPosterSnapshotDeadline hash]
+ -[PUIPosterSnapshotDeadline initWithCoder:]
+ -[PUIPosterSnapshotDeadline intervalBoundedByRemaining:]
+ -[PUIPosterSnapshotDeadline intervalBoundedByRemaining:atContinuousTime:]
+ -[PUIPosterSnapshotDeadline intervalForStage:]
+ -[PUIPosterSnapshotDeadline intervalForStage:atContinuousTime:]
+ -[PUIPosterSnapshotDeadline isEqual:]
+ -[PUIPosterSnapshotDeadline isExpired]
+ -[PUIPosterSnapshotDeadline remainingAtContinuousTime:]
+ -[PUIPosterSnapshotDeadline remainingLessReserve:]
+ -[PUIPosterSnapshotDeadline remaining]
+ -[PUIPosterSnapshotDescriptor copyWithDeadline:]
+ -[PUIPosterSnapshotHostConfigurationDescriptor copyWithDeadline:]
+ -[PUIPosterSnapshotHostConfigurationDescriptor deadline]
+ -[PUIPosterSnapshotHostConfigurationDescriptor initWithHostWorkQueue:waitUntilReady:inProcessSnapshot:abortsIfBacklightNotFull:captureTimeoutInterval:deadline:]
+ -[PUISceneResolverBridge .cxx_destruct]
+ -[PUISceneResolverBridge _forwardBarPositionResolvers]
+ -[PUISceneResolverBridge barPositionClientDidChangeResolvers:]
+ -[PUISceneResolverBridge dealloc]
+ -[PUISceneResolverBridge initWithScene:]
+ -[PUISceneResolverBridge invalidate]
+ -[PUISceneResolverBridge parentScene]
+ -[PUISceneResolverBridge setParentScene:]
+ -[PUISceneResolverBridgeHostComponent .cxx_destruct]
+ -[PUISceneResolverBridgeHostComponent parentScene]
+ -[PUISceneResolverBridgeHostComponent scene:willUpdateSettings:withTransitionContext:]
+ -[PUISceneResolverBridgeHostComponent setParentScene:]
+ -[PUIStylePickerHomeScreenComponentViewController _layoutAsPad]
+ -[PUIStylePickerHomeScreenComponentViewController estimatedWidth]
+ -[PUIStylePickerViewController _calculatePreferredContentWidth]
+ -[UISheetPresentationController(PosterUIFoundation) pui_applyPosterEditorGlassBackground]
+ -[UIView(PUIRedMode) pui_applyRedModeFilterAnimated:withCompletion:]
+ -[UIView(PUIRedMode) pui_applyRedModeFilterAnimated:withCoordinatedAnimationBlock:completion:]
+ -[UIView(PUIRedMode) pui_clearRedModeFilterAnimated:withCompletion:]
+ -[UIView(PUIRedMode) pui_clearRedModeFilterAnimated:withCoordinatedAnimationBlock:completion:]
+ -[UIView(PUIRedMode) shouldUseColorMatrixFilter]
+ GCC_except_table29
+ GCC_except_table32
+ GCC_except_table33
+ GCC_except_table34
+ GCC_except_table89
+ _BSHashPurifyNS
+ _OBJC_CLASS_$_BSAnimationSettings
+ _OBJC_CLASS_$_BSCornerRadiusConfiguration
+ _OBJC_CLASS_$_FBSDisplayConfigurationBuilder
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_PUIHingeState
+ _OBJC_CLASS_$_PUIMainDisplayTransformer
+ _OBJC_CLASS_$_PUIPosterPagedEditingSceneSpecification
+ _OBJC_CLASS_$_PUIPosterSnapshotDeadline
+ _OBJC_CLASS_$_PUISceneResolverBridge
+ _OBJC_CLASS_$_PUISceneResolverBridgeExtension
+ _OBJC_CLASS_$_PUISceneResolverBridgeHostComponent
+ _OBJC_CLASS_$_UISheetPresentationController
+ _OBJC_IVAR_$_PUIHingeState._angleDegrees
+ _OBJC_IVAR_$_PUIHingeState._hingeProgress
+ _OBJC_IVAR_$_PUIHingeState._status
+ _OBJC_IVAR_$_PUIMappedImageCacheManager._manifestIOQueue
+ _OBJC_IVAR_$_PUIPosterSceneSnapshotter._mainQueue_deadline
+ _OBJC_IVAR_$_PUIPosterSnapshotDeadline._continuousTime
+ _OBJC_IVAR_$_PUIPosterSnapshotHostConfigurationDescriptor._deadline
+ _OBJC_IVAR_$_PUISceneResolverBridge._hostComponent
+ _OBJC_IVAR_$_PUISceneResolverBridge._parentScene
+ _OBJC_IVAR_$_PUISceneResolverBridge._scene
+ _OBJC_IVAR_$_PUISceneResolverBridgeHostComponent._parentScene
+ _OBJC_METACLASS_$_PUIHingeState
+ _OBJC_METACLASS_$_PUIMainDisplayTransformer
+ _OBJC_METACLASS_$_PUIPosterPagedEditingSceneSpecification
+ _OBJC_METACLASS_$_PUIPosterSnapshotDeadline
+ _OBJC_METACLASS_$_PUISceneResolverBridge
+ _OBJC_METACLASS_$_PUISceneResolverBridgeExtension
+ _OBJC_METACLASS_$_PUISceneResolverBridgeHostComponent
+ _PFDeviceGlyphSystemImageName
+ _PFPosterRoleAmbient
+ _PF_IS_V68_DEVICE
+ _PUIPosterSnapshotDeadlineContinuousTimeNow
+ _PUIPosterSnapshotDeadlineContinuousTimeNow.onceToken
+ _PUIPosterSnapshotDeadlineContinuousTimeNow.timebase
+ _PUIPosterSnapshotDeadlineExtensionResponseReserve
+ _PUIPosterSnapshotDeadlineHostTransportReserve
+ _PUIPosterSnapshotMaximumWorkingBudget
+ _PUIPosterSnapshotSceneActionTimeoutInterval
+ _PUIRedModeAnimationCurve
+ _PUIRedModeAnimationDuration
+ _PUIRedModeAnimationSettings
+ _PUISceneRolePagedEditing
+ _PUIWindowSceneHostInformedOrientation
+ _PUIWindowSceneSetHostInformedOrientation
+ _PUIWindowSceneSetShouldSuppressFencedUpdates
+ _PUIWindowSceneShouldSuppressFencedUpdates
+ _SpringBoardHomeLibraryCore.frameworkLibrary
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_UISheetPresentationController_$_PosterUIFoundation
+ __OBJC_$_CATEGORY_UISheetPresentationController_$_PosterUIFoundation
+ __OBJC_$_CLASS_METHODS_PUIHingeState
+ __OBJC_$_CLASS_METHODS_PUIPosterSnapshotDeadline
+ __OBJC_$_CLASS_METHODS_PUISceneResolverBridgeExtension
+ __OBJC_$_CLASS_PROP_LIST_PUIHingeState
+ __OBJC_$_CLASS_PROP_LIST_PUIPosterSnapshotDeadline
+ __OBJC_$_INSTANCE_METHODS_PUIHingeState
+ __OBJC_$_INSTANCE_METHODS_PUIMainDisplayTransformer
+ __OBJC_$_INSTANCE_METHODS_PUIPosterSnapshotDeadline
+ __OBJC_$_INSTANCE_METHODS_PUISceneResolverBridge
+ __OBJC_$_INSTANCE_METHODS_PUISceneResolverBridgeHostComponent
+ __OBJC_$_INSTANCE_METHODS_UIView(UIKitViewHierarchy|PUIRedMode|PosterUIFoundation|PosterUIFoundation_Swift)
+ __OBJC_$_INSTANCE_VARIABLES_PUIHingeState
+ __OBJC_$_INSTANCE_VARIABLES_PUIPosterSnapshotDeadline
+ __OBJC_$_INSTANCE_VARIABLES_PUISceneResolverBridge
+ __OBJC_$_INSTANCE_VARIABLES_PUISceneResolverBridgeHostComponent
+ __OBJC_$_PROP_LIST_PUIHingeState
+ __OBJC_$_PROP_LIST_PUIMainDisplayTransformer
+ __OBJC_$_PROP_LIST_PUIPosterSnapshotDeadline
+ __OBJC_$_PROP_LIST_PUISceneResolverBridge
+ __OBJC_$_PROP_LIST_PUISceneResolverBridgeHostComponent
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FBSDisplayTransformer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__UISceneBarPositionClientObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSDisplayTransformer
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UISceneBarPositionClientObserver
+ __OBJC_$_PROTOCOL_REFS_FBSDisplayTransformer
+ __OBJC_$_PROTOCOL_REFS__UISceneBarPositionClientObserver
+ __OBJC_CLASS_PROTOCOLS_$_PUIHingeState
+ __OBJC_CLASS_PROTOCOLS_$_PUIMainDisplayTransformer
+ __OBJC_CLASS_PROTOCOLS_$_PUIPosterSnapshotDeadline
+ __OBJC_CLASS_PROTOCOLS_$_PUISceneResolverBridge
+ __OBJC_CLASS_RO_$_PUIHingeState
+ __OBJC_CLASS_RO_$_PUIMainDisplayTransformer
+ __OBJC_CLASS_RO_$_PUIPosterPagedEditingSceneSpecification
+ __OBJC_CLASS_RO_$_PUIPosterSnapshotDeadline
+ __OBJC_CLASS_RO_$_PUISceneResolverBridge
+ __OBJC_CLASS_RO_$_PUISceneResolverBridgeExtension
+ __OBJC_CLASS_RO_$_PUISceneResolverBridgeHostComponent
+ __OBJC_LABEL_PROTOCOL_$_FBSDisplayTransformer
+ __OBJC_LABEL_PROTOCOL_$__UISceneBarPositionClientObserver
+ __OBJC_METACLASS_RO_$_PUIHingeState
+ __OBJC_METACLASS_RO_$_PUIMainDisplayTransformer
+ __OBJC_METACLASS_RO_$_PUIPosterPagedEditingSceneSpecification
+ __OBJC_METACLASS_RO_$_PUIPosterSnapshotDeadline
+ __OBJC_METACLASS_RO_$_PUISceneResolverBridge
+ __OBJC_METACLASS_RO_$_PUISceneResolverBridgeExtension
+ __OBJC_METACLASS_RO_$_PUISceneResolverBridgeHostComponent
+ __OBJC_PROTOCOL_$_FBSDisplayTransformer
+ __OBJC_PROTOCOL_$__UISceneBarPositionClientObserver
+ ___113-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:candidateBundlesFutureProvider:]_block_invoke
+ ___113-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:candidateBundlesFutureProvider:]_block_invoke_2
+ ___113-[FBScene(PosterUIFoundation) pui_executeSnapshotForDescriptor:outputDestination:candidateBundlesFutureProvider:]_block_invoke_3
+ ___146-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:invalidateSnapshottingAssertion:]_block_invoke
+ ___146-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:invalidateSnapshottingAssertion:]_block_invoke_2
+ ___146-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:invalidateSnapshottingAssertion:]_block_invoke_3
+ ___146-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:invalidateSnapshottingAssertion:]_block_invoke_4
+ ___146-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:invalidateSnapshottingAssertion:]_block_invoke_5
+ ___146-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:invalidateSnapshottingAssertion:]_block_invoke_6
+ ___146-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:invalidateSnapshottingAssertion:]_block_invoke_7
+ ___146-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:invalidateSnapshottingAssertion:]_block_invoke_8
+ ___158-[FBScene(PosterUIFoundation) _pui_executeOutOfProcessSnapshotWithPromise:descriptor:outputDestination:snapshottingAssertion:invalidateSnapshottingAssertion:]_block_invoke
+ ___204-[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:invalidateSnapshottingAssertion:]_block_invoke
+ ___204-[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:invalidateSnapshottingAssertion:]_block_invoke_2
+ ___204-[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:invalidateSnapshottingAssertion:]_block_invoke_3
+ ___204-[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:invalidateSnapshottingAssertion:]_block_invoke_4
+ ___204-[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:invalidateSnapshottingAssertion:]_block_invoke_5
+ ___40-[PUIMappedImageCacheManager invalidate]_block_invoke
+ ___62-[PUIMappedImageCacheManager _cacheLock_scheduleManifestWrite]_block_invoke
+ ___67+[FBSDisplayMonitor(PosterUIFoundation) pui_mainDisplayTransformer]_block_invoke
+ ___94-[UIView(PUIRedMode) pui_applyRedModeFilterAnimated:withCoordinatedAnimationBlock:completion:]_block_invoke
+ ___94-[UIView(PUIRedMode) pui_applyRedModeFilterAnimated:withCoordinatedAnimationBlock:completion:]_block_invoke_2
+ ___94-[UIView(PUIRedMode) pui_clearRedModeFilterAnimated:withCoordinatedAnimationBlock:completion:]_block_invoke
+ ___94-[UIView(PUIRedMode) pui_clearRedModeFilterAnimated:withCoordinatedAnimationBlock:completion:]_block_invoke_2
+ ___PUIPosterSnapshotDeadlineContinuousTimeNow_block_invoke
+ ___SpringBoardHomeLibraryCore_block_invoke
+ ___block_descriptor_56_e8_32bs40r48r_e45_v24?0"PUIPosterSnapshotBundle"8"NSError"16lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32s40s48w_e33_v16?0"FBSMutableSceneSettings"8lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e35_v16?0"FBSMutableSceneParameters"8lw48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_66_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs64r_e26_v16?0"BSActionResponse"8ls32l8s40l8r64l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56bs64bs72w_e35_"<PFTFuture>"16?0"RBSAssertion"8lw72l8s56l8s32l8s64l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e30_"<PFTFuture>"16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_81_e8_32s40s48s56s64s72bs_e45_v24?0"PUIPosterSnapshotBundle"8"NSError"16ls32l8s40l8s48l8s56l8s72l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80bs_e30_"<PFTFuture>"16?0"NSArray"8ls72l8s32l8s40l8s48l8s80l8s56l8s64l8
+ ___getSBHDisplayCornerMetricsForScreenTypeSymbolLoc_block_invoke
+ __pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:invalidateSnapshottingAssertion:.fallbackQueue
+ __pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:invalidateSnapshottingAssertion:.onceToken
+ _audit_stringSpringBoardHome
+ _dispatch_sync
+ _getSBHDisplayCornerMetricsForScreenTypeSymbolLoc.ptr
+ _get_witness_table 7SwiftUI4ViewRzs12IdentifiableRd__AaBRd_0_r_0_lqd0__AaBHD4_AaBPAAE15fullScreenCover4item9onDismiss7contentQrAA7BindingVyqd__SgG_yycSgqd_0_qd__ctsACRd__AaBRd_0_r0_lFQOyx_qd__qd_0_Qo_HO
+ _kCAFilterColorMatrix
+ _kCAFilterInputColorMap
+ _kCAFilterInputColorMatrix
+ _kCAFilterInputPremultipliedValues
+ _kCAFilterLut
+ _kCAFilterVibrantColorMatrix
+ _kPUIWindowSceneHostInformedOrientationKey
+ _kPUIWindowSceneShouldSuppressFencedUpdatesKey
+ _mach_continuous_time
+ _mach_timebase_info
+ _pui_mainDisplayTransformer.displayTransformer
+ _pui_mainDisplayTransformer.onceToken
+ _symbolic _____yx_qd__qd_0_Qo_ 7SwiftUI4ViewPAAE15fullScreenCover4item9onDismiss7contentQrAA7BindingVyqd__SgG_yycSgqd_0_qd__cts12IdentifiableRd__AaBRd_0_r0_lFQO
- -[FBSMutableSceneSettings(PosterUIFoundation) pui_setRenderSessionTimeoutInterval:]
- -[FBSSceneSettings(PosterUIFoundation) pui_renderSessionTimeoutInterval]
- -[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:]
- -[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:]
- -[FBScene(PosterUIFoundation) _pui_executeOutOfProcessSnapshotWithPromise:descriptor:outputDestination:snapshottingAssertion:]
- -[FBScene(PosterUIFoundation) _pui_finishAndCleanupSnapshottingPromise:bundle:outputDestination:snapshottingAssertion:error:]
- -[PUIMappedImageCacheManager _cacheLock_writeManifest]
- GCC_except_table31
- GCC_except_table87
- _PF_IS_PAD_DEVICE
- _PUIDynamicRotationIsActive
- _PUIDynamicRotationIsActive.dynamicRotationIsActive
- _PUIDynamicRotationIsActive.onceToken
- __OBJC_$_INSTANCE_METHODS_UIView(UIKitViewHierarchy|PosterUIFoundation|PosterUIFoundation_Swift)
- ___114-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:]_block_invoke
- ___114-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:]_block_invoke_2
- ___114-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:]_block_invoke_3
- ___114-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:]_block_invoke_4
- ___114-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:]_block_invoke_5
- ___114-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:]_block_invoke_6
- ___114-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:]_block_invoke_7
- ___114-[FBScene(PosterUIFoundation) _pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:]_block_invoke_8
- ___126-[FBScene(PosterUIFoundation) _pui_executeOutOfProcessSnapshotWithPromise:descriptor:outputDestination:snapshottingAssertion:]_block_invoke
- ___172-[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:]_block_invoke
- ___172-[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:]_block_invoke_2
- ___172-[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:]_block_invoke_3
- ___172-[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:]_block_invoke_4
- ___172-[FBScene(PosterUIFoundation) _pui_checkForSuitableSnapshotBundlesWithPromise:candidateBundlesFuture:descriptor:outputDestination:snapshottingAssertion:executeIfNecessary:]_block_invoke_5
- ___PUIDynamicRotationIsActive_block_invoke
- ___block_descriptor_48_e8_32s40w_e33_v16?0"FBSMutableSceneSettings"8lw40l8s32l8
- ___block_descriptor_48_e8_32s40w_e35_v16?0"FBSMutableSceneParameters"8lw40l8s32l8
- ___block_descriptor_56_e8_32s40r48r_e45_v24?0"PUIPosterSnapshotBundle"8"NSError"16ls32l8r40l8r48l8
- ___block_descriptor_64_e8_32s40s48s56r_e26_v16?0"BSActionResponse"8ls32l8s40l8r56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e30_"<PFTFuture>"16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_72_e8_32s40s48s56s64s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_73_e8_32s40s48s56s64s_e45_v24?0"PUIPosterSnapshotBundle"8"NSError"16ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e30_"<PFTFuture>"16?0"NSArray"8ls72l8s32l8s40l8s48l8s56l8s64l8
- __pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:.fallbackQueue
- __pui_executeInProcessSnapshotForDescriptor:outputDestination:snapshottingAssertion:.onceToken
- _get_witness_table 7SwiftUI4ViewRzs12IdentifiableRd__AaBRd_0_r_0_lqd0__AaBHD4_AaBPAAE5sheet4item9onDismiss7contentQrAA7BindingVyqd__SgG_yycSgqd_0_qd__ctsACRd__AaBRd_0_r0_lFQOyx_qd__qd_0_Qo_HO
- _symbolic _____yx_qd__qd_0_Qo_ 7SwiftUI4ViewPAAE5sheet4item9onDismiss7contentQrAA7BindingVyqd__SgG_yycSgqd_0_qd__cts12IdentifiableRd__AaBRd_0_r0_lFQO
CStrings:
+ "<%@: %p; continuousTime: %.3f; remaining: %.3f>"
+ "@\"<PFTFuture>\"16@?0@\"RBSAssertion\"8"
+ "Error transforming display configuration: %{public}@;  Configuration: %{public}@"
+ "Failed to acquire snapshotting assertion"
+ "NightModeLUT"
+ "PosterKit.pagedEditing"
+ "SBHDisplayCornerMetricsForScreenType"
+ "Scene became invalid while acquiring snapshotting assertion"
+ "Scene deallocated while acquiring snapshotting assertion"
+ "[%{public}@/%p] scheduleManifestWrite"
+ "[%{public}@/%p] scheduleManifestWrite failed to write to url: %{public}@"
+ "[%{public}@/%p] scheduleManifestWrite finished"
+ "[%{public}@/%p] scheduleManifestWrite serialization failed: %{public}@"
+ "_deadline"
+ "angleDegrees"
+ "com.apple.PaperBoardUI.PUIMappedImageCacheManager.manifest-io"
+ "com.apple.PosterKit.UseColorMatrixNightModeFilter"
+ "continuousTime"
+ "customizeSheet"
+ "deadline"
+ "filters"
+ "filters.%@"
+ "filters.colorMatrix"
+ "filters.vibrantColorMatrix"
+ "hingeProgress"
+ "iPad19,1"
+ "iPad19,2"
+ "iPhone19,4"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SpringBoardHome.framework/SpringBoardHome"
+ "status"
- "Solarium"
- "SwiftUI"
- "[%{public}@/%p] writeManifest"
- "[%{public}@/%p] writeManifest failed to write to url: %{public}@"
- "[%{public}@/%p] writeManifest failed: %{public}@"
- "[%{public}@/%p] writeManifest finished"
- "ipad"
```
