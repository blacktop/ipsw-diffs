## libxpc.dylib

> `/usr/lib/system/libxpc.dylib`

```diff

-3298.0.21.0.0
-  __TEXT.__text: 0x52fe0
+3298.0.26.502.1
+  __TEXT.__text: 0x53050
   __TEXT.__objc_methlist: 0x374
   __TEXT.__const: 0x618
-  __TEXT.__cstring: 0x7ce6
+  __TEXT.__cstring: 0x7d30
   __TEXT.__oslogstring: 0x3109
   __TEXT.__dof_libxpc: 0xa5d
   __TEXT.__unwind_info: 0xfc0

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1e30
+  __DATA_CONST.__const: 0x1e40
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_nlclslist: 0xe8
   __DATA_CONST.__objc_protolist: 0xf8

   - /usr/lib/system/libunwind.dylib
   Functions: 1545
   Symbols:   2427
-  CStrings:  1295
+  CStrings:  1296
 
Functions:
~ __xpc_connection_init_recv_named : 1472 -> 1520
~ __xpc_connection_init_recv_anon : 256 -> 264
~ __xpc_connection_init_recv_port : 96 -> 116
~ __xpc_connection_derive_connection_port : 528 -> 564
~ __xpc_connection_init_send_named : 300 -> 292
~ __xpc_connection_init_send_anon : 256 -> 244
~ __xpc_connection_init_send_port : 96 -> 116
CStrings:
+ "An extension with the same bundle ID already exists with a different path"
```
