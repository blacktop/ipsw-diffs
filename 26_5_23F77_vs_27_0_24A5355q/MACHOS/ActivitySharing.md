## ActivitySharing

> `/System/Library/AccessibilityBundles/ActivitySharing.axbundle/ActivitySharing`

```diff

-1001.19.0.0.0
-  __TEXT.__text: 0x454
-  __TEXT.__auth_stubs: 0xd0
+1029.0.0.0.0
+  __TEXT.__text: 0x42c
+  __TEXT.__auth_stubs: 0xf0
   __TEXT.__objc_stubs: 0x200
   __TEXT.__objc_methlist: 0x70
   __TEXT.__objc_classname: 0x57
   __TEXT.__cstring: 0x11c
   __TEXT.__objc_methname: 0x2f4
   __TEXT.__objc_methtype: 0x3a
-  __TEXT.__unwind_info: 0x90
-  __DATA_CONST.__auth_got: 0x70
-  __DATA_CONST.__got: 0x20
+  __TEXT.__unwind_info: 0x88
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0x80
+  __DATA_CONST.__got: 0x20
   __DATA.__objc_const: 0x1b0
   __DATA.__objc_selrefs: 0xb0
   __DATA.__objc_data: 0xf0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AF89E95A-E785-36E3-ADEA-8842227DF51F
-  Functions: 13
-  Symbols:   76
+  UUID: 4F889E2D-D837-368D-ABD2-AEA10EE117D5
+  Functions: 12
+  Symbols:   77
   CStrings:  53
 
Symbols:
+ __block_literal_global.352
+ __block_literal_global.354
+ __block_literal_global.360
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
- +[AXActivitySharingGlue accessibilityInitializeBundle].cold.1
- __block_literal_global.331
- __block_literal_global.333
- __block_literal_global.339
- _objc_retain_x19
Functions:
~ +[ASFriendAccessibility _accessibilityPerformValidations:] : 176 -> 168
~ -[ASFriendAccessibility _accessibilityLoadAccessibilityInformation] : 348 -> 356
~ +[AXActivitySharingGlue accessibilityInitializeBundle] : 44 -> 40
~ ___54+[AXActivitySharingGlue accessibilityInitializeBundle]_block_invoke : 104 -> 100
~ ___54+[AXActivitySharingGlue accessibilityInitializeBundle]_block_invoke_3 : 100 -> 96
~ _accessibilityLocalizedString : 168 -> 160

```
