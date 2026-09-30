## RemoteXPC

> `/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC`

```diff

-3089.0.11.0.0
-  __TEXT.__text: 0xf548
+3089.40.13.0.1
+  __TEXT.__text: 0xf774
   __TEXT.__auth_stubs: 0xa60
   __TEXT.__objc_methlist: 0x2ac
   __TEXT.__const: 0xa0
   __TEXT.__gcc_except_tab: 0x318
   __TEXT.__cstring: 0xb27
-  __TEXT.__oslogstring: 0x2786
-  __TEXT.__unwind_info: 0x410
+  __TEXT.__oslogstring: 0x27c5
+  __TEXT.__unwind_info: 0x418
   __TEXT.__objc_classname: 0xdf
   __TEXT.__objc_methname: 0x79e
   __TEXT.__objc_methtype: 0x28d
   __TEXT.__objc_stubs: 0x280
   __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x730
+  __DATA_CONST.__const: 0x758
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/RemoteServiceDiscovery.framework/RemoteServiceDiscovery
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 532E494A-E1F4-33F6-B809-73FE00F8F892
-  Functions: 353
-  Symbols:   1146
+  UUID: 94A810BB-8E8A-3A3C-8587-F1559568F552
+  Functions: 363
+  Symbols:   1173
   CStrings:  456
 
Symbols:
+ GCC_except_table188
+ GCC_except_table193
+ GCC_except_table194
+ GCC_except_table195
+ GCC_except_table196
+ GCC_except_table257
+ _OUTLINED_FUNCTION_23
+ ____xpc_remote_connection_handle_read_block_invoke_3.cold.1
+ ____xpc_remote_connection_send_reply_message_block_invoke.cold.2
+ ____xpc_remote_connection_wakeup_block_invoke.cold.2
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0i8ls32l8s48l8s40l8
+ ___xpc_remote_channel_create_block_invoke.30.cold.2
+ ___xpc_remote_channel_send_block_invoke.cold.1
+ ___xpc_remote_connection_send_barrier_block_invoke.cold.2
+ ___xpc_remote_connection_send_message_block_invoke.cold.2
+ ___xpc_remote_connection_send_message_block_invoke.cold.3
+ ___xpc_remote_connection_send_message_with_reply_block_invoke.cold.3
+ __xpc_remote_channel_deliver_message.cold.1
+ __xpc_remote_connection_wakeup.cold.3
- GCC_except_table184
- GCC_except_table185
- GCC_except_table186
- GCC_except_table191
- GCC_except_table192
- GCC_except_table251
CStrings:
+ "[%p] Delivering message %llu to handler"
+ "[%p] Enqueueing message for send"
+ "[%p] Enqueueing send barrier"
+ "[%p] Message %llu send completed successfully"
+ "[%p] Message %llx send completed"
+ "[%p] PING sent successfully"
+ "[%p] Reply message send completed"
+ "[%p] Send of message %llx initiated"
+ "[%p] Sending reply message"
- "Delivering %llu"
- "[%p] Enqueueing barrier"
- "[%p] Enqueueing outgoing message"
- "[%p] Reply send completed"
- "[%p] Send completed"
- "[%p] Send initiated"
- "[%p] Send of msg_id %llu completed successfully"
- "[%p] Sending outgoing reply"
- "[%p] Successfully sent PING"

```
