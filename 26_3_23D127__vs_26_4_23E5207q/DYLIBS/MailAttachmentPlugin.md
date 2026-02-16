## MailAttachmentPlugin

> `/System/Library/AccessibilityBundles/MailAttachmentPlugin.axbundle/MailAttachmentPlugin`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x388
-  __TEXT.__auth_stubs: 0xf0
+3005.16.0.0.0
+  __TEXT.__text: 0x3b8
+  __TEXT.__auth_stubs: 0xe0
   __TEXT.__objc_methlist: 0x98
   __TEXT.__cstring: 0x14c
   __TEXT.__unwind_info: 0x80

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x80
+  __AUTH_CONST.__auth_got: 0x78
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x180
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EF7E9F32-B47F-3A4A-A8E7-B66040B3AB0E
+  UUID: E4E1744D-FF4C-3F3A-93FB-FE887A4224F3
   Functions: 14
-  Symbols:   87
+  Symbols:   86
   CStrings:  58
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[MFAttachmentViewAccessibility _accessibilityPerformValidations:] : 152 -> 160
~ -[MFAttachmentViewAccessibility accessibilityLabel] : 84 -> 92
~ -[MFAttachmentViewAccessibility accessibilityValue] : 184 -> 200
~ _accessibilityLocalizedString : 156 -> 164
~ +[AXMailAttachmentGlue accessibilityInitializeBundle] : 148 -> 152
~ ___53+[AXMailAttachmentGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88

```
