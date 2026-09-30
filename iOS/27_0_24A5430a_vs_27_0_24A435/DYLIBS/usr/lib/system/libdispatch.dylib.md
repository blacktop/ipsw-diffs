## libdispatch.dylib

> `/usr/lib/system/libdispatch.dylib`

```diff

 1605.0.2.0.0
-  __TEXT.__text: 0x3de44
+  __TEXT.__text: 0x3de60
   __TEXT.__objc_methlist: 0x684
   __TEXT.__const: 0x750
   __TEXT.__cstring: 0x61a0
-  __TEXT.__unwind_info: 0xde8
+  __TEXT.__unwind_info: 0xde0
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
Functions:
~ __dispatch_workloop_invoke : 2200 -> 2204
~ __dispatch_root_queue_push_override_stealer : 396 -> 380
~ __dispatch_event_loop_drain_timers : 1208 -> 1168
~ _voucher_activity_create_with_data_2 : 2200 -> 2208
~ _voucher_activity_flush : 364 -> 368
~ _voucher_activity_trace_v_2 : 2028 -> 2020
~ _firehose_buffer_ring_enqueue : 636 -> 628
~ _firehose_buffer_tracepoint_reserve_slow : 1032 -> 1048
~ _firehose_buffer_stream_chunk_install : 1068 -> 1072
~ _firehose_buffer_tracepoint_reserve_wait_for_chunks_from_logd : 1152 -> 1160
~ _firehose_client_start_quarantine : 1028 -> 1040
~ __dispatch_alloc_continuation_alloc : 260 -> 272
~ __dispatch_alloc_continuation_free : 188 -> 196
~ __dispatch_alloc_continuation_from_heap : 420 -> 440
~ __dispatch_alloc_maybe_madvise_page : 244 -> 248
```
