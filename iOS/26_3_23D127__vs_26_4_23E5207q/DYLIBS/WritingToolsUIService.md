## WritingToolsUIService

> `/System/Library/AccessibilityBundles/WritingToolsUIService.axbundle/WritingToolsUIService`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x284
-  __TEXT.__auth_stubs: 0xf0
+3005.16.0.0.0
+  __TEXT.__text: 0x298
+  __TEXT.__auth_stubs: 0xd0
   __TEXT.__objc_methlist: 0x5c
   __TEXT.__cstring: 0xc1
   __TEXT.__unwind_info: 0x78

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x80
+  __AUTH_CONST.__auth_got: 0x70
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5C836741-6FF4-35E9-AD5C-ACAE8EBA36AF
+  UUID: 358A877F-482F-3E92-9624-41B6304C259E
   Functions: 10
-  Symbols:   80
+  Symbols:   78
   CStrings:  39
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_release_x21
- _objc_retain
- _objc_retain_x1
Functions:
~ -[UITextViewAccessibility__WritingToolsUIService__UIKit _accessibilitySetSelectedTextRange:] : 152 -> 156
~ +[AXWritingToolsUIServiceGlue accessibilityInitializeBundle] : 148 -> 152
~ ___60+[AXWritingToolsUIServiceGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184

```
