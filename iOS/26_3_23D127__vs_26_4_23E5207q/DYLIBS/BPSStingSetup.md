## BPSStingSetup

> `/System/Library/AccessibilityBundles/BPSStingSetup.axbundle/BPSStingSetup`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x2f0
-  __TEXT.__auth_stubs: 0xe0
+3005.16.0.0.0
+  __TEXT.__text: 0x314
+  __TEXT.__auth_stubs: 0xd0
   __TEXT.__objc_methlist: 0x68
   __TEXT.__cstring: 0xe6
   __TEXT.__unwind_info: 0x80

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x78
+  __AUTH_CONST.__auth_got: 0x70
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4497A12A-1C5B-32BC-BAEC-C8A0EBF6040A
+  UUID: 06FD09AF-1355-3DE4-B076-C34F4FD7AFCF
   Functions: 10
-  Symbols:   76
+  Symbols:   75
   CStrings:  46
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXBPSStingSetupGlue accessibilityInitializeBundle] : 148 -> 152
~ ___52+[AXBPSStingSetupGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184
~ +[BPSStingFeatureCellAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[BPSStingFeatureCellAccessibility accessibilityLabel] : 148 -> 160

```
