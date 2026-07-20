## tccd

> `/System/Library/PrivateFrameworks/TCC.framework/Support/tccd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-909.0.0.0.0
-  __TEXT.__text: 0x85664
-  __TEXT.__auth_stubs: 0x1650
+910.0.0.0.0
+  __TEXT.__text: 0x85964
+  __TEXT.__auth_stubs: 0x1660
   __TEXT.__objc_stubs: 0xb1c0
   __TEXT.__objc_methlist: 0x52f4
-  __TEXT.__cstring: 0x120b3
+  __TEXT.__cstring: 0x120c4
   __TEXT.__const: 0x6f8
-  __TEXT.__gcc_except_tab: 0x2d88
+  __TEXT.__gcc_except_tab: 0x2d8c
   __TEXT.__objc_methname: 0x12795
-  __TEXT.__oslogstring: 0xf36a
+  __TEXT.__oslogstring: 0xf4f1
   __TEXT.__objc_classname: 0x6ce
   __TEXT.__objc_methtype: 0x22f6
   __TEXT.__dlopen_cstrs: 0x90
-  __TEXT.__unwind_info: 0x1940
-  __DATA_CONST.__const: 0x2788
+  __TEXT.__unwind_info: 0x1958
+  __DATA_CONST.__const: 0x27c8
   __DATA_CONST.__cfstring: 0x8940
   __DATA_CONST.__objc_classlist: 0x1f0
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_arraydata: 0x1620
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA_CONST.__objc_dictobj: 0xeb0
-  __DATA_CONST.__auth_got: 0xb38
+  __DATA_CONST.__auth_got: 0xb40
   __DATA_CONST.__got: 0x4a8
   __DATA_CONST.__auth_ptr: 0x38
   __DATA.__objc_const: 0xa1b0

   __DATA.__objc_ivar: 0x708
   __DATA.__objc_data: 0x1360
   __DATA.__data: 0x730
-  __DATA.__bss: 0x439
-  __DATA.__common: 0x20
+  __DATA.__bss: 0x431
+  __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2918
-  Symbols:   505
-  CStrings:  5737
+  Functions: 2924
+  Symbols:   506
+  CStrings:  5741
 
Symbols:
+ __exit
CStrings:
+ "AppleLanguagePreferencesChangedNotification"
+ "Force-exiting tccd: language change drain exceeded grace period."
+ "Handling language change (AppleLanguagePreferencesChangedNotification)..."
+ "Initiating language-change shutdown."
+ "ManagedSettings: ignoring Location profile update for %{private}@ - disclosure already acknowledged, managed_overrides record preserved"
+ "tccd_replica_sync_update_from_ManagedOverrideAction: unknown service %{public}@; cannot notify/kill client"
- "Handling language change..."
- "com.apple.language.changed"
```
