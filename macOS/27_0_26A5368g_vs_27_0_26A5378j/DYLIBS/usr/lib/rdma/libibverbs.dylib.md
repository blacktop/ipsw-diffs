## libibverbs.dylib

> `/usr/lib/rdma/libibverbs.dylib`

```diff

-  __TEXT.__text: 0xd778
+  __TEXT.__text: 0xd718
   __TEXT.__cstring: 0x12a9
   __TEXT.__const: 0x1f8
   __TEXT.__unwind_info: 0x330
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __DATA.__data : content changed
Functions:
~ _try_driver : 828 -> 784
~ _ibv_init_ah_from_wc : 496 -> 488
~ _ibv_cmd_post_recv : 404 -> 388
~ _ibv_cmd_post_srq_recv : 404 -> 388
~ _open_node_name_map : 960 -> 948

```
