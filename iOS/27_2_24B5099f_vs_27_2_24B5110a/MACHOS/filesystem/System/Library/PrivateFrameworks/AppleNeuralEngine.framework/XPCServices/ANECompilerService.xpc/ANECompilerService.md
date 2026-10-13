## ANECompilerService

> `System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANECompilerService.xpc/ANECompilerService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
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
-  __TEXT.__text: 0x198fc
-  __TEXT.__auth_stubs: 0x8a0
+382.101.2.0.0
+  __TEXT.__text: 0x191a4
+  __TEXT.__auth_stubs: 0x890
   __TEXT.__objc_stubs: 0x2280
   __TEXT.__objc_methlist: 0x9ac
   __TEXT.__const: 0x118
-  __TEXT.__cstring: 0x1303
-  __TEXT.__oslogstring: 0x25e2
+  __TEXT.__cstring: 0x12e5
+  __TEXT.__oslogstring: 0x2554
   __TEXT.__objc_classname: 0x19e
   __TEXT.__objc_methname: 0x25fa
   __TEXT.__objc_methtype: 0x67b
-  __TEXT.__gcc_except_tab: 0x1288
-  __TEXT.__unwind_info: 0x570
-  __DATA_CONST.__const: 0x348
+  __TEXT.__gcc_except_tab: 0x1120
+  __TEXT.__unwind_info: 0x558
+  __DATA_CONST.__const: 0x2f8
   __DATA_CONST.__cfstring: 0x1940
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__auth_got: 0x468
+  __DATA_CONST.__auth_got: 0x460
   __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0xd48

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 314
-  Symbols:   968
-  CStrings:  882
+  Functions: 313
+  Symbols:   963
+  CStrings:  877
 
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
