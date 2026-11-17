## SidecarRelay

> `/usr/libexec/SidecarRelay`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__cstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-414.1.0.0.0
-  __TEXT.__text: 0x83c70
+414.2.0.0.0
+  __TEXT.__text: 0x83ff0
   __TEXT.__auth_stubs: 0x1ce0
   __TEXT.__objc_stubs: 0x1a60
   __TEXT.__objc_methlist: 0xb40

   __TEXT.__cstring: 0x14ed
   __TEXT.__oslogstring: 0x2602
   __TEXT.__swift5_capture: 0x3e64
-  __TEXT.__unwind_info: 0x2678
-  __TEXT.__eh_frame: 0x1068
+  __TEXT.__unwind_info: 0x2668
+  __TEXT.__eh_frame: 0x1048
   __DATA_CONST.__const: 0xc228
   __DATA_CONST.__cfstring: 0x60
   __DATA_CONST.__objc_classlist: 0x168

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4574
+  Functions: 4582
   Symbols:   773
   CStrings:  880
 
CStrings:
+ "414.2"
- "414.1"
```
