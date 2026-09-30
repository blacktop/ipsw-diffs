## libdispatch.dylib

> `/usr/lib/system/introspection/libdispatch.dylib`

```diff

-  __TEXT.__text: 0x433e0
+  __TEXT.__text: 0x433d8
   __TEXT.__objc_methlist: 0x684
   __TEXT.__const: 0x820
   __TEXT.__cstring: 0x6483
-  __TEXT.__unwind_info: 0xe80
+  __TEXT.__unwind_info: 0xe88
   __TEXT.__eh_frame: 0xb8
   __TEXT.__objc_stubs: 0x1e0
   __TEXT.__auth_stubs: 0xd20
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__eh_frame : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__auth_got : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Functions:
~ __os_workgroup_lookup_type_from_workload_id : 164 -> 172
~ ___dispatch_io_create_with_path_block_invoke : 664 -> 668
~ _dispatch_data_copy_region : 356 -> 368
~ _dispatch_introspection_get_queues : 384 -> 364
~ _dispatch_introspection_get_queue_threads : 472 -> 460

```
