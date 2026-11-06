## tipsd

> `/usr/libexec/tipsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-866.0.0.0.0
-  __TEXT.__text: 0x17c3c
-  __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_stubs: 0x2ca0
+866.2.4.0.0
+  __TEXT.__text: 0x17d10
+  __TEXT.__auth_stubs: 0xad0
+  __TEXT.__objc_stubs: 0x2cc0
   __TEXT.__objc_methlist: 0xd18
-  __TEXT.__const: 0x36e
+  __TEXT.__const: 0x376
   __TEXT.__gcc_except_tab: 0x498
   __TEXT.__cstring: 0xccc
-  __TEXT.__objc_methname: 0x3655
+  __TEXT.__objc_methname: 0x366c
   __TEXT.__oslogstring: 0x177e
   __TEXT.__objc_classname: 0x225
   __TEXT.__objc_methtype: 0x1139

   __TEXT.__swift_as_entry: 0x38
   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0xac
-  __TEXT.__info_plist: 0x898
+  __TEXT.__info_plist: 0x89c
   __TEXT.__unwind_info: 0x858
   __TEXT.__eh_frame: 0xa20
   __DATA_CONST.__const: 0xd50

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__auth_got: 0x570
+  __DATA_CONST.__auth_got: 0x578
   __DATA_CONST.__got: 0x390
   __DATA_CONST.__auth_ptr: 0xd8
   __DATA.__objc_const: 0xc50
-  __DATA.__objc_selrefs: 0xe50
+  __DATA.__objc_selrefs: 0xe58
   __DATA.__objc_ivar: 0x68
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x650

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 505
-  Symbols:   346
-  CStrings:  892
+  Symbols:   347
+  CStrings:  893
 
Symbols:
+ _TPSHMManagerHomeAccessoryAddedNotificationString
Functions:
~ sub_1000051c0 : 688 -> 780
~ sub_100007bac -> sub_100007c08 : 100 -> 172
~ sub_100007c10 -> sub_100007cb4 : 64 -> 104
~ sub_10000c544 -> sub_10000c610 : 488 -> 496
CStrings:
+ "setRequestingBundleId:"
```
