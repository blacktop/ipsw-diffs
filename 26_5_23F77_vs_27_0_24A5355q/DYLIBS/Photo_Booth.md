## Photo Booth

> `/System/Library/AccessibilityBundles/Photo Booth.axbundle/Photo Booth`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x1470
-  __TEXT.__auth_stubs: 0x190
+3036.2.0.0.0
+  __TEXT.__text: 0x13f0
   __TEXT.__objc_methlist: 0x1e4
-  __TEXT.__cstring: 0x6ce
   __TEXT.__const: 0x8
+  __TEXT.__cstring: 0x6ce
   __TEXT.__unwind_info: 0xe0
-  __TEXT.__objc_classname: 0x127
-  __TEXT.__objc_methname: 0x55c
-  __TEXT.__objc_methtype: 0x68
-  __TEXT.__objc_stubs: 0x480
-  __DATA_CONST.__got: 0x70
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1c8
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xd0
+  __DATA_CONST.__got: 0x70
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x720
   __AUTH_CONST.__objc_const: 0x550
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6DE20A96-3360-3684-9FC3-7B43D384D0B9
+  UUID: 3A564A98-D593-33B5-AA88-6AFFC38733A2
   Functions: 37
-  Symbols:   209
-  CStrings:  205
+  Symbols:   212
+  CStrings:  128
 
Symbols:
+ ___block_literal_global.430
+ ___block_literal_global.439
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- ___block_literal_global.409
- ___block_literal_global.418
- _objc_retainAutoreleasedReturnValue
Functions:
~ _axLocalizedString : 184 -> 176
~ +[AXPhotoBoothGlue accessibilityInitializeBundle] : 152 -> 148
~ ___49+[AXPhotoBoothGlue accessibilityInitializeBundle]_block_invoke : 484 -> 480
~ ___49+[AXPhotoBoothGlue accessibilityInitializeBundle]_block_invoke_2 : 100 -> 96
~ ___49+[AXPhotoBoothGlue accessibilityInitializeBundle]_block_invoke_3 : 140 -> 132
~ -[UIApplication(PhotoBoothCategory) accessibilityStartStopToggle] : 120 -> 112
~ +[PBControllerAccessibility _accessibilityPerformValidations:] : 320 -> 312
~ -[PBControllerAccessibility _accessibilityLoadAccessibilityInformation] : 180 -> 168
~ -[PBControllerAccessibility _addTilesForPhotos:animated:] : 116 -> 112
~ -[PBControllerAccessibility _accessibilityApplyLabels:] : 332 -> 340
~ -[PBControllerAccessibility _reviewModeFooter] : 180 -> 176
~ -[PBControllerAccessibility toggleCamera:] : 124 -> 120
~ +[PBEffectsViewAccessibility _accessibilityPerformValidations:] : 304 -> 296
~ -[PBEffectsViewAccessibility accessibilityLabel] : 212 -> 204
~ -[PBEffectsViewAccessibility isAccessibilityElement] : 72 -> 68
~ -[PBEffectsViewAccessibility accessibilityElements] : 292 -> 272
~ -[PBEffectsViewAccessibility _accessibilityShouldHitTestLayers] : 72 -> 68
~ -[PBEffectsViewAccessibility dealloc] : 284 -> 296
~ -[PBEffectsViewAccessibility _accessibilityLoadAccessibilityInformation] : 304 -> 296
~ ___72-[PBEffectsViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 176 -> 168
~ -[PBShelfTileAccessibility accessibilityTraits] : 108 -> 104
~ -[PBContainerViewAccessibility _accessibilityHitTest:withEvent:] : 116 -> 100
CStrings:
- "#16@0:8"
- "@16@0:8"
- "@28@0:8@16B24"
- "@40@0:8{CGPoint=dd}16@32"
- "AXPhotoBoothGlue"
- "B16@0:8"
- "PhotoBoothCategory"
- "Q16@0:8"
- "SafeCategory"
- "__PBContainerViewAccessibility_super"
- "__PBControllerAccessibility_super"
- "__PBEffectsViewAccessibility_super"
- "__PBShelfTileAccessibility_super"
- "_accessibilityAllowsSiblingsWhenOvergrown"
- "_accessibilityApplyLabels:"
- "_accessibilityHitTest:withEvent:"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilityShouldHitTestLayers"
- "_addTilesForPhotos:animated:"
- "_reviewModeFooter"
- "accessibilityCompareGeometry:"
- "accessibilityElements"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityStartStopToggle"
- "accessibilityTraits"
- "addObject:"
- "boolValue"
- "bundleForClass:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "dealloc"
- "enumerateObjectsUsingBlock:"
- "indexOfObject:"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "intValue"
- "isAccessibilityElement"
- "items"
- "localizedStringForKey:value:table:"
- "objectAtIndex:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeIntegerForKey:"
- "safeValueForKey:"
- "safeValueForKeyPath:"
- "setAccessibilityContainer:"
- "setAccessibilityHint:"
- "setAccessibilityLabel:"
- "setCurrentMode:animated:"
- "setDebugBuild:"
- "setIsAccessibilityElement:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedApplication"
- "sharedInstance"
- "sortedArrayUsingSelector:"
- "statusBarOrientation"
- "stringWithFormat:"
- "tag"
- "v16@0:8"
- "v24@0:8@16"
- "v24@0:8i16B20"
- "validateClass:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"

```
