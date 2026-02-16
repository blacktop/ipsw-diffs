## Calendar-Assistant

> `/System/Library/AccessibilityBundles/Calendar-Assistant.axbundle/Calendar-Assistant`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x410
-  __TEXT.__auth_stubs: 0x120
+3005.16.0.0.0
+  __TEXT.__text: 0x444
+  __TEXT.__auth_stubs: 0x110
   __TEXT.__objc_methlist: 0x5c
   __TEXT.__cstring: 0x120
   __TEXT.__unwind_info: 0x88

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x98
+  __AUTH_CONST.__auth_got: 0x90
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 589AD830-AAB8-3172-A52C-C192CD9FC7B4
+  UUID: 1CB2F622-F67F-33C6-A9C9-D7F494730B2E
   Functions: 11
-  Symbols:   92
+  Symbols:   91
   CStrings:  54
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ ___54+[CalendarAssistantGlue accessibilityInitializeBundle]_block_invoke : 100 -> 104
~ ___54+[CalendarAssistantGlue accessibilityInitializeBundle]_block_invoke_3 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184
~ +[CalendarAssistantUIControllerAccessibility _accessibilityPerformValidations:] : 172 -> 184
~ -[CalendarAssistantUIControllerAccessibility tableView:viewForHeaderInSection:] : 380 -> 404

```
