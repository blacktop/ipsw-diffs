## metalperftrace

> `/usr/bin/metalperftrace`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_assocty`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`

```diff

-5.0.24.0.0
-  __TEXT.__text: 0x38460
+5.0.26.0.0
+  __TEXT.__text: 0x3944c
   __TEXT.__auth_stubs: 0x1110
   __TEXT.__objc_stubs: 0x15e0
   __TEXT.__objc_methlist: 0x1b4

   __TEXT.__cstring: 0x3084
   __TEXT.__objc_classname: 0xb6
   __TEXT.__objc_methtype: 0x247
-  __TEXT.__swift5_typeref: 0xaf0
-  __TEXT.__swift5_capture: 0x390
+  __TEXT.__swift5_typeref: 0xb0c
+  __TEXT.__swift5_capture: 0x3b4
   __TEXT.__constg_swiftt: 0x320
   __TEXT.__swift5_reflstr: 0x4c3
   __TEXT.__swift5_fieldmd: 0x624

   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__unwind_info: 0x950
+  __TEXT.__unwind_info: 0x958
   __TEXT.__eh_frame: 0xd20
   __DATA_CONST.__const: 0x1450
   __DATA_CONST.__cfstring: 0x240

   __DATA.__objc_selrefs: 0x5c0
   __DATA.__objc_ivar: 0x30
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x720
+  __DATA.__data: 0x728
   __DATA.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 623
+  Functions: 627
   Symbols:   422
   CStrings:  442
 
```
