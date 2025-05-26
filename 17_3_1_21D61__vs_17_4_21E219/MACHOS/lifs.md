## lifs

> `/System/Library/Extensions/lifs.kext/lifs`

```diff

-208.80.5.0.0
-  __TEXT.__os_log: 0x1190
-  __TEXT.__cstring: 0x1d00
-  __TEXT.__const: 0x270
-  __TEXT_EXEC.__text: 0x19b58
-  __TEXT_EXEC.__auth_stubs: 0xf10
+208.100.36.0.3
+  __TEXT.__os_log: 0x11c5
+  __TEXT.__cstring: 0x1d28
+  __TEXT.__const: 0x290
+  __TEXT_EXEC.__text: 0x19f38
+  __TEXT_EXEC.__auth_stubs: 0xf20
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138
   __DATA.__bss: 0x50
-  __DATA_CONST.__auth_got: 0x788
+  __DATA_CONST.__auth_got: 0x790
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x1688
   __DATA_CONST.__kalloc_type: 0xb40
-  Functions: 302
-  Symbols:   2784
-  CStrings:  352
+  Functions: 304
+  Symbols:   2852
+  CStrings:  355
 
Symbols:
+ _clock_interval_to_deadline
+ _lifs_fsync_internal
+ _lifs_meta_sync_call
+ _lifs_schedule_meta_flush
+ _strlcpy
+ _thread_call_enter_delayed
+ _vnode_ref
+ _vnode_rele
+ lifs_create_endio_context.kalloc_type_view_859
+ lifs_destroy_endio_context.kalloc_type_view_878
+ lifs_endio_thread._os_log_fmt.66
+ lifs_io_strategy_thread._os_log_fmt.64
+ lifs_koio_blockmap._os_log_fmt
+ lifs_koio_done.kalloc_type_view_1853
+ lifs_mount.kalloc_type_view_581
+ lifs_mount.kalloc_type_view_607
+ lifs_mount.kalloc_type_view_608
+ lifs_mount.kalloc_type_view_798
+ lifs_mount.kalloc_type_view_802
+ lifs_mount.kalloc_type_view_806
+ lifs_reclaim_done.kalloc_type_view_4166
+ lifs_submit_io.kalloc_type_view_1824
+ lifs_submit_koio.kalloc_type_view_1878
+ lifs_unmount.kalloc_type_view_927
+ lifs_vnop_clonefile.cold.1
+ lifs_vnop_create.cold.1
+ lifs_vnop_dorename.cold.1
+ lifs_vnop_dorename.cold.2
+ lifs_vnop_link.cold.1
+ lifs_vnop_lookup.cold.1
+ lifs_vnop_mkdir.cold.1
+ lifs_vnop_readdir.kalloc_type_view_2564
+ lifs_vnop_readdir.kalloc_type_view_2566
+ lifs_vnop_readdir.kalloc_type_view_2648
+ lifs_vnop_readdir.kalloc_type_view_2650
+ lifs_vnop_reclaim.kalloc_type_view_4210
+ lifs_vnop_reclaim.kalloc_type_view_4262
+ lifs_vnop_remove.cold.1
+ lifs_vnop_rmdir.cold.1
+ lifs_vnop_strategy.kalloc_type_view_1935
+ lifs_vnop_strategy_done.kalloc_type_view_1688
+ lifs_vnop_symlink.cold.1
- ___memcpy_chk
- ___memmove_chk
- ___strlcpy_chk
- _memset
- lifs_create_endio_context.kalloc_type_view_857
- lifs_destroy_endio_context.kalloc_type_view_876
- lifs_endio_thread._os_log_fmt.65
- lifs_io_strategy_thread._os_log_fmt.63
- lifs_koio_done.kalloc_type_view_1839
- lifs_mount.kalloc_type_view_549
- lifs_mount.kalloc_type_view_575
- lifs_mount.kalloc_type_view_576
- lifs_mount.kalloc_type_view_718
- lifs_mount.kalloc_type_view_754
- lifs_mount.kalloc_type_view_762
- lifs_reclaim_done.kalloc_type_view_4107
- lifs_submit_io.kalloc_type_view_1810
- lifs_submit_koio.kalloc_type_view_1864
- lifs_unmount.kalloc_type_view_877
- lifs_vnop_readdir.kalloc_type_view_2533
- lifs_vnop_readdir.kalloc_type_view_2535
- lifs_vnop_readdir.kalloc_type_view_2617
- lifs_vnop_readdir.kalloc_type_view_2619
- lifs_vnop_reclaim.kalloc_type_view_4151
- lifs_vnop_reclaim.kalloc_type_view_4203
- lifs_vnop_strategy.kalloc_type_view_1921
- lifs_vnop_strategy_done.kalloc_type_view_1674
CStrings:
+ "%s: copyObjectForPortNameInTask for port %d returned %d\n"
+ "%s: no extent found for lnode %p offset %lld size %u"
+ "111222222222222222222222222222222222222222222222223322221222222222222212111111111222222222222222212222221122"
+ "lifs_koio_blockmap"
+ "methodGetVolumePortReply"
- "%s: copyObjectForPortNameInTask for task %p port %d error %d\n"
- "11122222222222222222222222222222222222222222222222332222122222222222221211111111122222222222222221222222122"

```
