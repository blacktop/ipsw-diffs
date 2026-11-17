## kbd

> `/System/Library/TextInput/kbd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3568.2.4.0.0
-  __TEXT.__text: 0x14604
+3568.2.8.0.0
+  __TEXT.__text: 0x14428
   __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_stubs: 0x2a40
-  __TEXT.__objc_methlist: 0x142c
+  __TEXT.__objc_stubs: 0x29c0
+  __TEXT.__objc_methlist: 0x1414
   __TEXT.__const: 0x316
   __TEXT.__objc_classname: 0x5fa
-  __TEXT.__objc_methname: 0x368d
+  __TEXT.__objc_methname: 0x364d
   __TEXT.__objc_methtype: 0x1350
-  __TEXT.__cstring: 0x1aa7
-  __TEXT.__oslogstring: 0xcf2
+  __TEXT.__cstring: 0x1a67
+  __TEXT.__oslogstring: 0xcc2
   __TEXT.__dlopen_cstrs: 0x22c
   __TEXT.__constg_swiftt: 0x110
   __TEXT.__swift5_typeref: 0x11e

   __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift_as_cont: 0x64
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x858
+  __TEXT.__unwind_info: 0x850
   __TEXT.__eh_frame: 0x520
   __DATA_CONST.__const: 0x950
-  __DATA_CONST.__cfstring: 0xb60
+  __DATA_CONST.__cfstring: 0xb40
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__auth_got: 0x708
-  __DATA_CONST.__got: 0x460
+  __DATA_CONST.__got: 0x458
   __DATA_CONST.__auth_ptr: 0xb0
   __DATA.__objc_const: 0x4c28
-  __DATA.__objc_selrefs: 0xeb0
+  __DATA.__objc_selrefs: 0xe90
   __DATA.__objc_ivar: 0xc0
   __DATA.__objc_data: 0x888
   __DATA.__data: 0xda8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 546
-  Symbols:   415
-  CStrings:  1012
+  Functions: 543
+  Symbols:   414
+  CStrings:  1005
 
Symbols:
+ _TI_CREATE_TEMPORARY_KB_USER_DIRECTORY
- _NSTemporaryDirectory
- _OBJC_CLASS_$_NSUUID
CStrings:
- "%s  Failed to create temporary directory: %@"
- "+[TIUserDirectoryTrader createDirectoryAtPath:]"
- "TempUserDir-%@"
- "UUID"
- "UUIDString"
- "createDirectoryAtPath:"
- "createTemporaryDirectory"
```
