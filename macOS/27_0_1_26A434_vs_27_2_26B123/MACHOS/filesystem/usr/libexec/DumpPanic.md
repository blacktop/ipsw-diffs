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
+41.40.7.0.0
+  __TEXT.__text: 0x2dcc8
   __TEXT.__auth_stubs: 0xff0
   __TEXT.__objc_stubs: 0x2600
   __TEXT.__objc_methlist: 0x8f4

   __TEXT.__objc_classname: 0x12c
   __TEXT.__objc_methtype: 0x56b
   __TEXT.__objc_methname: 0x205a
-  __TEXT.__const: 0x2d0
+  __TEXT.__const: 0x2e0
   __TEXT.__gcc_except_tab: 0xc78
-  __TEXT.__oslogstring: 0x5008
+  __TEXT.__oslogstring: 0x5058
   __TEXT.__constg_swiftt: 0x90
   __TEXT.__swift5_typeref: 0x8b
   __TEXT.__swift5_reflstr: 0x27

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
-  CStrings:  1370
+  CStrings:  1372
 
CStrings:
+ "failed to fchmod file at path %s to mode 0666 with error : %s"
+ "fd identity mismatch for %s — possible TOCTOU, skipping"
+ "lstat failed for %s: %s"
+ "refusing to chown/chmod suspect file %s (uid=%u nlink=%u mode=0%o)"
- "failed to fchmod group for file at path %s to %d with error : %s"
- "skipping fchmod/fchown for suspect file at path : %s"
```
