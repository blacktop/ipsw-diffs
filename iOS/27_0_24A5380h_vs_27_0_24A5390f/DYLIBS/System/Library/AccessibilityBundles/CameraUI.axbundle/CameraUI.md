## CameraUI

> `/System/Library/AccessibilityBundles/CameraUI.axbundle/CameraUI`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-3042.0.0.0.0
-  __TEXT.__text: 0x18344
-  __TEXT.__objc_methlist: 0x267c
+3045.0.0.0.0
+  __TEXT.__text: 0x18528
+  __TEXT.__objc_methlist: 0x26a4
   __TEXT.__const: 0x160
   __TEXT.__gcc_except_tab: 0x378
-  __TEXT.__cstring: 0x3443
+  __TEXT.__cstring: 0x3474
   __TEXT.__oslogstring: 0x381
   __TEXT.__unwind_info: 0x900
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1518
+  __DATA_CONST.__objc_selrefs: 0x1530
   __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x48
   __DATA_CONST.__got: 0x2c0
   __AUTH_CONST.__const: 0x580
-  __AUTH_CONST.__cfstring: 0x4560
+  __AUTH_CONST.__cfstring: 0x45a0
   __AUTH_CONST.__objc_const: 0x5310
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 818
-  Symbols:   2390
-  CStrings:  614
+  Functions: 822
+  Symbols:   2400
+  CStrings:  616
 
Symbols:
+ -[CAMCaptureEngineAccessibility _accessibilityHasActiveRecording]
+ -[CAMFullscreenViewfinderAccessibility axLastSuggestionButton]
+ -[CAMFullscreenViewfinderAccessibility setAxLastSuggestionButton:]
+ GCC_except_table476
+ GCC_except_table490
+ GCC_except_table493
+ GCC_except_table499
+ GCC_except_table505
+ GCC_except_table518
+ GCC_except_table548
+ GCC_except_table560
+ GCC_except_table573
+ GCC_except_table606
+ GCC_except_table652
+ GCC_except_table666
+ GCC_except_table749
+ ___54-[CAMMotionControllerAccessibility _axDoMotionUpdate:]_block_invoke
+ ___CAMFullscreenViewfinderAccessibility__axLastSuggestionButton
+ ___UIAccessibilityGetAssociatedLong
+ ___UIAccessibilitySetAssociatedLong
+ _objc_msgSend$_accessibilityHasActiveRecording
+ _objc_msgSend$axLastSuggestionButton
+ _objc_msgSend$setAxLastSuggestionButton:
- GCC_except_table472
- GCC_except_table489
- GCC_except_table492
- GCC_except_table498
- GCC_except_table504
- GCC_except_table517
- GCC_except_table547
- GCC_except_table559
- GCC_except_table572
- GCC_except_table605
- GCC_except_table649
- GCC_except_table662
- GCC_except_table745
CStrings:
+ "__captureController"
+ "isCapturingPanorama"
+ "isCapturingTimelapse"
- "viewDidLoad"
```
