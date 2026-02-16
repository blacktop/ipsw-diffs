## ActiveSyncSettings

> `/System/Library/AccessibilityBundles/ActiveSyncSettings.axbundle/ActiveSyncSettings`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x224
-  __TEXT.__auth_stubs: 0xb0
+3005.16.0.0.0
+  __TEXT.__text: 0x234
+  __TEXT.__auth_stubs: 0xa0
   __TEXT.__objc_methlist: 0x5c
   __TEXT.__cstring: 0xab
   __TEXT.__unwind_info: 0x78

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x70
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x60
+  __AUTH_CONST.__auth_got: 0x58
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0x1b0

   - /usr/lib/libAXSafeCategoryBundle.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 12A9E8FB-89AB-3BC1-809A-2E0B5193BB01
+  UUID: 98FF10C0-94B5-3005-92FB-AE705AC7A869
   Functions: 9
-  Symbols:   70
+  Symbols:   69
   CStrings:  36
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
Functions:
~ +[AXActiveSyncSettingsGlue accessibilityInitializeBundle] : 148 -> 152
~ ___57+[AXActiveSyncSettingsGlue accessibilityInitializeBundle]_block_invoke_2 : 96 -> 100
~ _accessibilityLocalizedString : 176 -> 184

```
