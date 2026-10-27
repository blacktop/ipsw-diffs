## kmutil

> `/usr/bin/kmutil`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__cstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-514.0.2.0.0
-  __TEXT.__text: 0x151b20
+514.40.8.0.0
+  __TEXT.__text: 0x151cc8
   __TEXT.__auth_stubs: 0x37a0
   __TEXT.__objc_stubs: 0x1200
   __TEXT.__objc_methlist: 0x274

   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__unwind_info: 0x8928
-  __TEXT.__eh_frame: 0xd7bc
+  __TEXT.__unwind_info: 0x8960
+  __TEXT.__eh_frame: 0xd864
   __DATA_CONST.__const: 0xd9c0
   __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x268

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 10698
+  Functions: 10705
   Symbols:   1281
   CStrings:  2171
 
CStrings:
+ "KernelManagement_executables-514.40.8"
+ "kmutil: KernelManagement Utility (KernelManagement_executables-514.40.8)"
- "KernelManagement_executables-514.0.2"
- "kmutil: KernelManagement Utility (KernelManagement_executables-514.0.2)"
```
