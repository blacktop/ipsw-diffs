## RemoteServiceDiscovery

> `/System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/Versions/A/RemoteServiceDiscovery`

```diff

-162.0.0.0.0
-  __TEXT.__text: 0xee88
+161.0.0.0.0
+  __TEXT.__text: 0xed30
   __TEXT.__auth_stubs: 0x890
   __TEXT.__objc_methlist: 0x36c
   __TEXT.__const: 0xa0
   __TEXT.__cstring: 0x127c
-  __TEXT.__gcc_except_tab: 0x3e4
-  __TEXT.__oslogstring: 0x1c02
-  __TEXT.__unwind_info: 0x4c8
+  __TEXT.__gcc_except_tab: 0x3cc
+  __TEXT.__oslogstring: 0x1bd7
+  __TEXT.__unwind_info: 0x4d0
   __TEXT.__objc_classname: 0x9b
-  __TEXT.__objc_methname: 0x971
+  __TEXT.__objc_methname: 0x965
   __TEXT.__objc_methtype: 0x189
   __TEXT.__objc_stubs: 0x760
   __DATA_CONST.__got: 0xf8

   - /usr/lib/libFDR.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 443
-  Symbols:   924
+  Functions: 441
+  Symbols:   921
   CStrings:  168
 
Symbols:
+ -[SocketRemoteXpcProxy getClientSocket]
+ GCC_except_table102
+ GCC_except_table104
+ GCC_except_table106
+ GCC_except_table108
+ GCC_except_table110
+ GCC_except_table113
+ GCC_except_table116
+ GCC_except_table118
+ GCC_except_table130
+ GCC_except_table150
+ GCC_except_table154
+ GCC_except_table159
+ GCC_except_table195
+ GCC_except_table26
+ GCC_except_table394
+ GCC_except_table45
+ GCC_except_table55
+ GCC_except_table96
+ GCC_except_table98
+ _dup
+ _objc_msgSend$getClientSocket
- -[OS_remote_service proxySocketOverRemoteXPC:].cold.2
- -[SocketRemoteXpcProxy takeOwnershipOfClientSocket]
- GCC_except_table103
- GCC_except_table105
- GCC_except_table107
- GCC_except_table109
- GCC_except_table111
- GCC_except_table114
- GCC_except_table117
- GCC_except_table119
- GCC_except_table131
- GCC_except_table151
- GCC_except_table155
- GCC_except_table160
- GCC_except_table196
- GCC_except_table27
- GCC_except_table396
- GCC_except_table46
- GCC_except_table56
- GCC_except_table97
- GCC_except_table99
- ___30-[SocketRemoteXpcProxy cancel]_block_invoke
- _objc_msgSend$takeOwnershipOfClientSocket
- _remote_service_accept.cold.2
- _xpc_remote_connection_send_barrier

```
