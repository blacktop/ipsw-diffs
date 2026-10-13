## SpringBoard

> `/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`

```diff

-4637.1.12.101.0
-  __TEXT.__text: 0xacef7c
+4637.1.14.103.0
+  __TEXT.__text: 0xad435c
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0xbe090
-  __TEXT.__const: 0x11360
-  __TEXT.__oslogstring: 0x659af
-  __TEXT.__cstring: 0x855ed
-  __TEXT.__gcc_except_tab: 0x186e4
+  __TEXT.__objc_methlist: 0xbe4f0
+  __TEXT.__const: 0x11370
+  __TEXT.__oslogstring: 0x65afe
+  __TEXT.__cstring: 0x85af0
+  __TEXT.__gcc_except_tab: 0x18890
   __TEXT.__ustring: 0xd04
   __TEXT.__dlopen_cstrs: 0x373
-  __TEXT.__unwind_info: 0x39ef8
+  __TEXT.__unwind_info: 0x3a080
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1da68
-  __DATA_CONST.__objc_classlist: 0x54f8
+  __DATA_CONST.__const: 0x1dae0
+  __DATA_CONST.__objc_classlist: 0x5520
   __DATA_CONST.__objc_catlist: 0x338
   __DATA_CONST.__objc_nlcatlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x2ae0
+  __DATA_CONST.__objc_protolist: 0x2af8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4eb60
+  __DATA_CONST.__objc_selrefs: 0x4ed30
   __DATA_CONST.__objc_protorefs: 0xd8
-  __DATA_CONST.__objc_superrefs: 0x40a0
+  __DATA_CONST.__objc_superrefs: 0x40c0
   __DATA_CONST.__objc_arraydata: 0x18b8
-  __DATA_CONST.__got: 0xa980
-  __AUTH_CONST.__const: 0x10c48
-  __AUTH_CONST.__cfstring: 0x74d80
-  __AUTH_CONST.__objc_const: 0x288dd8
+  __DATA_CONST.__got: 0xa9c0
+  __AUTH_CONST.__const: 0x10c68
+  __AUTH_CONST.__cfstring: 0x74f80
+  __AUTH_CONST.__objc_const: 0x28a9f0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x1740
   __AUTH_CONST.__objc_doubleobj: 0x850
-  __AUTH_CONST.__objc_intobj: 0x2ca0
+  __AUTH_CONST.__objc_intobj: 0x2cb8
   __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH_CONST.__auth_got: 0x2c00
-  __AUTH.__objc_data: 0xd840
-  __DATA.__objc_ivar: 0xfca4
-  __DATA.__data: 0x20f80
+  __AUTH.__objc_data: 0xd9d0
+  __DATA.__objc_ivar: 0xfd40
+  __DATA.__data: 0x210a0
   __DATA.__common: 0xa40
   __DATA_DIRTY.__objc_data: 0x27970
   __DATA_DIRTY.__data: 0x140
-  __DATA_DIRTY.__bss: 0x19f8
+  __DATA_DIRTY.__bss: 0x19e8
   __DATA_DIRTY.__common: 0x40
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libutil.dylib
-  Functions: 73638
-  Symbols:   119483
-  CStrings:  23587
+  Functions: 73747
+  Symbols:   119682
+  CStrings:  23612
 
Symbols:
+ +[SBHomeScreenService _validationErrorForStashedLayoutName:]
+ -[FBScene(SBScreenBrightnessHost) sb_screenBrightnessHost]
+ -[SBContinuitySession _updateSystemGestureWindowFrame]
+ -[SBContinuousExposeAppToAppModifier appLayoutsToEnsureExistForMainTransitionEvent:]
+ -[SBContinuousExposeAppToAppModifier ignoredAppLayout]
+ -[SBContinuousExposeAppToAppModifier setIgnoredAppLayout:]
+ -[SBContinuousExposeAppToAppModifier setShouldOrderToAppLayoutFront:]
+ -[SBContinuousExposeAppToAppModifier shouldOrderToAppLayoutFront]
+ -[SBDashBoardHostableEntityHostingFluidSwitcherViewController _invalidateZStackParticipant]
+ -[SBDashBoardHostableEntityHostingFluidSwitcherViewController _removeBottomEdgeRecognizer]
+ -[SBDeviceApplicationSceneViewController _isDoubleTapTopToZoomEnabled]
+ -[SBDisplayItemLayoutAttributes attributesByZoomingToLargestSizeAllowedBySupportedSizingPolicies:]
+ -[SBFlexibleWindowingAutoLayoutSpace setStageSpanningSplit:]
+ -[SBFlexibleWindowingAutoLayoutSpace stageSpanningSplit]
+ -[SBFullScreenToPeekAnimationModifier isLayoutRoleMatchMovedToScene:inAppLayout:]
+ -[SBHomeScreenController iconManager:shouldAvoidPlacingIconOnFirstPage:]
+ -[SBHomeScreenService simulateCampoEnablementChange]
+ -[SBMinimizeItemFromSplitResizeWindowingModifier dimmingAlphaForLayoutRole:inAppLayout:]
+ -[SBPIPPegasusContainerAdapter _settleInFlightRotationAnimation]
+ -[SBScreenBrightnessCoordinator .cxx_destruct]
+ -[SBScreenBrightnessCoordinator _keyForWindowScene:]
+ -[SBScreenBrightnessCoordinator acquireParticipantForObserver:]
+ -[SBScreenBrightnessCoordinator debugHUDForWindowScene:]
+ -[SBScreenBrightnessCoordinator displayClientForWindowScene:]
+ -[SBScreenBrightnessCoordinator init]
+ -[SBScreenBrightnessCoordinator windowSceneDidConnect:]
+ -[SBScreenBrightnessCoordinator windowSceneDidDisconnect:]
+ -[SBScreenBrightnessDebugHUDView .cxx_destruct]
+ -[SBScreenBrightnessDebugHUDView _clearNumberLabel:]
+ -[SBScreenBrightnessDebugHUDView _invalidateLayout]
+ -[SBScreenBrightnessDebugHUDView _numberLabel]
+ -[SBScreenBrightnessDebugHUDView _titleLabelWithString:]
+ -[SBScreenBrightnessDebugHUDView _updateNumberLabel:withDoubleValue:]
+ -[SBScreenBrightnessDebugHUDView _windowSceneBrightnessDidUpdate:]
+ -[SBScreenBrightnessDebugHUDView brightnessDidChange:]
+ -[SBScreenBrightnessDebugHUDView dealloc]
+ -[SBScreenBrightnessDebugHUDView initWithCoordinator:]
+ -[SBScreenBrightnessDebugHUDView invalidate]
+ -[SBScreenBrightnessDebugHUDView sanitizedBrightnessDidChange:]
+ -[SBScreenBrightnessDebugHUDView sizeThatFits:]
+ -[SBScreenBrightnessDebugHUDView updateWindowScene:]
+ -[SBScreenBrightnessDisplayClient .cxx_destruct]
+ -[SBScreenBrightnessDisplayClient _displayDidTurnOn]
+ -[SBScreenBrightnessDisplayClient _displayWillTurnOff]
+ -[SBScreenBrightnessDisplayClient _isBrightnessUnchangedFrom:to:]
+ -[SBScreenBrightnessDisplayClient _newRequestWithBrightness:pendingDisplayOn:]
+ -[SBScreenBrightnessDisplayClient _notifyQueue_readBrightnessFromDisplayForced:]
+ -[SBScreenBrightnessDisplayClient _sanitizedBrightnessLevel:]
+ -[SBScreenBrightnessDisplayClient _updateBrightnessTracking]
+ -[SBScreenBrightnessDisplayClient _updateDisplayWithBrightness:displayClient:]
+ -[SBScreenBrightnessDisplayClient addObserver:]
+ -[SBScreenBrightnessDisplayClient backlightController:didTransitionToBacklightState:source:]
+ -[SBScreenBrightnessDisplayClient backlightController:willTransitionToBacklightState:source:]
+ -[SBScreenBrightnessDisplayClient brightnessControlAvailableUpdate:]
+ -[SBScreenBrightnessDisplayClient brightnessUpdate:]
+ -[SBScreenBrightnessDisplayClient initWithClient:windowScene:]
+ -[SBScreenBrightnessDisplayClient invalidate]
+ -[SBScreenBrightnessDisplayClient notifyQueue]
+ -[SBScreenBrightnessDisplayClient relinquishRequest:]
+ -[SBScreenBrightnessDisplayClient removeObserver:]
+ -[SBScreenBrightnessDisplayClient requestPreferredBrightness:]
+ -[SBScreenBrightnessHostComponent _hostWindowScene]
+ -[SBScreenBrightnessHostComponent _observeHostedScenePolicyHostComponentIfNeeded]
+ -[SBScreenBrightnessHostComponent _updateParticipantForSettings:]
+ -[SBScreenBrightnessHostComponent activateWithSanitizedBrightnessUpdates:]
+ -[SBScreenBrightnessHostComponent brightnessDidChange:]
+ -[SBScreenBrightnessHostComponent deactivate]
+ -[SBScreenBrightnessHostComponent sanitizedBrightnessDidChange:]
+ -[SBScreenBrightnessHostComponent scene:willUpdateSettings:]
+ -[SBScreenBrightnessHostComponent sceneHostingPolicyHostComponentDidUpdateHostWindowScene:]
+ -[SBScreenBrightnessParticipant .cxx_destruct]
+ -[SBScreenBrightnessParticipant _clearBrightnessRequest]
+ -[SBScreenBrightnessParticipant _updateBrightnessRequest]
+ -[SBScreenBrightnessParticipant _updateDisplayClient:]
+ -[SBScreenBrightnessParticipant dealloc]
+ -[SBScreenBrightnessParticipant displayClient:brightnessDidChange:]
+ -[SBScreenBrightnessParticipant displayClient:sanitizedBrightnessDidChange:]
+ -[SBScreenBrightnessParticipant displayClientDidInvalidate:]
+ -[SBScreenBrightnessParticipant initWithObserver:coordinator:]
+ -[SBScreenBrightnessParticipant invalidate]
+ -[SBScreenBrightnessParticipant preferredBrightness]
+ -[SBScreenBrightnessParticipant resignWindowScene]
+ -[SBScreenBrightnessParticipant setPreferredBrightness:]
+ -[SBScreenBrightnessParticipant updateWindowScene:]
+ -[SBScreenBrightnessRequest .cxx_destruct]
+ -[SBScreenBrightnessRequest brightness]
+ -[SBScreenBrightnessRequest delivered]
+ -[SBScreenBrightnessRequest initWithDisplayClient:brightness:pendingDisplayOn:]
+ -[SBScreenBrightnessRequest invalidate]
+ -[SBScreenBrightnessRequest isOverruled]
+ -[SBScreenBrightnessRequest isPendingDisplayOn]
+ -[SBScreenBrightnessRequest overruled]
+ -[SBSplitResizeWindowingModifier dimmingAlphaForLayoutRole:inAppLayout:]
+ -[SBSwitcherController _autoLayoutSpaceForAppLayout:layoutAttributes:]
+ -[SBSwitcherModifier(SharedModifierUtilities) displayItemsChangingSizeFromAppLayout:toAppLayout:fromDisplayItemLayoutAttributesMap:toDisplayItemLayoutAttributesMap:]
+ -[SpringBoard screenBrightnessCoordinator]
+ GCC_except_table317
+ GCC_except_table561
+ GCC_except_table571
+ GCC_except_table584
+ _OBJC_CLASS_$_CBDisplayBrightnessClient
+ _OBJC_CLASS_$_SBScreenBrightnessCoordinator
+ _OBJC_CLASS_$_SBScreenBrightnessDebugHUDView
+ _OBJC_CLASS_$_SBScreenBrightnessDisplayClient
+ _OBJC_CLASS_$_SBScreenBrightnessParticipant
+ _OBJC_CLASS_$_SBScreenBrightnessRequest
+ _OBJC_IVAR_$_SBAccessibilityUIServerUISceneController._presentersByPresentationStyle
+ _OBJC_IVAR_$_SBContinuityDisplayDelayedUIWindowSceneDelegate._systemEdgeGesturesIgnoreHIDEdgeFlagsAssertion
+ _OBJC_IVAR_$_SBContinuitySession._disableHomeGestureAssertion
+ _OBJC_IVAR_$_SBContinuousExposeAppToAppModifier._ignoredAppLayout
+ _OBJC_IVAR_$_SBContinuousExposeAppToAppModifier._shouldOrderToAppLayoutFront
+ _OBJC_IVAR_$_SBFlexibleWindowingAutoLayoutSpace._stageSpanningSplit
+ _OBJC_IVAR_$_SBFullScreenToPeekAnimationModifier._displayItemLayoutAttributesCalculator
+ _OBJC_IVAR_$_SBFullScreenToPeekAnimationModifier._fromLayoutAttributesMap
+ _OBJC_IVAR_$_SBFullScreenToPeekAnimationModifier._toLayoutAttributesMap
+ _OBJC_IVAR_$_SBPIPPegasusContainerAdapter._inFlightRotation
+ _OBJC_IVAR_$_SBPIPPegasusContainerAdapter._inFlightRotationCompletionHandler
+ _OBJC_IVAR_$_SBPIPPegasusContainerAdapter._inFlightRotationContentViewFrame
+ _OBJC_IVAR_$_SBPIPPegasusContainerAdapter._rotationAnimationGeneration
+ _OBJC_IVAR_$_SBScreenBrightnessCoordinator._client
+ _OBJC_IVAR_$_SBScreenBrightnessCoordinator._displayClientsByDisplayProxyIdentifier
+ _OBJC_IVAR_$_SBScreenBrightnessDebugHUDView._participant
+ _OBJC_IVAR_$_SBScreenBrightnessDebugHUDView._rawValueLabel
+ _OBJC_IVAR_$_SBScreenBrightnessDebugHUDView._sanitizedValueLabel
+ _OBJC_IVAR_$_SBScreenBrightnessDebugHUDView._stackView
+ _OBJC_IVAR_$_SBScreenBrightnessDebugHUDView._windowScene
+ _OBJC_IVAR_$_SBScreenBrightnessDebugHUDView._windowSceneValueLabel
+ _OBJC_IVAR_$_SBScreenBrightnessDisplayClient._backlightController
+ _OBJC_IVAR_$_SBScreenBrightnessDisplayClient._displayHardwareIdentifier
+ _OBJC_IVAR_$_SBScreenBrightnessDisplayClient._lock
+ _OBJC_IVAR_$_SBScreenBrightnessDisplayClient._lock_displayClient
+ _OBJC_IVAR_$_SBScreenBrightnessDisplayClient._lock_displayIsOff
+ _OBJC_IVAR_$_SBScreenBrightnessDisplayClient._lock_lastNotifiedBrightness
+ _OBJC_IVAR_$_SBScreenBrightnessDisplayClient._lock_observers
+ _OBJC_IVAR_$_SBScreenBrightnessDisplayClient._lock_registeredForBrightnessUpdates
+ _OBJC_IVAR_$_SBScreenBrightnessDisplayClient._lock_request
+ _OBJC_IVAR_$_SBScreenBrightnessDisplayClient._notifyQueue
+ _OBJC_IVAR_$_SBScreenBrightnessHostComponent._isActive
+ _OBJC_IVAR_$_SBScreenBrightnessHostComponent._observingHostedScenePolicyHostComponent
+ _OBJC_IVAR_$_SBScreenBrightnessHostComponent._participant
+ _OBJC_IVAR_$_SBScreenBrightnessHostComponent._updatesWithSanitizedBrightness
+ _OBJC_IVAR_$_SBScreenBrightnessParticipant._coordinator
+ _OBJC_IVAR_$_SBScreenBrightnessParticipant._displayClient
+ _OBJC_IVAR_$_SBScreenBrightnessParticipant._invalidated
+ _OBJC_IVAR_$_SBScreenBrightnessParticipant._observer
+ _OBJC_IVAR_$_SBScreenBrightnessParticipant._preferredBrightness
+ _OBJC_IVAR_$_SBScreenBrightnessParticipant._request
+ _OBJC_IVAR_$_SBScreenBrightnessRequest._brightness
+ _OBJC_IVAR_$_SBScreenBrightnessRequest._lock
+ _OBJC_IVAR_$_SBScreenBrightnessRequest._lock_displayClient
+ _OBJC_IVAR_$_SBScreenBrightnessRequest._lock_state
+ _OBJC_IVAR_$_SpringBoard._screenBrightnessCoordinator
+ _OBJC_METACLASS_$_SBScreenBrightnessCoordinator
+ _OBJC_METACLASS_$_SBScreenBrightnessDebugHUDView
+ _OBJC_METACLASS_$_SBScreenBrightnessDisplayClient
+ _OBJC_METACLASS_$_SBScreenBrightnessParticipant
+ _OBJC_METACLASS_$_SBScreenBrightnessRequest
+ _SBScreenBrightnessNotSet
+ _UIScreenBrightnessDidChangeNotification
+ __OBJC_$_CLASS_METHODS_SBChainableModifier(RuntimeProviding|SwitcherModifier|WindowingModifier)
+ __OBJC_$_INSTANCE_METHODS_FBScene(SBVisibilitySceneExtension_ForSceneManager|SafeAreaResolverExtensionDelegate|SBSUIHomeScreenIconStyle|InputUISceneController|LocalSynchronous|CompanionSceneHost|CompanionSceneHost_Internal|CompanionSceneHost_Testing|SBWindowSceneAccessorySceneProvider|SBScreenBrightnessHost|SBProductivityGestureDestination|SBDynamicMemoryControllingHost|SBHostedScenePolicy)
+ __OBJC_$_INSTANCE_METHODS_SBChainableModifier(RuntimeProviding|SwitcherModifier|WindowingModifier)
+ __OBJC_$_INSTANCE_METHODS_SBChainableModifierEvent(SBSwitcherModifierEvent|SBWindowingModifierActivity)
+ __OBJC_$_INSTANCE_METHODS_SBChainableModifierEventResponse(SBSwitcherModifierEventResponse|SBWindowingModifierResponse)
+ __OBJC_$_INSTANCE_METHODS_SBScreenBrightnessCoordinator
+ __OBJC_$_INSTANCE_METHODS_SBScreenBrightnessDebugHUDView
+ __OBJC_$_INSTANCE_METHODS_SBScreenBrightnessDisplayClient
+ __OBJC_$_INSTANCE_METHODS_SBScreenBrightnessParticipant
+ __OBJC_$_INSTANCE_METHODS_SBScreenBrightnessRequest
+ __OBJC_$_INSTANCE_METHODS_SBWindowingModifierActivity(TransitionEvent|GestureEvent|StripChangedModifierActivity)
+ __OBJC_$_INSTANCE_VARIABLES_SBScreenBrightnessCoordinator
+ __OBJC_$_INSTANCE_VARIABLES_SBScreenBrightnessDebugHUDView
+ __OBJC_$_INSTANCE_VARIABLES_SBScreenBrightnessDisplayClient
+ __OBJC_$_INSTANCE_VARIABLES_SBScreenBrightnessParticipant
+ __OBJC_$_INSTANCE_VARIABLES_SBScreenBrightnessRequest
+ __OBJC_$_PROP_LIST_SBScreenBrightnessCoordinator
+ __OBJC_$_PROP_LIST_SBScreenBrightnessDebugHUDView
+ __OBJC_$_PROP_LIST_SBScreenBrightnessDisplayClient
+ __OBJC_$_PROP_LIST_SBScreenBrightnessParticipant
+ __OBJC_$_PROP_LIST_SBScreenBrightnessRequest
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBScreenBrightnessDisplayClientObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SBScreenBrightnessObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBScreenBrightnessDisplayClientObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SBScreenBrightnessHost
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBScreenBrightnessDisplayClientObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBScreenBrightnessHost
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SBScreenBrightnessObserving
+ __OBJC_$_PROTOCOL_REFS_SBScreenBrightnessDisplayClientObserver
+ __OBJC_$_PROTOCOL_REFS_SBScreenBrightnessHost
+ __OBJC_$_PROTOCOL_REFS_SBScreenBrightnessObserving
+ __OBJC_CLASS_PROTOCOLS_$_FBScene(SBVisibilitySceneExtension_ForSceneManager|SafeAreaResolverExtensionDelegate|SBSUIHomeScreenIconStyle|InputUISceneController|LocalSynchronous|CompanionSceneHost|CompanionSceneHost_Internal|CompanionSceneHost_Testing|SBWindowSceneAccessorySceneProvider|SBScreenBrightnessHost|SBProductivityGestureDestination|SBDynamicMemoryControllingHost|SBHostedScenePolicy)
+ __OBJC_CLASS_PROTOCOLS_$_SBScreenBrightnessCoordinator
+ __OBJC_CLASS_PROTOCOLS_$_SBScreenBrightnessDebugHUDView
+ __OBJC_CLASS_PROTOCOLS_$_SBScreenBrightnessDisplayClient
+ __OBJC_CLASS_PROTOCOLS_$_SBScreenBrightnessParticipant
+ __OBJC_CLASS_PROTOCOLS_$_SBScreenBrightnessRequest
+ __OBJC_CLASS_RO_$_SBScreenBrightnessCoordinator
+ __OBJC_CLASS_RO_$_SBScreenBrightnessDebugHUDView
+ __OBJC_CLASS_RO_$_SBScreenBrightnessDisplayClient
+ __OBJC_CLASS_RO_$_SBScreenBrightnessParticipant
+ __OBJC_CLASS_RO_$_SBScreenBrightnessRequest
+ __OBJC_LABEL_PROTOCOL_$_SBScreenBrightnessDisplayClientObserver
+ __OBJC_LABEL_PROTOCOL_$_SBScreenBrightnessHost
+ __OBJC_LABEL_PROTOCOL_$_SBScreenBrightnessObserving
+ __OBJC_METACLASS_RO_$_SBScreenBrightnessCoordinator
+ __OBJC_METACLASS_RO_$_SBScreenBrightnessDebugHUDView
+ __OBJC_METACLASS_RO_$_SBScreenBrightnessDisplayClient
+ __OBJC_METACLASS_RO_$_SBScreenBrightnessParticipant
+ __OBJC_METACLASS_RO_$_SBScreenBrightnessRequest
+ __OBJC_PROTOCOL_$_SBScreenBrightnessDisplayClientObserver
+ __OBJC_PROTOCOL_$_SBScreenBrightnessHost
+ __OBJC_PROTOCOL_$_SBScreenBrightnessObserving
+ __UISceneRenderingEnvironmentBrightnessNotSet
+ ___165-[SBSwitcherModifier(SharedModifierUtilities) displayItemsChangingSizeFromAppLayout:toAppLayout:fromDisplayItemLayoutAttributesMap:toDisplayItemLayoutAttributesMap:]_block_invoke
+ ___52-[SBScreenBrightnessDisplayClient _displayDidTurnOn]_block_invoke
+ ___52-[SBScreenBrightnessDisplayClient _displayDidTurnOn]_block_invoke_2
+ ___52-[SBScreenBrightnessDisplayClient brightnessUpdate:]_block_invoke
+ ___60+[SBHomeScreenService _validationErrorForStashedLayoutName:]_block_invoke
+ ___60-[SBScreenBrightnessDisplayClient _updateBrightnessTracking]_block_invoke
+ ___62-[SBContinuousExposeAppToAppModifier didMoveToParentModifier:]_block_invoke
+ ___68-[SBScreenBrightnessDisplayClient brightnessControlAvailableUpdate:]_block_invoke
+ ___75-[_SBFullScreenAppFloorSwitcherModifier handleSwitcherShortcutActionEvent:]_block_invoke_10
+ ___75-[_SBFullScreenAppFloorSwitcherModifier handleSwitcherShortcutActionEvent:]_block_invoke_9
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_36
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_37
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_38
+ ___79-[SBMainDisplayLayoutStateManager _layoutStateForApplicationTransitionContext:]_block_invoke_39
+ ___83-[SBContinuousExposeRootSwitcherModifier transitionModifierForMainTransitionEvent:]_block_invoke_10
+ ___block_descriptor_48_e8_32s40r_e26_v24?0"SBDisplayItem"8q16ls32l8r40l8
+ ___block_descriptor_49_e8_32s40s_e25_B16?0"SBLayoutElement"8ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e43_B16?0"SBFlexibleWindowingAutoLayoutItem"8ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e23_B16?0"SBDisplayItem"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48bs56r64r72r_e17_v16?0"NSArray"8lr56l8s32l8s40l8r64l8s48l8r72l8
+ ___block_descriptor_88_e8_32s40s48bs56r64r72r80r_e8_v16?0q8ls32l8s40l8r56l8r64l8r72l8r80l8s48l8
+ __clamp
+ __validationErrorForStashedLayoutName:.invalidCharacters
+ __validationErrorForStashedLayoutName:.onceToken
- -[SBMinimizeItemFromSplitResizeWindowingModifier opacityForLayoutRole:inAppLayout:atIndex:]
- -[SBScreenBrightnessHostComponent _applyPreferredBrightness:]
- -[SBScreenBrightnessHostComponent _configureDisplayClientForDisplayConfiguration:]
- -[SBScreenBrightnessHostComponent _flushPendingBrightnessToScene:]
- -[SBScreenBrightnessHostComponent _tearDownDisplayClient]
- -[SBScreenBrightnessHostComponent brightnessUpdate:]
- -[SBScreenBrightnessHostComponent init]
- -[SBScreenBrightnessHostComponent notifyQueue]
- -[SBScreenBrightnessHostComponent scene:didUpdateClientSettings:]
- -[SBScreenBrightnessHostComponent scene:didUpdateSettings:]
- -[SBScreenBrightnessHostComponent setScene:]
- -[SBSplitResizeWindowingModifier opacityForLayoutRole:inAppLayout:atIndex:]
- -[SBSwitcherWindowingSettings setWindowDragRubberBandedTranslationRange:]
- -[SBSwitcherWindowingSettings windowDragRubberBandedTranslationRange]
- GCC_except_table570
- GCC_except_table583
- GCC_except_table585
- _OBJC_IVAR_$_SBFlexibleWindowingWindowDragSwitcherModifier._rubberBandingRange
- _OBJC_IVAR_$_SBScreenBrightnessHostComponent._displayClient
- _OBJC_IVAR_$_SBScreenBrightnessHostComponent._lastNotifiedBrightnessLock
- _OBJC_IVAR_$_SBScreenBrightnessHostComponent._lock_lastNotifiedBrightness
- _OBJC_IVAR_$_SBScreenBrightnessHostComponent._notifyQueue
- _OBJC_IVAR_$_SBScreenBrightnessHostComponent._pendingBrightness
- _OBJC_IVAR_$_SBSwitcherWindowingSettings._windowDragRubberBandedTranslationRange
- _SBScreenBrightnessSharedCBClient.onceToken
- _SBScreenBrightnessSharedCBClient.sharedClient
- __OBJC_$_CLASS_METHODS_SBChainableModifier(RuntimeProviding|WindowingModifier|SwitcherModifier)
- __OBJC_$_INSTANCE_METHODS_FBScene(SBVisibilitySceneExtension_ForSceneManager|SBSUIHomeScreenIconStyle|InputUISceneController|LocalSynchronous|CompanionSceneHost|CompanionSceneHost_Internal|CompanionSceneHost_Testing|SBWindowSceneAccessorySceneProvider|SBProductivityGestureDestination|SafeAreaResolverExtensionDelegate|SBDynamicMemoryControllingHost|SBHostedScenePolicy)
- __OBJC_$_INSTANCE_METHODS_SBChainableModifier(RuntimeProviding|WindowingModifier|SwitcherModifier)
- __OBJC_$_INSTANCE_METHODS_SBChainableModifierEvent(SBWindowingModifierActivity|SBSwitcherModifierEvent)
- __OBJC_$_INSTANCE_METHODS_SBChainableModifierEventResponse(SBWindowingModifierResponse|SBSwitcherModifierEventResponse)
- __OBJC_$_INSTANCE_METHODS_SBWindowingModifierActivity(TransitionEvent|StripChangedModifierActivity|GestureEvent)
- __OBJC_CLASS_PROTOCOLS_$_FBScene(SBVisibilitySceneExtension_ForSceneManager|SBSUIHomeScreenIconStyle|InputUISceneController|LocalSynchronous|CompanionSceneHost|CompanionSceneHost_Internal|CompanionSceneHost_Testing|SBWindowSceneAccessorySceneProvider|SBProductivityGestureDestination|SafeAreaResolverExtensionDelegate|SBDynamicMemoryControllingHost|SBHostedScenePolicy)
- ___52-[SBScreenBrightnessHostComponent brightnessUpdate:]_block_invoke
- ___SBScreenBrightnessSharedCBClient_block_invoke
- ___block_descriptor_72_e8_32s40s48r56r64r_e17_v16?0"NSArray"8lr48l8s32l8s40l8r56l8r64l8
- ___block_descriptor_80_e8_32s40s48r56r64r72r_e8_v16?0q8ls32l8s40l8r48l8r56l8r64l8r72l8
- ___block_descriptor_88_e8_32s40bs_e11_v16?0B8B12ls32l8s40l8
CStrings:
+ "%.04f"
+ "%s failed to save icon state for stashed layout \"%{public}@\""
+ "(Display - %{public}@) not evaluating enablement because I'm invalidated"
+ "-[SBHomeScreenService simulateCampoEnablementChange]"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SpringBoard/Extensions/Screen Brightness/SBScreenBrightnessCoordinator.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SpringBoard/Extensions/Screen Brightness/SBScreenBrightnessDisplayClient.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SpringBoard/Extensions/Screen Brightness/SBScreenBrightnessParticipant.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/SpringBoard/Extensions/Screen Brightness/SBScreenBrightnessRequest.m"
+ "Display %@ already has a screen brightness client"
+ "Failed to deliver preferred brightness %.2f for display %{public}@: %{public}@"
+ "Failed to get brightness for display %{public}@: %{public}@"
+ "Failed to save the Home Screen layout as \"%@\"."
+ "Layout name \"%@\" contains invalid characters; only letters, digits, '-', and '_' are allowed."
+ "Layout name must be %lu characters or fewer."
+ "Layout name must not be empty."
+ "Not reading brightness for display %{public}@: control availability is %lu (%{public}@)"
+ "Raw:"
+ "SBScreenBrightnessCoordinator.m"
+ "SBScreenBrightnessDisplayClient.m"
+ "SBScreenBrightnessParticipant.m"
+ "SBScreenBrightnessRequest.m"
+ "Sanitized:"
+ "Window Scene:"
+ "[%p] [PIP Pegasus Adapter] Performing rotation: %ld from contentViewFrame: %{public}@"
+ "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
+ "com.apple.springboard.screenbrightness.notify.%@"
+ "displayClient"
+ "stageSpanningSplit"
+ "updating system gesture window frame from %{public}@ to %{public}@"
+ "v24@?0@\"SBDisplayItem\"8q16"
+ "\xa4\xf0Q"
- "Failed to get initial brightness for display %{public}@: %{public}@"
- "Failed to set preferred brightness %.2f: %{public}@"
- "No CADisplay found matching hardware identifier %{public}@"
- "Rubber-Banded Translation Range"
- "com.apple.springboard.screenbrightness.notify"
- "\xa4\xf0A"
```
