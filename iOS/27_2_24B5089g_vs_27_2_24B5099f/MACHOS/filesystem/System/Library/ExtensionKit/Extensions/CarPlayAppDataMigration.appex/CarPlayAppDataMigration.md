## CarPlayAppDataMigration

> `/System/Library/ExtensionKit/Extensions/CarPlayAppDataMigration.appex/CarPlayAppDataMigration`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-591.2.0.0.0
-  __TEXT.__text: 0x122bc
-  __TEXT.__auth_stubs: 0xb70
+591.6.0.0.0
+  __TEXT.__text: 0x122f4
+  __TEXT.__auth_stubs: 0xb80
   __TEXT.__objc_stubs: 0x600
   __TEXT.__objc_methlist: 0x184
   __TEXT.__const: 0x684

   __TEXT.__swift_as_ret: 0x44
   __TEXT.__swift_as_cont: 0x7c
   __TEXT.__unwind_info: 0x570
-  __TEXT.__eh_frame: 0xa90
+  __TEXT.__eh_frame: 0xab8
   __DATA_CONST.__const: 0x7f9
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0x5c0
+  __DATA_CONST.__auth_got: 0x5c8
   __DATA_CONST.__got: 0x168
   __DATA_CONST.__auth_ptr: 0x150
   __DATA.__objc_const: 0x5a8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 309
-  Symbols:   161
+  Symbols:   162
   CStrings:  141
 
Symbols:
+ _swift_release_x22
Functions:
~ sub_100002df4 : 32 -> 68
~ sub_100004528 -> sub_10000454c : 588 -> 592
~ sub_100004774 -> sub_10000479c : 588 -> 592
~ sub_1000062f4 -> sub_100006320 : 284 -> 296
```
