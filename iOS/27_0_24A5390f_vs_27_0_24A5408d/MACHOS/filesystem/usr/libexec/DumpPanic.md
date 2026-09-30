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
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-37.0.0.0.0
-  __TEXT.__text: 0x2b194
+37.0.1.0.0
+  __TEXT.__text: 0x2b414
   __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_stubs: 0x2640
+  __TEXT.__objc_stubs: 0x2660
   __TEXT.__objc_methlist: 0x8bc
   __TEXT.__cstring: 0x2b8b
   __TEXT.__objc_classname: 0x12c
   __TEXT.__objc_methtype: 0x546
-  __TEXT.__objc_methname: 0x1fc4
+  __TEXT.__objc_methname: 0x1fdb
   __TEXT.__const: 0x2e0
-  __TEXT.__gcc_except_tab: 0xbb8
-  __TEXT.__oslogstring: 0x48d8
+  __TEXT.__gcc_except_tab: 0xbdc
+  __TEXT.__oslogstring: 0x49a8
   __TEXT.__ustring: 0x1c6
   __TEXT.__constg_swiftt: 0x90
   __TEXT.__swift5_typeref: 0x8b
   __TEXT.__swift5_reflstr: 0x27
   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x8d0
+  __TEXT.__unwind_info: 0x8e8
   __TEXT.__eh_frame: 0xa0
   __DATA_CONST.__const: 0x778
   __DATA_CONST.__cfstring: 0x2400

   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__auth_got: 0x8d8
-  __DATA_CONST.__got: 0x2a8
+  __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__auth_ptr: 0x78
   __DATA.__objc_const: 0x10e0
-  __DATA.__objc_selrefs: 0xb00
+  __DATA.__objc_selrefs: 0xb08
   __DATA.__objc_ivar: 0xa0
   __DATA.__objc_data: 0x528
   __DATA.__data: 0x3b8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 863
+  Functions: 870
   Symbols:   400
-  CStrings:  1334
+  CStrings:  1340
 
CStrings:
+ "Empty RTKit crashlog data"
+ "Failed to encode RTKit crashlog data to base64"
+ "Failed to process RTKit crashlog data"
+ "Invalid parameters for RTKit crashlog processing"
+ "Successfully processed RTKit crashlog data (%zu bytes)"
+ "useCrashlogContainers:"
```
