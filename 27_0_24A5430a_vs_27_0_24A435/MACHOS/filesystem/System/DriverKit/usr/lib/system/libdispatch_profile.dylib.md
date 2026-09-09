## libdispatch_profile.dylib

> `/System/DriverKit/usr/lib/system/libdispatch_profile.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__dof_dispatch`
- `__TEXT.__dof_voucher`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__auth_got`
- `__AUTH.__data`

```diff

 1605.0.2.0.0
-  __TEXT.__text: 0x496dc
+  __TEXT.__text: 0x4973c
   __TEXT.__const: 0x7a0
   __TEXT.__cstring: 0x6493
   __TEXT.__dof_dispatch: 0x4712
Functions:
~ __dispatch_workloop_invoke : 4116 -> 4124
~ __dispatch_root_queue_push_override_stealer : 400 -> 384
~ __dispatch_apply_with_attr_f : 1824 -> 1836
~ _voucher_activity_create_with_data_2 : 2544 -> 2548
~ _voucher_activity_flush : 364 -> 368
~ _voucher_activity_trace_v_2 : 2228 -> 2236
~ _firehose_buffer_ring_enqueue : 636 -> 628
~ _firehose_buffer_tracepoint_reserve_slow : 1024 -> 1040
~ _firehose_buffer_stream_chunk_install : 1192 -> 1196
~ _firehose_buffer_tracepoint_reserve_wait_for_chunks_from_logd : 1196 -> 1204
~ _firehose_client_start_quarantine : 1032 -> 1044
~ __dispatch_alloc_continuation_alloc : 268 -> 280
~ __dispatch_alloc_continuation_free : 188 -> 196
~ __dispatch_alloc_continuation_from_heap : 420 -> 440
~ __dispatch_alloc_maybe_madvise_page : 248 -> 252
```
