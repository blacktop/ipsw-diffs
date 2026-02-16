## Mail-Assistant

> `/System/Library/AccessibilityBundles/Mail-Assistant.axbundle/Mail-Assistant`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0xbd8
-  __TEXT.__auth_stubs: 0x190
+3005.16.0.0.0
+  __TEXT.__text: 0xcc0
+  __TEXT.__auth_stubs: 0x180
   __TEXT.__objc_methlist: 0xa4
   __TEXT.__cstring: 0x2ca
   __TEXT.__unwind_info: 0x90

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xd0
+  __AUTH_CONST.__auth_got: 0xc8
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x4c0
   __AUTH_CONST.__objc_const: 0x2d0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7715FF43-D5FE-37D0-9CEC-EDE1479D9ACA
+  UUID: 6B2AA88C-3FA6-3052-828E-4801A0166523
   Functions: 16
-  Symbols:   129
+  Symbols:   128
   CStrings:  122
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ ___54+[AXMailAssistantUIGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___54+[AXMailAssistantUIGlue accessibilityInitializeBundle]_block_invoke_2 : 504 -> 508
~ ___54+[AXMailAssistantUIGlue accessibilityInitializeBundle]_block_invoke_3 : 84 -> 88
~ ___54+[AXMailAssistantUIGlue accessibilityInitializeBundle]_block_invoke_4 : 92 -> 100
~ _accessibilityMobileMailLocalizedString : 176 -> 196
~ -[MFEmailSnippetComposeViewAccessibility accessibilityLabel] : 840 -> 936
~ -[MFEmailSnippetSearchResultCellViewAccessibility accessibilityLabel] : 604 -> 664
~ -[MFEmailSnippetSearchResultCellViewAccessibility setEmail:] : 504 -> 540

```
