## NanoMediaBridgeUI

> `/System/Library/AccessibilityBundles/NanoMediaBridgeUI.axbundle/NanoMediaBridgeUI`

```diff

-1001.4.8.0.0
-  __TEXT.__text: 0x684
-  __TEXT.__auth_stubs: 0x110
+1001.12.0.0.0
+  __TEXT.__text: 0x6c4
+  __TEXT.__auth_stubs: 0x100
   __TEXT.__objc_stubs: 0x240
   __TEXT.__objc_methlist: 0xa0
   __TEXT.__objc_classname: 0x6f

   __TEXT.__objc_methname: 0x2e2
   __TEXT.__objc_methtype: 0x46
   __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x90
+  __DATA_CONST.__auth_got: 0x88
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__cfstring: 0x1a0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 43046BFB-2380-3EEE-B537-697DADE41C41
+  UUID: 682AF674-1557-382D-A639-DECFC4BB6F11
   Functions: 17
-  Symbols:   89
+  Symbols:   88
   CStrings:  65
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[NMBUIMediaTableCellAccessibility _accessibilityPerformValidations:] : 240 -> 248
~ -[NMBUIMediaTableCellAccessibility accessibilityActivationPoint] : 228 -> 236
~ -[NMBUIMediaTableCellAccessibility accessibilityTraits] : 148 -> 152
~ -[NMBUIMediaTableCellAccessibility accessibilityValue] : 148 -> 160
~ -[NMBUIMediaTableCellAccessibility _axIsShowingControl] : 404 -> 420
~ ___56+[AXNanoMediaBridgeUIGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___56+[AXNanoMediaBridgeUIGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ _accessibilityLocalizedString : 160 -> 168

```
