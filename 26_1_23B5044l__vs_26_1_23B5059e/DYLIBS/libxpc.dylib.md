## libxpc.dylib

> `/usr/lib/system/libxpc.dylib`

```diff

-3089.40.13.0.1
-  __TEXT.__text: 0x42244
-  __TEXT.__auth_stubs: 0x1220
+3089.40.15.0.0
+  __TEXT.__text: 0x4236c
+  __TEXT.__auth_stubs: 0x1230
   __TEXT.__objc_methlist: 0x374
   __TEXT.__const: 0x630
-  __TEXT.__cstring: 0x773b
-  __TEXT.__oslogstring: 0x30b5
+  __TEXT.__cstring: 0x79cd
+  __TEXT.__oslogstring: 0x30ec
   __TEXT.__dof_libxpc: 0xa5d
-  __TEXT.__unwind_info: 0x1258
+  __TEXT.__unwind_info: 0x1260
   __TEXT.__objc_classname: 0x243
   __TEXT.__objc_methname: 0x1e2
   __TEXT.__objc_methtype: 0xb5

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x100
   __DATA_CONST.__objc_superrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x918
+  __AUTH_CONST.__auth_got: 0x920
   __AUTH_CONST.__const: 0x1af8
   __AUTH_CONST.__objc_const: 0x2338
   __AUTH.__objc_data: 0x50
-  __DATA.__data: 0xba8
+  __DATA.__data: 0xcf8
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x8
   __DATA.__bss: 0x88

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libunwind.dylib
-  UUID: C7D28DD7-F5FB-3D59-861E-3379F2C5FA10
-  Functions: 1910
-  Symbols:   4536
-  CStrings:  1359
+  UUID: C022ECE6-E6CE-32E5-8714-AE504E4D8066
+  Functions: 1912
+  Symbols:   4542
+  CStrings:  1368
 
Symbols:
+ ___block_descriptor_tmp.121
+ ___block_literal_global.123
+ ___block_literal_global.131
+ __xpc_connection_cancel.cold.1
+ __xpc_connection_cancelation_description
+ __xpc_connection_cancelation_get_description
+ _fmtcheck
- ___block_descriptor_tmp.114
- ___block_descriptor_tmp.122
- ___block_literal_global.116
- ___block_literal_global.124
Functions:
~ __xpc_connection_debug : 328 -> 364
~ __xpc_connection_dispose : 352 -> 328
~ __xpc_connection_bs_cancel : 144 -> 148
~ __xpc_connection_cancel : 164 -> 156
~ _do_mach_notify_send_once : 336 -> 332
~ __xpc_connection_activate_if_needed : 740 -> 752
~ _xpc_connection_send_message_with_reply_sync : 664 -> 660
~ _xpc_connection_copy_invalidation_reason : 32 -> 84
+ __xpc_connection_cancelation_get_description
~ __xpc_connection_handle_disconnect_event : 424 -> 420
~ __xpc_connection_init : 1952 -> 1936
~ __xpc_connection_init_failed : 460 -> 432
~ __xpc_connection_mach_event : 2064 -> 2020
~ __xpc_connection_handle_sent_event : 544 -> 540
+ __xpc_connection_cancel.cold.1
CStrings:
+ "%d %s"
+ "%x"
+ "Client is gone"
+ "Connection init failed at listener activation with error %d - %s"
+ "Connection init failed at lookup with error %d - %s"
+ "Connection init failed at no-senders registration with error %d - %s"
+ "Connection init failed at receive right creation with error %d - %s"
+ "Connection init failed at send right creation with error %d - %s"
+ "Connection init failed with error %d - %s)"
+ "Connection init failed with readying error with error %d - %s"
+ "Connection was released"
+ "Failed to check-in, peer may have been unloaded: mach_error=%x"
+ "Finalizing BS connection"
+ "Peer image changed"
+ "Reconnect failed at listener activation with error %d - %s"
+ "Reconnect failed at lookup with error %d - %s"
+ "Reconnect failed at no-senders registration with error %d - %s"
+ "Reconnect failed at receive right creation with error %d - %s"
+ "Reconnect failed at send right creation with error %d - %s"
+ "Reconnect failed with error %d - %s"
+ "Reconnect failed with readying error with error %d - %s"
+ "assertion failure: \"self->_cancelation.reason\" -> %llu"
- " (reconnect)"
- "client is gone"
- "connection was released"
- "failed at %s%s with error %d - %s"
- "failed to check-in, peer may have been unloaded: mach_error=%x"
- "finalizing BS connection"
- "listener activation"
- "lookup"
- "no-senders registration"
- "peer image changed"
- "readying error"
- "receive right creation"
- "send right creation"

```
