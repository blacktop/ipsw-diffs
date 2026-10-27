## kernelmanagerd

> `/usr/libexec/kernelmanagerd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_typeref`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__cstring`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-514.0.2.0.0
-  __TEXT.__text: 0x133760
+514.40.8.0.0
+  __TEXT.__text: 0x133908
   __TEXT.__auth_stubs: 0x3370
   __TEXT.__objc_stubs: 0x1600
   __TEXT.__objc_methlist: 0x8e8

   __TEXT.__swift5_mpenum: 0x64
   __TEXT.__oslogstring: 0xd40
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x6918
-  __TEXT.__eh_frame: 0x9278
+  __TEXT.__unwind_info: 0x6970
+  __TEXT.__eh_frame: 0x9338
   __DATA_CONST.__const: 0xd4d8
   __DATA_CONST.__cfstring: 0x420
   __DATA_CONST.__objc_classlist: 0x2a8

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9543
+  Functions: 9554
   Symbols:   1208
   CStrings:  2432
 
CStrings:
+ "KernelManagement_executables-514.40.8"
- "KernelManagement_executables-514.0.2"
```
