## lifs

> `/System/Library/Extensions/lifs.kext/lifs`

```diff

-531.120.13.0.0
+531.120.18.0.0
   __TEXT.__os_log: 0x12f9
   __TEXT.__cstring: 0x217f
   __TEXT.__const: 0x2c0
-  __TEXT_EXEC.__text: 0x1ac48
-  __TEXT_EXEC.__auth_stubs: 0xf80
+  __TEXT_EXEC.__text: 0x1b138
+  __TEXT_EXEC.__auth_stubs: 0xfa0
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138
   __DATA.__bss: 0x90
-  __DATA_CONST.__auth_got: 0x7c0
+  __DATA_CONST.__auth_got: 0x7d0
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x16a0
   __DATA_CONST.__kalloc_type: 0xbc0
-  Functions: 400
-  Symbols:   3033
+  Functions: 401
+  Symbols:   3040
   CStrings:  393
 
Symbols:
+ _lifs_get_extent_layout
+ _ubc_is_mapped_writable
+ _ubc_msync
+ lifs_create_endio_context.kalloc_type_view_1071
+ lifs_destroy_endio_context.kalloc_type_view_1090
+ lifs_fsync_internal.kalloc_type_view_3694
+ lifs_koio_done.kalloc_type_view_2058
+ lifs_reclaim_done.kalloc_type_view_4606
+ lifs_setfsattr_done.kalloc_type_view_3625
+ lifs_submit_io.kalloc_type_view_2039
+ lifs_submit_koio.kalloc_type_view_2080
+ lifs_vnop_readdir.kalloc_type_view_2835
+ lifs_vnop_readdir.kalloc_type_view_2837
+ lifs_vnop_readdir.kalloc_type_view_2932
+ lifs_vnop_readdir.kalloc_type_view_2934
+ lifs_vnop_reclaim.kalloc_type_view_4650
+ lifs_vnop_reclaim.kalloc_type_view_4704
+ lifs_vnop_strategy.kalloc_type_view_2137
+ lifs_vnop_strategy_done.kalloc_type_view_1903
- lifs_create_endio_context.kalloc_type_view_905
- lifs_destroy_endio_context.kalloc_type_view_924
- lifs_fsync_internal.kalloc_type_view_3525
- lifs_koio_done.kalloc_type_view_1890
- lifs_reclaim_done.kalloc_type_view_4437
- lifs_setfsattr_done.kalloc_type_view_3456
- lifs_submit_io.kalloc_type_view_1871
- lifs_submit_koio.kalloc_type_view_1912
- lifs_vnop_readdir.kalloc_type_view_2666
- lifs_vnop_readdir.kalloc_type_view_2668
- lifs_vnop_readdir.kalloc_type_view_2763
- lifs_vnop_readdir.kalloc_type_view_2765
- lifs_vnop_reclaim.kalloc_type_view_4481
- lifs_vnop_reclaim.kalloc_type_view_4535
- lifs_vnop_strategy.kalloc_type_view_1969
- lifs_vnop_strategy_done.kalloc_type_view_1735

```
