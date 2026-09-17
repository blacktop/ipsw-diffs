## syspolicy_check

> `/usr/bin/syspolicy_check`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_entry`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dupclass`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-823.1.1.0.0
-  __TEXT.__text: 0x15a18
+823.40.10.0.0
+  __TEXT.__text: 0x15b38
   __TEXT.__auth_stubs: 0xd60
-  __TEXT.__objc_stubs: 0x1260
+  __TEXT.__objc_stubs: 0x12a0
   __TEXT.__objc_methlist: 0x6e4
   __TEXT.__const: 0xae2
   __TEXT.__cstring: 0x45f6
   __TEXT.__oslogstring: 0xabe
   __TEXT.__gcc_except_tab: 0x2b4
-  __TEXT.__objc_methname: 0x1931
+  __TEXT.__objc_methname: 0x1961
   __TEXT.__objc_classname: 0x9a
   __TEXT.__objc_methtype: 0x241
   __TEXT.__swift5_typeref: 0x1fe

   __DATA_CONST.__got: 0x370
   __DATA_CONST.__auth_ptr: 0x188
   __DATA.__objc_const: 0x1370
-  __DATA.__objc_selrefs: 0x6d8
+  __DATA.__objc_selrefs: 0x6e8
   __DATA.__objc_ivar: 0x12c
   __DATA.__objc_data: 0x430
   __DATA.__data: 0x320

   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 484
+  Functions: 485
   Symbols:   405
-  CStrings:  809
+  CStrings:  811
 
CStrings:
+ "URLByStandardizingPath"
+ "pathComponents"
```
