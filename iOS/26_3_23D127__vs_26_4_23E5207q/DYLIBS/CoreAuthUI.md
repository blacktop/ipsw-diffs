## CoreAuthUI

> `/System/Library/AccessibilityBundles/CoreAuthUI.axbundle/CoreAuthUI`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x474
-  __TEXT.__auth_stubs: 0x120
+3005.16.0.0.0
+  __TEXT.__text: 0x498
+  __TEXT.__auth_stubs: 0x110
   __TEXT.__objc_methlist: 0x8c
   __TEXT.__cstring: 0x10c
   __TEXT.__const: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x98
+  __AUTH_CONST.__auth_got: 0x90
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x120
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 40CB37ED-7675-3AB0-A1C4-16E0F602D924
+  UUID: 9536012E-3FD3-349F-9EF9-5711DF085A55
   Functions: 14
-  Symbols:   96
+  Symbols:   95
   CStrings:  53
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
Functions:
~ +[AXCoreAuthUIGlue accessibilityInitializeBundle] : 148 -> 152
~ ___49+[AXCoreAuthUIGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184
~ -[FaceIdViewControllerAccessibility _accessibilityNotificationFeedbackGenerator] : 96 -> 100
~ ___64-[FaceIdViewControllerAccessibility mechanismEvent:value:reply:]_block_invoke : 248 -> 264

```
