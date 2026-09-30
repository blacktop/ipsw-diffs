## ScreenshotServicesService

> `/System/Library/AccessibilityBundles/ScreenshotServicesService.axbundle/ScreenshotServicesService`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x17bc
-  __TEXT.__auth_stubs: 0x230
+3005.16.0.0.0
+  __TEXT.__text: 0x18a8
+  __TEXT.__auth_stubs: 0x220
   __TEXT.__objc_methlist: 0x330
   __TEXT.__cstring: 0x6cb
   __TEXT.__const: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1f0
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x128
+  __AUTH_CONST.__auth_got: 0x120
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__cfstring: 0x940
   __AUTH_CONST.__objc_const: 0x990

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1D00C4AB-9795-3611-A9EA-5886FF734D75
+  UUID: EDA41795-7277-3F30-BF8E-434AB0DB8BA5
   Functions: 65
-  Symbols:   333
+  Symbols:   332
   CStrings:  247
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ ___64+[AXScreenshotServicesServiceGlue accessibilityInitializeBundle]_block_invoke : 152 -> 160
~ ___64+[AXScreenshotServicesServiceGlue accessibilityInitializeBundle]_block_invoke_3 : 84 -> 88
~ ___64+[AXScreenshotServicesServiceGlue accessibilityInitializeBundle]_block_invoke_4 : 212 -> 220
~ ___64+[AXScreenshotServicesServiceGlue accessibilityInitializeBundle]_block_invoke_5 : 92 -> 96
~ ___64+[AXScreenshotServicesServiceGlue accessibilityInitializeBundle]_block_invoke_6 : 116 -> 120
~ ___64+[AXScreenshotServicesServiceGlue accessibilityInitializeBundle]_block_invoke_7 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184
~ -[SSSCropOverlayCornerViewAccessibility accessibilityLabel] : 100 -> 104
~ +[SSSDittoRootViewControllerAccessibility _accessibilityPerformValidations:] : 180 -> 188
~ +[SSSScreenshotsViewAccessibility _accessibilityPerformValidations:] : 320 -> 332
~ -[SSSScreenshotsViewAccessibility _accessibilitySupplementaryFooterViews] : 332 -> 368
~ +[SSSScreenshotsViewControllerAccessibility _accessibilityPerformValidations:] : 340 -> 348
~ -[SSSScreenshotsViewControllerAccessibility _accessibilityAnnotateItems] : 376 -> 416
~ -[SSSScreenshotsViewControllerAccessibility _updateAnnotationButtonAccessibilityTraits] : 176 -> 184
~ -[SSSScreenshotsViewControllerAccessibility _accessibilityPostLayoutChangeIfNecessary] : 228 -> 236
~ -[SSS_UIWindowAccessibility accessibilityRemoteSubstituteChildren:] : 344 -> 356
~ +[_SSSScreenshotAnnotationControllerAKOverlayContainerViewAccessibility _accessibilityPerformValidations:] : 200 -> 208
~ -[_SSSScreenshotAnnotationControllerAKOverlayContainerViewAccessibility _axMarkupAKOverlayView] : 360 -> 372
~ ___95-[_SSSScreenshotAnnotationControllerAKOverlayContainerViewAccessibility _axMarkupAKOverlayView]_block_invoke : 76 -> 80
~ -[_SSSScreenshotAnnotationControllerAKOverlayContainerViewAccessibility _accessibilityLabelForOverlayView] : 300 -> 324
~ +[SSSCropOverlayGrabberViewAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[SSSCropOverlayGrabberViewAccessibility accessibilityLabel] : 100 -> 104

```
