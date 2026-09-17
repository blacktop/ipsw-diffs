## DumpPanic

> `/usr/libexec/DumpPanic`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-37.0.1.0.0
-  __TEXT.__text: 0x2db3c
+41.40.5.0.0
+  __TEXT.__text: 0x2dbc8
   __TEXT.__auth_stubs: 0xff0
   __TEXT.__objc_stubs: 0x2600
   __TEXT.__objc_methlist: 0x8f4

   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0xde8
   __TEXT.__eh_frame: 0xa0
-  __DATA_CONST.__const: 0x7c8
+  __DATA_CONST.__const: 0x7d8
   __DATA_CONST.__cfstring: 0x22c0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 906
+  Functions: 905
   Symbols:   370
   CStrings:  1370
 
```
