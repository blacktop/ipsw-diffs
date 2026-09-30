## SpringBoardDisplayServices

> `/System/Library/PrivateFrameworks/SpringBoardDisplayServices.framework/SpringBoardDisplayServices`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH.__objc_data`
- `__AUTH.__data`

```diff

-39.0.0.0.0
-  __TEXT.__text: 0x3e74
+41.0.0.0.0
+  __TEXT.__text: 0x40a4
   __TEXT.__objc_methlist: 0xe0
   __TEXT.__const: 0x240
   __TEXT.__constg_swiftt: 0x140

   __TEXT.__swift5_types: 0x1c
   __TEXT.__cstring: 0x1a6
   __TEXT.__swift5_capture: 0xb0
-  __TEXT.__oslogstring: 0x3c
+  __TEXT.__oslogstring: 0x83
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_cont: 0x4
-  __TEXT.__unwind_info: 0x180
+  __TEXT.__unwind_info: 0x188
   __TEXT.__eh_frame: 0xe8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 109
+  Functions: 110
   Symbols:   247
-  CStrings:  11
+  CStrings:  12
 
CStrings:
+ "[rdar://180980793 HACK] overriding systemUISize 360x780 -> 375x812"
```
