## CoverSheet

> `/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet`

```diff

-4557.1.8.105.0
-  __TEXT.__text: 0x171678
+4557.1.15.102.0
+  __TEXT.__text: 0x1725e4
   __TEXT.__auth_stubs: 0x1400
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x161b4
-  __TEXT.__const: 0x2bf0
-  __TEXT.__cstring: 0xa05a
-  __TEXT.__oslogstring: 0x8c19
+  __TEXT.__objc_methlist: 0x1635c
+  __TEXT.__const: 0x2be0
+  __TEXT.__cstring: 0xa146
+  __TEXT.__oslogstring: 0x8cb2
   __TEXT.__gcc_except_tab: 0xcfc
   __TEXT.__ustring: 0xa4
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__unwind_info: 0x4108
-  __TEXT.__objc_classname: 0x3489
-  __TEXT.__objc_methname: 0x4074f
-  __TEXT.__objc_methtype: 0x9d1c
-  __TEXT.__objc_stubs: 0x25aa0
-  __DATA_CONST.__got: 0x1580
-  __DATA_CONST.__const: 0x2a90
-  __DATA_CONST.__objc_classlist: 0x798
+  __TEXT.__unwind_info: 0x4170
+  __TEXT.__objc_classname: 0x34bf
+  __TEXT.__objc_methname: 0x40db9
+  __TEXT.__objc_methtype: 0x9e0f
+  __TEXT.__objc_stubs: 0x25dc0
+  __DATA_CONST.__got: 0x1588
+  __DATA_CONST.__const: 0x2af8
+  __DATA_CONST.__objc_classlist: 0x7a0
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x688
+  __DATA_CONST.__objc_protolist: 0x690
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc4a8
+  __DATA_CONST.__objc_selrefs: 0xc5a0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x5e0
+  __DATA_CONST.__objc_superrefs: 0x5e8
   __DATA_CONST.__objc_arraydata: 0x1078
   __AUTH_CONST.__auth_got: 0xa10
-  __AUTH_CONST.__const: 0x860
-  __AUTH_CONST.__cfstring: 0xbf40
-  __AUTH_CONST.__objc_const: 0x3c5a0
+  __AUTH_CONST.__const: 0x8a0
+  __AUTH_CONST.__cfstring: 0xc0a0
+  __AUTH_CONST.__objc_const: 0x3c7e0
   __AUTH_CONST.__objc_doubleobj: 0x660
   __AUTH_CONST.__objc_arrayobj: 0x1248
   __AUTH_CONST.__objc_intobj: 0x438
-  __AUTH.__objc_data: 0x1310
-  __DATA.__objc_ivar: 0x1b44
-  __DATA.__data: 0x4e68
+  __AUTH.__objc_data: 0x12c0
+  __DATA.__objc_ivar: 0x1b60
+  __DATA.__data: 0x4ec8
   __DATA.__bss: 0xd0
-  __DATA_DIRTY.__objc_data: 0x38e0
+  __DATA_DIRTY.__objc_data: 0x3980
   __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A27931A7-F633-3ED6-9B18-C1C53BF108E1
-  Functions: 7093
-  Symbols:   25951
-  CStrings:  14268
+  UUID: E2353496-7DC6-38F8-93BC-2DF9E6E16DE9
+  Functions: 7129
+  Symbols:   26074
+  CStrings:  14344
 
Symbols:
+ +[CSAODTransitionSettings settingsControllerModule]
+ +[CSNotificationLegibilityDimView _fullDimColorMatrixWithUserInterfaceStyle:]
+ +[CSNotificationLegibilityDimView _localizedColorMatrixWithUserInterfaceStyle:]
+ -[CSAODTransitionSettings aodClockResponse]
+ -[CSAODTransitionSettings aodGeneralResponse]
+ -[CSAODTransitionSettings setAodClockResponse:]
+ -[CSAODTransitionSettings setAodGeneralResponse:]
+ -[CSAODTransitionSettings setDefaultValues]
+ -[CSActivityViewController _handleButtonPressOfType:]
+ -[CSActivityViewController _lockButtonPressed:]
+ -[CSActivityViewController _volumeButtonPressed:]
+ -[CSCombinedListViewController coverSheetViewControllerDidWakeForSource:]
+ -[CSCombinedListViewController notificationStructuredListViewControllerRequestsDiagnosticsDictionary:]
+ -[CSCoverSheetViewController _clearChargingModalTimerPerformingHandler:]
+ -[CSCoverSheetViewController _complicationsInterpretGestureRecognizerLocationAsContent:]
+ -[CSCoverSheetViewController _gestureRecognizer:hitContainerWithView:componentType:interpretsViewAsContent:]
+ -[CSCoverSheetViewController _updateClockAppearanceForAODTransitionToInactive:animated:]
+ -[CSCoverSheetViewController _updateGeneralAppearanceForAODTransitionToInactive:animated:]
+ -[CSCoverSheetViewController _wallpaperLumaFromWallpaperComponent:]
+ -[CSCoverSheetViewController prepareForTransitionToPresented:reversingTransition:forUserGesture:]
+ -[CSCoverSheetViewController timeTextHeight]
+ -[CSLockScreenSettings aodTransitionSettings]
+ -[CSLockScreenSettings setAodTransitionSettings:]
+ -[CSMainPageContentViewController diagnosticsDictionaryForCombinedListViewController:]
+ -[CSMainPageContentViewController diagnosticsProvider]
+ -[CSMainPageContentViewController setDiagnosticsProvider:]
+ -[CSNotificationLegibilityDimView _updateDimLayerVisibility]
+ -[CSNotificationLegibilityDimView _updateForUserInterfaceStyle]
+ -[CSNotificationLegibilityDimView isVisible]
+ -[CSPosterSwitcherViewController _updatePreferredActiveAppearance:withReason:forSceneHandle:]
+ -[CSPosterSwitcherViewController activeAppearanceAssertion]
+ -[CSPosterSwitcherViewController zStackParticipant:updatePreferences:]
+ -[CSPosterSwitcherViewController zStackParticipantDidChange:]
+ GCC_except_table120
+ GCC_except_table177
+ GCC_except_table218
+ GCC_except_table317
+ GCC_except_table463
+ GCC_except_table522
+ GCC_except_table542
+ GCC_except_table553
+ GCC_except_table633
+ GCC_except_table690
+ GCC_except_table700
+ GCC_except_table702
+ GCC_except_table711
+ GCC_except_table724
+ GCC_except_table734
+ GCC_except_table87
+ GCC_except_table90
+ _OBJC_CLASS_$_CSAODTransitionSettings
+ _OBJC_CLASS_$_UISpringTimingParameters
+ _OBJC_IVAR_$_CSAODTransitionSettings._aodClockResponse
+ _OBJC_IVAR_$_CSAODTransitionSettings._aodGeneralResponse
+ _OBJC_IVAR_$_CSCombinedListViewController._reduceIdleTimerDurationDueToNotificationWake
+ _OBJC_IVAR_$_CSLockScreenSettings._aodTransitionSettings
+ _OBJC_IVAR_$_CSMainPageContentViewController._diagnosticsProvider
+ _OBJC_IVAR_$_CSNotificationLegibilityDimView._visible
+ _OBJC_IVAR_$_CSPosterSwitcherViewController._activeAppearanceAssertion
+ _OBJC_METACLASS_$_CSAODTransitionSettings
+ __OBJC_$_CLASS_METHODS_CSAODTransitionSettings
+ __OBJC_$_INSTANCE_METHODS_CSAODTransitionSettings
+ __OBJC_$_INSTANCE_VARIABLES_CSAODTransitionSettings
+ __OBJC_$_PROP_LIST_CSAODTransitionSettings
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSMainPageDiagnosticsProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSMainPageDiagnosticsProvider
+ __OBJC_$_PROTOCOL_REFS_CSMainPageDiagnosticsProvider
+ __OBJC_CLASS_RO_$_CSAODTransitionSettings
+ __OBJC_LABEL_PROTOCOL_$_CSMainPageDiagnosticsProvider
+ __OBJC_METACLASS_RO_$_CSAODTransitionSettings
+ __OBJC_PROTOCOL_$_CSMainPageDiagnosticsProvider
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.831
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.835
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.836
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.837
+ ___48-[CSCoverSheetViewController accessoryDetached:]_block_invoke.797
+ ___51-[CSCoverSheetViewController _updateHomeAffordance]_block_invoke.696
+ ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.469
+ ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.478
+ ___61-[CSCoverSheetViewController _updateNotificationDimmingLayer]_block_invoke
+ ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.761
+ ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.762
+ ___65-[CSCoverSheetViewController transitionSource:didEndWithContext:]_block_invoke.508
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.808
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.809
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.816
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke_2.814
+ ___79-[CSCoverSheetViewController _dismissRemoteViewControllerForReason:completion:]_block_invoke.605
+ ___88-[CSCoverSheetViewController _complicationsInterpretGestureRecognizerLocationAsContent:]_block_invoke
+ ___88-[CSCoverSheetViewController _complicationsInterpretGestureRecognizerLocationAsContent:]_block_invoke_2
+ ___88-[CSCoverSheetViewController _complicationsInterpretGestureRecognizerLocationAsContent:]_block_invoke_3
+ ___88-[CSCoverSheetViewController _updateClockAppearanceForAODTransitionToInactive:animated:]_block_invoke
+ ___88-[CSCoverSheetViewController _updateClockAppearanceForAODTransitionToInactive:animated:]_block_invoke_2
+ ___89-[CSCoverSheetViewController _updateActiveBehaviorsForReason:updatingAppearanceIfNeeded:]_block_invoke.669
+ ___90-[CSCoverSheetViewController _removeRemoteViewControllerForInvalidatedSession:completion:]_block_invoke.606
+ ___90-[CSCoverSheetViewController _updateGeneralAppearanceForAODTransitionToInactive:animated:]_block_invoke
+ ___90-[CSCoverSheetViewController _updateGeneralAppearanceForAODTransitionToInactive:animated:]_block_invoke_2
+ ___90-[CSCoverSheetViewController _updateGeneralAppearanceForAODTransitionToInactive:animated:]_block_invoke_3
+ ___90-[CSCoverSheetViewController _updateGeneralAppearanceForAODTransitionToInactive:animated:]_block_invoke_4
+ ___block_descriptor_32_e8_v12?0B8l
+ ___block_descriptor_40_e27_v16?0"<UIMutableTraits>"8l
+ ___block_descriptor_40_e8_32s_e16_B16?0"UIView"8ls32l8
+ ___block_literal_global.2368
+ ___block_literal_global.268
+ ___block_literal_global.273
+ ___block_literal_global.353
+ ___block_literal_global.421
+ ___block_literal_global.426
+ ___block_literal_global.431
+ ___block_literal_global.436
+ ___block_literal_global.441
+ ___block_literal_global.446
+ ___block_literal_global.45
+ ___block_literal_global.52
+ ___block_literal_global.71
+ ___block_literal_global.826
+ ___block_literal_global.828
+ _objc_msgSend$_clearChargingModalTimerPerformingHandler:
+ _objc_msgSend$_complicationsInterpretGestureRecognizerLocationAsContent:
+ _objc_msgSend$_fullDimColorMatrixWithUserInterfaceStyle:
+ _objc_msgSend$_gestureRecognizer:hitContainerWithView:componentType:interpretsViewAsContent:
+ _objc_msgSend$_handleButtonPressOfType:
+ _objc_msgSend$_localizedColorMatrixWithUserInterfaceStyle:
+ _objc_msgSend$_updateClockAppearanceForAODTransitionToInactive:animated:
+ _objc_msgSend$_updateDimLayerVisibility
+ _objc_msgSend$_updateGeneralAppearanceForAODTransitionToInactive:animated:
+ _objc_msgSend$_updatePreferredActiveAppearance:withReason:forSceneHandle:
+ _objc_msgSend$_wallpaperLumaFromWallpaperComponent:
+ _objc_msgSend$acquireActiveAppearanceAssertionWithReason:activeAppearance:priority:
+ _objc_msgSend$adaptiveTimeTextHeight
+ _objc_msgSend$aodClockResponse
+ _objc_msgSend$aodGeneralResponse
+ _objc_msgSend$aodTransitionSettings
+ _objc_msgSend$coverSheetViewControllerDidWakeForSource:
+ _objc_msgSend$diagnosticsDictionaryForCombinedListViewController:
+ _objc_msgSend$initWithDuration:bounce:
+ _objc_msgSend$isVisible
+ _objc_msgSend$registerForTraitChanges:withTarget:action:
+ _objc_msgSend$setAodClockResponse:
+ _objc_msgSend$setAodGeneralResponse:
+ _objc_msgSend$setDiagnosticsProvider:
+ _objc_msgSend$setLuminanceChangeAnimationResponse:
+ _objc_msgSend$setSuppressSystemApertureForSystemChromeSuppression:
+ _objc_msgSend$settlingDuration
+ _objc_msgSend$timeTextHeight
+ _objc_msgSend$traitCollectionByModifyingTraits:
+ _objc_msgSend$widgetGridContentView
- +[CSNotificationLegibilityDimView _fullDimColorMatrix]
- +[CSNotificationLegibilityDimView _localizedDimColorMatrix]
- -[CSActivityViewController wouldHandleButtonEvent:]
- -[CSCoverSheetViewController _shouldAllowBottomGridPosition]
- GCC_except_table116
- GCC_except_table171
- GCC_except_table212
- GCC_except_table216
- GCC_except_table311
- GCC_except_table451
- GCC_except_table509
- GCC_except_table529
- GCC_except_table540
- GCC_except_table619
- GCC_except_table677
- GCC_except_table687
- GCC_except_table689
- GCC_except_table698
- GCC_except_table710
- GCC_except_table720
- GCC_except_table86
- GCC_except_table89
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.819
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.823
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.824
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.825
- ___48-[CSCoverSheetViewController accessoryDetached:]_block_invoke.785
- ___51-[CSCoverSheetViewController _updateHomeAffordance]_block_invoke.687
- ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.461
- ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.462
- ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.750
- ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.751
- ___65-[CSCoverSheetViewController transitionSource:didEndWithContext:]_block_invoke.500
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.796
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.797
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.804
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke_2.802
- ___74-[CSCoverSheetViewController _updateAppearanceForAODTransitionToInactive:]_block_invoke
- ___74-[CSCoverSheetViewController _updateAppearanceForAODTransitionToInactive:]_block_invoke_2
- ___74-[CSCoverSheetViewController _updateAppearanceForAODTransitionToInactive:]_block_invoke_3
- ___79-[CSCoverSheetViewController _dismissRemoteViewControllerForReason:completion:]_block_invoke.596
- ___89-[CSCoverSheetViewController _updateActiveBehaviorsForReason:updatingAppearanceIfNeeded:]_block_invoke.660
- ___90-[CSCoverSheetViewController _removeRemoteViewControllerForInvalidatedSession:completion:]_block_invoke.597
- ___block_literal_global.2346
- ___block_literal_global.345
- ___block_literal_global.413
- ___block_literal_global.42
- ___block_literal_global.423
- ___block_literal_global.428
- ___block_literal_global.433
- ___block_literal_global.438
- ___block_literal_global.49
- ___block_literal_global.66
- ___block_literal_global.814
- ___block_literal_global.816
- _objc_msgSend$_fullDimColorMatrix
- _objc_msgSend$_localizedDimColorMatrix
- _objc_msgSend$_setFont:
- _objc_msgSend$_shouldAllowBottomGridPosition
- _objc_msgSend$handleHardwareButtonPressForType:
CStrings:
+ "%{public}@ [ActivityID: %{public}@, hardware button press of type %lu was sent to scene: %{BOOL}u"
+ "?\n"
+ "@\"<CSMainPageDiagnosticsProvider>\""
+ "@\"CSAODTransitionSettings\""
+ "@\"NSDictionary\"24@0:8@\"CSCombinedListViewController\"16"
+ "@\"SBSceneHandleActiveAppearanceAssertion\""
+ "AOD Transition"
+ "AOD Transition Settings"
+ "B16@?0@\"UIView\"8"
+ "B48@0:8@16@24q32@?40"
+ "CSAODTransitionSettings"
+ "CSMainPageDiagnosticsProvider"
+ "Clock-Specific"
+ "General"
+ "Response"
+ "T@\"<CSMainPageDiagnosticsProvider>\",W,N,V_diagnosticsProvider"
+ "T@\"CSAODTransitionSettings\",&,V_aodTransitionSettings"
+ "T@\"SBSceneHandleActiveAppearanceAssertion\",R,N,V_activeAppearanceAssertion"
+ "Td,N,V_aodClockResponse"
+ "Td,N,V_aodGeneralResponse"
+ "[CSCombinedList][AggBehavior] woke up for notification"
+ "_UIBacklightLuminance-Clock"
+ "_activeAppearanceAssertion"
+ "_aodClockResponse"
+ "_aodGeneralResponse"
+ "_aodTransitionSettings"
+ "_clearChargingModalTimerPerformingHandler:"
+ "_complicationsInterpretGestureRecognizerLocationAsContent:"
+ "_diagnosticsProvider"
+ "_fullDimColorMatrixWithUserInterfaceStyle:"
+ "_gestureRecognizer:hitContainerWithView:componentType:interpretsViewAsContent:"
+ "_handleButtonPressOfType:"
+ "_localizedColorMatrixWithUserInterfaceStyle:"
+ "_reduceIdleTimerDurationDueToNotificationWake"
+ "_updateClockAppearanceForAODTransitionToInactive:animated:"
+ "_updateDimLayerVisibility"
+ "_updateForUserInterfaceStyle"
+ "_updateGeneralAppearanceForAODTransitionToInactive:animated:"
+ "_updatePreferredActiveAppearance:withReason:forSceneHandle:"
+ "_volumeButtonPressed:"
+ "_wallpaperLumaFromWallpaperComponent:"
+ "acquireActiveAppearanceAssertionWithReason:activeAppearance:priority:"
+ "activeAppearanceAssertion"
+ "adaptiveTimeTextHeight"
+ "aodClockResponse"
+ "aodGeneralResponse"
+ "aodTransitionSettings"
+ "clockTimeHeight"
+ "coverSheetViewControllerDidWakeForSource:"
+ "diagnosticsDictionaryForCombinedListViewController:"
+ "diagnosticsProvider"
+ "initWithDuration:bounce:"
+ "notificationStructuredListViewControllerRequestsDiagnosticsDictionary:"
+ "poster view controller did appear"
+ "prepareForTransitionToPresented:reversingTransition:forUserGesture:"
+ "registerForTraitChanges:withTarget:action:"
+ "setAodClockResponse:"
+ "setAodGeneralResponse:"
+ "setAodTransitionSettings:"
+ "setDiagnosticsProvider:"
+ "setLuminanceChangeAnimationResponse:"
+ "setSuppressSystemApertureForSystemChromeSuppression:"
+ "settlingDuration"
+ "timeTextHeight"
+ "traitCollectionByModifyingTraits:"
+ "v16@?0@\"<UIMutableTraits>\"8"
+ "v40@0:8q16@24@32"
+ "zStackParticipantDidChange:"
+ "{CAColorMatrix=ffffffffffffffffffff}24@0:8q16"
- "?\t"
- "InspectorGadget"
- "_fullDimColorMatrix"
- "_localizedDimColorMatrix"
- "_setFont:"
- "_shouldAllowBottomGridPosition"
- "handleHardwareButtonPressForType:"

```
