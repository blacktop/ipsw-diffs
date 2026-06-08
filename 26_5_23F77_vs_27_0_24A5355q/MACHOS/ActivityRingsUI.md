## ActivityRingsUI

> `/System/Library/AccessibilityBundles/ActivityRingsUI.axbundle/ActivityRingsUI`

```diff

-1001.19.0.0.0
-  __TEXT.__text: 0x1248
-  __TEXT.__auth_stubs: 0x200
+1029.0.0.0.0
+  __TEXT.__text: 0x1144
+  __TEXT.__auth_stubs: 0x210
   __TEXT.__objc_stubs: 0x540
   __TEXT.__objc_methlist: 0x120
+  __TEXT.__const: 0x10
   __TEXT.__objc_classname: 0xf1
   __TEXT.__cstring: 0x1d4
   __TEXT.__objc_methname: 0x4d5
   __TEXT.__objc_methtype: 0x2b
-  __TEXT.__const: 0x10
   __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x108
-  __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x150
   __DATA_CONST.__cfstring: 0x2a0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
+  __DATA_CONST.__auth_got: 0x110
+  __DATA_CONST.__got: 0x68
   __DATA.__objc_const: 0x3f0
   __DATA.__objc_selrefs: 0x190
   __DATA.__objc_data: 0x230

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: ED530396-F2E0-3A51-A8D4-C779B9CD7702
-  Functions: 28
+  UUID: 4D5CAC4A-4E7B-3E1E-BCE4-1596CB6C6A01
+  Functions: 27
   Symbols:   170
   CStrings:  110
 
Symbols:
+ __block_literal_global.358
+ __block_literal_global.360
+ __block_literal_global.366
+ __block_literal_global.383
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- +[AXActivityRingsUIGlue accessibilityInitializeBundle].cold.1
- __block_literal_global.337
- __block_literal_global.339
- __block_literal_global.345
- __block_literal_global.362
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[ARUIRingGroupControllerAccessibility _accessibilityPerformValidations:] : 188 -> 180
~ -[ARUIRingGroupControllerAccessibility _accessibilityLocalizedRingDescriptions] : 980 -> 900
~ -[ARUIRingGroupAccessibility accessibilityLabel] : 872 -> 792
~ +[ARUIRingsViewAccessibility _accessibilityPerformValidations:] : 128 -> 120
~ -[ARUIRingsViewAccessibility isAccessibilityElement] : 100 -> 92
~ -[ARUIRingsViewAccessibility accessibilityLabel] : 736 -> 716
~ +[AXActivityRingsUIGlue accessibilityInitializeBundle] : 44 -> 40
~ ___54+[AXActivityRingsUIGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___54+[AXActivityRingsUIGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 96
~ ___54+[AXActivityRingsUIGlue accessibilityInitializeBundle]_block_invoke_4 : 120 -> 112
~ _accessibilityLocalizedString : 168 -> 160
~ __userIsWheelchairUserWithVoiceOverOn : 340 -> 336
~ ____userIsWheelchairUserWithVoiceOverOn_block_invoke : 116 -> 112

```
