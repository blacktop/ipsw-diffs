## LocalAuthenticationUI

> `/System/Library/AccessibilityBundles/LocalAuthenticationUI.axbundle/LocalAuthenticationUI`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x1b0
-  __TEXT.__auth_stubs: 0xa0
+3005.16.0.0.0
+  __TEXT.__text: 0x1c0
+  __TEXT.__auth_stubs: 0x90
   __TEXT.__objc_methlist: 0x14
   __TEXT.__cstring: 0x7a
   __TEXT.__unwind_info: 0x70

   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x48
-  __AUTH_CONST.__auth_got: 0x58
+  __AUTH_CONST.__auth_got: 0x50
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x80
   __AUTH_CONST.__objc_const: 0x90

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 136595AD-D7CC-3C9F-B01E-6D9E27BCC34D
+  UUID: 6B65727B-3968-33DE-BD05-149D46D9EA98
   Functions: 5
-  Symbols:   47
+  Symbols:   46
   CStrings:  20
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
Functions:
~ +[AXLocalAuthenticationUIGlue accessibilityInitializeBundle] : 148 -> 152
~ ___60+[AXLocalAuthenticationUIGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184

```
