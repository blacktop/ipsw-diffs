## SystemStatusServer

> `/System/Library/PrivateFrameworks/SystemStatusServer.framework/SystemStatusServer`

```diff

-  __TEXT.__text: 0x1fc3c
+  __TEXT.__text: 0x1fac4
   __TEXT.__objc_methlist: 0x1d90
   __TEXT.__const: 0xd0
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__cstring: 0x1ca0
+  __TEXT.__cstring: 0x1c7a
   __TEXT.__gcc_except_tab: 0x328
   __TEXT.__oslogstring: 0xaee
   __TEXT.__unwind_info: 0x870

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xe00
+  __DATA_CONST.__const: 0xdd8
   __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1360
+  __DATA_CONST.__objc_selrefs: 0x1358
   __DATA_CONST.__objc_superrefs: 0x108
-  __DATA_CONST.__got: 0x418
+  __DATA_CONST.__got: 0x410
   __AUTH_CONST.__const: 0x2a0
   __AUTH_CONST.__cfstring: 0x1760
   __AUTH_CONST.__objc_const: 0x4260

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 742
-  Symbols:   2938
-  CStrings:  473
+  Functions: 740
+  Symbols:   2930
+  CStrings:  472
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ ___block_descriptor_74_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ _dispatch_block_create
- +[STStatusDomainPublisherXPCClientHandle _serverCompletionForXPCReplyBlock:]
- _OBJC_CLASS_$_NSXPCConnection
- ___76+[STStatusDomainPublisherXPCClientHandle _serverCompletionForXPCReplyBlock:]_block_invoke
- ___block_descriptor_40_e8_32bs_e37_v16?0"NSObject<OS_dispatch_queue>"8ls32l8
- ___block_descriptor_74_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
- _objc_msgSend$_handoffCurrentReplyToQueue:block:
- _objc_opt_self
- _objc_retainBlock
Functions:
~ ___119-[STStatusDomainPublisherXPCClientHandle publishDiff:forDomain:withChangeContext:replacingData:discardingOnExit:reply:]_block_invoke : 912 -> 876
~ -[STLocalStatusServer _internalQueue_updateVolatileDataForPublisherClient:domain:usingDiffProvider:completion:] : 800 -> 788
~ -[STLocalStatusServer _internalQueue_mutateDataForDomain:withChangeContext:block:] : 1148 -> 1164
~ -[STLocalStatusServer _internalQueue_publishData:forPublisherClient:domain:inDataChangeRecord:withChangeContext:completion:] : 428 -> 420
~ -[STLocalStatusServer _internalQueue_publishVolatileData:forPublisherClient:domain:withChangeContext:completion:] : 368 -> 364
~ -[STLocalStatusServer _internalQueue_replaceDataChangeRecord:forPublisherClient:completion:] : 452 -> 448
~ -[STLocalStatusServer _internalQueue_replaceVolatileDataChangeRecord:forPublisherClient:completion:] : 452 -> 448
~ -[STLocalStatusServer _internalQueue_publishData:forPublisherClient:domain:withChangeContext:completion:] : 368 -> 364
~ -[STLocalStatusServer _internalQueue_updateDataForPublisherClient:domain:usingDiffProvider:completion:] : 568 -> 564
~ -[STLocalStatusServer _internalQueue_replaceDataChangeRecord:forPublisherClient:inDataChangeRecord:applyBlock:completion:] : 492 -> 484
~ ___89-[STStatusDomainPublisherXPCClientHandle replaceDataChangeRecord:discardingOnExit:reply:]_block_invoke : 672 -> 636
- ___89-[STStatusDomainPublisherXPCClientHandle replaceDataChangeRecord:discardingOnExit:reply:]_block_invoke_3
~ ___105-[STStatusDomainPublisherXPCClientHandle publishData:forDomain:withChangeContext:discardingOnExit:reply:]_block_invoke : 480 -> 440
- ___76+[STStatusDomainPublisherXPCClientHandle _serverCompletionForXPCReplyBlock:]_block_invoke
CStrings:
- "v16@?0@\"NSObject<OS_dispatch_queue>\"8"

```
