## aneuserd

> `/usr/libexec/aneuserd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`

```diff

-382.15.1.0.0
-  __TEXT.__text: 0x7ebf0
-  __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_stubs: 0x3660
-  __TEXT.__objc_methlist: 0x12cc
+382.101.2.0.0
+  __TEXT.__text: 0x7e780
+  __TEXT.__auth_stubs: 0xe10
+  __TEXT.__objc_stubs: 0x3640
+  __TEXT.__objc_methlist: 0x12c4
   __TEXT.__const: 0x6100
-  __TEXT.__cstring: 0x650c
-  __TEXT.__objc_methname: 0x416a
-  __TEXT.__oslogstring: 0x6d99
+  __TEXT.__cstring: 0x650b
+  __TEXT.__objc_methname: 0x412e
+  __TEXT.__oslogstring: 0x6d9c
   __TEXT.__objc_classname: 0x261
   __TEXT.__objc_methtype: 0xecd
-  __TEXT.__gcc_except_tab: 0x5f64
+  __TEXT.__gcc_except_tab: 0x5e10
   __TEXT.__unwind_info: 0x2bb8
-  __DATA_CONST.__const: 0x2c80
-  __DATA_CONST.__cfstring: 0x14a0
+  __DATA_CONST.__const: 0x2c40
+  __DATA_CONST.__cfstring: 0x14c0
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x718
+  __DATA_CONST.__auth_got: 0x720
   __DATA_CONST.__got: 0x280
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__objc_const: 0x1fa8
-  __DATA.__objc_selrefs: 0x1068
-  __DATA.__objc_ivar: 0xf8
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA.__objc_const: 0x1f88
+  __DATA.__objc_selrefs: 0x1060
+  __DATA.__objc_ivar: 0xf4
   __DATA.__objc_data: 0x640
-  __DATA.__data: 0x6a0
-  __DATA.__bss: 0xa8
+  __DATA.__data: 0x6a8
+  __DATA.__bss: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2824
-  Symbols:   4242
-  CStrings:  1870
+  Functions: 2821
+  Symbols:   4236
+  CStrings:  1865
 
Symbols:
+ GCC_except_table21
+ GCC_except_table34
+ GCC_except_table67
+ GCC_except_table71
+ __32-[_ANEServer maxModelMemorySize]_block_invoke
+ __ANEStorageProbeFileIsReadable
+ __ZZ32-[_ANEServer maxModelMemorySize]E19sMaxModelMemorySize
+ __ZZ32-[_ANEServer maxModelMemorySize]E9onceToken
+ ___32-[_ANEServer maxModelMemorySize]_block_invoke
+ _kANEFModelMutableClusterIndexKey
+ _pread
+ _usleep
- -[_ANEServer setMaxModelMemorySize:]
- GCC_except_table32
- GCC_except_table49
- GCC_except_table50
- GCC_except_table59
- GCC_except_table62
- GCC_except_table63
- GCC_except_table66
- GCC_except_table69
- OBJC_IVAR_$__ANEServer._maxModelMemorySize
- __43+[_ANEStorageHelper memoryMapWeightAtPath:]_block_invoke
- __72+[_ANEStorageHelper memoryMapModelAtPath:isPrecompiled:modelAttributes:]_block_invoke
- ___block_descriptor_192_e8_32r_e5_v8?0l
- ___block_descriptor_40_e8_32r_e5_v8?0l
- ___copy_helper_block_e8_32r
- ___destroy_helper_block_e8_32r
- _fcntl
- _objc_msgSend$setMaxModelMemorySize:
CStrings:
+ "%@: %@ failed readability probe. Returning nil"
+ "%@: perTdStats Model patching is not enabled"
+ "%@: pread(%@, offset=%zu, want=%zu) failed. got=%zd errno=%d : %s"
+ "ANEFModelMutableClusterIndex"
+ "TQ,R,N"
+ "maxModelMemorySize: 0x%llx"
+ "maxModelMemorySize: non-internal build, using 0"
+ "maxModelMemorySize: unable to connect to ANE device"
+ "maxModelMemorySize: unable to create device controller"
- "%@: Model patching is not enabled"
- "%@: fcntl(F_RDADVISE). errno=%d : %s"
- "Maximum model memory size: %llu"
- "TQ,V_maxModelMemorySize"
- "Unable to connect to ANE device."
- "Unable to create device controller"
- "_ANED_MODEL_READ_ADVISE"
- "_ANED_WEIGHT_READ_ADVISE"
- "_maxModelMemorySize"
- "com.apple.aned.storageAsyncIO"
- "set maxModelMemorySize to 0"
- "set maxModelMemorySize to 0x%llx"
- "setMaxModelMemorySize:"
- "size=%d\n %{public, signpost.description:begin_time}llu "
```
