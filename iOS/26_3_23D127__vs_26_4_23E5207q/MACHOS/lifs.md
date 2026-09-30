## lifs

> `/System/Library/Extensions/lifs.kext/lifs`

```diff

-737.80.2.0.0
-  __TEXT.__os_log: 0x13e3
-  __TEXT.__cstring: 0x2226
+737.100.107.0.0
+  __TEXT.__os_log: 0x1385
+  __TEXT.__cstring: 0x21a0
   __TEXT.__const: 0x2c0
-  __TEXT_EXEC.__text: 0x1bad0
-  __TEXT_EXEC.__auth_stubs: 0xff0
-  __DATA.__data: 0x5d0
-  __DATA.__common: 0x138
+  __TEXT_EXEC.__text: 0x1acbc
+  __TEXT_EXEC.__auth_stubs: 0xf60
+  __DATA.__data: 0x528
+  __DATA.__common: 0x130
   __DATA.__bss: 0x90
-  __DATA_CONST.__auth_got: 0x7f8
-  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__auth_got: 0x7b0
+  __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
   __DATA_CONST.__const: 0x16b8
   __DATA_CONST.__kalloc_type: 0xbc0
   __DATA_CONST.__kalloc_var: 0xf0
-  UUID: B401263A-4F9E-3807-900C-34771770D4B1
-  Functions: 406
-  Symbols:   3086
-  CStrings:  403
+  UUID: 73F73E23-E005-3AB3-9CD0-66794E78A452
+  Functions: 402
+  Symbols:   3042
+  CStrings:  398
 
Symbols:
+ /Library/Caches/com.apple.xbs/AC617D1B-B752-42B1-9DC0-1B06A595E694/TemporaryDirectory.ZqsF9Y/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/DerivedSources/
+ /Library/Caches/com.apple.xbs/AC617D1B-B752-42B1-9DC0-1B06A595E694/TemporaryDirectory.ZqsF9Y/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/IOCancelationWrapper.o
+ /Library/Caches/com.apple.xbs/AC617D1B-B752-42B1-9DC0-1B06A595E694/TemporaryDirectory.ZqsF9Y/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/IOWrappedMemoryDescriptor.o
+ /Library/Caches/com.apple.xbs/AC617D1B-B752-42B1-9DC0-1B06A595E694/TemporaryDirectory.ZqsF9Y/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/lifs_comm.o
+ /Library/Caches/com.apple.xbs/AC617D1B-B752-42B1-9DC0-1B06A595E694/TemporaryDirectory.ZqsF9Y/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/lifs_extent.o
+ /Library/Caches/com.apple.xbs/AC617D1B-B752-42B1-9DC0-1B06A595E694/TemporaryDirectory.ZqsF9Y/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/lifs_info.o
+ /Library/Caches/com.apple.xbs/AC617D1B-B752-42B1-9DC0-1B06A595E694/TemporaryDirectory.ZqsF9Y/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/lifs_iokit.o
+ /Library/Caches/com.apple.xbs/AC617D1B-B752-42B1-9DC0-1B06A595E694/TemporaryDirectory.ZqsF9Y/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/lifs_kext.o
+ /Library/Caches/com.apple.xbs/AC617D1B-B752-42B1-9DC0-1B06A595E694/TemporaryDirectory.ZqsF9Y/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/lifs_mig.o
+ /Library/Caches/com.apple.xbs/AC617D1B-B752-42B1-9DC0-1B06A595E694/TemporaryDirectory.ZqsF9Y/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/lifs_subr.o
+ /Library/Caches/com.apple.xbs/AC617D1B-B752-42B1-9DC0-1B06A595E694/TemporaryDirectory.ZqsF9Y/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/lifs_vfsops.o
+ /Library/Caches/com.apple.xbs/AC617D1B-B752-42B1-9DC0-1B06A595E694/TemporaryDirectory.ZqsF9Y/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/lifs_vnops.o
+ /Library/Caches/com.apple.xbs/AC617D1B-B752-42B1-9DC0-1B06A595E694/TemporaryDirectory.ZqsF9Y/Sources/FSKit_FileProvider/lifs_kext/
+ _OUTLINED_FUNCTION_1
+ __ZZL24lifs_destroy_iouc_volumeP19lifs_iouc_containerP16lifs_iouc_volumeE20kalloc_type_view_189
+ __ZZL26lifs_create_iouc_containeriiE20kalloc_type_view_209
+ __ZZL27lifs_destroy_iouc_containeriiE20kalloc_type_view_246
+ __ZZN19AppleLIFSUserClient18methodOpenKernelFDEPS_PvP25IOExternalMethodArgumentsE20kalloc_type_view_974
+ add_sillyrename_entry.kalloc_type_view_1955
+ add_sillyrename_entry.kalloc_type_view_1978
+ cleanup_sillyrename_entries.kalloc_type_view_2068
+ lifs_create_endio_context.kalloc_type_view_1081
+ lifs_create_node.kalloc_type_view_435
+ lifs_create_node.kalloc_type_view_590
+ lifs_destroy_endio_context.kalloc_type_view_1100
+ lifs_fsync_internal.kalloc_type_view_3800
+ lifs_koio_done.kalloc_type_view_2099
+ lifs_mirror_mount_domount.kalloc_type_view_1165
+ lifs_mirror_mount_domount.kalloc_type_view_1216
+ lifs_mount.kalloc_type_view_622
+ lifs_mount.kalloc_type_view_648
+ lifs_mount.kalloc_type_view_649
+ lifs_mount.kalloc_type_view_821
+ lifs_mount.kalloc_type_view_867
+ lifs_mount.kalloc_type_view_871
+ lifs_mount.kalloc_type_view_875
+ lifs_reclaim_done.kalloc_type_view_4712
+ lifs_setfsattr_done.kalloc_type_view_3728
+ lifs_setup_mount_for_devvp._os_log_fmt.82
+ lifs_submit_io.kalloc_type_view_2080
+ lifs_submit_koio.kalloc_type_view_2121
+ lifs_unmount.kalloc_type_view_1010
+ lifs_unmount_dangling_all.kalloc_type_view_1504
+ lifs_unmount_dangling_all.kalloc_type_view_1525
+ lifs_unmount_dangling_thread.kalloc_type_view_1477
+ lifs_vnop_readdir.kalloc_type_view_2916
+ lifs_vnop_readdir.kalloc_type_view_2918
+ lifs_vnop_readdir.kalloc_type_view_3013
+ lifs_vnop_readdir.kalloc_type_view_3015
+ lifs_vnop_reclaim.kalloc_type_view_4756
+ lifs_vnop_reclaim.kalloc_type_view_4810
+ lifs_vnop_strategy.kalloc_type_view_2180
+ lifs_vnop_strategy_done.kalloc_type_view_1945
+ move_sillyrename_entries.kalloc_type_view_2042
- /Library/Caches/com.apple.xbs/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/DerivedSources/
- /Library/Caches/com.apple.xbs/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/IOCancelationWrapper.o
- /Library/Caches/com.apple.xbs/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/IOWrappedMemoryDescriptor.o
- /Library/Caches/com.apple.xbs/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/lifs_comm.o
- /Library/Caches/com.apple.xbs/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/lifs_extent.o
- /Library/Caches/com.apple.xbs/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/lifs_info.o
- /Library/Caches/com.apple.xbs/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/lifs_iokit.o
- /Library/Caches/com.apple.xbs/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/lifs_kext.o
- /Library/Caches/com.apple.xbs/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/lifs_mig.o
- /Library/Caches/com.apple.xbs/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/lifs_subr.o
- /Library/Caches/com.apple.xbs/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/lifs_vfsops.o
- /Library/Caches/com.apple.xbs/Binaries/FSKit_FileProvider/install/TempContent/Objects/FSKit.build/lifs_kext.build/Objects-normal/arm64e/lifs_vnops.o
- /Library/Caches/com.apple.xbs/Sources/FSKit_FileProvider/lifs_kext/
- __ZN18IOMemoryDescriptor11withOptionsEPvjjP4taskjP8IOMapper
- __ZN18IOMemoryDescriptor16withAddressRangeEyyjP4task
- __ZN25IOWrappedMemoryDescriptorC1Ev
- __ZN25IOWrappedMemoryDescriptornwEm
- __ZZL24lifs_destroy_iouc_volumeP19lifs_iouc_containerP16lifs_iouc_volumeE20kalloc_type_view_188
- __ZZL26lifs_create_iouc_containeriiE20kalloc_type_view_208
- __ZZL27lifs_destroy_iouc_containeriiE20kalloc_type_view_245
- __ZZN19AppleLIFSUserClient18methodOpenKernelFDEPS_PvP25IOExternalMethodArgumentsE20kalloc_type_view_973
- _get_aiotask
- _iokit_make_ident_port
- _kernel_task
- _lifs_max_dev_read_size
- _lifs_max_dev_write_size
- _lifs_read_wrapped_send
- _lifs_request_init
- _lifs_write_wrapped_send
- _mach_msg_destroy_from_kernel_proper
- _mach_msg_rpc_from_kernel_proper
- _mig_dealloc_reply_port
- _mig_get_reply_port
- _mig_put_reply_port
- _sysctl__vfs_generic_lifs_max_dev_read_size
- _sysctl__vfs_generic_lifs_max_dev_write_size
- _sysctl_max_dev_read_size
- _sysctl_max_dev_write_size
- _use_new_strategy
- _wrapperObjectForBuf
- add_sillyrename_entry.kalloc_type_view_1954
- add_sillyrename_entry.kalloc_type_view_1977
- cleanup_sillyrename_entries.kalloc_type_view_2067
- lifs_create_endio_context.kalloc_type_view_1080
- lifs_create_node.kalloc_type_view_434
- lifs_create_node.kalloc_type_view_589
- lifs_destroy_endio_context.kalloc_type_view_1099
- lifs_fsync_internal.kalloc_type_view_3796
- lifs_koio_done.kalloc_type_view_2096
- lifs_mirror_mount_domount.kalloc_type_view_1164
- lifs_mirror_mount_domount.kalloc_type_view_1215
- lifs_mount.kalloc_type_view_629
- lifs_mount.kalloc_type_view_655
- lifs_mount.kalloc_type_view_656
- lifs_mount.kalloc_type_view_828
- lifs_mount.kalloc_type_view_874
- lifs_mount.kalloc_type_view_878
- lifs_mount.kalloc_type_view_882
- lifs_reclaim_done.kalloc_type_view_4708
- lifs_request_alloc_init._os_log_fmt
- lifs_request_init._os_log_fmt
- lifs_setfsattr_done.kalloc_type_view_3724
- lifs_setup_mount_for_devvp._os_log_fmt.88
- lifs_submit_io.kalloc_type_view_2077
- lifs_submit_koio.kalloc_type_view_2118
- lifs_unmount.kalloc_type_view_1017
- lifs_unmount_dangling_all.kalloc_type_view_1521
- lifs_unmount_dangling_all.kalloc_type_view_1542
- lifs_unmount_dangling_thread.kalloc_type_view_1494
- lifs_vnop_readdir.kalloc_type_view_2912
- lifs_vnop_readdir.kalloc_type_view_2914
- lifs_vnop_readdir.kalloc_type_view_3009
- lifs_vnop_readdir.kalloc_type_view_3011
- lifs_vnop_reclaim.kalloc_type_view_4752
- lifs_vnop_reclaim.kalloc_type_view_4806
- lifs_vnop_strategy.kalloc_type_view_2175
- lifs_vnop_strategy_done.kalloc_type_view_1942
- move_sillyrename_entries.kalloc_type_view_2041
CStrings:
- "Max transfer size for read from device (1MB-8MB)"
- "Max transfer size for write to device (1MB-8MB)"
- "lifs_request for opcode %x outside valid range"
- "max_dev_read_size"
- "max_dev_write_size"

```
