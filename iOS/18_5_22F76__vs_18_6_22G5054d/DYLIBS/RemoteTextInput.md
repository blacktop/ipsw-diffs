## RemoteTextInput

> `/System/Library/PrivateFrameworks/RemoteTextInput.framework/RemoteTextInput`

```diff

-159.310.0.0.0
-  __TEXT.__text: 0x211d8
+159.601.0.0.0
+  __TEXT.__text: 0x211fc
   __TEXT.__auth_stubs: 0x770
-  __TEXT.__objc_methlist: 0x2b64
+  __TEXT.__objc_methlist: 0x2b74
   __TEXT.__const: 0x108
   __TEXT.__cstring: 0x2f26
   __TEXT.__oslogstring: 0xccc

   __TEXT.__dlopen_cstrs: 0xf6
   __TEXT.__unwind_info: 0x930
   __TEXT.__objc_classname: 0x419
-  __TEXT.__objc_methname: 0x748a
+  __TEXT.__objc_methname: 0x74ae
   __TEXT.__objc_methtype: 0x1745
-  __TEXT.__objc_stubs: 0x4740
+  __TEXT.__objc_stubs: 0x4760
   __DATA_CONST.__got: 0x260
   __DATA_CONST.__const: 0xc90
   __DATA_CONST.__objc_classlist: 0x108
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1938
+  __DATA_CONST.__objc_selrefs: 0x1940
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xd8
   __AUTH_CONST.__auth_got: 0x3c8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8113F6F7-43C4-34E1-A1AF-E189C5652541
-  Functions: 1010
-  Symbols:   3654
-  CStrings:  2317
+  UUID: D4D04CB7-D917-3EB4-803D-8EBA69E744AF
+  Functions: 1011
+  Symbols:   3657
+  CStrings:  2318
 
Symbols:
+ +[RTIUtilities makeClientCodingQueuePthreadKeyOnce]
+ +[RTIUtilities makeClientCodingQueuePthreadKeyOnce].cold.1
+ GCC_except_table25
+ ___51+[RTIUtilities makeClientCodingQueuePthreadKeyOnce]_block_invoke
+ _makeClientCodingQueuePthreadKeyOnce.onceToken
+ _objc_msgSend$makeClientCodingQueuePthreadKeyOnce
- +[RTIUtilities performClientCoding:withServiceOptions:].cold.1
- GCC_except_table24
- ___55+[RTIUtilities performClientCoding:withServiceOptions:]_block_invoke
- _performClientCoding:withServiceOptions:.onceToken
Functions:
~ +[RTIUtilities performClientCoding:withServiceOptions:] : 184 -> 172
+ +[RTIUtilities makeClientCodingQueuePthreadKeyOnce]
~ +[RTIUtilities currentClientCodingServiceOptions] : 72 -> 76
CStrings:
+ "makeClientCodingQueuePthreadKeyOnce"

```
