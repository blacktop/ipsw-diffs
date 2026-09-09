## DumpPanic

> `/usr/libexec/DumpPanic`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__constg_swiftt`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA.__objc_data`

```diff

 37.0.1.0.0
-  __TEXT.__text: 0x2b414
+  __TEXT.__text: 0x2b410
   __TEXT.__auth_stubs: 0x1180
   __TEXT.__objc_stubs: 0x2660
   __TEXT.__objc_methlist: 0x8bc

   __TEXT.__swift5_reflstr: 0x27
   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x8e8
+  __TEXT.__unwind_info: 0x8f0
   __TEXT.__eh_frame: 0xa0
   __DATA_CONST.__const: 0x778
   __DATA_CONST.__cfstring: 0x2400

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 870
+  Functions: 871
   Symbols:   400
   CStrings:  1340
 
```
