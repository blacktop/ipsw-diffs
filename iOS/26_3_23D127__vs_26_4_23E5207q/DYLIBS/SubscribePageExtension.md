## SubscribePageExtension

> `/System/Library/AccessibilityBundles/SubscribePageExtension.axbundle/SubscribePageExtension`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x348
-  __TEXT.__auth_stubs: 0xf0
+3005.16.0.0.0
+  __TEXT.__text: 0x36c
+  __TEXT.__auth_stubs: 0xe0
   __TEXT.__objc_methlist: 0x74
   __TEXT.__cstring: 0xfc
   __TEXT.__unwind_info: 0x88

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x80
+  __AUTH_CONST.__auth_got: 0x78
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BFFD0FB4-7351-379A-81A4-97AA11797DCA
+  UUID: CB33B746-7CA3-328E-B7DF-A6E23D54BBFE
   Functions: 11
-  Symbols:   81
+  Symbols:   80
   CStrings:  48
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[OfferButtonAccessibility _accessibilityPerformValidations:] : 124 -> 132
~ -[OfferButtonAccessibility accessibilityLabel] : 148 -> 160
~ +[AXSubscribePageExtensionGlue accessibilityInitializeBundle] : 148 -> 152
~ ___61+[AXSubscribePageExtensionGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184

```
