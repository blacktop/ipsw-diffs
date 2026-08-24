## DumpPanic

> `/usr/libexec/DumpPanic`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-37.0.0.0.0
-  __TEXT.__text: 0x2e07c
+37.0.1.0.0
+  __TEXT.__text: 0x2e0fc
   __TEXT.__auth_stubs: 0xff0
-  __TEXT.__objc_stubs: 0x25e0
+  __TEXT.__objc_stubs: 0x2600
   __TEXT.__objc_methlist: 0x8f4
   __TEXT.__cstring: 0x2b9b
   __TEXT.__objc_classname: 0x12c
   __TEXT.__objc_methtype: 0x56b
-  __TEXT.__objc_methname: 0x2043
+  __TEXT.__objc_methname: 0x205a
   __TEXT.__const: 0x2d0
-  __TEXT.__gcc_except_tab: 0xc54
+  __TEXT.__gcc_except_tab: 0xc78
   __TEXT.__oslogstring: 0x5008
   __TEXT.__constg_swiftt: 0x90
   __TEXT.__swift5_typeref: 0x8b
   __TEXT.__swift5_reflstr: 0x27
   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x8f8
+  __TEXT.__unwind_info: 0x900
   __TEXT.__eh_frame: 0xa0
   __DATA_CONST.__const: 0x7c8
   __DATA_CONST.__cfstring: 0x22c0

   __DATA_CONST.__got: 0x278
   __DATA_CONST.__auth_ptr: 0x68
   __DATA.__objc_const: 0x1110
-  __DATA.__objc_selrefs: 0xaf0
+  __DATA.__objc_selrefs: 0xaf8
   __DATA.__objc_ivar: 0xa4
   __DATA.__objc_data: 0x528
   __DATA.__data: 0x3d8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 904
+  Functions: 905
   Symbols:   370
-  CStrings:  1369
+  CStrings:  1370
 
CStrings:
+ "useCrashlogContainers:"
```
