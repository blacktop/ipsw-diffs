## SiriSetup

> `/System/Library/AccessibilityBundles/SiriSetup.axbundle/SiriSetup`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x36c
-  __TEXT.__auth_stubs: 0x100
+3005.16.0.0.0
+  __TEXT.__text: 0x38c
+  __TEXT.__auth_stubs: 0xf0
   __TEXT.__objc_stubs: 0x1e0
   __TEXT.__objc_methlist: 0x74
   __TEXT.__cstring: 0xd6

   __TEXT.__objc_methname: 0x260
   __TEXT.__objc_methtype: 0x2e
   __TEXT.__unwind_info: 0x78
-  __DATA_CONST.__auth_got: 0x88
+  __DATA_CONST.__auth_got: 0x80
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__cfstring: 0x100

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2FDCD2FF-285E-3B5E-B4D2-91050045F861
+  UUID: 1360FC2F-B529-330B-A198-25BCCACA98DD
   Functions: 11
-  Symbols:   75
+  Symbols:   74
   CStrings:  48
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain_x1
- _objc_retain_x2
Functions:
~ +[AXSiriSetupGlue accessibilityInitializeBundle] : 148 -> 152
~ ___48+[AXSiriSetupGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184
~ +[EducationWelcomeControllerAccessibility _accessibilityPerformValidations:] : 128 -> 136
~ -[EducationWelcomeControllerAccessibility _accessibilityHideVideoPlayer] : 124 -> 132

```
