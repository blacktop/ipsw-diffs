## libmlx5.dylib

> `/usr/lib/rdma/libmlx5.dylib`

```diff

   __TEXT.__init_offsets: 0x4
   __TEXT.__cstring: 0xb13
   __TEXT.__const: 0x23a0
-  __TEXT.__unwind_info: 0x860
+  __TEXT.__unwind_info: 0x868
   __TEXT.__eh_frame: 0x48
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x38
Sections:
~ __TEXT.__init_offsets : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__data : content changed
Functions:
~ _dr_ste_build_ste_arr : 324 -> 280
~ _mlx5_store_uidx : 276 -> 288
~ _mlx5_alloc_dbrec : 528 -> 532
~ _dr_ste_v1_set_action_decap_l3_list : 320 -> 336
~ _dr_buddy_alloc_mem : 376 -> 392
~ _dr_buddy_free_mem : 256 -> 272
~ _copy_to_scat : 216 -> 196

```
