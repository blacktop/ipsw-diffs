## RemoteServiceDiscovery

> `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery`

```diff

-202.0.0.0.0
-  __TEXT.__text: 0xe1c8
-  __TEXT.__auth_stubs: 0xa40
+202.0.1.0.0
+  __TEXT.__text: 0xe188
+  __TEXT.__auth_stubs: 0xa30
   __TEXT.__objc_methlist: 0x36c
-  __TEXT.__const: 0xa0
+  __TEXT.__const: 0xa8
   __TEXT.__cstring: 0x12bc
   __TEXT.__gcc_except_tab: 0x3bc
   __TEXT.__oslogstring: 0x1c37

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x218
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x530
+  __AUTH_CONST.__auth_got: 0x528
   __AUTH_CONST.__const: 0x240
   __AUTH_CONST.__objc_const: 0xb68
   __AUTH.__objc_data: 0x28
   __DATA.__objc_ivar: 0xbc
-  __DATA.__bss: 0x18
+  __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x1b8
-  __DATA_DIRTY.__bss: 0x48
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libFDR.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B5005367-5999-36BD-BC7E-DC4371235ED0
-  Functions: 433
-  Symbols:   1352
+  UUID: F6E259FD-78DE-3832-890C-E7DEC27666F1
+  Functions: 432
+  Symbols:   1349
   CStrings:  494
 
Symbols:
+ ___block_descriptor_56_e8_32s40r48r_e33_v16?0"NSObject<OS_xpc_object>"8lr40l8s32l8r48l8
- ___30-[SocketRemoteXpcProxy cancel]_block_invoke
- ___block_descriptor_52_e8_32s40r_e33_v16?0"NSObject<OS_xpc_object>"8ls32l8r40l8
- _xpc_remote_connection_send_barrier
Functions:
~ -[OS_remote_service proxySocketOverRemoteXPC:] : 412 -> 420
~ -[SocketRemoteXpcProxy initWithSocket:device:queue:server:] : 644 -> 636
~ -[SocketRemoteXpcProxy activate] : 504 -> 548
~ ___32-[SocketRemoteXpcProxy activate]_block_invoke : 408 -> 448
~ -[SocketRemoteXpcProxy cancel] : 136 -> 156
- ___30-[SocketRemoteXpcProxy cancel]_block_invoke

```
