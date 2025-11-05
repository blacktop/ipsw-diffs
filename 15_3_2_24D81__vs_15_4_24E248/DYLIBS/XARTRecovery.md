## XARTRecovery

> `/System/Library/PrivateFrameworks/XARTRecovery.framework/Versions/A/XARTRecovery`

```diff

-842.60.8.0.0
-  __TEXT.__text: 0x19a4
+850.100.14.0.0
+  __TEXT.__text: 0x19a0
   __TEXT.__auth_stubs: 0x2b0
   __TEXT.__const: 0x78
   __TEXT.__gcc_except_tab: 0x50

   - /System/Library/PrivateFrameworks/EmbeddedOSSupportHost.framework/Versions/A/EmbeddedOSSupportHost
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8C9721D9-D66A-30B2-9962-4DE61780A370
+  UUID: 484793F1-B0A7-35B1-BC2B-7DAECD2F7039
   Functions: 62
   Symbols:   143
   CStrings:  54
Functions:
~ _xrec_directory_count : 32 -> 28
~ xart_msg_send_with_reply.cold.1 : 60 -> 96
~ xart_msg_send_with_reply.cold.3 : 132 -> 60
~ xart_msg_send_with_reply.cold.4 : 60 -> 132
~ xart_msg_send_with_reply.cold.6 : 96 -> 60
~ _xart_msg_log_bridge_xpc_error.cold.1 -> _xart_msg_log_bridge_xpc_error.cold.2 : 60 -> 128
~ _xart_msg_log_bridge_xpc_error.cold.2 -> _xart_msg_log_bridge_xpc_error.cold.3 : 128 -> 60
~ xart_msg_request_server_start.cold.1 : 44 -> 60
~ xart_msg_request_server_start.cold.3 : 60 -> 44
~ xrec_directory_fetch_snapshot.cold.4 : 60 -> 124
~ xrec_directory_fetch_snapshot.cold.5 : 124 -> 60

```
