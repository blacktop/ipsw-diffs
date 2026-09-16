## DumpPanic

> `/usr/libexec/DumpPanic`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
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
-  __TEXT.__text: 0x2ae94
+41.40.5.0.0
+  __TEXT.__text: 0x2af20
   __TEXT.__auth_stubs: 0x1180
   __TEXT.__objc_stubs: 0x2660
   __TEXT.__objc_methlist: 0x8bc

   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0xd80
   __TEXT.__eh_frame: 0xa0
-  __DATA_CONST.__const: 0x778
+  __DATA_CONST.__const: 0x780
   __DATA_CONST.__cfstring: 0x2400
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 871
+  Functions: 870
   Symbols:   400
   CStrings:  1340
 
```
