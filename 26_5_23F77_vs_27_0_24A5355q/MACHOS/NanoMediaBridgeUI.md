## NanoMediaBridgeUI

> `/System/Library/AccessibilityBundles/NanoMediaBridgeUI.axbundle/NanoMediaBridgeUI`

```diff

-1001.19.0.0.0
-  __TEXT.__text: 0x6c4
-  __TEXT.__auth_stubs: 0x100
+1029.0.0.0.0
+  __TEXT.__text: 0x690
+  __TEXT.__auth_stubs: 0x110
   __TEXT.__objc_stubs: 0x240
   __TEXT.__objc_methlist: 0xa0
   __TEXT.__objc_classname: 0x6f

   __TEXT.__objc_methname: 0x2e2
   __TEXT.__objc_methtype: 0x46
   __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__auth_got: 0x88
-  __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__cfstring: 0x1a0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0x90
+  __DATA_CONST.__got: 0x38
   __DATA.__objc_const: 0x1b0
   __DATA.__objc_selrefs: 0xc8
   __DATA.__objc_data: 0xf0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A3FF2586-89DD-3256-8503-8F7499104065
-  Functions: 17
+  UUID: 24567402-9C41-3125-95F8-6CEB1F5DE832
+  Functions: 16
   Symbols:   88
   CStrings:  65
 
Symbols:
+ __block_literal_global.352
+ __block_literal_global.354
+ __block_literal_global.360
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- +[AXNanoMediaBridgeUIGlue accessibilityInitializeBundle].cold.1
- __block_literal_global.331
- __block_literal_global.333
- __block_literal_global.339
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[NMBUIMediaTableCellAccessibility _accessibilityPerformValidations:] : 248 -> 240
~ -[NMBUIMediaTableCellAccessibility accessibilityActivationPoint] : 236 -> 220
~ -[NMBUIMediaTableCellAccessibility accessibilityTraits] : 152 -> 148
~ -[NMBUIMediaTableCellAccessibility accessibilityValue] : 160 -> 144
~ -[NMBUIMediaTableCellAccessibility _axIsShowingControl] : 420 -> 452
~ +[AXNanoMediaBridgeUIGlue accessibilityInitializeBundle] : 44 -> 40
~ ___56+[AXNanoMediaBridgeUIGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___56+[AXNanoMediaBridgeUIGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 96
~ _accessibilityLocalizedString : 168 -> 160

```
