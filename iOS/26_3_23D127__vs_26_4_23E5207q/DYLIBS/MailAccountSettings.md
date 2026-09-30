## MailAccountSettings

> `/System/Library/AccessibilityBundles/MailAccountSettings.axbundle/MailAccountSettings`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x338
-  __TEXT.__auth_stubs: 0xf0
+3005.16.0.0.0
+  __TEXT.__text: 0x358
+  __TEXT.__auth_stubs: 0xe0
   __TEXT.__objc_methlist: 0x5c
   __TEXT.__cstring: 0x11e
   __TEXT.__unwind_info: 0x70

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x88
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x80
+  __AUTH_CONST.__auth_got: 0x78
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x160
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 998FE042-3A28-37F0-8013-175569C37C97
+  UUID: C7103A38-BB83-311C-B611-DEAFC031FAA8
   Functions: 9
-  Symbols:   77
+  Symbols:   76
   CStrings:  52
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AccountPSOutgoingDetailControllerAccessibility _accessibilityPerformValidations:] : 200 -> 208
~ -[AccountPSOutgoingDetailControllerAccessibility processValidationResult:] : 152 -> 160
~ +[AXMailAccountSettingsGlue accessibilityInitializeBundle] : 148 -> 152
~ ___58+[AXMailAccountSettingsGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184

```
