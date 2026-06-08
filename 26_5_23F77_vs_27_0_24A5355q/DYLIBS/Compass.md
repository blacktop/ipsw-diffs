## Compass

> `/System/Library/AccessibilityBundles/Compass.axbundle/Compass`

```diff

-3005.28.0.0.0
-  __TEXT.__text: 0x13f4
-  __TEXT.__auth_stubs: 0x1a0
+3036.2.0.0.0
+  __TEXT.__text: 0x1420
   __TEXT.__objc_methlist: 0x194
   __TEXT.__cstring: 0x34f
   __TEXT.__unwind_info: 0xb8
-  __TEXT.__objc_classname: 0x139
-  __TEXT.__objc_methname: 0x508
-  __TEXT.__objc_methtype: 0x91
-  __TEXT.__objc_stubs: 0x4a0
-  __DATA_CONST.__got: 0x60
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x180
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xd8
+  __DATA_CONST.__got: 0x60
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x520
   __AUTH_CONST.__objc_const: 0x4e8
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0x8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B8EA1655-6B4B-3761-8EDB-33BA7E34A6A9
+  UUID: A8D392E5-6884-307B-AD65-6501FD57AE2C
   Functions: 33
-  Symbols:   196
-  CStrings:  161
+  Symbols:   197
+  CStrings:  90
 
Symbols:
+ ___block_literal_global.351
+ ___block_literal_global.360
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- ___block_literal_global.330
- ___block_literal_global.339
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[AXCompassGlue accessibilityInitializeBundle] : 152 -> 148
~ ___46+[AXCompassGlue accessibilityInitializeBundle]_block_invoke_2 : 88 -> 84
~ ___46+[AXCompassGlue accessibilityInitializeBundle]_block_invoke_3 : 120 -> 112
~ _accessibilityLocalizedString : 164 -> 156
~ _axCompassController : 96 -> 88
~ _axCompassPageViewController : 92 -> 116
~ _axLevelPageViewController : 92 -> 116
~ +[CompassPageViewControllerAccessibility _accessibilityPerformValidations:] : 436 -> 428
~ -[CompassPageViewControllerAccessibility _axAnnounceDegreesIfNeeded:] : 424 -> 408
~ -[CompassPageViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 112 -> 108
~ -[CompassPageViewControllerAccessibility _updateDegreesLabel:] : 112 -> 108
~ -[CompassPageViewControllerAccessibility setCrosshairLevelForData:] : 324 -> 312
~ -[UIPageControlCompassAccessibility _axNumberOfPages] : 68 -> 64
~ -[UIPageControlCompassAccessibility _axCurrentPage] : 68 -> 64
~ -[UIPageControlCompassAccessibility accessibilityValue] : 308 -> 284
~ +[UIViewCompassAccessibility _accessibilityPerformValidations:] : 156 -> 148
~ -[UIViewCompassAccessibility isAccessibilityElement] : 172 -> 168
~ -[UIViewCompassAccessibility _accessibilitySupplementaryFooterViews] : 404 -> 428
~ -[UIViewCompassAccessibility accessibilityLabel] : 492 -> 552
~ -[UIViewCompassAccessibility _accessibilityScrollStatus] : 272 -> 300
~ -[UIViewCompassAccessibility accessibilityHint] : 164 -> 152
~ -[UIViewCompassAccessibility accessibilityScroll:] : 220 -> 236
CStrings:
- "#16@0:8"
- "@16@0:8"
- "@40@0:8{CGPoint=dd}16@32"
- "AXCompassGlue"
- "B16@0:8"
- "B24@0:8q16"
- "CGPointValue"
- "CompassAccessibility"
- "SafeCategory"
- "__CompassPageViewControllerAccessibility"
- "__CompassPageViewControllerAccessibility_super"
- "__UIPageControlCompassAccessibility_super"
- "__UIViewCompassAccessibility_super"
- "_accessibilityHitTest:withEvent:"
- "_accessibilityLoadAccessibilityInformation"
- "_accessibilityPerformValidations:"
- "_accessibilityScrollStatus"
- "_accessibilitySupplementaryFooterViews"
- "_accessibilityViewIsVisible"
- "_axAnnounceDegreesIfNeeded:"
- "_axCurrentPage"
- "_axNumberOfPages"
- "accessibilityDecrement"
- "accessibilityHint"
- "accessibilityIdentifier"
- "accessibilityIncrement"
- "accessibilityInitializeBundle"
- "accessibilityLabel"
- "accessibilityScroll:"
- "accessibilityValue"
- "axArrayByIgnoringNilElementsWithCount:"
- "bundleWithIdentifier:"
- "convertPoint:toView:"
- "countByEnumeratingWithState:objects:count:"
- "doubleValue"
- "init"
- "installSafeCategory:canInteractWithTargetClass:"
- "integerValue"
- "isAccessibilityElement"
- "isEqualToString:"
- "keyWindow"
- "localizedStringForKey:value:table:"
- "performValidations:withPreValidationHandler:postValidationHandler:safeCategoryInstallationHandler:"
- "pointInside:withEvent:"
- "q16@0:8"
- "rootViewController"
- "safeCategoryBaseClass"
- "safeCategoryTargetClassName"
- "safeValueForKey:"
- "setAccessibilityHint:"
- "setAccessibilityIdentifier:"
- "setIsAccessibilityElement:"
- "setOverrideProcessName:"
- "setValidationTargetName:"
- "sharedInstance"
- "stringByAppendingString:"
- "stringWithFormat:"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@16"
- "v24@0:8d16"
- "v40@0:8{?=ddd}16"
- "validateClass:hasInstanceMethod:withFullSignature:"
- "validateClass:hasInstanceVariable:withType:"
- "{CGPoint=\"x\"d\"y\"d}"

```
