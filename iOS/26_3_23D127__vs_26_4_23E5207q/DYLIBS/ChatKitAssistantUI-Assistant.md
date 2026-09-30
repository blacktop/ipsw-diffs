## ChatKitAssistantUI-Assistant

> `/System/Library/AccessibilityBundles/ChatKitAssistantUI-Assistant.axbundle/ChatKitAssistantUI-Assistant`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x44c
-  __TEXT.__auth_stubs: 0x100
+3005.16.0.0.0
+  __TEXT.__text: 0x484
+  __TEXT.__auth_stubs: 0xf0
   __TEXT.__objc_methlist: 0x64
   __TEXT.__cstring: 0x196
   __TEXT.__unwind_info: 0x78

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x88
+  __AUTH_CONST.__auth_got: 0x80
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x240
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E8BEB689-6EE2-39A5-B9A9-5BC9E3AE4947
+  UUID: E9D6607C-D891-3AC9-B4DE-2FA9EB60E063
   Functions: 10
-  Symbols:   83
+  Symbols:   82
   CStrings:  71
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
Functions:
~ -[CKMessageSnippetContentViewAccessibility accessibilityLabel] : 316 -> 348
~ -[CKMessageSnippetContentViewAccessibility setBalloonType:] : 124 -> 128
~ +[ChatAssistantUIGlue accessibilityInitializeBundle] : 148 -> 152
~ ___52+[ChatAssistantUIGlue accessibilityInitializeBundle]_block_invoke : 200 -> 204
~ ___52+[ChatAssistantUIGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ _accessibilityAssistantLocalizedString : 176 -> 184

```
