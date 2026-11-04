## PosterBoardUIServices

> `/System/Library/PrivateFrameworks/PosterBoardUIServices.framework/PosterBoardUIServices`

```diff

-355.2.12.101.0
-  __TEXT.__text: 0x864d4
-  __TEXT.__objc_methlist: 0x6668
-  __TEXT.__const: 0x33e8
-  __TEXT.__cstring: 0x3bc9
-  __TEXT.__gcc_except_tab: 0xa40
-  __TEXT.__oslogstring: 0x4acf
-  __TEXT.__constg_swiftt: 0xf94
-  __TEXT.__swift5_typeref: 0x9b67
-  __TEXT.__swift5_reflstr: 0x923
-  __TEXT.__swift5_fieldmd: 0x954
+355.3.7.0.0
+  __TEXT.__text: 0x89998
+  __TEXT.__objc_methlist: 0x6990
+  __TEXT.__const: 0x3408
+  __TEXT.__cstring: 0x3c89
+  __TEXT.__gcc_except_tab: 0xa7c
+  __TEXT.__oslogstring: 0x51cf
+  __TEXT.__constg_swiftt: 0xfac
+  __TEXT.__swift5_typeref: 0x9b5d
+  __TEXT.__swift5_reflstr: 0x943
+  __TEXT.__swift5_fieldmd: 0x960
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_assocty: 0x370
   __TEXT.__swift5_proto: 0x104

   __TEXT.__swift_as_entry: 0x48
   __TEXT.__swift_as_ret: 0x54
   __TEXT.__swift_as_cont: 0xac
-  __TEXT.__unwind_info: 0x2e58
+  __TEXT.__unwind_info: 0x2f58
   __TEXT.__eh_frame: 0x1318
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1d08
-  __DATA_CONST.__objc_classlist: 0x370
+  __DATA_CONST.__const: 0x1d58
+  __DATA_CONST.__objc_classlist: 0x380
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x270
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b00
-  __DATA_CONST.__objc_protorefs: 0x90
-  __DATA_CONST.__objc_superrefs: 0x238
-  __DATA_CONST.__got: 0xe18
-  __AUTH_CONST.__const: 0x21e8
-  __AUTH_CONST.__cfstring: 0x30c0
-  __AUTH_CONST.__objc_const: 0x15288
+  __DATA_CONST.__objc_selrefs: 0x3c60
+  __DATA_CONST.__objc_protorefs: 0x88
+  __DATA_CONST.__objc_superrefs: 0x248
+  __DATA_CONST.__got: 0xe48
+  __AUTH_CONST.__const: 0x2208
+  __AUTH_CONST.__cfstring: 0x31c0
+  __AUTH_CONST.__objc_const: 0x15798
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH_CONST.__auth_got: 0x12a8
-  __AUTH.__objc_data: 0x248
+  __AUTH_CONST.__auth_got: 0x1318
+  __AUTH.__objc_data: 0x338
   __AUTH.__data: 0x288
-  __DATA.__objc_ivar: 0x78c
-  __DATA.__data: 0x2c70
-  __DATA_DIRTY.__objc_data: 0x28d0
-  __DATA_DIRTY.__data: 0x838
-  __DATA_DIRTY.__bss: 0x160
+  __DATA.__objc_ivar: 0x7d4
+  __DATA.__data: 0x2ca0
+  __DATA_DIRTY.__objc_data: 0x2880
+  __DATA_DIRTY.__data: 0x848
+  __DATA_DIRTY.__bss: 0x118
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3588
-  Symbols:   5083
-  CStrings:  855
+  Functions: 3655
+  Symbols:   5211
+  CStrings:  879
 
Symbols:
+ +[PRUISExternallyHostedPosterEditingService isExternalEditingSupportedForRole:]
+ +[PRUISModalEntryPointFaceEditor supportsBSXPCSecureCoding]
+ +[PRUISPosterEditingViewController _topButtonLayoutForScreen:]
+ -[FBSMutableSceneClientSettings(PosterBoardUI) pruis_setPosterEditorPresented:]
+ -[FBSSceneClientSettings(PosterBoardUI) pruis_isPosterEditorPresented]
+ -[PRUISAmbientPosterViewController _ensureHingeProgressProvider]
+ -[PRUISAmbientPosterViewController _userInterfaceStyleTraitDidChange:previousTraitCollection:]
+ -[PRUISAmbientPosterViewController startSendingHingeProgressEvents]
+ -[PRUISAmbientPosterViewController stopSendingHingeProgressEvents]
+ -[PRUISDeviceMotionProvider _motionGenerationQueue_anyObserverWantsMotion]
+ -[PRUISDeviceMotionProvider _motionGenerationQueue_motionProvider:motionDidUpdateWithRotation:fromDampening:]
+ -[PRUISDeviceMotionProvider _motionGenerationQueue_pauseGeneratingMotionEventsForObserver:]
+ -[PRUISDeviceMotionProvider _motionGenerationQueue_startGeneratingMotionEventsForObserver:]
+ -[PRUISDeviceMotionProvider _motionGenerationQueue_stopGeneratingMotionEventsForObserver:]
+ -[PRUISDeviceMotionProvider addObserver:]
+ -[PRUISDeviceMotionProvider pauseGeneratingMotionEventsForObserver:]
+ -[PRUISDeviceMotionProvider removeObserver:]
+ -[PRUISDeviceMotionProvider startGeneratingMotionEventsForObserver:]
+ -[PRUISDeviceMotionProvider stopGeneratingMotionEventsForObserver:]
+ -[PRUISHingeProgressController .cxx_destruct]
+ -[PRUISHingeProgressController _startGenerating]
+ -[PRUISHingeProgressController _stopGenerating]
+ -[PRUISHingeProgressController dealloc]
+ -[PRUISHingeProgressController delegate]
+ -[PRUISHingeProgressController hingeProgressProvider:didUpdateHingeState:]
+ -[PRUISHingeProgressController hingeProgressProvider]
+ -[PRUISHingeProgressController initWithScene:renderingServiceSceneComponent:hingeProgressProvider:]
+ -[PRUISHingeProgressController invalidate]
+ -[PRUISHingeProgressController scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:]
+ -[PRUISHingeProgressController setDelegate:]
+ -[PRUISHingeProgressController setHingeProgressProvider:]
+ -[PRUISHingeProgressController startSendingHingeProgressEvents]
+ -[PRUISHingeProgressController stopSendingHingeProgressEvents]
+ -[PRUISHingeProgressProvider .cxx_destruct]
+ -[PRUISHingeProgressProvider delegate]
+ -[PRUISHingeProgressProvider initWithFBSScene:]
+ -[PRUISHingeProgressProvider sceneHingeStateClientComponent:didUpdateFromHingeState:toHingeState:]
+ -[PRUISHingeProgressProvider setDelegate:]
+ -[PRUISHingeProgressProvider startGeneratingHingeProgressEvents]
+ -[PRUISHingeProgressProvider stopGeneratingHingeProgressEvents]
+ -[PRUISModalEntryPointAmbientEditingSwitcher role]
+ -[PRUISModalEntryPointAmbientEditingSwitcherWithActiveConfiguration role]
+ -[PRUISModalEntryPointEditHomeScreen role]
+ -[PRUISModalEntryPointEditing role]
+ -[PRUISModalEntryPointFaceEditor .cxx_destruct]
+ -[PRUISModalEntryPointFaceEditor containerCornerRadius]
+ -[PRUISModalEntryPointFaceEditor copyWithZone:]
+ -[PRUISModalEntryPointFaceEditor editorFaceScale]
+ -[PRUISModalEntryPointFaceEditor encodeWithBSXPCCoder:]
+ -[PRUISModalEntryPointFaceEditor hash]
+ -[PRUISModalEntryPointFaceEditor initWithBSXPCCoder:]
+ -[PRUISModalEntryPointFaceEditor initWithConfiguration:containerCornerRadius:]
+ -[PRUISModalEntryPointFaceEditor initWithConfiguration:containerCornerRadius:editorFaceScale:]
+ -[PRUISModalEntryPointFaceEditor isEqual:]
+ -[PRUISModalEntryPointFaceEditor role]
+ -[PRUISModalEntryPointFaceEditor serverPosterPath]
+ -[PRUISModalEntryPointFocusPosterSelection role]
+ -[PRUISModalEntryPointHomeScreenSwitcher role]
+ -[PRUISModalEntryPointTinyPosterRack role]
+ -[PRUISPosterChannelViewController hingeProgressEventsGenerator]
+ -[PRUISPosterEditingViewController _ensureHingeProgressProvider]
+ -[PRUISPosterEditingViewController hingeProgressController]
+ -[PRUISPosterEditingViewController setHingeProgressController:]
+ -[PRUISPosterEditingViewController startSendingHingeProgressEvents]
+ -[PRUISPosterEditingViewController stopSendingHingeProgressEvents]
+ -[PRUISPosterEditingViewController viewIsAppearing:]
+ -[PRUISPosterRenderingViewController _acquireAssertionForMaximumRenderingMode:reason:]
+ -[PRUISPosterRenderingViewController _buildMaximumRenderingModeAssertion]
+ -[PRUISPosterRenderingViewController _cachedSnapshotBundleForDefinition:]
+ -[PRUISPosterRenderingViewController _ensureHingeProgressProvider]
+ -[PRUISPosterRenderingViewController _maximumRenderingMode]
+ -[PRUISPosterRenderingViewController _sceneSnapshotDidComplete:]
+ -[PRUISPosterRenderingViewController _sceneSnapshotWillBegin:]
+ -[PRUISPosterRenderingViewController _setActiveRenderingMode:options:]
+ -[PRUISPosterRenderingViewController _setPosterSceneHiddenWhileKeptAlive:]
+ -[PRUISPosterRenderingViewController _updateActiveRenderingMode]
+ -[PRUISPosterRenderingViewController hingeProgressController]
+ -[PRUISPosterRenderingViewController startSendingHingeProgressEvents]
+ -[PRUISPosterRenderingViewController stopSendingHingeProgressEvents]
+ -[PRUISPosterRenderingViewController viewIsAppearing:]
+ -[PRUISSwitcherSceneClientSettingsDiffInspector observePosterEditorPresentedWithBlock:]
+ -[PRUISTestingDeviceMotionProvider _observersSnapshot]
+ -[PRUISTestingDeviceMotionProvider _startTimerIfNeeded]
+ -[PRUISTestingDeviceMotionProvider _stopTimer]
+ -[PRUISTestingDeviceMotionProvider addObserver:]
+ -[PRUISTestingDeviceMotionProvider pauseGeneratingMotionEventsForObserver:]
+ -[PRUISTestingDeviceMotionProvider removeObserver:]
+ -[PRUISTestingDeviceMotionProvider startGeneratingMotionEventsForObserver:]
+ -[PRUISTestingDeviceMotionProvider stopGeneratingMotionEventsForObserver:]
+ -[PRUISTestingHingeProgressProvider .cxx_destruct]
+ -[PRUISTestingHingeProgressProvider delegate]
+ -[PRUISTestingHingeProgressProvider setDelegate:]
+ -[PRUISTestingHingeProgressProvider startGeneratingHingeProgressEvents]
+ -[PRUISTestingHingeProgressProvider stopGeneratingHingeProgressEvents]
+ -[PRUISTestingHingeProgressProvider updateHingeState:]
+ -[_PRUISPosterStagedSceneSettings pui_isComplicationColumnConfigured]
+ -[_PRUISPosterStagedSceneSettings pui_setComplicationColumnConfigured:]
+ -[_PRUISPosterStagedSceneSettings pui_setSnapshotDeadlineContinuousTime:]
+ -[_PRUISPosterStagedSceneSettings pui_setSuppressesPresentationGraces:]
+ -[_PRUISPosterStagedSceneSettings pui_snapshotDeadlineContinuousTime]
+ -[_PRUISPosterStagedSceneSettings pui_suppressesPresentationGraces]
+ GCC_except_table106
+ GCC_except_table107
+ GCC_except_table117
+ GCC_except_table125
+ GCC_except_table13
+ GCC_except_table160
+ GCC_except_table161
+ GCC_except_table170
+ GCC_except_table21
+ GCC_except_table24
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table4
+ GCC_except_table46
+ GCC_except_table60
+ GCC_except_table70
+ GCC_except_table78
+ GCC_except_table96
+ _BSInterfaceOrientationToString
+ _OBJC_CLASS_$_PRUISHingeProgressController
+ _OBJC_CLASS_$_PRUISHingeProgressProvider
+ _OBJC_CLASS_$_PRUISModalEntryPointFaceEditor
+ _OBJC_CLASS_$_PRUISTestingHingeProgressProvider
+ _OBJC_CLASS_$_PUIHingeState
+ _OBJC_CLASS_$_PUISceneResolverBridge
+ _OBJC_IVAR_$_PRUISAmbientPosterViewController._hingeProgressController
+ _OBJC_IVAR_$_PRUISAmbientPosterViewController._outstandingSnapshotFetchRequests
+ _OBJC_IVAR_$_PRUISDeviceMotionProvider._motionGenerationQueue_pausedObservers
+ _OBJC_IVAR_$_PRUISDeviceMotionProvider._motionGenerationQueue_startedObservers
+ _OBJC_IVAR_$_PRUISDeviceMotionProvider._observerLock
+ _OBJC_IVAR_$_PRUISDeviceMotionProvider._observers
+ _OBJC_IVAR_$_PRUISHingeProgressController._delegate
+ _OBJC_IVAR_$_PRUISHingeProgressController._hostHasRequested
+ _OBJC_IVAR_$_PRUISHingeProgressController._isGenerating
+ _OBJC_IVAR_$_PRUISHingeProgressController._posterHasRequested
+ _OBJC_IVAR_$_PRUISHingeProgressController._provider
+ _OBJC_IVAR_$_PRUISHingeProgressController._scene
+ _OBJC_IVAR_$_PRUISHingeProgressController._sceneComponent
+ _OBJC_IVAR_$_PRUISHingeProgressProvider._delegate
+ _OBJC_IVAR_$_PRUISHingeProgressProvider._fbsScene
+ _OBJC_IVAR_$_PRUISHingeProgressProvider._isGenerating
+ _OBJC_IVAR_$_PRUISModalEntryPointFaceEditor._containerCornerRadius
+ _OBJC_IVAR_$_PRUISModalEntryPointFaceEditor._editorFaceScale
+ _OBJC_IVAR_$_PRUISModalEntryPointFaceEditor._serverPosterPath
+ _OBJC_IVAR_$_PRUISModalRemoteViewController._resolverBridge
+ _OBJC_IVAR_$_PRUISPosterEditingViewController._hingeProgressController
+ _OBJC_IVAR_$_PRUISPosterRenderingViewController._activeRenderingMode
+ _OBJC_IVAR_$_PRUISPosterRenderingViewController._hingeProgressController
+ _OBJC_IVAR_$_PRUISPosterRenderingViewController._maximumRenderingModeAssertion
+ _OBJC_IVAR_$_PRUISPosterRenderingViewController._posterSceneHiddenWhileKeptAlive
+ _OBJC_IVAR_$_PRUISPosterRenderingViewController._requestedRenderingMode
+ _OBJC_IVAR_$_PRUISPosterRenderingViewController._snapshotRenderingModeAssertion
+ _OBJC_IVAR_$_PRUISTestingDeviceMotionProvider._lock
+ _OBJC_IVAR_$_PRUISTestingDeviceMotionProvider._observers
+ _OBJC_IVAR_$_PRUISTestingDeviceMotionProvider._pausedObservers
+ _OBJC_IVAR_$_PRUISTestingDeviceMotionProvider._startedObservers
+ _OBJC_IVAR_$_PRUISTestingHingeProgressProvider._currentHingeState
+ _OBJC_IVAR_$_PRUISTestingHingeProgressProvider._delegate
+ _OBJC_IVAR_$_PRUISTestingHingeProgressProvider._isGenerating
+ _OBJC_IVAR_$__PRUISPosterStagedSceneSettings._complicationColumnConfigured
+ _OBJC_IVAR_$__PRUISPosterStagedSceneSettings._snapshotDeadlineContinuousTime
+ _OBJC_IVAR_$__PRUISPosterStagedSceneSettings._suppressesPresentationGraces
+ _OBJC_METACLASS_$_PRUISHingeProgressController
+ _OBJC_METACLASS_$_PRUISHingeProgressProvider
+ _OBJC_METACLASS_$_PRUISModalEntryPointFaceEditor
+ _OBJC_METACLASS_$_PRUISTestingHingeProgressProvider
+ _PFFeatureEnabled
+ _PF_IS_PAD_DEVICE
+ _PF_IS_V68_DEVICE
+ _PRAmbientWidgetStateSceneExtensionGetClass
+ _PRPagedRendererSceneExtensionGetClass
+ _PRPagedRendererSceneExtensionIsClientEditingSupported
+ _PRPagedRendererSceneExtensionSendCancelTouchesAction
+ _PRPagedRendererSceneExtensionSendInvalidateCancelTouchesAction
+ _PRPagedRendererSceneExtensionSetContainerCornerRadius
+ _PRPagedRendererSceneExtensionSetEditorFaceScale
+ _PRPagedRendererSceneExtensionSetIsInteractiveModeActive
+ _PRPagedRendererSceneExtensionSetIsScaledForEditing
+ _PRPagedRendererSceneExtensionSetSupportsInteractablePressFeedback
+ _SBSTopButtonFramesForPostersForDisplayIdentifier
+ __OBJC_$_CLASS_METHODS_PRUISModalEntryPointFaceEditor
+ __OBJC_$_INSTANCE_METHODS_PRUISHingeProgressController
+ __OBJC_$_INSTANCE_METHODS_PRUISHingeProgressProvider
+ __OBJC_$_INSTANCE_METHODS_PRUISModalEntryPointFaceEditor
+ __OBJC_$_INSTANCE_METHODS_PRUISTestingHingeProgressProvider
+ __OBJC_$_INSTANCE_VARIABLES_PRUISHingeProgressController
+ __OBJC_$_INSTANCE_VARIABLES_PRUISHingeProgressProvider
+ __OBJC_$_INSTANCE_VARIABLES_PRUISModalEntryPointFaceEditor
+ __OBJC_$_INSTANCE_VARIABLES_PRUISTestingHingeProgressProvider
+ __OBJC_$_PROP_LIST_PRUISHingeProgressController
+ __OBJC_$_PROP_LIST_PRUISHingeProgressProvider
+ __OBJC_$_PROP_LIST_PRUISHingeProgressProviding
+ __OBJC_$_PROP_LIST_PRUISModalEntryPoint
+ __OBJC_$_PROP_LIST_PRUISModalEntryPointFaceEditor
+ __OBJC_$_PROP_LIST_PRUISTestingHingeProgressProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__UISceneHingeStateClientObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PRUISDeviceMotionProviderObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PRUISHingeProgressProviderDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PRUISHingeProgressProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PRUISModalEntryPoint
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PRUISPosterHingeProgressEventsGenerating
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PRUISDeviceMotionProviderObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PRUISHingeProgressProviderDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PRUISHingeProgressProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PRUISModalEntryPoint
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PRUISPosterHingeProgressEventsGenerating
+ __OBJC_$_PROTOCOL_METHOD_TYPES__UISceneHingeStateClientObserver
+ __OBJC_$_PROTOCOL_REFS_PRUISHingeProgressProviderDelegate
+ __OBJC_$_PROTOCOL_REFS_PRUISHingeProgressProviding
+ __OBJC_$_PROTOCOL_REFS__UISceneHingeStateClientObserver
+ __OBJC_CLASS_PROTOCOLS_$_PRUISHingeProgressController
+ __OBJC_CLASS_PROTOCOLS_$_PRUISHingeProgressProvider
+ __OBJC_CLASS_PROTOCOLS_$_PRUISModalEntryPointFaceEditor
+ __OBJC_CLASS_PROTOCOLS_$_PRUISTestingHingeProgressProvider
+ __OBJC_CLASS_RO_$_PRUISHingeProgressController
+ __OBJC_CLASS_RO_$_PRUISHingeProgressProvider
+ __OBJC_CLASS_RO_$_PRUISModalEntryPointFaceEditor
+ __OBJC_CLASS_RO_$_PRUISTestingHingeProgressProvider
+ __OBJC_LABEL_PROTOCOL_$_PRUISDeviceMotionProviderObserver
+ __OBJC_LABEL_PROTOCOL_$_PRUISHingeProgressProviderDelegate
+ __OBJC_LABEL_PROTOCOL_$_PRUISHingeProgressProviding
+ __OBJC_LABEL_PROTOCOL_$_PRUISPosterHingeProgressEventsGenerating
+ __OBJC_LABEL_PROTOCOL_$__UISceneHingeStateClientObserver
+ __OBJC_METACLASS_RO_$_PRUISHingeProgressController
+ __OBJC_METACLASS_RO_$_PRUISHingeProgressProvider
+ __OBJC_METACLASS_RO_$_PRUISModalEntryPointFaceEditor
+ __OBJC_METACLASS_RO_$_PRUISTestingHingeProgressProvider
+ __OBJC_PROTOCOL_$_PRUISDeviceMotionProviderObserver
+ __OBJC_PROTOCOL_$_PRUISHingeProgressProviderDelegate
+ __OBJC_PROTOCOL_$_PRUISHingeProgressProviding
+ __OBJC_PROTOCOL_$_PRUISPosterHingeProgressEventsGenerating
+ __OBJC_PROTOCOL_$__UISceneHingeStateClientObserver
+ __UISceneDidCompleteSystemSnapshotSequence
+ __UISceneWillBeginSystemSnapshotSequence
+ ___41-[PRUISDeviceMotionController invalidate]_block_invoke
+ ___42-[PRUISModalEntryPointFaceEditor isEqual:]_block_invoke
+ ___42-[PRUISModalEntryPointFaceEditor isEqual:]_block_invoke_2
+ ___42-[PRUISModalEntryPointFaceEditor isEqual:]_block_invoke_3
+ ___55-[PRUISTestingDeviceMotionProvider _startTimerIfNeeded]_block_invoke
+ ___67-[PRUISDeviceMotionProvider stopGeneratingMotionEventsForObserver:]_block_invoke
+ ___68-[PRUISDeviceMotionProvider pauseGeneratingMotionEventsForObserver:]_block_invoke
+ ___68-[PRUISDeviceMotionProvider startGeneratingMotionEventsForObserver:]_block_invoke
+ ___70-[PRUISPosterRenderingViewController _setActiveRenderingMode:options:]_block_invoke
+ ___70-[PRUISPosterRenderingViewController _setActiveRenderingMode:options:]_block_invoke_2
+ ___73-[PRUISPosterRenderingViewController _buildMaximumRenderingModeAssertion]_block_invoke
+ ___73-[PRUISPosterRenderingViewController _buildMaximumRenderingModeAssertion]_block_invoke_2
+ ___79-[PRUISAmbientPosterViewController cancelTouchesForCurrentEventInHostedContent]_block_invoke_2
+ ___85+[PRUISSwitcherSceneClientSettingsDiffInspector diffInspectorForObservingDiffContext]_block_invoke_5
+ ___block_descriptor_40_e8_32s_e5_d8?0ls32l8
+ ___block_descriptor_40_e8_32w_e29_v16?0"BSAbsoluteMachTimer"8lw32l8
+ ___block_descriptor_40_e8_32w_e36_v16?0"<BSCompoundAssertionState>"8lw32l8
+ ___block_descriptor_57_e8_32s40bs_e46_B24?0"PUIPosterSnapshotBundle"8"NSString"16ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48w_e78_v32?0"PRUISPosterSnapshotRequest"8"PRUISPosterSnapshotResult"16"NSError"24lw48l8s32l8s40l8
+ ___block_descriptor_58_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s_e63_v24?0"FBSMutableSceneSettings"8"FBSSceneTransitionContext"16ls32l8s40l8s48l8
+ _dispatch_get_specific
+ _dispatch_queue_set_specific
+ _kPRUISMotionGenerationQueueKey
+ _symbolic So33PRUISTestingHingeProgressProviderCSg
+ _symbolic _____ 7SwiftUI17EnvironmentValuesV21PosterBoardUIServicesE27__Key_hingeProgressOverride33_890EF9A79DBBAA2BF529DB8962144A0DLLV
- +[PRUISPosterEditingViewController _topButtonLayout]
- -[PRUISAmbientPosterViewController startSendingDisplayStateProgressEvents]
- -[PRUISAmbientPosterViewController stopSendingDisplayStateProgressEvents]
- -[PRUISDeviceMotionProvider _motionGenerationQueue_motionProvider:motionDidUpdateWithRotation:]
- -[PRUISDeviceMotionProvider delegate]
- -[PRUISDeviceMotionProvider pauseGeneratingMotionEvents]
- -[PRUISDeviceMotionProvider setDelegate:]
- -[PRUISDeviceMotionProvider startGeneratingMotionEvents]
- -[PRUISDeviceMotionProvider stopGeneratingMotionEvents]
- -[PRUISDisplayStateProgressController .cxx_destruct]
- -[PRUISDisplayStateProgressController _startGenerating]
- -[PRUISDisplayStateProgressController _stopGenerating]
- -[PRUISDisplayStateProgressController dealloc]
- -[PRUISDisplayStateProgressController delegate]
- -[PRUISDisplayStateProgressController displayStateProgressProvider:didUpdateDisplayStateProgress:]
- -[PRUISDisplayStateProgressController displayStateProgressProvider]
- -[PRUISDisplayStateProgressController initWithScene:renderingServiceSceneComponent:]
- -[PRUISDisplayStateProgressController initWithScene:renderingServiceSceneComponent:displayStateProgressProvider:]
- -[PRUISDisplayStateProgressController invalidate]
- -[PRUISDisplayStateProgressController scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:]
- -[PRUISDisplayStateProgressController setDelegate:]
- -[PRUISDisplayStateProgressController setDisplayStateProgressProvider:]
- -[PRUISDisplayStateProgressController startSendingDisplayStateProgressEvents]
- -[PRUISDisplayStateProgressController stopSendingDisplayStateProgressEvents]
- -[PRUISPosterChannelViewController displayStateProgressEventsGenerator]
- -[PRUISPosterEditingViewController displayStateProgressController]
- -[PRUISPosterEditingViewController setDisplayStateProgressController:]
- -[PRUISPosterEditingViewController startSendingDisplayStateProgressEvents]
- -[PRUISPosterEditingViewController stopSendingDisplayStateProgressEvents]
- -[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]
- -[PRUISPosterRenderingViewController displayStateProgressController]
- -[PRUISPosterRenderingViewController startSendingDisplayStateProgressEvents]
- -[PRUISPosterRenderingViewController stopSendingDisplayStateProgressEvents]
- -[PRUISTestingDeviceMotionProvider _rescheduleTimer]
- -[PRUISTestingDeviceMotionProvider _scheduleTimerIfNeeded]
- -[PRUISTestingDeviceMotionProvider delegate]
- -[PRUISTestingDeviceMotionProvider pauseGeneratingMotionEvents]
- -[PRUISTestingDeviceMotionProvider setDelegate:]
- -[PRUISTestingDeviceMotionProvider startGeneratingMotionEvents]
- -[PRUISTestingDeviceMotionProvider stopGeneratingMotionEvents]
- -[PRUISTestingDisplayStateProgressProvider .cxx_destruct]
- -[PRUISTestingDisplayStateProgressProvider delegate]
- -[PRUISTestingDisplayStateProgressProvider setDelegate:]
- -[PRUISTestingDisplayStateProgressProvider startGeneratingDisplayStateProgressEvents]
- -[PRUISTestingDisplayStateProgressProvider stopGeneratingDisplayStateProgressEvents]
- -[PRUISTestingDisplayStateProgressProvider updateDisplayStateProgress:]
- -[_PRUISPosterStagedSceneSettings pui_renderSessionTimeoutInterval]
- -[_PRUISPosterStagedSceneSettings pui_setRenderSessionTimeoutInterval:]
- GCC_except_table104
- GCC_except_table114
- GCC_except_table122
- GCC_except_table156
- GCC_except_table157
- GCC_except_table158
- GCC_except_table40
- GCC_except_table54
- GCC_except_table67
- GCC_except_table69
- GCC_except_table93
- _BSDispatchQueueAssertNot
- _OBJC_CLASS_$_PRUISDisplayStateProgressController
- _OBJC_CLASS_$_PRUISTestingDisplayStateProgressProvider
- _OBJC_IVAR_$_PRUISAmbientPosterViewController._displayStateProgressController
- _OBJC_IVAR_$_PRUISDeviceMotionProvider._delegate
- _OBJC_IVAR_$_PRUISDisplayStateProgressController._delegate
- _OBJC_IVAR_$_PRUISDisplayStateProgressController._hostHasRequested
- _OBJC_IVAR_$_PRUISDisplayStateProgressController._isGenerating
- _OBJC_IVAR_$_PRUISDisplayStateProgressController._posterHasRequested
- _OBJC_IVAR_$_PRUISDisplayStateProgressController._provider
- _OBJC_IVAR_$_PRUISDisplayStateProgressController._scene
- _OBJC_IVAR_$_PRUISDisplayStateProgressController._sceneComponent
- _OBJC_IVAR_$_PRUISPosterEditingViewController._displayStateProgressController
- _OBJC_IVAR_$_PRUISPosterRenderingViewController._displayStateProgressController
- _OBJC_IVAR_$_PRUISPosterRenderingViewController._renderingMode
- _OBJC_IVAR_$_PRUISTestingDeviceMotionProvider._delegate
- _OBJC_IVAR_$_PRUISTestingDeviceMotionProvider._isGeneratingMotionEvents
- _OBJC_IVAR_$_PRUISTestingDisplayStateProgressProvider._currentValue
- _OBJC_IVAR_$_PRUISTestingDisplayStateProgressProvider._delegate
- _OBJC_IVAR_$_PRUISTestingDisplayStateProgressProvider._hasValue
- _OBJC_IVAR_$_PRUISTestingDisplayStateProgressProvider._isGenerating
- _OBJC_IVAR_$__PRUISPosterStagedSceneSettings._renderSessionTimeoutInterval
- _OBJC_METACLASS_$_PRUISDisplayStateProgressController
- _OBJC_METACLASS_$_PRUISTestingDisplayStateProgressProvider
- _PUIDynamicRotationIsActive
- _SBSTopButtonFramesForPosters
- __OBJC_$_INSTANCE_METHODS_PRUISDisplayStateProgressController
- __OBJC_$_INSTANCE_METHODS_PRUISTestingDisplayStateProgressProvider
- __OBJC_$_INSTANCE_VARIABLES_PRUISDisplayStateProgressController
- __OBJC_$_INSTANCE_VARIABLES_PRUISTestingDisplayStateProgressProvider
- __OBJC_$_PROP_LIST_PRUISDisplayStateProgressController
- __OBJC_$_PROP_LIST_PRUISDisplayStateProgressProviding
- __OBJC_$_PROP_LIST_PRUISTestingDisplayStateProgressProvider
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PRUISDeviceMotionProviderDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PRUISDisplayStateProgressProviderDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PRUISDisplayStateProgressProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_PRUISPosterDisplayStateProgressEventsGenerating
- __OBJC_$_PROTOCOL_METHOD_TYPES_PRUISDeviceMotionProviderDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_PRUISDisplayStateProgressProviderDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_PRUISDisplayStateProgressProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_PRUISPosterDisplayStateProgressEventsGenerating
- __OBJC_$_PROTOCOL_REFS_PRUISDisplayStateProgressProviderDelegate
- __OBJC_$_PROTOCOL_REFS_PRUISDisplayStateProgressProviding
- __OBJC_CLASS_PROTOCOLS_$_PRUISDisplayStateProgressController
- __OBJC_CLASS_PROTOCOLS_$_PRUISTestingDisplayStateProgressProvider
- __OBJC_CLASS_RO_$_PRUISDisplayStateProgressController
- __OBJC_CLASS_RO_$_PRUISTestingDisplayStateProgressProvider
- __OBJC_LABEL_PROTOCOL_$_PRUISDeviceMotionProviderDelegate
- __OBJC_LABEL_PROTOCOL_$_PRUISDisplayStateProgressProviderDelegate
- __OBJC_LABEL_PROTOCOL_$_PRUISDisplayStateProgressProviding
- __OBJC_LABEL_PROTOCOL_$_PRUISPosterDisplayStateProgressEventsGenerating
- __OBJC_METACLASS_RO_$_PRUISDisplayStateProgressController
- __OBJC_METACLASS_RO_$_PRUISTestingDisplayStateProgressProvider
- __OBJC_PROTOCOL_$_PRUISDeviceMotionProviderDelegate
- __OBJC_PROTOCOL_$_PRUISDisplayStateProgressProviderDelegate
- __OBJC_PROTOCOL_$_PRUISDisplayStateProgressProviding
- __OBJC_PROTOCOL_$_PRUISPosterDisplayStateProgressEventsGenerating
- ___52+[PRUISPosterEditingViewController _topButtonLayout]_block_invoke
- ___55-[PRUISDeviceMotionProvider stopGeneratingMotionEvents]_block_invoke
- ___56-[PRUISDeviceMotionProvider pauseGeneratingMotionEvents]_block_invoke
- ___56-[PRUISDeviceMotionProvider startGeneratingMotionEvents]_block_invoke
- ___58-[PRUISTestingDeviceMotionProvider _scheduleTimerIfNeeded]_block_invoke
- ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke
- ___84-[PRUISPosterRenderingViewController _setRenderingMode:canUseInitialSnapshotBundle:]_block_invoke_2
- ___block_descriptor_48_e8_32s40w_e29_v16?0"BSAbsoluteMachTimer"8lw40l8s32l8
- ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_49_e8_32s40w_e78_v32?0"PRUISPosterSnapshotRequest"8"PRUISPosterSnapshotResult"16"NSError"24lw40l8s32l8
- ___block_descriptor_56_e8_32s40bs_e46_B24?0"PUIPosterSnapshotBundle"8"NSString"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40s_e63_v24?0"FBSMutableSceneSettings"8"FBSSceneTransitionContext"16ls32l8s40l8
- __topButtonLayout.layout
- __topButtonLayout.onceToken
- _flat unique So34PRUISDisplayStateProgressProviding_p
- _symbolic _____ 7SwiftUI17EnvironmentValuesV21PosterBoardUIServicesE34__Key_displayStateProgressOverride33_890EF9A79DBBAA2BF529DB8962144A0DLLV
- _symbolic ______pSg So34PRUISDisplayStateProgressProvidingP
CStrings:
+ "<%{public}@:%{public}p> %{public}@ the poster scene's presentation views"
+ "<%{public}@:%{public}p> Cannot synchronously transition to snapshot rendering mode: no snapshot bundle already in hand (initial bundle usable: %{BOOL}d, cache hit: %{BOOL}d). Capturing one would be asynchronous and land too late, so not updating rendering mode. Keeping mode as '%{public}@'"
+ "<%{public}@:%{public}p> Ignoring scene content readiness change while the rendering mode is limited"
+ "<%{public}@:%{public}p> Invalid maximum rendering mode %@, not acquiring assertion"
+ "<%{public}@:%{public}p> Invalid requested rendering mode %@, bailing"
+ "<%{public}@:%{public}p> Limiting requested rendering mode '%{public}@' to '%{public}@' to satisfy maximum rendering mode '%{public}@'. Outstanding assertions: %{public}@"
+ "<%{public}@:%{public}p> No cached snapshot bundle for definition %{public}@: %{public}@"
+ "<%{public}@:%{public}p> Requested rendering mode: %{public}@"
+ "<%{public}@:%{public}p> Successfully set up snapshot image views. Hiding the poster scene, but keeping it alive."
+ "<%{public}@:%{public}p> _sceneSnapshotDidComplete (ourScene: %@  snapshottingScene: %@  ours: %{BOOL}u)"
+ "<%{public}@:%{public}p> _sceneSnapshotWillBegin (ourScene: %@  snapshottingScene: %@  ours: %{BOOL}u)"
+ "<%{public}@:%{public}p> viewWillTransitionToSize:%@"
+ "Cached snapshot bundle was insufficient."
+ "Hiding"
+ "MaximumRenderingMode"
+ "PRUISExternallyHostedPosterEditingServer rejecting connection on a device that does not support external editing: %{public}@"
+ "PRUISModalEntryPointFaceEditor: could not decode poster path"
+ "PRUISModalEntryPointFaceEditor: could not obtain poster path with sandbox extension: %@"
+ "Showing"
+ "Updating to new orientation with fenced animation: contentState = %{public}@; oldOrientation = %{public}@; newOrientation = %{public}@; scene=%{public}@"
+ "Updating to new orientation without animation: contentState = %{public}@; oldOrientation = %{public}@; newOrientation = %{public}@; scene=%{public}@"
+ "_editorFaceScale"
+ "d8@?0"
+ "pui_complicationColumnConfigured"
+ "pui_snapshotDeadlineContinuousTime"
+ "pui_suppressesPresentationGraces"
+ "scene snapshot"
+ "{CGSize=dd}"
+ "\xf0\xf0a"
+ "\xf0\xf0\xb2"
- "PRUISExternallyHostedPosterEditingServer rejecting connections on non-iPads: %{public}@"
- "pui_renderSessionTimeoutInterval"
- "\xa1"
- "\xf0\xc1"
- "\xf0\xf0Q"
- "\xf0\xf0r"
```
