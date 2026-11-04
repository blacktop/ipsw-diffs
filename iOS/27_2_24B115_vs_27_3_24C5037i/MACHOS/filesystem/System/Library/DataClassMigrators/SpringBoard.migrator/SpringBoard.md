## SpringBoard

> `/System/Library/DataClassMigrators/SpringBoard.migrator/SpringBoard`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-4637.1.14.103.0
-  __TEXT.__text: 0xda64
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_stubs: 0x1be0
-  __TEXT.__objc_methlist: 0x67c
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x18d9
-  __TEXT.__objc_methname: 0x1b92
-  __TEXT.__oslogstring: 0x153e
-  __TEXT.__objc_classname: 0x145
-  __TEXT.__objc_methtype: 0x329
+4637.2.11.104.0
+  __TEXT.__text: 0xe960
+  __TEXT.__auth_stubs: 0x6c0
+  __TEXT.__objc_stubs: 0x1d60
+  __TEXT.__objc_methlist: 0x714
+  __TEXT.__const: 0x140
+  __TEXT.__cstring: 0x1933
+  __TEXT.__objc_methname: 0x1db0
+  __TEXT.__oslogstring: 0x179f
+  __TEXT.__objc_classname: 0x141
+  __TEXT.__objc_methtype: 0x389
   __TEXT.__gcc_except_tab: 0x14c
-  __TEXT.__unwind_info: 0x830
-  __DATA_CONST.__const: 0x15f8
-  __DATA_CONST.__cfstring: 0xf40
+  __TEXT.__unwind_info: 0x880
+  __DATA_CONST.__const: 0x16d8
+  __DATA_CONST.__cfstring: 0xf20
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_arraydata: 0x120
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x318
-  __DATA_CONST.__got: 0x248
-  __DATA.__objc_const: 0xdb8
-  __DATA.__objc_selrefs: 0x848
+  __DATA_CONST.__auth_got: 0x370
+  __DATA_CONST.__got: 0x238
+  __DATA.__objc_const: 0xe10
+  __DATA.__objc_selrefs: 0x8d8
   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x128

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 647
-  Symbols:   387
-  CStrings:  717
+  Functions: 679
+  Symbols:   403
+  CStrings:  755
 
Symbols:
+ _BSInterfaceOrientationDescription
+ _BSInterfaceOrientationIsLandscape
+ _BSRectWithSize
+ _BSSizeSwap
+ _BSStringFromBOOL
+ _BSStringFromCGSize
+ _CGAffineTransformMakeRotation
+ _MGIsDeviceOneOfType
+ _NSStringFromCGPoint
+ _NSStringFromCGSize
+ _OBJC_CLASS_$_SBCoverDisplayConfigurationTransformer
+ _OBJC_METACLASS_$_SBCoverDisplayConfigurationTransformer
+ _SBLogContinuousFold
+ _SBLogInteractionSuppression
+ _SBLogMotionEffects
+ _SBLogSceneRegions
+ _SBLogSystemAperturePreferencesStackBlankingRegions
+ _SBSCurrentCoverDisplaySize
+ _SBV68DisplayTransformerLogicalPointSize
+ _SBV68DisplayTransformerPhysicalPointSize
+ __SBFLoggingMethodProem
+ _objc_retain_x27
- _CATransform3DMakeTranslation
- _CFPreferencesGetAppBooleanValue
- _OBJC_CLASS_$_FBSDeviceEmulationConfiguration
- _OBJC_CLASS_$_NSValue
- _OBJC_CLASS_$_SBScreenEdgeCompensationDisplayTransformer
- _OBJC_METACLASS_$_SBScreenEdgeCompensationDisplayTransformer
CStrings:
+ "@32@0:8@16q24"
+ "B16@?0@8"
+ "ContinuousFold"
+ "Cover-display %@ Rotated display configuration configuration, %{public}@ -> %{public}@:\n %@"
+ "Cover-display %@ Scaling display configuration configuration, %{public}@ -> %{public}@:\n %@"
+ "Cover-display %@ not transforming configuration, it's what we want already:\n %@"
+ "Cover-display %@ opportunity to override:\n %@ -> %@ (%fx)\n %@ -> %@,\n %@ -> %@,\n %@ -> %@"
+ "Cover-display Unable to create overridden display configuration: %@ from configuration:%@"
+ "Cover-display Unable to determined scaled size to use"
+ "Cover-display applied right-aligned cover size to %{public}@: %@ -> %@ (cover %@)"
+ "Cover-display cover-size reduction entry: isMainDisplay=%d hardwareIdentifier=%{public}@ bounds=%@"
+ "Cover-display cover-size reduction no-op: bounds %@ already matches resolved cover %@"
+ "Cover-display cover-size reduction skipped (not a genuine cover device): sizeMatchesCover=%{public}@ bounds=%@ expected=%@ hasMultipleAlwaysConnectedDisplays=%{public}@"
+ "Cover-display unable to create cover-size display configuration: %@ from configuration: %@"
+ "InteractionSuppression"
+ "MotionEffects"
+ "SBCoverDisplayConfigurationTransformer"
+ "SceneRegions"
+ "SystemAperturePreferencesStackBlankingRegions"
+ "T@\"NSString\",C"
+ "Tq"
+ "T{UIEdgeInsets=dddd}"
+ "_setAdditionalRootLayerAffineTransform:"
+ "activeTransformMode"
+ "appliedCoverInsets"
+ "bs_filter:"
+ "buildWithError:"
+ "connectionType"
+ "d16@0:8"
+ "displayConfigurationByApplyingCoverInsetsToConfiguration:"
+ "displayConfigurationByTransformingConfiguration:usingTransformMode:"
+ "displayType"
+ "displays"
+ "hardwareIdentifier"
+ "identity"
+ "insetDisplayConfigurationHardwareIdentifier"
+ "isMainDisplay"
+ "pointScale"
+ "q16@0:8"
+ "renderingCenter"
+ "rotatedDisplayConfigurationHardwareIdentifier"
+ "rotationAngle"
+ "scaleX"
+ "scaleY"
+ "setActiveTransformMode:"
+ "setAppliedCoverInsets:"
+ "setInsetDisplayConfigurationHardwareIdentifier:"
+ "setRotatedDisplayConfigurationHardwareIdentifier:"
+ "setTransformedDisplayConfigurationHardwareIdentifier:"
+ "transformedDisplayConfigurationHardwareIdentifier"
+ "updateSystemGestureWindowTransformIfNeeded:"
+ "v24@0:8q16"
+ "v48@0:8{UIEdgeInsets=dddd}16"
+ "windowScene"
+ "{UIEdgeInsets=dddd}16@0:8"
- "%{public}@: screen edge compensation transform built: %{BOOL}u"
- "Applying screen edge compensation: D76 main display size matched; rewriting bounds from %{public}@ to %{public}@"
- "EdgeSwipeBandExpansionEnabled"
- "SBScreenEdgeCompensationDisplayTransformer"
- "Skipping screen edge compensation: isMainD76Display=%{BOOL}u"
- "Unable to build screen edge compensated display configuration: %{public}@ from configuration: %{public}@"
- "Unable to create redacted display configuration: %@ from configuration:%@"
- "_fbsDisplayIdentity"
- "buildConfigurationWithError:"
- "emulatedDeviceBounds"
- "hasEmulatedDeviceBounds"
- "isEmulatedDevice"
- "isMainRootDisplay"
- "isScreenEdgeCompensationEnabled"
- "sceneTransformForWindowScene:"
- "transformedConfigurationForConfiguration:"
- "valueWithCATransform3D:"
```
