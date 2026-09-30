## VideoConferenceControlCenterModule

> `/System/Library/ControlCenter/Bundles/VideoConferenceControlCenterModule.bundle/VideoConferenceControlCenterModule`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`

```diff

 740.63.1.2.0
-  __TEXT.__text: 0x22e94
-  __TEXT.__auth_stubs: 0x1030
-  __TEXT.__objc_stubs: 0x1a20
-  __TEXT.__objc_methlist: 0x9f4
-  __TEXT.__const: 0x10c8
-  __TEXT.__objc_methname: 0x28b5
-  __TEXT.__objc_classname: 0x341
-  __TEXT.__objc_methtype: 0x734
-  __TEXT.__cstring: 0x13c4
-  __TEXT.__oslogstring: 0xd4f
+  __TEXT.__text: 0x27534
+  __TEXT.__auth_stubs: 0x10d0
+  __TEXT.__objc_stubs: 0x1d20
+  __TEXT.__objc_methlist: 0xb14
+  __TEXT.__const: 0x10e8
+  __TEXT.__objc_methname: 0x2d18
+  __TEXT.__objc_classname: 0x351
+  __TEXT.__objc_methtype: 0x744
+  __TEXT.__cstring: 0x18c4
+  __TEXT.__oslogstring: 0x143f
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__constg_swiftt: 0x838
-  __TEXT.__swift5_typeref: 0x5de
-  __TEXT.__swift5_reflstr: 0xc11
-  __TEXT.__swift5_fieldmd: 0x774
+  __TEXT.__constg_swiftt: 0x870
+  __TEXT.__swift5_typeref: 0x5ec
+  __TEXT.__swift5_reflstr: 0xe31
+  __TEXT.__swift5_fieldmd: 0x870
   __TEXT.__swift5_types: 0x60
   __TEXT.__swift5_capture: 0x154
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_proto: 0x60
-  __TEXT.__unwind_info: 0x8b0
-  __DATA_CONST.__const: 0x1048
+  __TEXT.__unwind_info: 0x960
+  __DATA_CONST.__const: 0x1118
   __DATA_CONST.__cfstring: 0x340
-  __DATA_CONST.__objc_classlist: 0x68
+  __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__auth_got: 0x828
-  __DATA_CONST.__got: 0x290
+  __DATA_CONST.__auth_got: 0x878
+  __DATA_CONST.__got: 0x2a8
   __DATA_CONST.__auth_ptr: 0x190
-  __DATA.__objc_const: 0x2410
-  __DATA.__objc_selrefs: 0x9f0
-  __DATA.__objc_ivar: 0x64
-  __DATA.__objc_data: 0xa28
-  __DATA.__data: 0x988
-  __DATA.__common: 0x2e8
+  __DATA.__objc_const: 0x2650
+  __DATA.__objc_selrefs: 0xae0
+  __DATA.__objc_ivar: 0x74
+  __DATA.__objc_data: 0xae8
+  __DATA.__data: 0x9c0
+  __DATA.__common: 0x378
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 872
-  Symbols:   268
-  CStrings:  721
+  Functions: 942
+  Symbols:   282
+  CStrings:  818
 
Symbols:
+ _AVControlCenterVideoEffectRingLight
+ _AVControlCenterVideoEffectsModuleGetRingLightActiveForBundleID
+ _AVControlCenterVideoEffectsModuleGetRingLightColorForBundleID
+ _AVControlCenterVideoEffectsModuleGetRingLightModeForBundleID
+ _AVControlCenterVideoEffectsModuleGetRingLightWidthForBundleID
+ _AVControlCenterVideoEffectsModuleRingLightModeDidChangeNotification
+ _AVControlCenterVideoEffectsModuleSetRingLightColorForBundleID
+ _AVControlCenterVideoEffectsModuleSetRingLightModeForBundleID
+ _AVControlCenterVideoEffectsModuleSetRingLightWidthForBundleID
+ _MGGetProductType
+ _OBJC_CLASS_$_EdgeLightVideoEffects
+ _OBJC_CLASS_$_UISwitch
+ _OBJC_METACLASS_$_EdgeLightVideoEffects
+ _objc_opt_respondsToSelector
CStrings:
+ " [ERROR] %{public}s:%d cannot set automaticMode for unsupported effect=%d"
+ " [ERROR] %{public}s:%d cannot set lineWidth for unsupported effect=%d"
+ " [INFO] %{public}s:%d automaticModeEnabled=%d (mode=%ld)"
+ " [INFO] %{public}s:%d backgroundBlurControlMode=%ld centerStageControlMode=%ld StudioLightingControlMode=%ld reactionsControlMode=%ld gesturesControlMode=%ld edgeLightControlMode=%ld"
+ " [INFO] %{public}s:%d backgroundBlurControlMode=%ld centerStageControlMode=%ld StudioLightingControlMode=%ld reactionsControlMode=%ld gesturesControlMode=%ld edgeLightControlMode=%ld backgroundReplacementControlMode=%ld"
+ " [INFO] %{public}s:%d backgroundBlurEnabled=%d centerStageEnabled=%d StudioLightingEnabled=%d reactionsEnabled=%d gesturesEnabled=%d edgeLightEnabled=%d"
+ " [INFO] %{public}s:%d backgroundBlurEnabled=%d centerStageEnabled=%d StudioLightingEnabled=%d reactionsEnabled=%d gesturesEnabled=%d edgeLightEnabled=%d backgroundReplacementEnabled=%d"
+ " [INFO] %{public}s:%d backgroundBlurSupported=%d centerStageSupported=%d StudioLightingSupported=%d reactionsSupported=%d gesturesSupported=%d edgeLightSupported=%d"
+ " [INFO] %{public}s:%d bundleID=%@"
+ " [INFO] %{public}s:%d intensity=%f"
+ " [INFO] %{public}s:%d isRingLightActive=%d"
+ " [INFO] %{public}s:%d lineWidth=%f"
+ " [INFO] %{public}s:%d ringLightModeChanged isRingLightActive=%d"
+ " [INFO] %{public}s:%d setting automaticModeEnabled=%d bundleID=%@"
+ " [INFO] %{public}s:%d setting lineWidth=%f bundleID=%@"
+ " [INFO] %{public}s:%d setting ring light color=%f bundleID=%@"
+ " [INFO] %{public}s:%d surface rotated, correcting orientation %ld -> %ld"
+ " [INFO] %{public}s:%d updating ring light color"
+ "%s automatic mode toggle changed to %{bool}d"
+ "%s lineWidth slider changed to %f"
+ "%s lineWidth slider released at %f"
+ "-[EdgeLightVideoEffects setAutomaticModeEnabled:withBundleID:]"
+ "-[EdgeLightVideoEffects setIntensity:withBundleID:]"
+ "-[EdgeLightVideoEffects setLineWidth:withBundleID:]"
+ "-[EdgeLightVideoEffects updateAutomaticModeEnabledWithBundleID:]"
+ "-[EdgeLightVideoEffects updateEdgeLightParametersWithBundleID:]"
+ "-[EdgeLightVideoEffects updateIntensityWithBundleID:]"
+ "-[EdgeLightVideoEffects updateLineWidthWithBundleID:]"
+ "-[EdgeLightVideoEffects updateRingLightActiveWithBundleID:]"
+ "-[EdgeLightVideoEffects updateVideoEffectStatesWithBundleID:]"
+ "-[RPCCUIVideoView currentInterfaceOrientation]"
+ "-[VideoEffectsManager setAutomaticMode:forEffect:]"
+ "-[VideoEffectsManager setLineWidth:forEffect:]"
+ "@\"EdgeLightVideoEffects\""
+ "CONTROL_CENTER_AUTOMATIC"
+ "CONTROL_CENTER_COLOR"
+ "CONTROL_CENTER_EDGE_LIGHT"
+ "CONTROL_CENTER_EDGE_LIGHT_DESCRIPTION"
+ "CONTROL_CENTER_LINE_WIDTH"
+ "EdgeLightAutomaticToggleChanged"
+ "EdgeLightAutomaticToggleValue"
+ "EdgeLightEnabled"
+ "EdgeLightEnabledChanged"
+ "EdgeLightIntensitySliderChanged"
+ "EdgeLightIntensitySliderValue"
+ "EdgeLightLineWidthSliderChanged"
+ "EdgeLightLineWidthSliderValue"
+ "EdgeLightVideoEffects"
+ "T@\"EdgeLightVideoEffects\",&,N,V_edgeLight"
+ "TB,N,V_automaticModeEnabled"
+ "TB,N,V_isRingLightActive"
+ "Tf,N,V_lineWidth"
+ "_automaticModeEnabled"
+ "_edgeLight"
+ "_isRingLightActive"
+ "_lineWidth"
+ "_rpLocalizableTableName"
+ "_rpLocalizedStringFromFrameworkBundleWithKey:tableName:"
+ "_windowInterfaceOrientation"
+ "autoColorLabel"
+ "autoColorRow"
+ "autoColorToggle"
+ "automaticModeEnabled"
+ "edgeLight"
+ "edgeLightAutomaticModeChanged(sender:)"
+ "edgeLightAutomaticModeChangedWithSender:"
+ "edgeLightButton"
+ "edgeLightEnabled"
+ "edgeLightLineWidthChanged(sender:)"
+ "edgeLightLineWidthChangedWithSender:"
+ "edgeLightLineWidthTouchUp(sender:)"
+ "edgeLightLineWidthTouchUpWithSender:"
+ "isOn"
+ "isRingLightActive"
+ "line.3.horizontal.decrease"
+ "lineWidth"
+ "lineWidthRow"
+ "lineWidthSlider"
+ "multiExpandedButtonRect"
+ "setAutomaticMode:forEffect:"
+ "setAutomaticModeEnabled:"
+ "setAutomaticModeEnabled:withBundleID:"
+ "setEdgeLight:"
+ "setIsRingLightActive:"
+ "setLineWidth:"
+ "setLineWidth:forEffect:"
+ "setLineWidth:withBundleID:"
+ "setOn:animated:"
+ "setTextColor:"
+ "surfaceType"
+ "updateAutomaticModeEnabledWithBundleID:"
+ "updateEdgeLightParametersWithBundleID:"
+ "updateLineWidthWithBundleID:"
+ "updateRingLightActiveWithBundleID:"
+ "whiteColor"
+ "window"
+ "windowScene"
```
