## SystemStatus

> `/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus`

```diff

-  __TEXT.__text: 0x59824
+  __TEXT.__text: 0x59438
   __TEXT.__objc_methlist: 0x84f0
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x3f2b
+  __TEXT.__cstring: 0x3f0e
   __TEXT.__oslogstring: 0x14a3
   __TEXT.__gcc_except_tab: 0x42c
-  __TEXT.__unwind_info: 0x2238
+  __TEXT.__unwind_info: 0x2228
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x19e0
+  __DATA_CONST.__const: 0x1980
   __DATA_CONST.__objc_classlist: 0x598
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fb8
+  __DATA_CONST.__objc_selrefs: 0x1fb0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__got: 0x590
   __AUTH_CONST.__const: 0x8c0
-  __AUTH_CONST.__cfstring: 0x4840
+  __AUTH_CONST.__cfstring: 0x4860
   __AUTH_CONST.__objc_const: 0xf578
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x3c0
+  __AUTH.__objc_data: 0x16d0
   __DATA.__objc_ivar: 0x5d4
   __DATA.__data: 0xd28
   __DATA.__common: 0x20
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_ivar: 0x18
-  __DATA_DIRTY.__objc_data: 0x3430
+  __DATA_DIRTY.__objc_data: 0x2120
   __DATA_DIRTY.__bss: 0x160
   __DATA_DIRTY.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3178
-  Symbols:   9602
-  CStrings:  1344
+  Functions: 3172
+  Symbols:   9587
+  CStrings:  1345
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __DATA.__data : content changed
Symbols:
+ GCC_except_table48
+ ___block_descriptor_65_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ _dispatch_block_create
- +[STStatusDomainPublisherXPCServerHandle _xpcReplyBlockForServerCompletion:]
- GCC_except_table50
- ___59-[STStatusDomainPublisher _updateDataWithBlock:completion:]_block_invoke_2
- ___65-[STStatusDomainPublisher _setData:withChangeContext:completion:]_block_invoke
- ___67-[STStatusDomainPublisher _updateVolatileDataWithBlock:completion:]_block_invoke_2
- ___73-[STStatusDomainPublisher _setVolatileData:withChangeContext:completion:]_block_invoke
- ___76+[STStatusDomainPublisherXPCServerHandle _xpcReplyBlockForServerCompletion:]_block_invoke
- ___block_descriptor_40_e8_32bs_e37_v16?0"NSObject<OS_dispatch_queue>"8ls32l8
- ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
- ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_73_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- _objc_msgSend$_handoffCurrentReplyToQueue:block:
CStrings:
+ "ethernet"
- "v16@?0@\"NSObject<OS_dispatch_queue>\"8"

```
