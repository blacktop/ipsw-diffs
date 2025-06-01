## EmbeddedDataReset

> `/System/Library/PrivateFrameworks/EmbeddedDataReset.framework/EmbeddedDataReset`

```diff

   __TEXT.__oslogstring: 0x48c
   __TEXT.__unwind_info: 0xe0
   __TEXT.__objc_classname: 0xb6
-  __TEXT.__objc_methname: 0x9fa
+  __TEXT.__objc_methname: 0xa0c
   __TEXT.__objc_methtype: 0x27c
   __TEXT.__objc_stubs: 0x6c0
   __DATA_CONST.__got: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x918
   __DATA_CONST.__objc_selrefs: 0x250
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_classrefs: 0x40
+  __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x140
   __AUTH_CONST.__objc_const: 0x1b0
   __AUTH_CONST.__auth_got: 0x188
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x40
-  __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x3c
   __DATA.__data: 0x2a0
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B1B664AD-98DB-3258-B274-D35AAB6F000E
+  UUID: 7ABD8F57-249F-3690-8B5D-C70ADDADEE8D
   Functions: 62
   Symbols:   349
-  CStrings:  238
+  CStrings:  239
 
Symbols:
+ ___41-[DDRResetService dataResetXPCConnection]_block_invoke.72
+ ___47-[DDRResetService resetWithRequest:completion:]_block_invoke.75
+ ___52-[DDRResetService observerNonLaunchingXPCConnection]_block_invoke.58
- ___41-[DDRResetService dataResetXPCConnection]_block_invoke.71
- ___47-[DDRResetService resetWithRequest:completion:]_block_invoke.74
- ___52-[DDRResetService observerNonLaunchingXPCConnection]_block_invoke.57
CStrings:
+ "T@\"NSString\",?,R,C"

```
