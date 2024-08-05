## lifs

> `/System/Library/Extensions/lifs.kext/lifs`

```diff

-445.0.0.0.0
-  __TEXT.__os_log: 0x1278
-  __TEXT.__cstring: 0x21bd
+465.0.0.0.1
+  __TEXT.__os_log: 0x129b
+  __TEXT.__cstring: 0x21fb
   __TEXT.__const: 0x2d0
-  __TEXT_EXEC.__text: 0x1a8b4
+  __TEXT_EXEC.__text: 0x1ab94
   __TEXT_EXEC.__auth_stubs: 0xf80
   __DATA.__data: 0x5d0
   __DATA.__common: 0x138
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x90
   __DATA_CONST.__auth_got: 0x7c0
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x16a0
-  __DATA_CONST.__kalloc_type: 0xb40
-  Functions: 400
-  Symbols:   3006
-  CStrings:  394
+  __DATA_CONST.__kalloc_type: 0xbc0
+  Functions: 404
+  Symbols:   3034
+  CStrings:  396
 
Symbols:
+ __ZL16lifs_volume_releP16lifs_iouc_volume
+ __ZL16lifs_volume_releP16lifs_iouc_volume
+ __ZZL24lifs_destroy_iouc_volumeP19lifs_iouc_containerP16lifs_iouc_volumeE20kalloc_type_view_187
+ __ZZL24lifs_destroy_iouc_volumeP19lifs_iouc_containerP16lifs_iouc_volumeE20kalloc_type_view_187
+ __ZZL26lifs_create_iouc_containeriiE20kalloc_type_view_207
+ __ZZL26lifs_create_iouc_containeriiE20kalloc_type_view_207
+ __ZZL27lifs_destroy_iouc_containeriiE20kalloc_type_view_244
+ __ZZL27lifs_destroy_iouc_containeriiE20kalloc_type_view_244
+ __ZZN19AppleLIFSUserClient18methodOpenKernelFDEPS_PvP25IOExternalMethodArgumentsE20kalloc_type_view_972
+ __ZZN19AppleLIFSUserClient18methodOpenKernelFDEPS_PvP25IOExternalMethodArgumentsE20kalloc_type_view_972
+ _cache_lookup_ext
+ _handle_enoent_from_lookup
+ _handle_enoent_from_lookup
+ _invalidFH
+ _invalidFH
+ _lifs_setfsattr_done
+ _lifs_setfsattr_done
+ _lifs_setfsattr_request_async
+ _lifs_setfsattr_request_async
+ lifs_create_endio_context.kalloc_type_view_885
+ lifs_create_endio_context.kalloc_type_view_885
+ lifs_destroy_endio_context.kalloc_type_view_904
+ lifs_destroy_endio_context.kalloc_type_view_904
+ lifs_endio_thread._os_log_fmt.49
+ lifs_endio_thread._os_log_fmt.49
+ lifs_fsync_internal.kalloc_type_view_3513
+ lifs_fsync_internal.kalloc_type_view_3513
+ lifs_io_strategy_thread._os_log_fmt.47
+ lifs_io_strategy_thread._os_log_fmt.47
+ lifs_koio_done.kalloc_type_view_1874
+ lifs_koio_done.kalloc_type_view_1874
+ lifs_reclaim_done.kalloc_type_view_4425
+ lifs_reclaim_done.kalloc_type_view_4425
+ lifs_setfsattr_done.kalloc_type_view_3444
+ lifs_setfsattr_done.kalloc_type_view_3444
+ lifs_setfsattr_request_async._os_log_fmt
+ lifs_setfsattr_request_async._os_log_fmt
+ lifs_submit_io.kalloc_type_view_1855
+ lifs_submit_io.kalloc_type_view_1855
+ lifs_submit_koio.kalloc_type_view_1896
+ lifs_submit_koio.kalloc_type_view_1896
+ lifs_vnop_readdir.kalloc_type_view_2653
+ lifs_vnop_readdir.kalloc_type_view_2653
+ lifs_vnop_readdir.kalloc_type_view_2655
+ lifs_vnop_readdir.kalloc_type_view_2655
+ lifs_vnop_readdir.kalloc_type_view_2750
+ lifs_vnop_readdir.kalloc_type_view_2750
+ lifs_vnop_readdir.kalloc_type_view_2752
+ lifs_vnop_readdir.kalloc_type_view_2752
+ lifs_vnop_reclaim.kalloc_type_view_4469
+ lifs_vnop_reclaim.kalloc_type_view_4469
+ lifs_vnop_reclaim.kalloc_type_view_4523
+ lifs_vnop_reclaim.kalloc_type_view_4523
+ lifs_vnop_strategy.kalloc_type_view_1953
+ lifs_vnop_strategy.kalloc_type_view_1953
+ lifs_vnop_strategy_done.kalloc_type_view_1719
+ lifs_vnop_strategy_done.kalloc_type_view_1719
- __ZZL24lifs_destroy_iouc_volumeP19lifs_iouc_containerP16lifs_iouc_volumeE20kalloc_type_view_172
- __ZZL24lifs_destroy_iouc_volumeP19lifs_iouc_containerP16lifs_iouc_volumeE20kalloc_type_view_172
- __ZZL26lifs_create_iouc_containeriiE20kalloc_type_view_192
- __ZZL26lifs_create_iouc_containeriiE20kalloc_type_view_192
- __ZZL27lifs_destroy_iouc_containeriiE20kalloc_type_view_229
- __ZZL27lifs_destroy_iouc_containeriiE20kalloc_type_view_229
- __ZZN19AppleLIFSUserClient18methodOpenKernelFDEPS_PvP25IOExternalMethodArgumentsE20kalloc_type_view_957
- __ZZN19AppleLIFSUserClient18methodOpenKernelFDEPS_PvP25IOExternalMethodArgumentsE20kalloc_type_view_957
- _cache_lookup
- lifs_create_endio_context.kalloc_type_view_880
- lifs_create_endio_context.kalloc_type_view_880
- lifs_destroy_endio_context.kalloc_type_view_899
- lifs_destroy_endio_context.kalloc_type_view_899
- lifs_endio_thread._os_log_fmt.48
- lifs_endio_thread._os_log_fmt.48
- lifs_io_strategy_thread._os_log_fmt.46
- lifs_io_strategy_thread._os_log_fmt.46
- lifs_koio_done.kalloc_type_view_1869
- lifs_koio_done.kalloc_type_view_1869
- lifs_reclaim_done.kalloc_type_view_4327
- lifs_reclaim_done.kalloc_type_view_4327
- lifs_submit_io.kalloc_type_view_1850
- lifs_submit_io.kalloc_type_view_1850
- lifs_submit_koio.kalloc_type_view_1891
- lifs_submit_koio.kalloc_type_view_1891
- lifs_vnop_readdir.kalloc_type_view_2648
- lifs_vnop_readdir.kalloc_type_view_2648
- lifs_vnop_readdir.kalloc_type_view_2650
- lifs_vnop_readdir.kalloc_type_view_2650
- lifs_vnop_readdir.kalloc_type_view_2745
- lifs_vnop_readdir.kalloc_type_view_2745
- lifs_vnop_readdir.kalloc_type_view_2747
- lifs_vnop_readdir.kalloc_type_view_2747
- lifs_vnop_reclaim.kalloc_type_view_4371
- lifs_vnop_reclaim.kalloc_type_view_4371
- lifs_vnop_reclaim.kalloc_type_view_4425
- lifs_vnop_reclaim.kalloc_type_view_4425
- lifs_vnop_strategy.kalloc_type_view_1948
- lifs_vnop_strategy.kalloc_type_view_1948
- lifs_vnop_strategy_done.kalloc_type_view_1714
- lifs_vnop_strategy_done.kalloc_type_view_1714
CStrings:
+ "11111222222222"
+ "lifs_setfsattr_request_async"
+ "site.lifs_setfsattr_context_t"
- "11111222222"

```
