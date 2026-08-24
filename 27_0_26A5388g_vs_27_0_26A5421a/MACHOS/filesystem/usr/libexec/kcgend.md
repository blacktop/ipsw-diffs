## kcgend

> `/usr/libexec/kcgend`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_entry`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-514.0.0.0.0
-  __TEXT.__text: 0x7633c
+514.0.2.0.0
+  __TEXT.__text: 0x75e40
   __TEXT.__auth_stubs: 0x1fe0
   __TEXT.__objc_stubs: 0x8e0
   __TEXT.__objc_methlist: 0x418
   __TEXT.__const: 0xe1e1
-  __TEXT.__cstring: 0x7dfa
+  __TEXT.__cstring: 0x7de7
   __TEXT.__swift5_typeref: 0x2cc0
   __TEXT.__swift5_capture: 0x294
   __TEXT.__objc_methtype: 0x463

   __TEXT.__swift5_proto: 0xc74
   __TEXT.__swift5_types: 0x3e8
   __TEXT.__swift5_protos: 0xa0
-  __TEXT.__oslogstring: 0x89f
-  __TEXT.__unwind_info: 0x2690
+  __TEXT.__oslogstring: 0x8b5
+  __TEXT.__unwind_info: 0x2698
   __TEXT.__eh_frame: 0x2f48
   __DATA_CONST.__const: 0x7318
   __DATA_CONST.__cfstring: 0x280

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4179
+  Functions: 4175
   Symbols:   804
-  CStrings:  1116
+  CStrings:  1115
 
CStrings:
+ "disk is vitual ?: %d\n"
- "PATH_KEY_POLICY_PATH"
- "PATH_KEY_PREBOOT_FD"
```
