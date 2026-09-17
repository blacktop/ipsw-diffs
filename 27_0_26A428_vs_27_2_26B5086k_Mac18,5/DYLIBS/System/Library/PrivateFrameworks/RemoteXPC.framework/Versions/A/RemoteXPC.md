## RemoteXPC

> `/System/Library/PrivateFrameworks/RemoteXPC.framework/Versions/A/RemoteXPC`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-3298.1.1.0.0
-  __TEXT.__text: 0xeb48
+3298.40.20.0.0
+  __TEXT.__text: 0xebbc
   __TEXT.__objc_methlist: 0x27c
-  __TEXT.__const: 0x90
+  __TEXT.__const: 0x98
   __TEXT.__gcc_except_tab: 0x238
   __TEXT.__cstring: 0xb89
   __TEXT.__oslogstring: 0x27c5

   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__got: 0x98
   __AUTH_CONST.__const: 0x830
-  __AUTH_CONST.__objc_const: 0xf28
+  __AUTH_CONST.__objc_const: 0xf48
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__objc_ivar: 0x124
+  __DATA.__objc_ivar: 0x128
   __DATA.__data: 0xc8
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__data: 0xe0

   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/Versions/A/RemoteServiceDiscovery
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 187
-  Symbols:   535
+  Functions: 188
+  Symbols:   537
   CStrings:  285
 
Symbols:
+ GCC_except_table110
+ GCC_except_table136
+ GCC_except_table67
+ GCC_except_table98
+ OBJC_IVAR_$_OS_xpc_remote_connection.connected_device
+ _xpc_remote_connection_copy_remote_device
- GCC_except_table109
- GCC_except_table135
- GCC_except_table66
- GCC_except_table97
Functions:
~ _xpc_remote_connection_create_with_remote_service : 456 -> 464
+ _xpc_remote_connection_copy_remote_device
~ -[OS_xpc_remote_connection .cxx_destruct] : 260 -> 272
~ ____xpc_remote_connection_listen_block_invoke : 956 -> 972
```
