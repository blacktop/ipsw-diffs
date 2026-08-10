## libAONConnection.dylib

> `/usr/lib/libAONConnection.dylib`

### Sections with Same Size but Changed Content

- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`

```diff

-251.0.7.0.0
-  __TEXT.__text: 0xab80
+251.2.1.0.0
+  __TEXT.__text: 0xac88
   __TEXT.__const: 0x180
-  __TEXT.__cstring: 0x1f3d
+  __TEXT.__cstring: 0x2033
   __TEXT.__gcc_except_tab: 0x4c
   __TEXT.__oslogstring: 0xd55
-  __TEXT.__unwind_info: 0x2b8
+  __TEXT.__unwind_info: 0x2c0
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x328
+  __DATA_CONST.__const: 0x348
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x240
+  __AUTH_CONST.__const: 0x248
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__weak_auth_got: 0x38
   __AUTH_CONST.__auth_got: 0x340

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 206
-  Symbols:   366
-  CStrings:  225
+  Functions: 208
+  Symbols:   368
+  CStrings:  227
 
Symbols:
+ GCC_except_table147
+ __ZN22AONNetConnectionClient20onTransportConnectedEj
+ ____ZN4ULPN15TBClientAdaptor4initEP13tb_endpoint_sb_block_invoke_5
- GCC_except_table146
Functions:
+ __ZN22AONNetConnectionClient20onTransportConnectedEj
~ __ZN4ULPN15TBClientAdaptor4initEP13tb_endpoint_sb : 784 -> 860
+ ____ZN4ULPN15TBClientAdaptor4initEP13tb_endpoint_sb_block_invoke_5
~ ___aonnetworking_networkingservicecallback__server_start_owned_block_invoke : 2044 -> 2168
CStrings:
+ "TB_ASSERT: (server->transportconnected != ((void*)0)) && \"implementation for TransportConnected is not present\""
+ "v12@?0I8"
```
