## CoverSheet

> `/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet`

```diff

-4557.1.18.101.0
-  __TEXT.__text: 0x173048
-  __TEXT.__auth_stubs: 0x1410
+4557.1.19.106.0
+  __TEXT.__text: 0x174cb4
+  __TEXT.__auth_stubs: 0x1420
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x1642c
-  __TEXT.__const: 0x2bf0
-  __TEXT.__cstring: 0xa256
-  __TEXT.__oslogstring: 0x8f9f
+  __TEXT.__objc_methlist: 0x1656c
+  __TEXT.__const: 0x2c00
+  __TEXT.__cstring: 0xa37e
+  __TEXT.__oslogstring: 0x8fe7
   __TEXT.__gcc_except_tab: 0xd00
   __TEXT.__ustring: 0xa4
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__unwind_info: 0x4168
+  __TEXT.__unwind_info: 0x41a8
   __TEXT.__objc_classname: 0x34bf
-  __TEXT.__objc_methname: 0x410e4
-  __TEXT.__objc_methtype: 0x9e0f
-  __TEXT.__objc_stubs: 0x25ee0
+  __TEXT.__objc_methname: 0x41527
+  __TEXT.__objc_methtype: 0x9e39
+  __TEXT.__objc_stubs: 0x26140
   __DATA_CONST.__got: 0x1588
-  __DATA_CONST.__const: 0x2b20
+  __DATA_CONST.__const: 0x2b68
   __DATA_CONST.__objc_classlist: 0x7a0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x690
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc630
+  __DATA_CONST.__objc_selrefs: 0xc6f0
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x5e8
   __DATA_CONST.__objc_arraydata: 0x1078
-  __AUTH_CONST.__auth_got: 0xa18
-  __AUTH_CONST.__const: 0x8c0
-  __AUTH_CONST.__cfstring: 0xc220
-  __AUTH_CONST.__objc_const: 0x3c980
+  __AUTH_CONST.__auth_got: 0xa20
+  __AUTH_CONST.__const: 0xcc0
+  __AUTH_CONST.__cfstring: 0xc440
+  __AUTH_CONST.__objc_const: 0x3cad0
   __AUTH_CONST.__objc_doubleobj: 0x660
   __AUTH_CONST.__objc_arrayobj: 0x1248
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH.__objc_data: 0x12c0
-  __DATA.__objc_ivar: 0x1b7c
+  __DATA.__objc_ivar: 0x1b98
   __DATA.__data: 0x4ec8
   __DATA.__bss: 0xd0
   __DATA_DIRTY.__objc_data: 0x3980

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9D914418-436F-3550-8C66-1D12FB344841
-  Functions: 7149
-  Symbols:   26131
-  CStrings:  14410
+  UUID: D085E369-2A0D-3A0D-BB08-EAC89173DA53
+  Functions: 7208
+  Symbols:   26310
+  CStrings:  14485
 
Symbols:
+ -[CSAODTransitionSettings _setAodClockResponseMultiplier:]
+ -[CSAODTransitionSettings _setAodGeneralResponseMultiplier:]
+ -[CSCombinedListViewController _resetReducedIdleTimeFlagsIfNeeded]
+ -[CSCombinedListViewController coverSheetViewController:didWakeForSource:]
+ -[CSCoverSheetFlyInSettings _setFlyAlphaResponseMultiplier:]
+ -[CSCoverSheetFlyInSettings _setFlyInResponseMultiplier:]
+ -[CSCoverSheetFlyInSettings _setFlyOutResponseMultiplier:]
+ -[CSCoverSheetFlyInSettings _setFlyZCurveFactorMultiplier:]
+ -[CSCoverSheetFlyInSettings _setFlyZResponseMultiplier:]
+ -[CSCoverSheetFlyInSettings iconFlyAlphaResponse]
+ -[CSCoverSheetFlyInSettings iconFlyZCurveFactor]
+ -[CSCoverSheetFlyInSettings iconFlyZResponse]
+ -[CSCoverSheetFlyInSettings setIconFlyAlphaResponse:]
+ -[CSCoverSheetFlyInSettings setIconFlyZCurveFactor:]
+ -[CSCoverSheetFlyInSettings setIconFlyZResponse:]
+ -[CSCoverSheetTransitionsSettings _setBaseCoverSheetSettingsWithMultiplier:]
+ -[CSCoverSheetTransitionsSettings _setInPlaceCoverSheetSettingsWithMultiplier:]
+ -[CSCoverSheetTransitionsSettings damping]
+ -[CSCoverSheetTransitionsSettings inPlaceDamping]
+ -[CSCoverSheetTransitionsSettings inPlaceResponse]
+ -[CSCoverSheetTransitionsSettings response]
+ -[CSCoverSheetTransitionsSettings setDamping:]
+ -[CSCoverSheetTransitionsSettings setInPlaceDamping:]
+ -[CSCoverSheetTransitionsSettings setInPlaceResponse:]
+ -[CSCoverSheetTransitionsSettings setResponse:]
+ -[CSCoverSheetViewController _updateForGlassLegibilitySetting]
+ -[CSCoverSheetViewController isShowingNonNotificationContent]
+ -[CSHorizontalScrollFailureRecognizer allowsMostSwipes]
+ -[CSHorizontalScrollFailureRecognizer preventsScrollToTrailing]
+ -[CSHorizontalScrollFailureRecognizer setAllowsMostSwipes:]
+ -[CSHorizontalScrollFailureRecognizer setPreventsScrollToTrailing:]
+ -[CSMainPageContentViewController isShowingNonNotificationContent]
+ -[CSQuickActionControlGlyphView _updateControlConfigurationColorSchemeWithTraitCollection:previousTraitCollection:]
+ -[CSScrollGestureController preventsScrollToTrailing]
+ -[CSScrollGestureController setPreventsScrollToTrailing:]
+ GCC_except_table178
+ GCC_except_table219
+ GCC_except_table318
+ GCC_except_table464
+ GCC_except_table523
+ GCC_except_table543
+ GCC_except_table554
+ GCC_except_table636
+ GCC_except_table693
+ GCC_except_table703
+ GCC_except_table705
+ GCC_except_table714
+ GCC_except_table727
+ GCC_except_table738
+ GCC_except_table88
+ GCC_except_table91
+ _OBJC_IVAR_$_CSCombinedListViewController._reduceIdleTimerDurationDueToEmptyLiftToWake
+ _OBJC_IVAR_$_CSCoverSheetFlyInSettings._iconFlyAlphaResponse
+ _OBJC_IVAR_$_CSCoverSheetFlyInSettings._iconFlyZCurveFactor
+ _OBJC_IVAR_$_CSCoverSheetFlyInSettings._iconFlyZResponse
+ _OBJC_IVAR_$_CSCoverSheetTransitionsSettings._damping
+ _OBJC_IVAR_$_CSCoverSheetTransitionsSettings._inPlaceDamping
+ _OBJC_IVAR_$_CSCoverSheetTransitionsSettings._inPlaceResponse
+ _OBJC_IVAR_$_CSCoverSheetTransitionsSettings._response
+ _OBJC_IVAR_$_CSHorizontalScrollFailureRecognizer._allowsMostSwipes
+ _OBJC_IVAR_$_CSHorizontalScrollFailureRecognizer._preventsScrollToTrailing
+ _OBJC_IVAR_$_CSQuickActionControlGlyphView._cachedInterfaceStyle
+ _OBJC_IVAR_$_CSScrollGestureController._preventsScrollToTrailing
+ _UIViewGlassGetLegibilitySetting
+ _UIViewGlassLegibilityDidChangeNotification
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.838
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.843
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.844
+ ___115-[CSQuickActionControlGlyphView _updateControlConfigurationColorSchemeWithTraitCollection:previousTraitCollection:]_block_invoke
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.194
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.198
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.207
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke_2.201
+ ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke_2.210
+ ___48-[CSCoverSheetViewController accessoryDetached:]_block_invoke.804
+ ___49-[CSCoverSheetViewController _updateDateTimeView]_block_invoke.696
+ ___51+[CSAODTransitionSettings settingsControllerModule]_block_invoke
+ ___51+[CSAODTransitionSettings settingsControllerModule]_block_invoke_2
+ ___51+[CSAODTransitionSettings settingsControllerModule]_block_invoke_3
+ ___51+[CSAODTransitionSettings settingsControllerModule]_block_invoke_4
+ ___51+[CSAODTransitionSettings settingsControllerModule]_block_invoke_5
+ ___51+[CSAODTransitionSettings settingsControllerModule]_block_invoke_6
+ ___51+[CSAODTransitionSettings settingsControllerModule]_block_invoke_7
+ ___51+[CSAODTransitionSettings settingsControllerModule]_block_invoke_8
+ ___51-[CSCoverSheetViewController _updateHomeAffordance]_block_invoke.703
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_10
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_11
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_12
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_13
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_14
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_15
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_16
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_17
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_18
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_19
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_2
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_20
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_3
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_4
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_5
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_6
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_7
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_8
+ ___53+[CSCoverSheetFlyInSettings settingsControllerModule]_block_invoke_9
+ ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.471
+ ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.472
+ ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.480
+ ___59+[CSCoverSheetTransitionsSettings settingsControllerModule]_block_invoke_6
+ ___59+[CSCoverSheetTransitionsSettings settingsControllerModule]_block_invoke_7
+ ___59+[CSCoverSheetTransitionsSettings settingsControllerModule]_block_invoke_8
+ ___59+[CSCoverSheetTransitionsSettings settingsControllerModule]_block_invoke_9
+ ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.768
+ ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.769
+ ___65-[CSCoverSheetViewController transitionSource:didEndWithContext:]_block_invoke.510
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.815
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.816
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.823
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke_2.821
+ ___79-[CSCoverSheetViewController _dismissRemoteViewControllerForReason:completion:]_block_invoke.607
+ ___89-[CSCoverSheetViewController _updateActiveBehaviorsForReason:updatingAppearanceIfNeeded:]_block_invoke.674
+ ___90-[CSCoverSheetViewController _removeRemoteViewControllerForInvalidatedSession:completion:]_block_invoke.608
+ ___98-[CSCoverSheetViewController activateCameraWithHostableEntity:animated:sendingActions:completion:]_block_invoke.152
+ ___block_descriptor_32_e61_v24?0"CSQuickActionControlGlyphView"8"UITraitCollection"16l
+ ___block_descriptor_40_e8_32s_e50_v16?0"CHUISMutableControlInstanceConfiguration"8ls32l8
+ ___block_literal_global.1161
+ ___block_literal_global.1163
+ ___block_literal_global.1165
+ ___block_literal_global.1167
+ ___block_literal_global.1172
+ ___block_literal_global.1174
+ ___block_literal_global.1176
+ ___block_literal_global.1178
+ ___block_literal_global.1183
+ ___block_literal_global.1185
+ ___block_literal_global.1187
+ ___block_literal_global.1189
+ ___block_literal_global.1194
+ ___block_literal_global.1196
+ ___block_literal_global.1198
+ ___block_literal_global.1200
+ ___block_literal_global.1205
+ ___block_literal_global.1207
+ ___block_literal_global.1209
+ ___block_literal_global.1211
+ ___block_literal_global.14
+ ___block_literal_global.19
+ ___block_literal_global.200
+ ___block_literal_global.229
+ ___block_literal_global.2375
+ ___block_literal_global.24
+ ___block_literal_global.242
+ ___block_literal_global.247
+ ___block_literal_global.252
+ ___block_literal_global.270
+ ___block_literal_global.275
+ ___block_literal_global.326
+ ___block_literal_global.331
+ ___block_literal_global.336
+ ___block_literal_global.341
+ ___block_literal_global.355
+ ___block_literal_global.38
+ ___block_literal_global.40
+ ___block_literal_global.423
+ ___block_literal_global.428
+ ___block_literal_global.433
+ ___block_literal_global.438
+ ___block_literal_global.440
+ ___block_literal_global.442
+ ___block_literal_global.443
+ ___block_literal_global.448
+ ___block_literal_global.835
+ _objc_msgSend$_resetReducedIdleTimeFlagsIfNeeded
+ _objc_msgSend$_setAodClockResponseMultiplier:
+ _objc_msgSend$_setAodGeneralResponseMultiplier:
+ _objc_msgSend$_setBaseCoverSheetSettingsWithMultiplier:
+ _objc_msgSend$_setFlyAlphaResponseMultiplier:
+ _objc_msgSend$_setFlyInResponseMultiplier:
+ _objc_msgSend$_setFlyOutResponseMultiplier:
+ _objc_msgSend$_setFlyZCurveFactorMultiplier:
+ _objc_msgSend$_setFlyZResponseMultiplier:
+ _objc_msgSend$_setInPlaceCoverSheetSettingsWithMultiplier:
+ _objc_msgSend$_updateControlConfigurationColorSchemeWithTraitCollection:previousTraitCollection:
+ _objc_msgSend$_updateForGlassLegibilitySetting
+ _objc_msgSend$coverSheetViewController:didWakeForSource:
+ _objc_msgSend$gestureEnabled
+ _objc_msgSend$isShowingNonNotificationContent
+ _objc_msgSend$layoutDirection
+ _objc_msgSend$setAllowsMostSwipes:
+ _objc_msgSend$setIconFlyAlphaResponse:
+ _objc_msgSend$setIconFlyZCurveFactor:
+ _objc_msgSend$setIconFlyZResponse:
+ _objc_msgSend$setInPlaceDamping:
+ _objc_msgSend$setInPlaceResponse:
+ _objc_msgSend$setPreventsScrollToTrailing:
- -[CSCombinedListViewController coverSheetViewControllerDidWakeForSource:]
- -[CSCoverSheetTransitionsSettings friction]
- -[CSCoverSheetTransitionsSettings inPlaceFriction]
- -[CSCoverSheetTransitionsSettings inPlaceTension]
- -[CSCoverSheetTransitionsSettings setFriction:]
- -[CSCoverSheetTransitionsSettings setInPlaceFriction:]
- -[CSCoverSheetTransitionsSettings setInPlaceTension:]
- -[CSCoverSheetTransitionsSettings setTension:]
- -[CSCoverSheetTransitionsSettings tension]
- GCC_except_table177
- GCC_except_table218
- GCC_except_table317
- GCC_except_table463
- GCC_except_table522
- GCC_except_table542
- GCC_except_table553
- GCC_except_table635
- GCC_except_table692
- GCC_except_table702
- GCC_except_table704
- GCC_except_table713
- GCC_except_table726
- GCC_except_table736
- GCC_except_table87
- GCC_except_table90
- _OBJC_IVAR_$_CSCoverSheetTransitionsSettings._friction
- _OBJC_IVAR_$_CSCoverSheetTransitionsSettings._inPlaceFriction
- _OBJC_IVAR_$_CSCoverSheetTransitionsSettings._inPlaceTension
- _OBJC_IVAR_$_CSCoverSheetTransitionsSettings._tension
- _OBJC_IVAR_$_CSCoverSheetViewController._screenOnForLiftToWake
- _SBBacklightChangeSourceKey
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.836
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.840
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.841
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.192
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.196
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke.205
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke_2.199
- ___41-[CSCoverSheetViewController viewDidLoad]_block_invoke_2.208
- ___48-[CSCoverSheetViewController accessoryDetached:]_block_invoke.802
- ___49-[CSCoverSheetViewController _updateDateTimeView]_block_invoke.694
- ___51-[CSCoverSheetViewController _updateHomeAffordance]_block_invoke.701
- ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.469
- ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.470
- ___54-[CSCoverSheetViewController handleAction:fromSender:]_block_invoke.478
- ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.766
- ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.767
- ___65-[CSCoverSheetViewController transitionSource:didEndWithContext:]_block_invoke.508
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.813
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.814
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.821
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke_2.819
- ___79-[CSCoverSheetViewController _dismissRemoteViewControllerForReason:completion:]_block_invoke.605
- ___89-[CSCoverSheetViewController _updateActiveBehaviorsForReason:updatingAppearanceIfNeeded:]_block_invoke.672
- ___90-[CSCoverSheetViewController _removeRemoteViewControllerForInvalidatedSession:completion:]_block_invoke.606
- ___98-[CSCoverSheetViewController activateCameraWithHostableEntity:animated:sendingActions:completion:]_block_invoke.150
- ___block_literal_global.198
- ___block_literal_global.227
- ___block_literal_global.2373
- ___block_literal_global.268
- ___block_literal_global.273
- ___block_literal_global.308
- ___block_literal_global.313
- ___block_literal_global.318
- ___block_literal_global.353
- ___block_literal_global.418
- ___block_literal_global.420
- ___block_literal_global.421
- ___block_literal_global.426
- ___block_literal_global.431
- ___block_literal_global.436
- ___block_literal_global.441
- ___block_literal_global.446
- ___block_literal_global.831
- _objc_msgSend$coverSheetViewControllerDidWakeForSource:
- _objc_msgSend$setInPlaceFriction:
- _objc_msgSend$setInPlaceTension:
- _objc_msgSend$setTension:
CStrings:
+ "70% Duration"
+ "80% Duration"
+ "90% Duration"
+ "Alpha Response"
+ "CameraSwipe"
+ "Clock Specific"
+ "Damping"
+ "Fly In Presets"
+ "Fly Out Presets"
+ "Fly Z CurveFactor"
+ "Fly Z Response"
+ "Fly* Icon Alpha Response"
+ "Fly* Z Curve Factor"
+ "Fly* Z Response"
+ "GlassLegibilitySetting"
+ "In Place"
+ "Moving"
+ "Shipping"
+ "TB,N,V_allowsMostSwipes"
+ "TB,N,V_preventsScrollToTrailing"
+ "TB,R,N,GisShowingNonNotificationContent"
+ "Td,N,V_damping"
+ "Td,N,V_iconFlyAlphaResponse"
+ "Td,N,V_iconFlyZCurveFactor"
+ "Td,N,V_iconFlyZResponse"
+ "Td,N,V_inPlaceDamping"
+ "Td,N,V_inPlaceResponse"
+ "Td,N,V_response"
+ "[CSCombinedList][AggBehavior] woke up for raise to wake with no content"
+ "_allowsMostSwipes"
+ "_cachedInterfaceStyle"
+ "_damping"
+ "_iconFlyAlphaResponse"
+ "_iconFlyZCurveFactor"
+ "_iconFlyZResponse"
+ "_inPlaceDamping"
+ "_inPlaceResponse"
+ "_preventsScrollToTrailing"
+ "_reduceIdleTimerDurationDueToEmptyLiftToWake"
+ "_resetReducedIdleTimeFlagsIfNeeded"
+ "_response"
+ "_setAodClockResponseMultiplier:"
+ "_setAodGeneralResponseMultiplier:"
+ "_setBaseCoverSheetSettingsWithMultiplier:"
+ "_setFlyAlphaResponseMultiplier:"
+ "_setFlyInResponseMultiplier:"
+ "_setFlyOutResponseMultiplier:"
+ "_setFlyZCurveFactorMultiplier:"
+ "_setFlyZResponseMultiplier:"
+ "_setInPlaceCoverSheetSettingsWithMultiplier:"
+ "_updateControlConfigurationColorSchemeWithTraitCollection:previousTraitCollection:"
+ "_updateForGlassLegibilitySetting"
+ "allowsMostSwipes"
+ "coverSheetViewController:didWakeForSource:"
+ "gestureEnabled"
+ "iconFlyAlphaResponse"
+ "iconFlyZCurveFactor"
+ "iconFlyZResponse"
+ "inPlaceDamping"
+ "inPlaceResponse"
+ "isShowingNonNotificationContent"
+ "layoutDirection"
+ "preventsScrollToTrailing"
+ "response"
+ "setAllowsMostSwipes:"
+ "setIconFlyAlphaResponse:"
+ "setIconFlyZCurveFactor:"
+ "setIconFlyZResponse:"
+ "setInPlaceDamping:"
+ "setInPlaceResponse:"
+ "setPreventsScrollToTrailing:"
+ "showingNonNotificationContent"
+ "v24@?0@\"CSQuickActionControlGlyphView\"8@\"UITraitCollection\"16"
+ "v28@0:8@\"CSCoverSheetViewController\"16i24"
- "Clock-Specific"
- "In-Place Friction"
- "In-Place Tension"
- "Td,N,V_friction"
- "Td,N,V_inPlaceFriction"
- "Td,N,V_inPlaceTension"
- "Td,N,V_tension"
- "_displayWillTurnOnWhileOnCoverSheet"
- "_inPlaceFriction"
- "_inPlaceTension"
- "_screenOnForLiftToWake"
- "_tension"
- "coverSheetViewControllerDidWakeForSource:"
- "inPlaceFriction"
- "inPlaceTension"
- "setInPlaceFriction:"
- "setInPlaceTension:"
- "setTension:"
- "tension"

```
