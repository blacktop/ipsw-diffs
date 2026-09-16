## RemoteXPC

> `/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-3298.2.1.0.0
-  __TEXT.__text: 0xdd2c
+3298.40.20.0.0
+  __TEXT.__text: 0xdd9c
   __TEXT.__objc_methlist: 0x27c
-  __TEXT.__const: 0x90
+  __TEXT.__const: 0x98
   __TEXT.__gcc_except_tab: 0x234
   __TEXT.__cstring: 0xb89
   __TEXT.__oslogstring: 0x27c5

   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__got: 0x98
   __AUTH_CONST.__const: 0xe0
-  __AUTH_CONST.__objc_const: 0xf28
+  __AUTH_CONST.__objc_const: 0xf48
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x124
+  __DATA.__objc_ivar: 0x128
   __DATA.__data: 0xc8
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__data: 0xe0

   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 168
-  Symbols:   531
+  Functions: 169
+  Symbols:   533
   CStrings:  285
 
Symbols:
+ GCC_except_table120
+ GCC_except_table55
+ GCC_except_table84
+ GCC_except_table96
+ _OBJC_IVAR_$_OS_xpc_remote_connection.connected_device
+ _xpc_remote_connection_copy_remote_device
- GCC_except_table119
- GCC_except_table54
- GCC_except_table83
- GCC_except_table95
Functions:
~ -[OS_xpc_remote_connection .cxx_destruct] : 260 -> 272
~ _xpc_remote_connection_create_with_remote_service : 424 -> 432
+ _xpc_remote_connection_copy_remote_device
~ ____xpc_remote_connection_listen_block_invoke : 908 -> 924
```
