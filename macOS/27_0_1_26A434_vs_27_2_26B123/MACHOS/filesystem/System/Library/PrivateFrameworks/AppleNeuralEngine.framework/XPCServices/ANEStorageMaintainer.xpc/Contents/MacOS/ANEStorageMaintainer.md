## ANEStorageMaintainer

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANEStorageMaintainer.xpc/Contents/MacOS/ANEStorageMaintainer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-382.15.1.0.0
-  __TEXT.__text: 0x8e94
-  __TEXT.__auth_stubs: 0x3f0
+382.101.2.0.0
+  __TEXT.__text: 0x8984
+  __TEXT.__auth_stubs: 0x3c0
   __TEXT.__objc_stubs: 0xfa0
   __TEXT.__objc_methlist: 0x3e4
   __TEXT.__const: 0xd0
-  __TEXT.__oslogstring: 0x103c
+  __TEXT.__oslogstring: 0x101f
   __TEXT.__objc_classname: 0x86
   __TEXT.__objc_methname: 0x1094
   __TEXT.__objc_methtype: 0x276
-  __TEXT.__gcc_except_tab: 0x154
-  __TEXT.__cstring: 0x1ee
-  __TEXT.__unwind_info: 0x220
-  __DATA_CONST.__const: 0x130
+  __TEXT.__cstring: 0x1d0
+  __TEXT.__unwind_info: 0x200
+  __DATA_CONST.__const: 0xd0
   __DATA_CONST.__cfstring: 0x320
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x18

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x208
+  __DATA_CONST.__auth_got: 0x1e8
   __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x450
   __DATA.__objc_selrefs: 0x528
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x130
-  __DATA.__bss: 0x38
+  __DATA.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOSurface.framework/Versions/A/IOSurface

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 116
-  Symbols:   382
-  CStrings:  344
+  Functions: 113
+  Symbols:   371
+  CStrings:  341
 
Symbols:
+ __ANEStorageProbeFileIsReadable
+ ___chkstk_darwin
+ _pread
- GCC_except_table12
- GCC_except_table6
- __43+[_ANEStorageHelper memoryMapWeightAtPath:]_block_invoke
- __72+[_ANEStorageHelper memoryMapModelAtPath:isPrecompiled:modelAttributes:]_block_invoke
- __Unwind_Resume
- ___block_descriptor_192_e8_32r_e5_v8?0l
- ___block_descriptor_40_e8_32r_e5_v8?0l
- ___copy_helper_block_e8_32r
- ___destroy_helper_block_e8_32r
- ___objc_personality_v0
- __gAsyncIOq
- _dispatch_async
- _dispatch_queue_attr_make_with_autorelease_frequency
- _fcntl
CStrings:
+ "%@: %@ failed readability probe. Returning nil"
+ "%@: pread(%@, offset=%zu, want=%zu) failed. got=%zd errno=%d : %s"
- "%@: fcntl(F_RDADVISE). errno=%d : %s"
- "_ANED_MODEL_READ_ADVISE"
- "_ANED_WEIGHT_READ_ADVISE"
- "com.apple.aned.storageAsyncIO"
- "size=%d\n %{public, signpost.description:begin_time}llu "
```
