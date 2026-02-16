## System-Assistant

> `/System/Library/AccessibilityBundles/System-Assistant.axbundle/System-Assistant`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x2c8
-  __TEXT.__auth_stubs: 0xc0
+3005.16.0.0.0
+  __TEXT.__text: 0x2e8
+  __TEXT.__auth_stubs: 0xb0
   __TEXT.__objc_methlist: 0x58
   __TEXT.__cstring: 0x105
   __TEXT.__unwind_info: 0x78

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x68
+  __AUTH_CONST.__auth_got: 0x60
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x100
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C3A0B431-855B-3A04-808A-F1A22850F086
+  UUID: 11AA7EE2-2548-3688-893C-FFE3060A8912
   Functions: 11
-  Symbols:   80
+  Symbols:   79
   CStrings:  43
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
Functions:
~ ___47+[SiriSystemGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___47+[SiriSystemGlue accessibilityInitializeBundle]_block_invoke_3 : 84 -> 88
~ _accessibilityLocalizedString : 176 -> 184
~ -[ACAssistantAlternateProviderResultViewAccessibility accessibilityLabel] : 180 -> 196

```
