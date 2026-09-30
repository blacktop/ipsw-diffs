## Siri

> `/System/Library/DataClassMigrators/Siri.migrator/Siri`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-3600.68.45.0.0
-  __TEXT.__text: 0x3c1c
-  __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x1a8
+3600.68.61.11.1
+  __TEXT.__text: 0x3d14
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_stubs: 0xb80
+  __TEXT.__objc_methlist: 0x1b4
   __TEXT.__const: 0x34
-  __TEXT.__cstring: 0x861
-  __TEXT.__oslogstring: 0x966
+  __TEXT.__cstring: 0x894
+  __TEXT.__oslogstring: 0x987
   __TEXT.__objc_classname: 0xd
-  __TEXT.__objc_methname: 0x940
+  __TEXT.__objc_methname: 0x963
   __TEXT.__objc_methtype: 0x39
   __TEXT.__unwind_info: 0xd0
   __DATA_CONST.__const: 0x10
-  __DATA_CONST.__cfstring: 0x600
+  __DATA_CONST.__cfstring: 0x640
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__auth_got: 0x230
   __DATA_CONST.__got: 0x130
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0x300
+  __DATA.__objc_selrefs: 0x308
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 37
-  Symbols:   120
-  CStrings:  222
+  Functions: 38
+  Symbols:   119
+  CStrings:  225
 
Symbols:
+ _objc_retain_x25
- _objc_release_x26
- _objc_release_x27
Functions:
~ sub_3aa8 : 1936 -> 2076
+ sub_43d4
CStrings:
+ "%s Failed to set TCC denial for bundle %@. [sources: LFTA=%@, ShowContent=%@, ShowApp=%@, Locked=%@]"
+ "%s Marked %@ as denied in kTCCServiceSiriAccess. [sources: LFTA=%@, ShowContent=%@, ShowApp=%@, Locked=%@]"
+ "%s Source counts — LFTA-off: %lu, Show-Content-off: %lu, Show-App-off: %lu, Locked: %lu, Hidden (excluded): %lu, union to migrate: %lu."
+ "SiriCanLearnFromAppBlacklist"
+ "_bundleIdsWithLearnFromAppDisabled"
+ "com.apple.suggestions"
- "%s Failed to set TCC denial for bundle %@. [sources: ShowContent=%@, ShowApp=%@, Locked=%@]"
- "%s Marked %@ as denied in kTCCServiceSiriAccess. [sources: ShowContent=%@, ShowApp=%@, Locked=%@]"
- "%s Source counts — Show-Content-off: %lu, Show-App-off: %lu, Locked: %lu, Hidden (excluded): %lu, union to migrate: %lu."
```
