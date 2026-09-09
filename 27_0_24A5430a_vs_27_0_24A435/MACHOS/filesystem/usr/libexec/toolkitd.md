## toolkitd

> `/usr/libexec/toolkitd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 5037.109.0.0.0
-  __TEXT.__text: 0xa3198
+  __TEXT.__text: 0xa3138
   __TEXT.__auth_stubs: 0x2e10
   __TEXT.__objc_stubs: 0x1880
   __TEXT.__objc_methlist: 0x13c

   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_protos: 0x2c
   __TEXT.__swift5_mpenum: 0xc8
-  __TEXT.__unwind_info: 0x1f10
-  __TEXT.__eh_frame: 0x5f28
+  __TEXT.__unwind_info: 0x1f20
+  __TEXT.__eh_frame: 0x5f48
   __DATA_CONST.__const: 0x4480
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2977
+  Functions: 2985
   Symbols:   1277
   CStrings:  580
 
```
