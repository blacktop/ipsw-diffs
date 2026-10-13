## ANEStorageMaintainer

> `System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANEStorageMaintainer.xpc/ANEStorageMaintainer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-382.101.0.0.0
-  __TEXT.__text: 0x85dc
-  __TEXT.__auth_stubs: 0x590
+382.101.2.0.0
+  __TEXT.__text: 0x7e54
+  __TEXT.__auth_stubs: 0x550
   __TEXT.__objc_stubs: 0xfa0
   __TEXT.__objc_methlist: 0x3dc
-  __TEXT.__const: 0xd0
-  __TEXT.__oslogstring: 0x107a
+  __TEXT.__const: 0xc8
+  __TEXT.__oslogstring: 0xfec
   __TEXT.__objc_classname: 0x86
   __TEXT.__objc_methname: 0x1075
   __TEXT.__objc_methtype: 0x26b
-  __TEXT.__gcc_except_tab: 0x168
-  __TEXT.__cstring: 0x1ee
-  __TEXT.__unwind_info: 0x210
-  __DATA_CONST.__const: 0x118
+  __TEXT.__cstring: 0x1d0
+  __TEXT.__unwind_info: 0x1f0
+  __DATA_CONST.__const: 0xc8
   __DATA_CONST.__cfstring: 0x320
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x2d8
+  __DATA_CONST.__auth_got: 0x2b0
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x450

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 115
-  Symbols:   405
-  CStrings:  343
+  Functions: 112
+  Symbols:   393
+  CStrings:  338
 
Symbols:
- GCC_except_table11
- GCC_except_table6
- __43+[_ANEStorageHelper memoryMapWeightAtPath:]_block_invoke
- __72+[_ANEStorageHelper memoryMapModelAtPath:isPrecompiled:modelAttributes:]_block_invoke
- __Unwind_Resume
- ___block_descriptor_192_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___objc_personality_v0
- __gAsyncIOq
- _dispatch_async
- _dispatch_queue_attr_make_with_autorelease_frequency
- _fcntl
CStrings:
- "%@: fcntl(F_RDADVISE). errno=%d : %s"
- "_ANED_MODEL_READ_ADVISE"
- "_ANED_WEIGHT_READ_ADVISE"
- "com.apple.aned.storageAsyncIO"
- "size=%d\n %{public, signpost.description:begin_time}llu "
```
