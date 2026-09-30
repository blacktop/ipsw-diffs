## com.apple.fskit.apfs

> `/System/Library/ExtensionKit/Extensions/com.apple.fskit.apfs.appex/com.apple.fskit.apfs`

```diff

-  __TEXT.__text: 0xe42c0
+  __TEXT.__text: 0xe4d14
   __TEXT.__auth_stubs: 0x1050
   __TEXT.__objc_stubs: 0x1240
   __TEXT.__objc_methlist: 0x84c
   __TEXT.__const: 0x8ba0
-  __TEXT.__cstring: 0x3b3c0
-  __TEXT.__objc_methname: 0x1ee5
-  __TEXT.__oslogstring: 0x1d98
+  __TEXT.__cstring: 0x3b7c8
+  __TEXT.__objc_methname: 0x1ee7
+  __TEXT.__oslogstring: 0x1dd3
   __TEXT.__objc_classname: 0x124
-  __TEXT.__objc_methtype: 0x2b94
+  __TEXT.__objc_methtype: 0x2b9a
   __TEXT.__gcc_except_tab: 0x464
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x28

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1b68
+  __TEXT.__unwind_info: 0x1b78
   __DATA_CONST.__const: 0x1240
   __DATA_CONST.__cfstring: 0x3a0
   __DATA_CONST.__objc_classlist: 0x18

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__auth_got: 0x838
-  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0xd8
   __DATA.__objc_const: 0xae8
   __DATA.__objc_selrefs: 0x6f0
   __DATA.__objc_ivar: 0x44
   __DATA.__objc_data: 0xf0
-  __DATA.__data: 0x1360
+  __DATA.__data: 0x1368
   __DATA.__common: 0x6b8
   __DATA.__bss: 0x1e399
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3283
-  Symbols:   1565
-  CStrings:  5405
+  Functions: 3286
+  Symbols:   1566
+  CStrings:  5424
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__swift5_entry : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_proto : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__bss : content changed
Symbols:
+ _apfs_update_dir_stats_parent
+ _consider_drec_for_size_tracking
- _free_tmp_ino_helper
CStrings:
+ "%s (id %llu): class %u file references per-file crypto_id (%llu) but is missing INODE_PROT_CLASS_EXPLICIT\n"
+ "%s:%d: %s could not get correct parent of ino %llu (%d tries)\n"
+ "%s:%d: %s failed to clean-up proposed wvek record in nx keybag, err = %d\n"
+ "%s:%d: %s failed to commit proposed wvek record, err = 0x%x (%d more retries)\n"
+ "%s:%d: %s failed to enter tx to store proposed wvek record, err = %d\n"
+ "%s:%d: %s failed to enter tx to update wvek record, err = %d\n"
+ "%s:%d: %s failed to flush tx storing proposed wvek record in nx keybag, err = %d\n"
+ "%s:%d: %s failed to restore dir-stats for to_ino %llu: %d\n"
+ "%s:%d: %s failed to store proposed wvek record in nx keybag, err = %d\n"
+ "%s:%d: %s failed to update wvek record in nx keybag, err = %d\n"
+ "%s:%d: %s found existing proposed wvek record in nx keybag (from previous failure)\n"
+ "%s:%d: %s ino %llu has no name"
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n"
+ "%s:%d: %s op %d error getting cab %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n"
+ "%s:%d: %s op %d failed to allocate block from internal pool: %d\n"
+ "%s:%d: %s op %d failed to create bitmap object %lld: %d\n"
+ "%s:%d: %s op %d failed to free internal pool block %lld: %d\n"
+ "%s:%d: failed to lookup existing proposed wvek record in nx keybag, err = %d\n"
+ "3283.0.9.502.1"
+ "Set INODE_PROT_CLASS_EXPLICIT? "
+ "T^{apfs={obj=^{nx}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}},V_apfs"
+ "^{apfs={obj=^{nx}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}}"
+ "^{apfs={obj=^{nx}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}}16@0:8"
+ "apfs_update_dir_stats_parent"
+ "apfs_vek_commit_internal"
+ "consider_drec_for_size_tracking"
+ "kb"
+ "nx-tree-node-compact-lock"
+ "v24@0:8^{apfs={obj=^{nx}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}}16"
- "%s:%d: %s failed to create bitmap object %lld: %d\n"
- "%s:%d: %s failed to free internal pool block %lld: %d\n"
- "%s:%d: failed to add proposed wvek record in nx keybag, err = %d\n"
- "%s:%d: failed to clean-up proposed wvek record in nx keybag, err = %d\n"
- "%s:%d: failed to commit proposed wvek record, err = 0x%x (%d more retries)\n"
- "%s:%d: failed to update wvek record in nx keybag, err = %d\n"
- "3283"
- "T^{apfs={obj=^{nx}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}},V_apfs"
- "^{apfs={obj=^{nx}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}}"
- "^{apfs={obj=^{nx}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}}16@0:8"
- "apfs_commit_update_volume_key"
- "v24@0:8^{apfs={obj=^{nx}^{apfs}QqIIIIIi^{obj_phys}^{obj_phys}{?=^{obj}^^{obj}}{?=^{obj}^^{obj}}{?=^{obj}}QQqqQqIQ{_opaque_pthread_rwlock_t=q[192c]}}[0c]^{apfs_superblock}^{apfs_superblock}^{nx}*QQQQQQ[16C]QQ^v^v^{apfs}QQQ{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}{crypto_state={crypto_obj=QII{?=^{crypto_obj}^^{crypto_obj}}{?=^{crypto_obj}^^{crypto_obj}}}SSIISQ^{cpx}^vI}^{crypto_cache}{_opaque_pthread_mutex_t=q[56c]}^vQIiiiiIQ^{apfs_fake_context}Q^{dev_handle}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}^v{_opaque_pthread_rwlock_t=q[192c]}{_opaque_pthread_rwlock_t=q[192c]}QQII{_opaque_pthread_mutex_t=q[56c]}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}^{?}IIB}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{obj}^{omap}^{omap}{?=^{?}{_opaque_pthread_mutex_t=q[56c]}^Q^QIIII}^{nx_keybag}{prange=qQ}^{nx_keybag}{prange=qQ}qQiii{rolling_stats={_opaque_pthread_mutex_t=q[56c]}qII^qq}^{apfs}IBBBQ{_opaque_pthread_mutex_t=q[56c]}BIIQ[32c]{?={_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_cond_t=q[40c]}QQB[64{?=QQQ^{_opaque_pthread_t}}]}}16"

```
