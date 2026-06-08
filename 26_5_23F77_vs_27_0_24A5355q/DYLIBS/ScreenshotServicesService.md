## ScreenshotServicesService

> `/System/Library/AccessibilityBundles/ScreenshotServicesService.axbundle/ScreenshotServicesService`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x18a8
-  __TEXT.__auth_stubs: 0x220
+3036.2.0.0.0
+  __TEXT.__text: 0x17a8
   __TEXT.__objc_methlist: 0x330
-  __TEXT.__cstring: 0x6cb
   __TEXT.__const: 0x8
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x120
-  __TEXT.__objc_classname: 0x2e9
-  __TEXT.__objc_methname: 0x6c4
-  __TEXT.__objc_methtype: 0x49
-  __TEXT.__objc_stubs: 0x560
-  __DATA_CONST.__got: 0x88
+  __TEXT.__cstring: 0x6cb
+  __TEXT.__unwind_info: 0x118
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x158
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1f0
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x120
+  __DATA_CONST.__got: 0x88
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x940
   __AUTH_CONST.__objc_const: 0x990
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__bss: 0x1
   __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 35FCC9CE-47FE-384D-A023-B14A155C7E0D
-  Functions: 65
-  Symbols:   332
-  CStrings:  247
+  UUID: B459F1EC-E876-3CDA-86AF-70B02922C01A
+  Functions: 64
+  Symbols:   330
+  CStrings:  159
 
Symbols:
+ GCC_except_table52
+ ___block_literal_global.352
+ ___block_literal_global.354
+ ___block_literal_global.363
+ ___block_literal_global.390
+ ___block_literal_global.392
+ ___block_literal_global.404
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- +[AXScreenshotServicesServiceGlue accessibilityInitializeBundle].cold.1
- GCC_except_table5
- ___block_literal_global.331
- ___block_literal_global.333
- ___block_literal_global.342
- ___block_literal_global.369
- ___block_literal_global.371
- ___block_literal_global.383
- _objc_release_x23
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[AXScreenshotServicesServiceGlue accessibilityInitializeBundle] : 44 -> 40
~ ___64+[AXScreenshotServicesServiceGlue accessibilityInitializeBundle]_block_invoke : 160 -> 152
~ ___64+[AXScreenshotServicesServiceGlue accessibilityInitializeBundle]_block_invoke_3 : 88 -> 84
~ ___64+[AXScreenshotServicesServiceGlue accessibilityInitializeBundle]_block_invoke_4 : 220 -> 212
~ ___64+[AXScreenshotServicesServiceGlue accessibilityInitializeBundle]_block_invoke_5 : 96 -> 92
~ ___64+[AXScreenshotServicesServiceGlue accessibilityInitializeBundle]_block_invoke_6 : 120 -> 116
~ ___64+[AXScreenshotServicesServiceGlue accessibilityInitializeBundle]_block_invoke_7 : 100 -> 96
~ _accessibilityLocalizedString : 184 -> 176
~ -[SSSCropOverlayCornerViewAccessibility accessibilityLabel] : 104 -> 100
~ +[SSSDittoRootViewControllerAccessibility _accessibilityPerformValidations:] : 188 -> 180
~ +[SSSScreenshotsViewAccessibility _accessibilityPerformValidations:] : 332 -> 320
~ -[SSSScreenshotsViewAccessibility _accessibilitySupplementaryFooterViews] : 368 -> 332
~ +[SSSScreenshotsViewControllerAccessibility _accessibilityPerformValidations:] : 348 -> 340
~ -[SSSScreenshotsViewControllerAccessibility _accessibilityAnnotateItems] : 416 -> 376
~ -[SSSScreenshotsViewControllerAccessibility _updateAnnotationButtonAccessibilityTraits] : 184 -> 176
~ -[SSSScreenshotsViewControllerAccessibility _accessibilityPostLayoutChangeIfNecessary] : 236 -> 228
~ -[SSS_UIWindowAccessibility accessibilityRemoteSubstituteChildren:] : 356 -> 348
~ +[_SSSScreenshotAnnotationControllerAKOverlayContainerViewAccessibility _accessibilityPerformValidations:] : 208 -> 200
~ -[_SSSScreenshotAnnotationControllerAKOverlayContainerViewAccessibility _axMarkupAKOverlayView] : 372 -> 360
~ ___95-[_SSSScreenshotAnnotationControllerAKOverlayContainerViewAccessibility _axMarkupAKOverlayView]_block_invoke : 80 -> 76
~ -[_SSSScreenshotAnnotationControllerAKOverlayContainerViewAccessibility _accessibilityLabelForOverlayView] : 324 -> 300
~ +[SSSCropOverlayGrabberViewAccessibility _accessibilityPerformValidations:] : 124 -> 116
~ -[SSSCropOverlayGrabberViewAccessibility accessibilityLabel] : 104 -> 100
CStrings:
- "#16@0:8"
- "@16@0:8"
- "@24@0:8@16"
- "AXScreenshotServicesServiceGlue"
- "B16@0:8"
- "Q16@0:8"
- "SafeCategory"
- "__SSSCropOverlayCornerViewAccessibility_super"
- "__SSSCropOverlayGrabberViewAccessibility_super"
- "__SSSDittoRootViewControllerAccessibility_super"
- "__SSSScreenshotViewAccessibility_super"
- "__SSSScreenshotsViewAccessibility_super"
- "__SSSScreenshotsViewControllerAccessibility_super"
- "__SSS_UIWindowAccessibility_super"
- "___SSSScreenshotAnnotationControllerAKOverlayContainerViewAccessibility_super"
- "_accessibilityAncestorIsKindOf:"
- "_accessibilityAnnotateItems"
- "_accessibilityLabelForOverlayView"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilityPostLayoutChangeIfNecessary"
- "_accessibilitySupplementaryFooterViews"
- "_appearState"
- "_axDidPostNotification"
- "_axMarkupAKOverlayView"
- "_axSetDidPostNotification:"
- "_setAccessibilityLabelBlock:"
- "_updateAnnotationButtonAccessibilityTraits"
- "accessibilityBundles"
- "accessibilityCompareGeometry:"
- "accessibilityHint"
- "accessibilityIdentifier"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityRemoteSubstituteChildren:"
- "accessibilityTraits"
- "accessibilityViewIsModal"
- "addHandler:forBundleID:"
- "addObject:"
- "array"
- "axSafelyAddObjectsFromArray:"
- "bundleForClass:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "indexOfObject:"
- "installSafeCategory:canInteractWithTargetClass:"
- "isAccessibilityElement"
- "localizedStringForKey:value:table:"
- "localizedStringWithFormat:"
- "performValidations:withPreValidationHandler:postValidationHandler:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "reverseObjectEnumerator"
- "safeArrayForKey:"
- "safeBoolForKey:"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeIntegerForKey:"
- "safeValueForKey:"
- "setAccessibilityIdentifier:"
- "setAccessibilityLabel:"
- "setAccessibilityTraits:"
- "setDebugBuild:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "shouldGroupAccessibilityChildren"
- "sortedArrayUsingSelector:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "validateClass:"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "validateClass:isKindOfClass:"
- "viewDidAppear:"

```
