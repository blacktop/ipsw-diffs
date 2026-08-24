## SystemStatusServer

> `/System/Library/PrivateFrameworks/SystemStatusServer.framework/Versions/A/SystemStatusServer`

```diff

-284.0.0.0.0
-  __TEXT.__text: 0x12ea8
+286.200.1.0.0
+  __TEXT.__text: 0x13074
   __TEXT.__objc_methlist: 0xdf8
   __TEXT.__const: 0x88
-  __TEXT.__cstring: 0x72f
+  __TEXT.__cstring: 0x793
   __TEXT.__gcc_except_tab: 0x190
   __TEXT.__oslogstring: 0x49f
   __TEXT.__unwind_info: 0x4e8

   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9b8
+  __DATA_CONST.__objc_selrefs: 0x9d0
   __DATA_CONST.__objc_superrefs: 0xc8
-  __DATA_CONST.__got: 0x2c0
-  __AUTH_CONST.__const: 0xa80
-  __AUTH_CONST.__cfstring: 0x380
+  __DATA_CONST.__got: 0x2c8
+  __AUTH_CONST.__const: 0xa90
+  __AUTH_CONST.__cfstring: 0x3a0
   __AUTH_CONST.__objc_const: 0x24a0
   __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0x174

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 378
-  Symbols:   1225
-  CStrings:  73
+  Functions: 380
+  Symbols:   1234
+  CStrings:  75
 
Symbols:
+ +[STStatusDomainPublisherXPCClientHandle _serverCompletionForXPCReplyBlock:]
+ _BSDispatchQueueCreateSerialWithQoS
+ _OBJC_CLASS_$_NSXPCConnection
+ ___76+[STStatusDomainPublisherXPCClientHandle _serverCompletionForXPCReplyBlock:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e37_v16?0"NSObject<OS_dispatch_queue>"8l
+ ___copy_helper_block_e8_32b
+ _objc_msgSend$_handoffCurrentReplyToQueue:block:
+ _objc_msgSend$_setQueue:
+ _objc_msgSend$remoteObjectProxy
+ _objc_opt_self
+ _objc_retainBlock
- ___73-[STStatusDomainXPCClientHandle observeData:forDomain:withChangeContext:]_block_invoke_4
- _dispatch_block_create
CStrings:
+ "com.apple.systemstatus.publisher.xpcconnectionqueue.client-%d"
+ "v16@?0@\"NSObject<OS_dispatch_queue>\"8"
```
