## CardServices

> `/System/Library/PrivateFrameworks/CardServices.framework/CardServices`

```diff

-3303.2.1.0.0
+3304.3.1.0.0
   __TEXT.__text: 0x20bc
   __TEXT.__auth_stubs: 0x380
   __TEXT.__objc_methlist: 0x2b8

   __TEXT.__gcc_except_tab: 0x74
   __TEXT.__unwind_info: 0x10c
   __TEXT.__objc_classname: 0x15b
-  __TEXT.__objc_methname: 0x7f1
+  __TEXT.__objc_methname: 0x807
   __TEXT.__objc_methtype: 0x2e7
   __TEXT.__objc_stubs: 0x520
   __DATA_CONST.__got: 0x28

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1720
   __DATA_CONST.__objc_selrefs: 0x1d0
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x68
+  __DATA_CONST.__objc_superrefs: 0x20
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x360
   __AUTH_CONST.__auth_got: 0x1d0
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x68
-  __DATA.__objc_superrefs: 0x20
   __DATA.__objc_ivar: 0x28
   __DATA.__data: 0x3c0
   __DATA.__bss: 0x8

   - /System/Library/PrivateFrameworks/Cards.framework/Cards
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7D9565AE-7957-3DF2-A028-82604D6DFA33
+  UUID: 36BFE656-45DB-3302-AD9B-634384A9448E
   Functions: 65
   Symbols:   428
-  CStrings:  213
+  CStrings:  214
 
Symbols:
+ ___33-[CRSCardRequest startWithReply:]_block_invoke.52
+ ___33-[CRSCardRequest startWithReply:]_block_invoke.56
+ ___49-[CRSCardRequest _loadAndRegisterBundleServices:]_block_invoke.63
+ ___50-[CRSCardRequest _tryRemainingCardServices:reply:]_block_invoke.65
+ ___50-[CRSCardRequest _tryRemainingCardServices:reply:]_block_invoke.67
- ___33-[CRSCardRequest startWithReply:]_block_invoke.51
- ___33-[CRSCardRequest startWithReply:]_block_invoke.55
- ___49-[CRSCardRequest _loadAndRegisterBundleServices:]_block_invoke.62
- ___50-[CRSCardRequest _tryRemainingCardServices:reply:]_block_invoke.64
- ___50-[CRSCardRequest _tryRemainingCardServices:reply:]_block_invoke.66
CStrings:
+ "T@\"NSString\",?,R,C"
+ "T@\"SFCard\",?,R,N"
+ "TB,?,R,N"
- "T@\"SFCard\",R,N"
- "TB,R,N"

```
