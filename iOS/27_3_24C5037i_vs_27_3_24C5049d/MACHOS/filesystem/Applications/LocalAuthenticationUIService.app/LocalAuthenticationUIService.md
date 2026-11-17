## LocalAuthenticationUIService

> `/Applications/LocalAuthenticationUIService.app/LocalAuthenticationUIService`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_catlist2`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`

```diff

-2319.60.18.0.0
-  __TEXT.__text: 0x6e034
+2319.60.22.0.0
+  __TEXT.__text: 0x6ebb8
   __TEXT.__auth_stubs: 0x2200
-  __TEXT.__objc_stubs: 0x7660
-  __TEXT.__objc_methlist: 0x3d20
+  __TEXT.__objc_stubs: 0x7840
+  __TEXT.__objc_methlist: 0x3de8
   __TEXT.__const: 0x35f4
-  __TEXT.__objc_classname: 0x127c
-  __TEXT.__objc_methname: 0x9d25
-  __TEXT.__gcc_except_tab: 0x74c
-  __TEXT.__cstring: 0x163e
-  __TEXT.__oslogstring: 0x1d6e
-  __TEXT.__objc_methtype: 0x28e7
+  __TEXT.__objc_classname: 0x12ac
+  __TEXT.__objc_methname: 0x9f05
+  __TEXT.__gcc_except_tab: 0x778
+  __TEXT.__cstring: 0x165e
+  __TEXT.__oslogstring: 0x1f2e
+  __TEXT.__objc_methtype: 0x2927
   __TEXT.__swift5_typeref: 0x33c4
   __TEXT.__constg_swiftt: 0x1208
   __TEXT.__swift5_reflstr: 0xbcd

   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0x20
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x2560
+  __TEXT.__unwind_info: 0x25c8
   __TEXT.__eh_frame: 0x5a0
-  __DATA_CONST.__const: 0x36a0
+  __DATA_CONST.__const: 0x36b8
   __DATA_CONST.__cfstring: 0x1000
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_catlist2: 0x8
-  __DATA_CONST.__objc_protolist: 0x238
+  __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0xa0
   __DATA_CONST.__objc_intobj: 0x438
   __DATA_CONST.__auth_got: 0x1110
-  __DATA_CONST.__got: 0xba8
+  __DATA_CONST.__got: 0xbb0
   __DATA_CONST.__auth_ptr: 0x7f8
-  __DATA.__objc_const: 0xc318
-  __DATA.__objc_selrefs: 0x26e0
-  __DATA.__objc_ivar: 0x33c
+  __DATA.__objc_const: 0xc730
+  __DATA.__objc_selrefs: 0x2758
+  __DATA.__objc_ivar: 0x354
   __DATA.__objc_data: 0x2510
-  __DATA.__data: 0x2ae0
+  __DATA.__data: 0x2b40
   __DATA.__common: 0xc8
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2797
-  Symbols:   8113
-  CStrings:  2434
+  Functions: 2814
+  Symbols:   8163
+  CStrings:  2465
 
Symbols:
+ -[FaceIdViewController _addPhysicalButtonView]
+ -[FaceIdViewController _makePhysicalButtonView]
+ -[FaceIdViewController _removePhysicalButtonView]
+ -[FaceIdViewController _setWantsPhysicalButtonView:]
+ -[TouchIdViewController _configureSystemApertureUI]
+ -[TouchIdViewController _dismissSystemApertureUI:]
+ -[TouchIdViewController _frontMostParentView]
+ -[TouchIdViewController _isAlertPresentedAlongsideSystemApertureUI]
+ -[TouchIdViewController _isSystemApertureUIAvailable]
+ -[TouchIdViewController _isSystemApertureUIPresentedAlone]
+ -[TouchIdViewController _isSystemApertureUIUsable]
+ -[TouchIdViewController _needsLightweightUI]
+ -[TouchIdViewController _presentSystemApertureUI:]
+ -[TouchIdViewController _presentUI]
+ -[TouchIdViewController _replaceSystemApertureUIWithAlertUIShakingGlyph:]
+ -[TouchIdViewController _reportUIAppearanceIfNeeded]
+ -[TouchIdViewController _setupSensorReachabilityMonitorIfNeeded]
+ -[TouchIdViewController _setupSystemApertureUI]
+ -[TouchIdViewController uiEvent:options:]
+ -[TouchIdViewControllerWithCoachings _addPhysicalButtonView]
+ -[TouchIdViewControllerWithCoachings _configureSystemApertureUI]
+ -[TouchIdViewControllerWithCoachings _isPhysicalButtonInstructionHidden]
+ -[TouchIdViewControllerWithCoachings _makePhysicalButtonView]
+ -[TouchIdViewControllerWithCoachings _physicalButtonInstruction]
+ -[TouchIdViewControllerWithCoachings _physicalButtonViewStyle]
+ -[TouchIdViewControllerWithCoachings _presentSystemApertureUI:]
+ -[TouchIdViewControllerWithCoachings _removePhysicalButtonView]
+ -[TouchIdViewControllerWithCoachings _showPhysicalButtonView]
+ -[TouchIdViewControllerWithCoachings _updatePhysicalButtonViewVisibility]
+ -[TouchIdViewControllerWithCoachings _wantsPhysicalButtonOutline]
+ -[TouchIdViewControllerWithCoachings windowSceneSurfaceMonitorDidChangeSurface:]
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/LocalAuthenticationUI/install/TempContent/Objects/CoreAuthentication.build/LocalAuthenticationUIService.build/Objects-normal/arm64e/PasscodeContentViewControllerFullScreen-d5683a73b9a0343865a923b494b6f7de.o
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/LocalAuthenticationUI/install/TempContent/Objects/CoreAuthentication.build/LocalAuthenticationUIService.build/Objects-normal/arm64e/PinViewController-4faaf7973c5e250b115d7586985b71ca.o
+ GCC_except_table11
+ GCC_except_table47
+ GCC_except_table63
+ _OBJC_CLASS_$_LACUIWindowSceneSurfaceMonitor
+ _OBJC_IVAR_$_FaceIdViewController._usesPhysicalButtonView
+ _OBJC_IVAR_$_FaceIdViewController._wantsPhysicalButtonView
+ _OBJC_IVAR_$_TouchIdViewController._hasReportedUIAppearance
+ _OBJC_IVAR_$_TouchIdViewController._systemApertureToast
+ _OBJC_IVAR_$_TouchIdViewControllerWithCoachings._physicalButtonInstructionBackdropColor
+ _OBJC_IVAR_$_TouchIdViewControllerWithCoachings._physicalButtonView
+ _OBJC_IVAR_$_TouchIdViewControllerWithCoachings._surfaceMonitor
+ _OBJC_IVAR_$_TouchIdViewControllerWithCoachings._wantsPhysicalButtonView
+ __OBJC_$_PROP_LIST_TouchIdViewControllerWithCoachings
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACUIWindowSceneSurfaceMonitorObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACUIWindowSceneSurfaceMonitorObserver
+ __OBJC_$_PROTOCOL_REFS_LACUIWindowSceneSurfaceMonitorObserver
+ __OBJC_CLASS_PROTOCOLS_$_TouchIdViewControllerWithCoachings
+ __OBJC_LABEL_PROTOCOL_$_LACUIWindowSceneSurfaceMonitorObserver
+ __OBJC_PROTOCOL_$_LACUIWindowSceneSurfaceMonitorObserver
+ ___41-[TouchIdViewController _presentAlertUI:]_block_invoke
+ ___50-[TouchIdViewController _presentSystemApertureUI:]_block_invoke
+ ___50-[TouchIdViewController _presentSystemApertureUI:]_block_invoke_2
+ ___64-[TouchIdViewController _setupSensorReachabilityMonitorIfNeeded]_block_invoke
+ ___73-[TouchIdViewController _replaceSystemApertureUIWithAlertUIShakingGlyph:]_block_invoke
+ ___89-[TouchIdViewControllerWithCoachings viewWillTransitionToSize:withTransitionCoordinator:]_block_invoke
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_LocalAuthenticationUIService
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_LocalAuthenticationUIService
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_LocalAuthenticationUIService
+ _objc_msgSend$_addPhysicalButtonView
+ _objc_msgSend$_configureSystemApertureUI
+ _objc_msgSend$_dismissSystemApertureUI:
+ _objc_msgSend$_frontMostParentView
+ _objc_msgSend$_isAlertPresentedAlongsideSystemApertureUI
+ _objc_msgSend$_isPhysicalButtonInstructionHidden
+ _objc_msgSend$_isSystemApertureUIAvailable
+ _objc_msgSend$_isSystemApertureUIPresentedAlone
+ _objc_msgSend$_isSystemApertureUIUsable
+ _objc_msgSend$_makePhysicalButtonView
+ _objc_msgSend$_needsLightweightUI
+ _objc_msgSend$_physicalButtonInstruction
+ _objc_msgSend$_physicalButtonViewStyle
+ _objc_msgSend$_presentSystemApertureUI:
+ _objc_msgSend$_presentUI
+ _objc_msgSend$_removePhysicalButtonView
+ _objc_msgSend$_replaceSystemApertureUIWithAlertUIShakingGlyph:
+ _objc_msgSend$_reportUIAppearanceIfNeeded
+ _objc_msgSend$_setWantsPhysicalButtonView:
+ _objc_msgSend$_setupSensorReachabilityMonitorIfNeeded
+ _objc_msgSend$_setupSystemApertureUI
+ _objc_msgSend$_showPhysicalButtonView
+ _objc_msgSend$_updatePhysicalButtonViewVisibility
+ _objc_msgSend$_wantsPhysicalButtonOutline
+ _objc_msgSend$addObserver:
+ _objc_msgSend$featureFlagSystemApertureTouchIDEnabled
+ _objc_msgSend$removeObserver:
- -[TouchIdViewController _addFrontMostSubview:]
- -[TouchIdViewController _configureLightweightUI]
- -[TouchIdViewController _dismissLightweightUI:]
- -[TouchIdViewController _presentLightweightUI:]
- -[TouchIdViewController _presentUI:]
- -[TouchIdViewController _replaceLightweightUIWithAlertUIShakingGlyph:]
- -[TouchIdViewController _setupLightweightUI]
- -[TouchIdViewController _usesLightweightUI]
- -[TouchIdViewControllerWithCoachings _configureLightweightUI]
- -[TouchIdViewControllerWithCoachings _presentLightweightUI:]
- -[TouchIdViewControllerWithCoachings _setupCoachingView]
- -[TouchIdViewControllerWithCoachings _setupUI]
- -[TouchIdViewControllerWithCoachings _updateCoachingViewVisibility]
- -[TouchIdViewControllerWithCoachings _updateUI]
- -[TouchIdViewControllerWithCoachings viewWillLayoutSubviews]
- -[TouchIdViewControllerWithCoachings willTransitionToTraitCollection:withTransitionCoordinator:]
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/LocalAuthenticationUI/install/TempContent/Objects/CoreAuthentication.build/LocalAuthenticationUIService.build/Objects-normal/arm64e/PasscodeContentViewControllerFullScreen-6a987ffb390b1f42b847fcf51bf4e183.o
- /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/LocalAuthenticationUI/install/TempContent/Objects/CoreAuthentication.build/LocalAuthenticationUIService.build/Objects-normal/arm64e/PinViewController-ea9247c279af1b59da52e608261fc15f.o
- GCC_except_table0
- GCC_except_table23
- GCC_except_table41
- GCC_except_table42
- _OBJC_IVAR_$_TouchIdViewController._lightweightToast
- _OBJC_IVAR_$_TouchIdViewControllerWithCoachings._coachingView
- ___33-[TouchIdViewController loadView]_block_invoke
- ___47-[TouchIdViewController _presentLightweightUI:]_block_invoke
- ___47-[TouchIdViewController _presentLightweightUI:]_block_invoke_2
- ___47-[TouchIdViewControllerWithCoachings _updateUI]_block_invoke
- ___70-[TouchIdViewController _replaceLightweightUIWithAlertUIShakingGlyph:]_block_invoke
- _objc_msgSend$_addFrontMostSubview:
- _objc_msgSend$_configureLightweightUI
- _objc_msgSend$_dismissLightweightUI:
- _objc_msgSend$_presentLightweightUI:
- _objc_msgSend$_presentUI:
- _objc_msgSend$_replaceLightweightUIWithAlertUIShakingGlyph:
- _objc_msgSend$_setupCoachingView
- _objc_msgSend$_setupLightweightUI
- _objc_msgSend$_updateCoachingViewVisibility
- _objc_msgSend$_updateUI
- _objc_msgSend$_usesLightweightUI
- _objc_msgSend$featureFlagLightweightTouchIDEnabled
CStrings:
+ "%{public}@ %{public}s the physical button view"
+ "%{public}@ can't show the physical button view, as %{public}@ is not in a window scene"
+ "%{public}@ delays the physical button view until the surface of scene %p is known"
+ "%{public}@ leaves out the physical button view while the glyph is the only UI"
+ "%{public}@ removes the physical button view"
+ "%{public}@ shows the physical button view"
+ "%{public}@ shows the physical button view on surface type %ld"
+ "@\"LACUIWindowSceneSurfaceMonitor\""
+ "LACUIWindowSceneSurfaceMonitorObserver"
+ "_addPhysicalButtonView"
+ "_configureSystemApertureUI"
+ "_dismissSystemApertureUI:"
+ "_frontMostParentView"
+ "_hasReportedUIAppearance"
+ "_isAlertPresentedAlongsideSystemApertureUI"
+ "_isPhysicalButtonInstructionHidden"
+ "_isSystemApertureUIAvailable"
+ "_isSystemApertureUIPresentedAlone"
+ "_isSystemApertureUIUsable"
+ "_makePhysicalButtonView"
+ "_needsLightweightUI"
+ "_physicalButtonInstruction"
+ "_physicalButtonInstructionBackdropColor"
+ "_physicalButtonViewStyle"
+ "_presentSystemApertureUI:"
+ "_presentUI"
+ "_removePhysicalButtonView"
+ "_replaceSystemApertureUIWithAlertUIShakingGlyph:"
+ "_reportUIAppearanceIfNeeded"
+ "_setWantsPhysicalButtonView:"
+ "_setupSensorReachabilityMonitorIfNeeded"
+ "_setupSystemApertureUI"
+ "_showPhysicalButtonView"
+ "_surfaceMonitor"
+ "_systemApertureToast"
+ "_updatePhysicalButtonViewVisibility"
+ "_usesPhysicalButtonView"
+ "_wantsPhysicalButtonOutline"
+ "_wantsPhysicalButtonView"
+ "addObserver:"
+ "featureFlagSystemApertureTouchIDEnabled"
+ "no longer wants"
+ "removeObserver:"
+ "v24@0:8@\"LACUIWindowSceneSurfaceMonitor\"16"
+ "wants"
+ "windowSceneSurfaceMonitorDidChangeSurface:"
- "_addFrontMostSubview:"
- "_coachingView"
- "_configureLightweightUI"
- "_dismissLightweightUI:"
- "_lightweightToast"
- "_presentLightweightUI:"
- "_presentUI:"
- "_replaceLightweightUIWithAlertUIShakingGlyph:"
- "_setupCoachingView"
- "_setupLightweightUI"
- "_updateCoachingViewVisibility"
- "_updateUI"
- "_usesLightweightUI"
- "featureFlagLightweightTouchIDEnabled"
- "willTransitionToTraitCollection:withTransitionCoordinator:"
```
