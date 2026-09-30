## RemoteXPC

> `/System/Library/PrivateFrameworks/RemoteXPC.framework/RemoteXPC`

```diff

-2866.80.6.0.0
-  __TEXT.__text: 0xf57c
-  __TEXT.__auth_stubs: 0xa00
-  __TEXT.__objc_methlist: 0x1a4
-  __TEXT.__const: 0xa0
+2894.100.71.502.1
+  __TEXT.__text: 0xf4cc
+  __TEXT.__auth_stubs: 0xa10
+  __TEXT.__objc_methlist: 0x2ac
+  __TEXT.__const: 0xa8
   __TEXT.__gcc_except_tab: 0x318
   __TEXT.__cstring: 0xb0a
-  __TEXT.__oslogstring: 0x2744
-  __TEXT.__unwind_info: 0x3e8
+  __TEXT.__oslogstring: 0x2722
+  __TEXT.__unwind_info: 0x400
   __TEXT.__objc_classname: 0xdf
   __TEXT.__objc_methname: 0x79e
   __TEXT.__objc_methtype: 0x28d

   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb8
+  __DATA_CONST.__objc_selrefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x510
+  __AUTH_CONST.__auth_got: 0x518
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__objc_const: 0x1178
+  __AUTH_CONST.__objc_const: 0xf88
   __DATA.__objc_ivar: 0x12c
   __DATA.__data: 0xc8
   __DATA_DIRTY.__objc_data: 0x230

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 354
-  Symbols:   614
-  CStrings:  460
+  Functions: 356
+  Symbols:   616
+  CStrings:  459
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "assertion failure: \"((self)->pending_streams_stqh_first == ((void*)0))\" -> %llu"
+ "assertion failure: \"_next\" -> %llu"
+ "assertion failure: \"_xpc_dictionary_get_reply_msg_id(message) == 0\" -> %llu"
+ "assertion failure: \"body_buf != ((void*)0) && body_len > 0\" -> %llu"
+ "assertion failure: \"canceled\" -> %llu"
+ "assertion failure: \"channel != ((void*)0)\" -> %llu"
+ "assertion failure: \"device != ((void*)0)\" -> %llu"
+ "assertion failure: \"direction != XPC_REMOTE_CHANNEL_STREAM_DIRECTION_DUPLEX\" -> %llu"
+ "assertion failure: \"direction != XPC_REMOTE_CHANNEL_STREAM_DIRECTION_MSG_ORIENTED\" -> %llu"
+ "assertion failure: \"done\" -> %llu"
+ "assertion failure: \"fd != -1\" -> %llu"
+ "assertion failure: \"fd == -1\" -> %llu"
+ "assertion failure: \"h2_parameters\" -> %llu"
+ "assertion failure: \"msg_id != 0\" -> %llu"
+ "assertion failure: \"ps->direction == XPC_REMOTE_CHANNEL_STREAM_DIRECTION_RX\" -> %llu"
+ "assertion failure: \"ps->direction == direction\" -> %llu"
+ "assertion failure: \"reply != ((void*)0)\" -> %llu"
+ "assertion failure: \"self\" -> %llu"
+ "assertion failure: \"self->root_channel == ((void*)0)\" -> %llu"
+ "assertion failure: \"self->root_channel == channel\" -> %llu"
+ "assertion failure: \"self->root_connection == ((void*)0)\" -> %llu"
+ "assertion failure: \"self->root_listener == ((void*)0)\" -> %llu"
+ "assertion failure: \"self->state != XPC_REMOTE_CHANNEL_STATE_CANCELED\" -> %llu"
+ "assertion failure: \"self->state == XPC_REMOTE_CHANNEL_STATE_WAITING\" -> %llu"
+ "assertion failure: \"self->stream_direction == XPC_REMOTE_CHANNEL_STREAM_DIRECTION_MSG_ORIENTED\" -> %llu"
+ "assertion failure: \"self->stream_io != ((void*)0)\" -> %llu"
+ "assertion failure: \"self->type != XPC_REMOTE_LISTENER_TYPE_RSD\" -> %llu"
+ "assertion failure: \"self.state <= XPC_REMOTE_CONNECTION_STATE_CONNECTED\" -> %llu"
+ "assertion failure: \"self.state == XPC_REMOTE_CONNECTION_STATE_CONNECTED\" -> %llu"
+ "assertion failure: \"self.state == XPC_REMOTE_CONNECTION_STATE_CONNECTING\" -> %llu"
+ "assertion failure: \"self.state == XPC_REMOTE_CONNECTION_STATE_INACTIVE\" -> %llu"
+ "assertion failure: \"self.state == XPC_REMOTE_CONNECTION_STATE_NOT_CONNECTED\" -> %llu"
+ "assertion failure: \"self.type != XPC_REMOTE_CONNECTION_TYPE_LISTENER\" -> %llu"
+ "assertion failure: \"self.type == XPC_REMOTE_CONNECTION_TYPE_LISTENER\" -> %llu"
+ "assertion failure: \"self.type == XPC_REMOTE_CONNECTION_TYPE_RSD\" -> %llu"
+ "assertion failure: \"stream_id != 0\" -> %llu"
- "Invalid teardown type %d"
- "assertion failure: \"((self)->pending_streams_stqh_first == ((void *)0))\" -> %lld"
- "assertion failure: \"_next\" -> %lld"
- "assertion failure: \"_xpc_dictionary_get_reply_msg_id(message) == 0\" -> %lld"
- "assertion failure: \"body_buf != ((void *)0) && body_len > 0\" -> %lld"
- "assertion failure: \"canceled\" -> %lld"
- "assertion failure: \"channel != ((void *)0)\" -> %lld"
- "assertion failure: \"device != ((void *)0)\" -> %lld"
- "assertion failure: \"direction != XPC_REMOTE_CHANNEL_STREAM_DIRECTION_DUPLEX\" -> %lld"
- "assertion failure: \"direction != XPC_REMOTE_CHANNEL_STREAM_DIRECTION_MSG_ORIENTED\" -> %lld"
- "assertion failure: \"done\" -> %lld"
- "assertion failure: \"fd != -1\" -> %lld"
- "assertion failure: \"fd == -1\" -> %lld"
- "assertion failure: \"h2_parameters\" -> %lld"
- "assertion failure: \"msg_id != 0\" -> %lld"
- "assertion failure: \"ps->direction == XPC_REMOTE_CHANNEL_STREAM_DIRECTION_RX\" -> %lld"
- "assertion failure: \"ps->direction == direction\" -> %lld"
- "assertion failure: \"reply != ((void *)0)\" -> %lld"
- "assertion failure: \"self\" -> %lld"
- "assertion failure: \"self->root_channel == ((void *)0)\" -> %lld"
- "assertion failure: \"self->root_channel == channel\" -> %lld"
- "assertion failure: \"self->root_connection == ((void *)0)\" -> %lld"
- "assertion failure: \"self->root_listener == ((void *)0)\" -> %lld"
- "assertion failure: \"self->state != XPC_REMOTE_CHANNEL_STATE_CANCELED\" -> %lld"
- "assertion failure: \"self->state == XPC_REMOTE_CHANNEL_STATE_WAITING\" -> %lld"
- "assertion failure: \"self->stream_direction == XPC_REMOTE_CHANNEL_STREAM_DIRECTION_MSG_ORIENTED\" -> %lld"
- "assertion failure: \"self->stream_io != ((void *)0)\" -> %lld"
- "assertion failure: \"self->type != XPC_REMOTE_LISTENER_TYPE_RSD\" -> %lld"
- "assertion failure: \"self.state <= XPC_REMOTE_CONNECTION_STATE_CONNECTED\" -> %lld"
- "assertion failure: \"self.state == XPC_REMOTE_CONNECTION_STATE_CONNECTED\" -> %lld"
- "assertion failure: \"self.state == XPC_REMOTE_CONNECTION_STATE_CONNECTING\" -> %lld"
- "assertion failure: \"self.state == XPC_REMOTE_CONNECTION_STATE_INACTIVE\" -> %lld"
- "assertion failure: \"self.state == XPC_REMOTE_CONNECTION_STATE_NOT_CONNECTED\" -> %lld"
- "assertion failure: \"self.type != XPC_REMOTE_CONNECTION_TYPE_LISTENER\" -> %lld"
- "assertion failure: \"self.type == XPC_REMOTE_CONNECTION_TYPE_LISTENER\" -> %lld"
- "assertion failure: \"self.type == XPC_REMOTE_CONNECTION_TYPE_RSD\" -> %lld"
- "assertion failure: \"stream_id != 0\" -> %lld"

```
