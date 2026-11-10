## ANELargeModelCompilerService

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANELargeModelCompilerService.xpc/Contents/MacOS/ANELargeModelCompilerService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`

```diff

-382.15.1.0.0
-  __TEXT.__text: 0x1bffc
+382.101.2.0.0
+  __TEXT.__text: 0x1bae8
   __TEXT.__auth_stubs: 0x720
   __TEXT.__objc_stubs: 0x22c0
   __TEXT.__objc_methlist: 0x9b4
   __TEXT.__const: 0x128
-  __TEXT.__cstring: 0x1366
-  __TEXT.__oslogstring: 0x267e
+  __TEXT.__cstring: 0x1365
+  __TEXT.__oslogstring: 0x2661
   __TEXT.__objc_classname: 0x19e
-  __TEXT.__objc_methname: 0x2644
+  __TEXT.__objc_methname: 0x264d
   __TEXT.__objc_methtype: 0x67b
-  __TEXT.__gcc_except_tab: 0x12d4
-  __TEXT.__unwind_info: 0x5d8
-  __DATA_CONST.__const: 0x3b0
-  __DATA_CONST.__cfstring: 0x1980
+  __TEXT.__gcc_except_tab: 0x1180
+  __TEXT.__unwind_info: 0x5c0
+  __DATA_CONST.__const: 0x350
+  __DATA_CONST.__cfstring: 0x19a0
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28

   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__auth_got: 0x3a8
   __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0xd48
   __DATA.__objc_selrefs: 0xaa8
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x500
-  __DATA.__data: 0x400
-  __DATA.__bss: 0x88
+  __DATA.__data: 0x408
+  __DATA.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsandbox.1.dylib
-  Functions: 343
-  Symbols:   968
-  CStrings:  897
+  Functions: 340
+  Symbols:   965
+  CStrings:  895
 
Symbols:
+ __ANEStorageProbeFileIsReadable
+ ___chkstk_darwin
+ _kANEFModelMutableClusterIndexKey
+ _objc_msgSend$cloneIfWritable:isEncryptedModel:cloneDirectory:useClone:
+ _pread
- __43+[_ANEStorageHelper memoryMapWeightAtPath:]_block_invoke
- __72+[_ANEStorageHelper memoryMapModelAtPath:isPrecompiled:modelAttributes:]_block_invoke
- ___block_descriptor_192_e8_32r_e5_v8?0l
- ___block_descriptor_40_e8_32r_e5_v8?0l
- ___copy_helper_block_e8_32r
- ___destroy_helper_block_e8_32r
- _fcntl
- _objc_msgSend$cloneIfWritable:isEncryptedModel:cloneDirectory:
CStrings:
+ "%@: %@ failed readability probe. Returning nil"
+ "%@: pread(%@, offset=%zu, want=%zu) failed. got=%zd errno=%d : %s"
+ "ANEFModelMutableClusterIndex"
+ "cloneIfWritable:isEncryptedModel:cloneDirectory:useClone:"
- "%@: fcntl(F_RDADVISE). errno=%d : %s"
- "_ANED_MODEL_READ_ADVISE"
- "_ANED_WEIGHT_READ_ADVISE"
- "cloneIfWritable:isEncryptedModel:cloneDirectory:"
- "com.apple.aned.storageAsyncIO"
- "size=%d\n %{public, signpost.description:begin_time}llu "
```
