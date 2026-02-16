## DoNotDisturbSettings

> `/System/Library/AccessibilityBundles/DoNotDisturbSettings.axbundle/DoNotDisturbSettings`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x248
-  __TEXT.__auth_stubs: 0xb0
+3005.16.0.0.0
+  __TEXT.__text: 0x25c
+  __TEXT.__auth_stubs: 0xa0
   __TEXT.__objc_methlist: 0x5c
   __TEXT.__cstring: 0xd0
   __TEXT.__unwind_info: 0x78

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x60
+  __AUTH_CONST.__auth_got: 0x58
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6C22B845-7CDA-3955-ACD3-FA1C29BEE168
+  UUID: 3AD9E0CC-B4D8-358F-BDD2-16E2EE558800
   Functions: 9
-  Symbols:   72
+  Symbols:   71
   CStrings:  39
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
Functions:
~ -[PSTableCellAccessibility__DNDSettings__Preferences accessibilityTraits] : 156 -> 160
~ _accessibilityLocalizedString : 176 -> 184
~ +[AXDoNotDisturbSettingsGlue accessibilityInitializeBundle] : 100 -> 104
~ ___59+[AXDoNotDisturbSettingsGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100

```
