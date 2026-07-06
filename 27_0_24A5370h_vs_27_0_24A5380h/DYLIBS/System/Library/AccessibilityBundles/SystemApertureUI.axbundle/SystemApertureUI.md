## SystemApertureUI

> `/System/Library/AccessibilityBundles/SystemApertureUI.axbundle/SystemApertureUI`

```diff

-  __TEXT.__text: 0x26d4
+  __TEXT.__text: 0x270c
   __TEXT.__objc_methlist: 0x3d4
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x70
-  __TEXT.__cstring: 0x5c2
+  __TEXT.__cstring: 0x5de
   __TEXT.__unwind_info: 0x150
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__got: 0xb8
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x720
+  __AUTH_CONST.__cfstring: 0x740
   __AUTH_CONST.__objc_const: 0x5f0
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xa0
   __DATA.__data: 0x180
-  __DATA.__bss: 0x10
-  __DATA_DIRTY.__objc_data: 0x190
-  __DATA_DIRTY.__bss: 0x8
+  __DATA.__bss: 0x8
+  __DATA_DIRTY.__objc_data: 0x230
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libobjc.A.dylib
   Functions: 68
   Symbols:   391
-  CStrings:  126
+  CStrings:  128
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __DATA.__data : content changed
Functions:
~ -[SAUIElementViewAccessibility accessibilityCustomActions] : 1248 -> 1276
~ ___82-[SAUIElementViewControllerAccessibility _axShiftFocusToElementViewForPowerAlerts]_block_invoke : 220 -> 248
CStrings:
+ "SBChargingAlertElement"
+ "SBLowBatteryAlertElement"
- "SBPowerAlertElement"

```
