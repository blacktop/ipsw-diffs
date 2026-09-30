## RemoteXPC

> `/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC`

```diff

-3070.0.0.0.2
-  __TEXT.__text: 0xf59c
+3088.0.0.0.0
+  __TEXT.__text: 0xf548
   __TEXT.__auth_stubs: 0xa60
   __TEXT.__objc_methlist: 0x2ac
-  __TEXT.__const: 0xa0
+  __TEXT.__const: 0x98
   __TEXT.__gcc_except_tab: 0x318
   __TEXT.__cstring: 0xb27
-  __TEXT.__oslogstring: 0x2722
+  __TEXT.__oslogstring: 0x2786
   __TEXT.__unwind_info: 0x408
   __TEXT.__objc_classname: 0xdf
   __TEXT.__objc_methname: 0x79e

   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4280DD7F-D0D2-39AF-9A35-501810E4E130
-  Functions: 358
-  Symbols:   1156
-  CStrings:  453
+  UUID: C21FC7FC-F3B0-3FDA-80CA-E13695F6896A
+  Functions: 353
+  Symbols:   1146
+  CStrings:  456
 
Symbols:
+ GCC_except_table251
- GCC_except_table256
- ___xpc_remote_connection_teardown.cold.2
- ___xpc_remote_connection_teardown_continue.cold.4
- ___xpc_remote_connection_teardown_continue.cold.5
- ___xpc_remote_connection_teardown_continue.cold.6
- ___xpc_remote_connection_teardown_continue.cold.7
CStrings:
+ "[%p] Flushing outgoing messages"
+ "[%p] Flushing outstanding replies"
+ "[%p] disconnect: already canceled"

```
