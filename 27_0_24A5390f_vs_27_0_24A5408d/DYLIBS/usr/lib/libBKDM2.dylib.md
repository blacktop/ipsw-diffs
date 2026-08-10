## libBKDM2.dylib

> `/usr/lib/libBKDM2.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-980.0.18.0.0
-  __TEXT.__text: 0x7cabc
+980.0.26.0.0
+  __TEXT.__text: 0x7c2d8
   __TEXT.__objc_methlist: 0x5d84
   __TEXT.__const: 0xd7b8
-  __TEXT.__cstring: 0x7041
-  __TEXT.__oslogstring: 0x4720
-  __TEXT.__gcc_except_tab: 0x17c0
+  __TEXT.__cstring: 0x7066
+  __TEXT.__oslogstring: 0x46ec
+  __TEXT.__gcc_except_tab: 0x17b4
   __TEXT.__ustring: 0x11c
-  __TEXT.__unwind_info: 0xe20
+  __TEXT.__unwind_info: 0xe30
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d58
+  __DATA_CONST.__objc_selrefs: 0x3d60
   __DATA_CONST.__objc_superrefs: 0xc0
   __DATA_CONST.__objc_arraydata: 0x4a8
-  __DATA_CONST.__got: 0x450
+  __DATA_CONST.__got: 0x448
   __AUTH_CONST.__const: 0xc08
-  __AUTH_CONST.__cfstring: 0x65a0
-  __AUTH_CONST.__objc_const: 0x9a28
+  __AUTH_CONST.__cfstring: 0x65e0
+  __AUTH_CONST.__objc_const: 0x9a58
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x168
-  __AUTH_CONST.__auth_got: 0x730
+  __AUTH_CONST.__auth_got: 0x768
   __AUTH.__objc_data: 0x1e0
-  __DATA.__objc_ivar: 0xac8
+  __DATA.__objc_ivar: 0xacc
   __DATA.__data: 0x880
   __DATA.__bss: 0x49
   __DATA_DIRTY.__objc_data: 0x6e0

   - /usr/lib/libSystemHealth.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2904
-  Symbols:   5367
-  CStrings:  1608
+  Functions: 2905
+  Symbols:   5371
+  CStrings:  1613
 
Symbols:
+ -[BioLog cameraRotation]
+ -[BioLog setCameraRotation:]
+ _OBJC_IVAR_$_BioLog._cameraRotation
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_60
+ ___error
+ _fclose
+ _ferror
+ _fileno
+ _fopen
+ _fread
+ _fstat
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$setCameraRotation:
- +[BLRetention applyCustomerPolicyForType:withSequenceDirs:withSize:]
- +[BLRetention applyCustomerPolicyWithPath:]
- ___62+[BLRetention applyPolicyWithPath:sizeLimit:freeMissingSpace:]_block_invoke_2
- ___68+[BLRetention applyCustomerPolicyForType:withSequenceDirs:withSize:]_block_invoke
- ___68+[BLRetention applyCustomerPolicyForType:withSequenceDirs:withSize:]_block_invoke_2
- ___68+[BLRetention applyCustomerPolicyForType:withSequenceDirs:withSize:]_block_invoke_3
- ___68+[BLRetention applyCustomerPolicyForType:withSequenceDirs:withSize:]_block_invoke_4
- __dispatch_queue_attr_concurrent
- _objc_msgSend$applyCustomerPolicyForType:withSequenceDirs:withSize:
- _objc_msgSend$containsString:
- _objc_msgSend$limitSequenceDirs:withSize:toCount:withReplaceInterval:removalMethod:
CStrings:
+ "Limiting latest sequences (last %u minutes), count %lu ...\n"
+ "bytesRead == fileSize"
+ "file"
+ "fileSize > 0"
+ "fopen:%@ failed, errno:%u\n"
+ "fread:%@ failed\n"
+ "fstat:%@ failed, errno:%u\n"
+ "rb"
+ "sec-"
- "Applying customer retention policy...\n"
- "Customer retention fullfilled! Turn customer logging off for some time?\n"
- "Customer retention policy removed %.3fMB in %fs, resulting size %luMB\n"
- "dcnKernels"
```
