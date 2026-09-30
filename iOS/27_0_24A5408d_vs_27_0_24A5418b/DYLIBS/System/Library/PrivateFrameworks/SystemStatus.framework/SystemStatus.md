## SystemStatus

> `/System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus`

```diff

-286.101.0.0.0
-  __TEXT.__text: 0x59774
+286.104.0.0.0
+  __TEXT.__text: 0x59810
   __TEXT.__objc_methlist: 0x84f8
   __TEXT.__const: 0x100
-  __TEXT.__cstring: 0x3f47
+  __TEXT.__cstring: 0x3f7a
   __TEXT.__oslogstring: 0x14a3
-  __TEXT.__gcc_except_tab: 0x42c
+  __TEXT.__gcc_except_tab: 0x430
   __TEXT.__unwind_info: 0x2230
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fc0
+  __DATA_CONST.__objc_selrefs: 0x1fc8
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x400
   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__got: 0x598
   __AUTH_CONST.__const: 0x8c0
-  __AUTH_CONST.__cfstring: 0x4880
+  __AUTH_CONST.__cfstring: 0x48a0
   __AUTH_CONST.__objc_const: 0xf598
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3177
-  Symbols:   6353
-  CStrings:  769
+  Functions: 3178
+  Symbols:   6355
+  CStrings:  770
 
Symbols:
+ _BSDispatchBlockCreateWithQualityOfService
+ _objc_msgSend$_setQueue:
+ _st_dispatch_sync_user_initiated
- _BSDispatchQueueCreateSerial
Functions:
~ -[STStatusDomainXPCServerHandle _internalQueue_setupXPCConnectionIfNecessary] : 516 -> 552
~ -[STStatusDomainXPCServerHandle initWithXPCConnectionProvider:serverLaunchObservable:] : 380 -> 384
- ___77-[STStatusDomainXPCServerHandle _internalQueue_setupXPCConnectionIfNecessary]_block_invoke.31
~ -[STLocalDynamicActivityAttributionManager init] : 180 -> 184
+ ___77-[STStatusDomainXPCServerHandle _internalQueue_setupXPCConnectionIfNecessary]_block_invoke.34
~ -[STDynamicActivityAttributionPublisher init] : 140 -> 144
+ _st_dispatch_sync_user_initiated
~ -[STStatusDomainPublisherXPCServerHandle initWithXPCConnectionProvider:serverLaunchObservable:] : 560 -> 564
CStrings:
+ "com.apple.systemstatus.observer.xpcconnectionqueue"
```
