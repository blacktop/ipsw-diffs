## ActivityRingsUI

> `/System/Library/AccessibilityBundles/ActivityRingsUI.axbundle/ActivityRingsUI`

```diff

-1001.4.8.0.0
-  __TEXT.__text: 0x1138
-  __TEXT.__auth_stubs: 0x210
+1001.12.0.0.0
+  __TEXT.__text: 0x1248
+  __TEXT.__auth_stubs: 0x200
   __TEXT.__objc_stubs: 0x540
   __TEXT.__objc_methlist: 0x120
   __TEXT.__objc_classname: 0xf1

   __TEXT.__objc_methtype: 0x2b
   __TEXT.__const: 0x10
   __TEXT.__unwind_info: 0xc0
-  __DATA_CONST.__auth_got: 0x110
+  __DATA_CONST.__auth_got: 0x108
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__const: 0x150
   __DATA_CONST.__cfstring: 0x2a0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3A81A50A-816E-38C2-A5A8-1A0234BB6CDA
+  UUID: 6E040DD4-5FFC-3A4A-A429-51EEEA4A3D96
   Functions: 28
-  Symbols:   171
+  Symbols:   170
   CStrings:  110
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[ARUIRingGroupControllerAccessibility _accessibilityPerformValidations:] : 180 -> 188
~ -[ARUIRingGroupControllerAccessibility _accessibilityLocalizedRingDescriptions] : 900 -> 980
~ -[ARUIRingGroupControllerAccessibility _accessibilityRingValues] : 388 -> 404
~ -[ARUIRingGroupAccessibility accessibilityLabel] : 792 -> 872
~ +[ARUIRingsViewAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ -[ARUIRingsViewAccessibility isAccessibilityElement] : 92 -> 100
~ -[ARUIRingsViewAccessibility accessibilityLabel] : 696 -> 736
~ ___54+[AXActivityRingsUIGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___54+[AXActivityRingsUIGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ ___54+[AXActivityRingsUIGlue accessibilityInitializeBundle]_block_invoke_4 : 112 -> 120
~ _accessibilityLocalizedString : 160 -> 168
~ __userIsWheelchairUserWithVoiceOverOn : 336 -> 340
~ ____userIsWheelchairUserWithVoiceOverOn_block_invoke : 112 -> 116

```
