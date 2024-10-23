## lifs

> `/System/Library/Extensions/lifs.kext/lifs`

```diff

-470.40.4.0.0
-  __TEXT.__os_log: 0x129b
-  __TEXT.__cstring: 0x21fb
+474.60.39.0.0
+  __TEXT.__os_log: 0x12f9
+  __TEXT.__cstring: 0x217e
   __TEXT.__const: 0x2d0
-  __TEXT_EXEC.__text: 0x1ab94
+  __TEXT_EXEC.__text: 0x1aca8
   __TEXT_EXEC.__auth_stubs: 0xf80
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138

   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x16a0
   __DATA_CONST.__kalloc_type: 0xbc0
-  Functions: 404
-  Symbols:   3034
-  CStrings:  396
+  Functions: 405
+  Symbols:   3043
+  CStrings:  393
 
Symbols:
+ _lifs_request_alloc_init
+ _lifs_request_free
+ _lifs_request_init
+ lifs_endio_thread._os_log_fmt.48
+ lifs_fsync_internal.kalloc_type_view_3514
+ lifs_io_strategy_thread._os_log_fmt.46
+ lifs_koio_blockmap._os_log_fmt.34
+ lifs_koio_done.kalloc_type_view_1879
+ lifs_mount.kalloc_type_view_833
+ lifs_mount.kalloc_type_view_837
+ lifs_mount.kalloc_type_view_841
+ lifs_reclaim_done.kalloc_type_view_4426
+ lifs_req_callback_thread._os_log_fmt.12
+ lifs_request_alloc_init._os_log_fmt
+ lifs_request_free.kalloc_type_view_210
+ lifs_request_init._os_log_fmt
+ lifs_setfsattr_done.kalloc_type_view_3445
+ lifs_setxattr_request._os_log_fmt.8
+ lifs_submit_io.kalloc_type_view_1860
+ lifs_submit_koio.kalloc_type_view_1901
+ lifs_unmount.kalloc_type_view_975
+ lifs_vnop_getxattr._os_log_fmt.30
+ lifs_vnop_mkdir._os_log_fmt.21
+ lifs_vnop_mmap._os_log_fmt.20
+ lifs_vnop_readdir._os_log_fmt.15
+ lifs_vnop_readdir._os_log_fmt.18
+ lifs_vnop_readdir._os_log_fmt.7
+ lifs_vnop_readdir.kalloc_type_view_2657
+ lifs_vnop_readdir.kalloc_type_view_2754
+ lifs_vnop_reclaim.kalloc_type_view_4470
+ lifs_vnop_reclaim.kalloc_type_view_4524
+ lifs_vnop_strategy.kalloc_type_view_1958
+ lifs_vnop_strategy_done.kalloc_type_view_1724
- lifs_endio_thread._os_log_fmt.49
- lifs_fsync_internal.kalloc_type_view_3513
- lifs_io_strategy_thread._os_log_fmt.47
- lifs_koio_blockmap._os_log_fmt.35
- lifs_koio_done.kalloc_type_view_1874
- lifs_mount.kalloc_type_view_827
- lifs_mount.kalloc_type_view_831
- lifs_mount.kalloc_type_view_835
- lifs_reclaim_done.kalloc_type_view_4425
- lifs_req_callback_thread._os_log_fmt.14
- lifs_request_done.cold.1
- lifs_request_free.kalloc_type_view_198
- lifs_setfsattr_done.kalloc_type_view_3444
- lifs_setxattr_request._os_log_fmt.10
- lifs_submit_io.kalloc_type_view_1855
- lifs_submit_koio.kalloc_type_view_1896
- lifs_unmount.kalloc_type_view_970
- lifs_vnop_getxattr._os_log_fmt.31
- lifs_vnop_mkdir._os_log_fmt.22
- lifs_vnop_mmap._os_log_fmt.21
- lifs_vnop_readdir._os_log_fmt.12
- lifs_vnop_readdir._os_log_fmt.17
- lifs_vnop_readdir._os_log_fmt.20
- lifs_vnop_readdir.kalloc_type_view_2653
- lifs_vnop_readdir.kalloc_type_view_2750
- lifs_vnop_reclaim.kalloc_type_view_4469
- lifs_vnop_reclaim.kalloc_type_view_4523
- lifs_vnop_strategy.cold.1
- lifs_vnop_strategy.kalloc_type_view_1953
- lifs_vnop_strategy_done.kalloc_type_view_1719
CStrings:
+ "1112222222222222222222222222222222222222222222222233222212222222222222121111111112222222222222222122222221122"
+ "lifs_request for opcode %!x(MISSING) outside valid range"
- "\"%!s(MISSING): lmp->io_strategy_q_cnt overflowed\" @%!s(MISSING):%!d(MISSING)"
- "\"%!s(MISSING): lmp->req_callback_q_cnt overflowed\" @%!s(MISSING):%!d(MISSING)"
- "111222222222222222222222222222222222222222222222223322221222222222222212111111111222222222222222212222221122"
- "lifs_comm.c"
- "lifs_vnop_strategy"

```
