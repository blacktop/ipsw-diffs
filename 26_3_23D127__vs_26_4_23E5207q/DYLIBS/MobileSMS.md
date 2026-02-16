## MobileSMS

> `/System/Library/AccessibilityBundles/MobileSMS.axbundle/MobileSMS`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x520
-  __TEXT.__auth_stubs: 0x140
+3005.16.0.0.0
+  __TEXT.__text: 0x544
+  __TEXT.__auth_stubs: 0x130
   __TEXT.__objc_methlist: 0x80
   __TEXT.__cstring: 0x1c4
-  __TEXT.__unwind_info: 0x78
+  __TEXT.__unwind_info: 0x80
   __TEXT.__objc_classname: 0x74
   __TEXT.__objc_methname: 0x281
   __TEXT.__objc_methtype: 0x2b

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xa8
+  __AUTH_CONST.__auth_got: 0xa0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x2e0
   __AUTH_CONST.__objc_const: 0x1f0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DA1A2A1A-1B3E-310D-A579-17BA9B23F1A2
+  UUID: D3528E81-36C9-3FA2-B7D7-6262CBEEF882
   Functions: 11
-  Symbols:   92
+  Symbols:   91
   CStrings:  81
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXMobileSMSGlue accessibilityInitializeBundle] : 148 -> 152
~ ___48+[AXMobileSMSGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ ___48+[AXMobileSMSGlue accessibilityInitializeBundle]_block_invoke_3 : 136 -> 140
~ _accessibilityLocalizedString : 156 -> 164
~ +[SMSApplicationAccessibility _accessibilityPerformValidations:] : 352 -> 364
~ -[SMSApplicationAccessibility _accessibilitySoftwareKeyboardActive] : 204 -> 212
~ -[SMSApplicationAccessibility _accessibilityMainWindow] : 176 -> 172

```
