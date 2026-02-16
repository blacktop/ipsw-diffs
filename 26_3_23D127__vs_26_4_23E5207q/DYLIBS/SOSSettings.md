## SOSSettings

> `/System/Library/AccessibilityBundles/SOSSettings.axbundle/SOSSettings`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x1f8
-  __TEXT.__auth_stubs: 0xa0
+3005.16.0.0.0
+  __TEXT.__text: 0x208
+  __TEXT.__auth_stubs: 0x90
   __TEXT.__objc_methlist: 0x68
   __TEXT.__cstring: 0xb5
   __TEXT.__unwind_info: 0x70

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x58
+  __AUTH_CONST.__auth_got: 0x50
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xe0
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C4A1DFF8-E979-31A6-9001-6AB633191CC3
+  UUID: 6B26D9F7-3190-36DF-A48F-41BC4C2EBB28
   Functions: 10
-  Symbols:   71
+  Symbols:   70
   CStrings:  39
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
Functions:
~ +[AXSOSSettingsGlue accessibilityInitializeBundle] : 148 -> 152
~ ___50+[AXSOSSettingsGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184

```
