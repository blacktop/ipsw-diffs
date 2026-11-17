## CameraUI

> `/System/Library/AccessibilityBundles/CameraUI.axbundle/CameraUI`

```diff

-3050.3.12.0.0
-  __TEXT.__text: 0x19134
-  __TEXT.__objc_methlist: 0x2804
+3050.3.22.0.0
+  __TEXT.__text: 0x19390
+  __TEXT.__objc_methlist: 0x281c
   __TEXT.__const: 0x170
-  __TEXT.__gcc_except_tab: 0x418
-  __TEXT.__cstring: 0x37da
+  __TEXT.__gcc_except_tab: 0x404
+  __TEXT.__cstring: 0x380c
   __TEXT.__oslogstring: 0x381
-  __TEXT.__unwind_info: 0xb48
+  __TEXT.__unwind_info: 0xb50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x3e0
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15f8
+  __DATA_CONST.__objc_selrefs: 0x1610
   __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__got: 0x2d8
   __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0x49a0
+  __AUTH_CONST.__cfstring: 0x49e0
   __AUTH_CONST.__objc_const: 0x5550
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 866
-  Symbols:   1915
-  CStrings:  648
+  Functions: 868
+  Symbols:   1917
+  CStrings:  650
 
Symbols:
+ -[CAMCaptureEngineAccessibility _accessibilityCaptureSessionHasPanoramaOutput:]
+ -[CAMDynamicShutterControlAccessibility setShowingAutoCapture:animated:]
+ GCC_except_table496
+ GCC_except_table510
+ GCC_except_table515
+ GCC_except_table518
+ GCC_except_table525
+ GCC_except_table529
+ GCC_except_table533
+ GCC_except_table539
+ GCC_except_table545
+ GCC_except_table558
+ GCC_except_table589
+ GCC_except_table601
+ GCC_except_table614
+ GCC_except_table647
+ GCC_except_table693
+ GCC_except_table707
+ GCC_except_table791
- GCC_except_table492
- GCC_except_table509
- GCC_except_table514
- GCC_except_table517
- GCC_except_table524
- GCC_except_table528
- GCC_except_table532
- GCC_except_table538
- GCC_except_table544
- GCC_except_table557
- GCC_except_table587
- GCC_except_table599
- GCC_except_table612
- GCC_except_table645
- GCC_except_table691
- GCC_except_table705
- GCC_except_table789
Functions:
~ +[CAMCaptureEngineAccessibility _accessibilityPerformValidations:] : 392 -> 408
~ -[CAMCaptureEngineAccessibility _accessibilityDetectFaces:completionBlock:] : 140 -> 156
+ -[CAMCaptureEngineAccessibility _accessibilityCaptureSessionHasPanoramaOutput:]
~ +[CAMDynamicShutterControlAccessibility _accessibilityPerformValidations:] : 1176 -> 1208
+ -[CAMDynamicShutterControlAccessibility setShowingAutoCapture:animated:]
~ -[CAMDynamicShutterControlAccessibility _axElementForAutoCaptureButton] : 540 -> 572
~ ___71-[CAMDynamicShutterControlAccessibility _axElementForAutoCaptureButton]_block_invoke : 128 -> 204
~ ___71-[CAMDynamicShutterControlAccessibility _axElementForAutoCaptureButton]_block_invoke_7 : 164 -> 320
~ -[CAMDynamicShutterControlAccessibility _recordingAccessibilityLabel] : 972 -> 844
CStrings:
+ "CAMPanoramaOutput"
+ "setShowingAutoCapture:animated:"
```
