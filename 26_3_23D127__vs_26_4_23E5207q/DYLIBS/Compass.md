## Compass

> `/System/Library/AccessibilityBundles/Compass.axbundle/Compass`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x12ac
-  __TEXT.__auth_stubs: 0x1b0
+3005.16.0.0.0
+  __TEXT.__text: 0x13f4
+  __TEXT.__auth_stubs: 0x1a0
   __TEXT.__objc_methlist: 0x194
   __TEXT.__cstring: 0x34f
   __TEXT.__unwind_info: 0xb8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x180
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0xe0
+  __AUTH_CONST.__auth_got: 0xd8
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x520
   __AUTH_CONST.__objc_const: 0x4e8

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6F89CCB7-864F-3F21-A386-AFA27166C748
+  UUID: 157840D4-B8EA-3E35-9EFB-E017C07E886A
   Functions: 33
-  Symbols:   197
+  Symbols:   196
   CStrings:  161
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXCompassGlue accessibilityInitializeBundle] : 148 -> 152
~ ___46+[AXCompassGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___46+[AXCompassGlue accessibilityInitializeBundle]_block_invoke_3 : 112 -> 120
~ _accessibilityLocalizedString : 156 -> 164
~ _axCompassController : 88 -> 96
~ _axCompassPageViewController : 84 -> 92
~ _axLevelPageViewController : 84 -> 92
~ +[CompassPageViewControllerAccessibility _accessibilityPerformValidations:] : 428 -> 436
~ -[CompassPageViewControllerAccessibility _axAnnounceDegreesIfNeeded:] : 392 -> 424
~ -[CompassPageViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 112
~ -[CompassPageViewControllerAccessibility _updateDegreesLabel:] : 108 -> 112
~ -[CompassPageViewControllerAccessibility setCrosshairLevelForData:] : 288 -> 324
~ -[UIPageControlCompassAccessibility _axNumberOfPages] : 64 -> 68
~ -[UIPageControlCompassAccessibility _axCurrentPage] : 64 -> 68
~ -[UIPageControlCompassAccessibility accessibilityValue] : 284 -> 308
~ +[UIViewCompassAccessibility _accessibilityPerformValidations:] : 148 -> 156
~ -[UIViewCompassAccessibility isAccessibilityElement] : 164 -> 172
~ -[UIViewCompassAccessibility _accessibilitySupplementaryFooterViews] : 372 -> 404
~ -[UIViewCompassAccessibility _accessibilityHitTest:withEvent:] : 396 -> 400
~ -[UIViewCompassAccessibility accessibilityLabel] : 432 -> 492
~ -[UIViewCompassAccessibility _accessibilityScrollStatus] : 244 -> 272
~ -[UIViewCompassAccessibility accessibilityHint] : 152 -> 164
~ -[UIViewCompassAccessibility accessibilityScroll:] : 208 -> 220

```
