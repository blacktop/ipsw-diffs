## CoverSheet

> `/System/Library/PrivateFrameworks/CoverSheet.framework/CoverSheet`

```diff

-4557.1.15.102.0
-  __TEXT.__text: 0x1725e4
-  __TEXT.__auth_stubs: 0x1400
+4557.1.18.101.0
+  __TEXT.__text: 0x173048
+  __TEXT.__auth_stubs: 0x1410
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x1635c
-  __TEXT.__const: 0x2be0
-  __TEXT.__cstring: 0xa146
-  __TEXT.__oslogstring: 0x8cb2
-  __TEXT.__gcc_except_tab: 0xcfc
+  __TEXT.__objc_methlist: 0x1642c
+  __TEXT.__const: 0x2bf0
+  __TEXT.__cstring: 0xa256
+  __TEXT.__oslogstring: 0x8f9f
+  __TEXT.__gcc_except_tab: 0xd00
   __TEXT.__ustring: 0xa4
   __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__unwind_info: 0x4170
+  __TEXT.__unwind_info: 0x4168
   __TEXT.__objc_classname: 0x34bf
-  __TEXT.__objc_methname: 0x40db9
+  __TEXT.__objc_methname: 0x410e4
   __TEXT.__objc_methtype: 0x9e0f
-  __TEXT.__objc_stubs: 0x25dc0
+  __TEXT.__objc_stubs: 0x25ee0
   __DATA_CONST.__got: 0x1588
-  __DATA_CONST.__const: 0x2af8
+  __DATA_CONST.__const: 0x2b20
   __DATA_CONST.__objc_classlist: 0x7a0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x690
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc5a0
+  __DATA_CONST.__objc_selrefs: 0xc630
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x5e8
   __DATA_CONST.__objc_arraydata: 0x1078
-  __AUTH_CONST.__auth_got: 0xa10
-  __AUTH_CONST.__const: 0x8a0
-  __AUTH_CONST.__cfstring: 0xc0a0
-  __AUTH_CONST.__objc_const: 0x3c7e0
+  __AUTH_CONST.__auth_got: 0xa18
+  __AUTH_CONST.__const: 0x8c0
+  __AUTH_CONST.__cfstring: 0xc220
+  __AUTH_CONST.__objc_const: 0x3c980
   __AUTH_CONST.__objc_doubleobj: 0x660
   __AUTH_CONST.__objc_arrayobj: 0x1248
   __AUTH_CONST.__objc_intobj: 0x438
   __AUTH.__objc_data: 0x12c0
-  __DATA.__objc_ivar: 0x1b60
+  __DATA.__objc_ivar: 0x1b7c
   __DATA.__data: 0x4ec8
   __DATA.__bss: 0xd0
   __DATA_DIRTY.__objc_data: 0x3980

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E2353496-7DC6-38F8-93BC-2DF9E6E16DE9
-  Functions: 7129
-  Symbols:   26074
-  CStrings:  14344
+  UUID: 9D914418-436F-3550-8C66-1D12FB344841
+  Functions: 7149
+  Symbols:   26131
+  CStrings:  14410
 
Symbols:
+ -[CSCameraExtensionViewController secureCaptureSceneViewController:sceneContentStateDidChange:]
+ -[CSCoverSheetFlyInSettings animatesFlyOutToAODFromIdleDim]
+ -[CSCoverSheetFlyInSettings animatesFlyOutToAOD]
+ -[CSCoverSheetFlyInSettings animatesFlyOut]
+ -[CSCoverSheetFlyInSettings iconsFlyInResponse]
+ -[CSCoverSheetFlyInSettings iconsFlyOutResponse]
+ -[CSCoverSheetFlyInSettings setAnimatesFlyOut:]
+ -[CSCoverSheetFlyInSettings setAnimatesFlyOutToAOD:]
+ -[CSCoverSheetFlyInSettings setAnimatesFlyOutToAODFromIdleDim:]
+ -[CSCoverSheetFlyInSettings setIconsFlyInResponse:]
+ -[CSCoverSheetFlyInSettings setIconsFlyOutResponse:]
+ -[CSCoverSheetTransitionSettings setSupportsGlassEffects:]
+ -[CSCoverSheetTransitionSettings supportsGlassEffects]
+ -[CSCoverSheetViewController updateBackgroundGlassEffectForDraggingProgress:usingGlassEffects:]
+ -[CSPosterSwitcherViewController _initialAlongsideLayoutMode]
+ -[CSPosterSwitcherViewController hasEverGoneBeyondAlongside]
+ -[CSPosterSwitcherViewController setHasEverGoneBeyondAlongside:]
+ GCC_except_table123
+ GCC_except_table22
+ GCC_except_table635
+ GCC_except_table692
+ GCC_except_table704
+ GCC_except_table713
+ GCC_except_table726
+ GCC_except_table736
+ _BSStringFromCGRect
+ _OBJC_IVAR_$_CSCoverSheetFlyInSettings._animatesFlyOut
+ _OBJC_IVAR_$_CSCoverSheetFlyInSettings._animatesFlyOutToAOD
+ _OBJC_IVAR_$_CSCoverSheetFlyInSettings._animatesFlyOutToAODFromIdleDim
+ _OBJC_IVAR_$_CSCoverSheetFlyInSettings._iconsFlyInResponse
+ _OBJC_IVAR_$_CSCoverSheetFlyInSettings._iconsFlyOutResponse
+ _OBJC_IVAR_$_CSCoverSheetTransitionSettings._supportsGlassEffects
+ _OBJC_IVAR_$_CSPosterSwitcherViewController._hasEverGoneBeyondAlongside
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.840
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.841
+ ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.842
+ ___33-[CSSystemQuickAction fireAction]_block_invoke.cold.1
+ ___39-[CSCameraSystemQuickAction fireAction]_block_invoke.cold.1
+ ___48-[CSCoverSheetViewController accessoryDetached:]_block_invoke.802
+ ___49-[CSCoverSheetViewController _updateDateTimeView]_block_invoke.694
+ ___49-[CSCoverSheetViewController _updateDateTimeView]_block_invoke_5
+ ___51-[CSCoverSheetViewController _updateHomeAffordance]_block_invoke.701
+ ___55-[CSComplicationManager _updateWidgetHostConfiguration]_block_invoke_2
+ ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.766
+ ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.767
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.813
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.814
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.821
+ ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke_2.819
+ ___89-[CSCoverSheetViewController _updateActiveBehaviorsForReason:updatingAppearanceIfNeeded:]_block_invoke.672
+ ___block_descriptor_32_e34_16?0"CSComplicationDescriptor"8l
+ ___block_descriptor_40_e8_32s_e8_v16?0d8ls32l8
+ ___block_descriptor_48_e8_32bs_e5_v8?0ls32l8
+ ___block_literal_global.2373
+ ___block_literal_global.47
+ ___block_literal_global.54
+ ___block_literal_global.831
+ ___block_literal_global.833
+ _objc_msgSend$_initialAlongsideLayoutMode
+ _objc_msgSend$resolvedColorWithTraitCollection:
+ _objc_msgSend$setAnimatesFlyOut:
+ _objc_msgSend$setAnimatesFlyOutToAOD:
+ _objc_msgSend$setAnimatesFlyOutToAODFromIdleDim:
+ _objc_msgSend$setIconsFlyInResponse:
+ _objc_msgSend$setIconsFlyOutResponse:
+ _objc_msgSend$setPreallocatesScreenArea:
+ _objc_msgSend$setProvidesIdleTimerDuration:
+ _objc_msgSend$setSupportsGlassEffects:
- -[CSCoverSheetViewController updateBackgroundGlassEffectForDraggingProgress:]
- -[CSQuickActionControlGlyphView _updateControlConfigurationColorSchemeWithTraitCollection:previousTraitCollection:]
- GCC_except_table120
- GCC_except_table633
- GCC_except_table690
- GCC_except_table700
- GCC_except_table711
- GCC_except_table724
- GCC_except_table734
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.831
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.835
- ___101-[CSCoverSheetViewController _transitionChargingViewToVisible:suppressedByPack:showBattery:animated:]_block_invoke.837
- ___115-[CSQuickActionControlGlyphView _updateControlConfigurationColorSchemeWithTraitCollection:previousTraitCollection:]_block_invoke
- ___48-[CSCoverSheetViewController accessoryDetached:]_block_invoke.797
- ___51-[CSCoverSheetViewController _updateHomeAffordance]_block_invoke.696
- ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.761
- ___62-[CSCoverSheetViewController _handlePosterSwitcherActivation:]_block_invoke.762
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.808
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.809
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke.816
- ___66-[CSCoverSheetViewController _animateAccessory:toVisibleAnimated:]_block_invoke_2.814
- ___89-[CSCoverSheetViewController _updateActiveBehaviorsForReason:updatingAppearanceIfNeeded:]_block_invoke.669
- ___block_descriptor_32_e61_v24?0"CSQuickActionControlGlyphView"8"UITraitCollection"16l
- ___block_descriptor_40_e8_32s_e50_v16?0"CHUISMutableControlInstanceConfiguration"8ls32l8
- ___block_literal_global.2368
- ___block_literal_global.44
- ___block_literal_global.45
- ___block_literal_global.52
- ___block_literal_global.826
- ___block_literal_global.828
- _objc_msgSend$_updateControlConfigurationColorSchemeWithTraitCollection:previousTraitCollection:
CStrings:
+ "(SUTU) Fly Out Customization"
+ "@16@?0@\"CSComplicationDescriptor\"8"
+ "Animates Fly Out"
+ "Animates Fly Out To AOD"
+ "Animates Fly Out To AOD From Idle Dim"
+ "Fly In Response"
+ "Fly Out Response"
+ "TB,N,V_animatesFlyOut"
+ "TB,N,V_animatesFlyOutToAOD"
+ "TB,N,V_animatesFlyOutToAODFromIdleDim"
+ "TB,N,V_hasEverGoneBeyondAlongside"
+ "TB,N,V_supportsGlassEffects"
+ "Td,N,V_iconsFlyInResponse"
+ "Td,N,V_iconsFlyOutResponse"
+ "Transitions Settings"
+ "[%p/%{public}@] End Presentation mode transition to %{public}@ from %{public}@ -> %{public}@ completed for reason: %{public}@ for %lu widgets"
+ "[Adaptive Time] Calculated timeHeight: %f from honorsSalientContent: %{bool}u, posterDerivedTimeMaxY: %f, timeBottomFromList: %f, preferredSalientContent: %@, screenMax: %f, salientSpaceLeft: %f"
+ "[Camera Quick Action] Fired action successfully: %@"
+ "[Camera Quick Action] Performing control action failed: %{public}@"
+ "[Camera Quick Action] Will fire action %@"
+ "[Quick Action] Fired action successfully: %@"
+ "[Quick Action] Handling perform action %{public}@: %{public}@"
+ "[Quick Action] Launching capture application/extension for containing bundle identifier: %{public}@"
+ "[Quick Action] Performing control action failed: %{public}@"
+ "[Widget Grid] Backlight luminance changed from %lu to %lu"
+ "[Widget Grid] updating widgetHost %{public}@ with complication descriptors: %{public}@"
+ "_animatesFlyOut"
+ "_animatesFlyOutToAOD"
+ "_animatesFlyOutToAODFromIdleDim"
+ "_hasEverGoneBeyondAlongside"
+ "_iconsFlyInResponse"
+ "_iconsFlyOutResponse"
+ "_initialAlongsideLayoutMode"
+ "_supportsGlassEffects"
+ "animatesFlyOut"
+ "animatesFlyOutToAOD"
+ "animatesFlyOutToAODFromIdleDim"
+ "hasEverGoneBeyondAlongside"
+ "iconsFlyInResponse"
+ "iconsFlyOutResponse"
+ "resolvedColorWithTraitCollection:"
+ "secureCaptureSceneViewController:sceneContentStateDidChange:"
+ "setAnimatesFlyOut:"
+ "setAnimatesFlyOutToAOD:"
+ "setAnimatesFlyOutToAODFromIdleDim:"
+ "setCurrentTransitionSource"
+ "setHasEverGoneBeyondAlongside:"
+ "setIconsFlyInResponse:"
+ "setIconsFlyOutResponse:"
+ "setPreallocatesScreenArea:"
+ "setProvidesIdleTimerDuration:"
+ "setSupportsGlassEffects:"
+ "supportsGlassEffects"
+ "updateBackgroundGlassEffectForDraggingProgress:usingGlassEffects:"
+ "v16@?0d8"
+ "\xf01"
- "Hey"
- "[%p/%{public}@] End Presentation mode transition to %{public}@ from %{public}@ -> %{public}@ completed for reason: %{public}@"
- "[Quick Action] Will fire action %@"
- "_updateControlConfigurationColorSchemeWithTraitCollection:previousTraitCollection:"
- "updateBackgroundGlassEffectForDraggingProgress:"
- "v24@?0@\"CSQuickActionControlGlyphView\"8@\"UITraitCollection\"16"
- "\xf0!"

```
