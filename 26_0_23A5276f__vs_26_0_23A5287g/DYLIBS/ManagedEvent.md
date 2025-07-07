## ManagedEvent

> `/System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/ManagedEvent.framework/ManagedEvent`

```diff

-2138.0.0.0.0
+2144.0.0.0.0
   __TEXT.__text: 0xa8c
   __TEXT.__auth_stubs: 0x1d0
   __TEXT.__const: 0x18
   __TEXT.__oslogstring: 0x184
   __TEXT.__cstring: 0x776
-  __TEXT.__unwind_info: 0x88
+  __TEXT.__unwind_info: 0x90
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__const: 0xe0
   __AUTH_CONST.__auth_got: 0xe8

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
-  UUID: C560CA57-BC5A-32BD-9F43-7883D53B392A
+  UUID: 518FA7BF-E096-3690-9024-02165B7B5BD9
   Functions: 16
   Symbols:   164
   CStrings:  95
Functions:
~ ___managed_event_send_with_reply_block_invoke -> ___managed_event_fetch_helper_block_invoke : 392 -> 524
~ ___managed_event_fetch_helper_block_invoke -> ___managed_event_compose_from_xpc_object_block_invoke : 524 -> 324
~ ___managed_event_compose_from_xpc_object_block_invoke -> _managed_event_fetch_completion : 324 -> 224
~ _managed_event_fetch_completion -> ___managed_event_send_with_reply_block_invoke : 224 -> 392
~ ___managed_event_send_with_reply_block_invoke.1 -> _managed_event_fetch_series : 20 -> 176
~ _managed_event_fetch_series -> ___managed_event_get_queue_block_invoke : 176 -> 44
~ ___managed_event_get_queue_block_invoke -> ___managed_event_get_connection_block_invoke : 44 -> 468
~ ___managed_event_get_connection_block_invoke -> _managed_event_param_change : 468 -> 8
~ _managed_event_param_read_multiple -> _managed_event_send_with_reply.cold.1 : 8 -> 20

```
