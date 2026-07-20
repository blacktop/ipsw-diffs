## ValidUpdater

> `/usr/libexec/ValidUpdater`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-134.0.15.0.0
-  __TEXT.__text: 0x6a98
-  __TEXT.__auth_stubs: 0x6f0
+134.0.18.0.0
+  __TEXT.__text: 0x6b08
+  __TEXT.__auth_stubs: 0x700
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x104
   __TEXT.__const: 0x1d4

   __TEXT.__constg_swiftt: 0x74
   __TEXT.__swift5_fieldmd: 0x2c
   __TEXT.__objc_methtype: 0xdd
-  __TEXT.__oslogstring: 0x210
+  __TEXT.__oslogstring: 0x200
   __TEXT.__cstring: 0x107
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_reflstr: 0x9

   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__auth_got: 0x380
+  __DATA_CONST.__auth_got: 0x388
   __DATA_CONST.__got: 0x100
   __DATA_CONST.__auth_ptr: 0x48
   __DATA.__objc_const: 0x190

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 132
-  Symbols:   163
+  Symbols:   164
   CStrings:  75
 
Symbols:
+ _$s11SwiftCRLite15ValidDaemonCoreC19getUpdateBackgroundSbyFZ
Functions:
~ sub_100002b5c : 1240 -> 1308
~ sub_10000347c -> sub_1000034c0 : 1292 -> 1312
~ sub_100003d3c -> sub_100003d94 : 540 -> 564
CStrings:
+ "setDownloadInitialDatabaseTask: skipping — background updates disabled"
+ "validDownload initial: skipping — background updates disabled"
+ "validDownload: skipping — background updates disabled"
- "setDownloadInitialDatabaseTask: skipping — disable_background_updates is set"
- "validDownload initial: skipping — disable_background_updates is set"
- "validDownload: skipping — disable_background_updates is set"
```
