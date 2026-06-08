## libBacktraceRecording.dylib

> `/usr/lib/libBacktraceRecording.dylib`

```diff

-64575.39.1.0.0
-  __TEXT.__text: 0x58b8
+64578.47.1.0.0
+  __TEXT.__text: 0x5948
   __TEXT.__auth_stubs: 0x3a0
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x70
   __TEXT.__cstring: 0x180b
   __TEXT.__unwind_info: 0x138
+  __DATA_CONST.__const: 0x298
   __DATA_CONST.__auth_got: 0x1d0
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x288
   __DATA.__data: 0x140
   __DATA.__common: 0x19
   __DATA.__bss: 0xfd
   - /usr/lib/libSystem.B.dylib
-  UUID: 29CA8402-7D4D-3320-9982-E610EE352ED3
+  UUID: DAEA0CB2-8144-38B7-82D7-D62C230098D0
   Functions: 64
   Symbols:   187
   CStrings:  178
Functions:
~ ___introspection_dispatch_queue_item_get_info : 432 -> 440
~ _dispatch_queue_serialnum : 60 -> 68
~ _gcd_queue_item_enqueue_hook : 1248 -> 1252
~ _add_queue_info_to_list : 456 -> 460
~ _find_or_create_queue_info : 324 -> 332
~ _resetDyldInsertLibraries : 432 -> 436
~ _print_logical_backtrace : 1480 -> 1488
~ _print_queue_item : 1600 -> 1604
~ _print_gcd_queue_create_dispose : 472 -> 476
~ _print_gcd_queue_item_enqueue_dequeue : 840 -> 844
~ _print_gcd_item_conflict : 592 -> 596
~ _print_gcd_queue_item_complete : 732 -> 768
~ _print_pthread_event : 584 -> 588
~ _print_backtrace : 568 -> 572
~ _enter_stack_in_backtrace_uniquing_table : 828 -> 836
~ _stack_frames_for_uniqued_stack : 268 -> 272
~ __enter_frames_in_table_while_locked : 296 -> 312
~ _print_dispatch_info : 548 -> 556
~ _print_logical_backtrace : 752 -> 756

```
