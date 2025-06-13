## lifs

> `/System/Library/Extensions/lifs.kext/lifs`

```diff

-208.0.17.0.2
+208.42.1.0.0
   __TEXT.__os_log: 0x10fa
-  __TEXT.__cstring: 0x1bd8
+  __TEXT.__cstring: 0x1c42
   __TEXT.__const: 0x270
-  __TEXT_EXEC.__text: 0x18d6c
-  __TEXT_EXEC.__auth_stubs: 0xe40
+  __TEXT_EXEC.__text: 0x18fc8
+  __TEXT_EXEC.__auth_stubs: 0xe90
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138
   __DATA.__bss: 0x50
-  __DATA_CONST.__auth_got: 0x720
+  __DATA_CONST.__auth_got: 0x748
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x1670
-  __DATA_CONST.__kalloc_type: 0xa40
-  UUID: 5BD1356D-BBA5-32FB-ABC6-7D88B42ECE6B
-  Functions: 296
-  Symbols:   2725
-  CStrings:  334
+  __DATA_CONST.__kalloc_type: 0xac0
+  UUID: 63E8F605-DA40-3E4C-8C5A-3842C591D094
+  Functions: 297
+  Symbols:   2739
+  CStrings:  337
 
Symbols:
+ _buf_setfilter
+ _lifs_koio_done
+ _os_ref_init_count_external
+ _os_ref_release_barrier_external
+ _os_ref_retain_external
+ _vcount
+ lifs_create_endio_context.kalloc_type_view_699
+ lifs_destroy_endio_context.kalloc_type_view_718
+ lifs_endio_thread._os_log_fmt.59
+ lifs_io_strategy_thread._os_log_fmt.57
+ lifs_koio_done.kalloc_type_view_1678
+ lifs_mount.kalloc_type_view_518
+ lifs_mount.kalloc_type_view_544
+ lifs_mount.kalloc_type_view_545
+ lifs_mount.kalloc_type_view_679
+ lifs_mount.kalloc_type_view_711
+ lifs_mount.kalloc_type_view_715
+ lifs_mount.kalloc_type_view_719
+ lifs_submit_io.kalloc_type_view_1649
+ lifs_submit_koio.kalloc_type_view_1703
+ lifs_unmount.kalloc_type_view_828
+ lifs_vnop_readdir.kalloc_type_view_2354
+ lifs_vnop_readdir.kalloc_type_view_2356
+ lifs_vnop_readdir.kalloc_type_view_2438
+ lifs_vnop_readdir.kalloc_type_view_2440
+ lifs_vnop_reclaim.kalloc_type_view_3943
+ lifs_vnop_strategy.kalloc_type_view_1760
+ lifs_vnop_strategy_done.kalloc_type_view_1513
- lifs_create_endio_context.kalloc_type_view_692
- lifs_destroy_endio_context.kalloc_type_view_711
- lifs_endio_thread._os_log_fmt.57
- lifs_io_strategy_thread._os_log_fmt.55
- lifs_mount.kalloc_type_view_470
- lifs_mount.kalloc_type_view_496
- lifs_mount.kalloc_type_view_497
- lifs_mount.kalloc_type_view_629
- lifs_mount.kalloc_type_view_661
- lifs_mount.kalloc_type_view_665
- lifs_mount.kalloc_type_view_669
- lifs_submit_io.kalloc_type_view_1642
- lifs_unmount.kalloc_type_view_778
- lifs_vnop_readdir.kalloc_type_view_2285
- lifs_vnop_readdir.kalloc_type_view_2287
- lifs_vnop_readdir.kalloc_type_view_2369
- lifs_vnop_readdir.kalloc_type_view_2371
- lifs_vnop_reclaim.kalloc_type_view_3874
- lifs_vnop_strategy.kalloc_type_view_1691
- lifs_vnop_strategy_done.kalloc_type_view_1506
CStrings:
+ "%s: no volume found for client %p in container %p with fd %d\n"
+ "11122222222222222222222222222222222222222222222222332222122222222222221211111111122222222222222221222222"
+ "lifs_close_device"
+ "site.lifs_koio_context_t"
- "1112222222222222222222222222222222222222222222222233222212222222222222121111111112222222222222222122222"

```
