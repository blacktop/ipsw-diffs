## aned

> `usr/libexec/aned`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-382.101.0.0.0
-  __TEXT.__text: 0x7ca48
-  __TEXT.__auth_stubs: 0xf90
+382.101.2.0.0
+  __TEXT.__text: 0x7c300
+  __TEXT.__auth_stubs: 0xf80
   __TEXT.__objc_stubs: 0x3480
   __TEXT.__objc_methlist: 0x117c
   __TEXT.__const: 0x60ec
-  __TEXT.__gcc_except_tab: 0x61b4
-  __TEXT.__cstring: 0x5cfc
-  __TEXT.__oslogstring: 0x6d61
+  __TEXT.__gcc_except_tab: 0x604c
+  __TEXT.__cstring: 0x5cde
+  __TEXT.__oslogstring: 0x6cd3
   __TEXT.__objc_classname: 0x247
   __TEXT.__objc_methname: 0x3e6b
   __TEXT.__objc_methtype: 0xeaf
-  __TEXT.__unwind_info: 0x2c60
-  __DATA_CONST.__const: 0x2b68
+  __TEXT.__unwind_info: 0x2c40
+  __DATA_CONST.__const: 0x2b18
   __DATA_CONST.__cfstring: 0xb00
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x60

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x7e0
+  __DATA_CONST.__auth_got: 0x7d8
   __DATA_CONST.__got: 0x3c8
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x1c98

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 2789
-  Symbols:   4178
-  CStrings:  1757
+  Symbols:   4173
+  CStrings:  1752
 
Symbols:
- __43+[_ANEStorageHelper memoryMapWeightAtPath:]_block_invoke
- __72+[_ANEStorageHelper memoryMapModelAtPath:isPrecompiled:modelAttributes:]_block_invoke
- ___block_descriptor_192_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- _fcntl
CStrings:
- "%@: fcntl(F_RDADVISE). errno=%d : %s"
- "_ANED_MODEL_READ_ADVISE"
- "_ANED_WEIGHT_READ_ADVISE"
- "com.apple.aned.storageAsyncIO"
- "size=%d\n %{public, signpost.description:begin_time}llu "
```
