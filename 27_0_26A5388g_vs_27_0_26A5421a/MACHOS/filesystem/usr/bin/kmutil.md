## kmutil

> `/usr/bin/kmutil`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-514.0.0.0.0
-  __TEXT.__text: 0x15afec
+514.0.2.0.0
+  __TEXT.__text: 0x15ab58
   __TEXT.__auth_stubs: 0x37a0
   __TEXT.__objc_stubs: 0x1200
   __TEXT.__objc_methlist: 0x274
   __TEXT.__const: 0x17c89
   __TEXT.__gcc_except_tab: 0x5168
   __TEXT.__swift5_typeref: 0x4a90
-  __TEXT.__cstring: 0x13525
+  __TEXT.__cstring: 0x13512
   __TEXT.__swift5_capture: 0x8ac
   __TEXT.__constg_swiftt: 0x58fc
   __TEXT.__swift5_reflstr: 0x3863

   __TEXT.__objc_classname: 0xc6c
   __TEXT.__swift5_protos: 0xd8
   __TEXT.__objc_methname: 0x1b0a
-  __TEXT.__oslogstring: 0x982
+  __TEXT.__oslogstring: 0x998
   __TEXT.__objc_methtype: 0x6a7
   __TEXT.__swift5_mpenum: 0x64
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__unwind_info: 0x7368
+  __TEXT.__unwind_info: 0x7370
   __TEXT.__eh_frame: 0xd754
   __DATA_CONST.__const: 0xd9a0
   __DATA_CONST.__cfstring: 0x280

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 10676
+  Functions: 10673
   Symbols:   1280
-  CStrings:  2171
+  CStrings:  2170
 
CStrings:
+ "KernelManagement_executables-514.0.2"
+ "disk is vitual ?: %d\n"
+ "kmutil: KernelManagement Utility (KernelManagement_executables-514.0.2)"
- "KernelManagement_executables-514"
- "PATH_KEY_POLICY_PATH"
- "PATH_KEY_PREBOOT_FD"
- "kmutil: KernelManagement Utility (KernelManagement_executables-514)"
```
