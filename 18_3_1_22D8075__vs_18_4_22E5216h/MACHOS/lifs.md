## lifs

> `/System/Library/Extensions/lifs.kext/lifs`

```diff

-474.60.43.0.0
+531.100.67.0.0
   __TEXT.__os_log: 0x12f9
-  __TEXT.__cstring: 0x217e
-  __TEXT.__const: 0x2d0
-  __TEXT_EXEC.__text: 0x1aca8
+  __TEXT.__cstring: 0x217f
+  __TEXT.__const: 0x2c0
+  __TEXT_EXEC.__text: 0x1ac48
   __TEXT_EXEC.__auth_stubs: 0xf80
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138
   __DATA.__bss: 0x90
   __DATA_CONST.__auth_got: 0x7c0
-  __DATA_CONST.__got: 0x88
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x16a0
   __DATA_CONST.__kalloc_type: 0xbc0
-  Functions: 405
-  Symbols:   3043
+  Functions: 400
+  Symbols:   3033
   CStrings:  393
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _lifatype_to_stype
+ _lifatype_to_vtype
+ lifs_clear_meta_blocks.cold.2
+ lifs_create_endio_context.kalloc_type_view_905
+ lifs_destroy_endio_context.kalloc_type_view_924
+ lifs_flush_meta_blocks.cold.2
+ lifs_fsync_internal.kalloc_type_view_3525
+ lifs_koio_done.kalloc_type_view_1890
+ lifs_mount.kalloc_type_view_614
+ lifs_mount.kalloc_type_view_640
+ lifs_mount.kalloc_type_view_641
+ lifs_mount.kalloc_type_view_811
+ lifs_mount.kalloc_type_view_857
+ lifs_mount.kalloc_type_view_861
+ lifs_mount.kalloc_type_view_865
+ lifs_purge_meta_blocks.cold.2
+ lifs_reclaim_done.kalloc_type_view_4437
+ lifs_setfsattr_done.kalloc_type_view_3456
+ lifs_submit_io.kalloc_type_view_1871
+ lifs_submit_koio.kalloc_type_view_1912
+ lifs_unmount.kalloc_type_view_999
+ lifs_vnop_ioctl.cold.1
+ lifs_vnop_readdir.kalloc_type_view_2666
+ lifs_vnop_readdir.kalloc_type_view_2668
+ lifs_vnop_readdir.kalloc_type_view_2763
+ lifs_vnop_readdir.kalloc_type_view_2765
+ lifs_vnop_reclaim.kalloc_type_view_4481
+ lifs_vnop_reclaim.kalloc_type_view_4535
+ lifs_vnop_strategy.cold.1
+ lifs_vnop_strategy.kalloc_type_view_1969
+ lifs_vnop_strategy_done.kalloc_type_view_1735
- lifs_create_endio_context.kalloc_type_view_885
- lifs_destroy_endio_context.kalloc_type_view_904
- lifs_fsync_internal.kalloc_type_view_3514
- lifs_koio_done.kalloc_type_view_1879
- lifs_mount.kalloc_type_view_599
- lifs_mount.kalloc_type_view_625
- lifs_mount.kalloc_type_view_626
- lifs_mount.kalloc_type_view_787
- lifs_mount.kalloc_type_view_833
- lifs_mount.kalloc_type_view_837
- lifs_mount.kalloc_type_view_841
- lifs_reclaim_done.kalloc_type_view_4426
- lifs_setfsattr_done.kalloc_type_view_3445
- lifs_submit_io.kalloc_type_view_1860
- lifs_submit_koio.kalloc_type_view_1901
- lifs_unmount.kalloc_type_view_975
- lifs_vnop_clonefile.cold.1
- lifs_vnop_create.cold.1
- lifs_vnop_dorename.cold.1
- lifs_vnop_dorename.cold.2
- lifs_vnop_link.cold.1
- lifs_vnop_lookup.cold.1
- lifs_vnop_mkdir.cold.1
- lifs_vnop_readdir.kalloc_type_view_2655
- lifs_vnop_readdir.kalloc_type_view_2657
- lifs_vnop_readdir.kalloc_type_view_2752
- lifs_vnop_readdir.kalloc_type_view_2754
- lifs_vnop_reclaim.kalloc_type_view_4470
- lifs_vnop_reclaim.kalloc_type_view_4524
- lifs_vnop_remove.cold.1
- lifs_vnop_rmdir.cold.1
- lifs_vnop_strategy.kalloc_type_view_1958
- lifs_vnop_strategy_done.kalloc_type_view_1724
- lifs_vnop_symlink.cold.1
CStrings:
+ "11122222222222222222222222222222222222222222222222332222122222222222222121111111112222222222222222122222221122"
- "1112222222222222222222222222222222222222222222222233222212222222222222121111111112222222222222222122222221122"

```
