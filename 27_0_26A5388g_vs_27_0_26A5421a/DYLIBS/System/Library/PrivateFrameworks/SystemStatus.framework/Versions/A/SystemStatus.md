## SystemStatus

> `/System/Library/PrivateFrameworks/SystemStatus.framework/Versions/A/SystemStatus`

```diff

-284.0.0.0.0
-  __TEXT.__text: 0x3fd70
-  __TEXT.__objc_methlist: 0x5350
+286.200.1.0.0
+  __TEXT.__text: 0x401d0
+  __TEXT.__objc_methlist: 0x5358
   __TEXT.__const: 0x108
-  __TEXT.__cstring: 0x2fa6
+  __TEXT.__cstring: 0x2fff
   __TEXT.__gcc_except_tab: 0x3d4
   __TEXT.__oslogstring: 0x1444
-  __TEXT.__unwind_info: 0x1748
+  __TEXT.__unwind_info: 0x1760
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1590
+  __DATA_CONST.__objc_selrefs: 0x15a8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x260
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x3e0
-  __AUTH_CONST.__const: 0x16f0
-  __AUTH_CONST.__cfstring: 0x2dc0
-  __AUTH_CONST.__objc_const: 0x9c00
+  __DATA_CONST.__got: 0x3e8
+  __AUTH_CONST.__const: 0x1780
+  __AUTH_CONST.__cfstring: 0x2de0
+  __AUTH_CONST.__objc_const: 0x9c20
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x34c
+  __DATA.__objc_ivar: 0x350
   __DATA.__data: 0xcc8
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_ivar: 0x8

   - /System/Library/PrivateFrameworks/BaseBoard.framework/Versions/A/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2056
-  Symbols:   4238
-  CStrings:  541
+  Functions: 2063
+  Symbols:   4251
+  CStrings:  543
 
Symbols:
+ +[STStatusDomainPublisher _serverCompletionForClientCompletion:]
+ +[STStatusDomainPublisherXPCServerHandle _xpcReplyBlockForServerCompletion:]
+ -[STDynamicActivityAttributionXPCClientHandle invalidateConnection]
+ GCC_except_table29
+ GCC_except_table54
+ OBJC_IVAR_$_STDynamicActivityAttributionXPCClientHandle._connectionLock
+ _BSDispatchBlockCreateWithQualityOfService
+ ___64+[STStatusDomainPublisher _serverCompletionForClientCompletion:]_block_invoke
+ ___76+[STStatusDomainPublisherXPCServerHandle _xpcReplyBlockForServerCompletion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e37_v16?0"NSObject<OS_dispatch_queue>"8l
+ ___block_descriptor_40_e8_32bs_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0l
+ ___block_descriptor_73_e8_32s40s48s56bs_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56b
+ _objc_msgSend$_handoffCurrentReplyToQueue:block:
+ _objc_msgSend$_setQueue:
+ _objc_msgSend$invalidateConnection
+ _st_dispatch_sync_user_initiated
- GCC_except_table31
- GCC_except_table52
- _BSDispatchQueueCreateSerial
- ___block_descriptor_65_e8_32s40s48s_e5_v8?0l
- _dispatch_block_create
CStrings:
+ "a"
+ "com.apple.systemstatus.observer.xpcconnectionqueue"
+ "v16@?0@\"NSObject<OS_dispatch_queue>\"8"
- "A"
```
