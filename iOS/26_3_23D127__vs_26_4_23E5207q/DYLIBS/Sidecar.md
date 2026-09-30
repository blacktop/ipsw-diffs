## Sidecar

> `/System/Library/AccessibilityBundles/Sidecar.axbundle/Sidecar`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x1a4
-  __TEXT.__auth_stubs: 0xa0
+3005.16.0.0.0
+  __TEXT.__text: 0x1b4
+  __TEXT.__auth_stubs: 0x90
   __TEXT.__objc_methlist: 0x14
   __TEXT.__cstring: 0x65
   __TEXT.__unwind_info: 0x70

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x40
-  __AUTH_CONST.__auth_got: 0x58
+  __AUTH_CONST.__auth_got: 0x50
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x90

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 44D1229B-9AEB-3E72-878D-0EF62D970EEC
+  UUID: CD5E1DD5-A969-3794-B257-28E4235EDDA7
   Functions: 5
-  Symbols:   46
+  Symbols:   45
   CStrings:  19
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
Functions:
~ +[AXSidecarGlue accessibilityInitializeBundle] : 148 -> 152
~ ___46+[AXSidecarGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ _accessibilityLocalizedString : 176 -> 184

```
