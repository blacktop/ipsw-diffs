## com.apple.filesystems.hfs.kext

> `com.apple.filesystems.hfs.kext`

```diff

-677.81.4.0.0
-  __TEXT.__const: 0x1a08
-  __TEXT.__cstring: 0xa724
-  __TEXT_EXEC.__text: 0x4e0a0
+683.100.9.0.0
+  __TEXT.__const: 0x1a90
+  __TEXT.__cstring: 0xa789
+  __TEXT_EXEC.__text: 0x4e75c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4d0
   __DATA.__common: 0x10

   __DATA_CONST.__mod_term_func: 0x8
   __DATA_CONST.__const: 0x1340
   __DATA_CONST.__kalloc_type: 0x2cc0
-  __DATA_CONST.__kalloc_var: 0x5f0
-  UUID: 9FAAB5E5-5AF8-33F0-A067-FC371644E74F
-  Functions: 522
-  Symbols:   1565
-  CStrings:  853
+  __DATA_CONST.__kalloc_var: 0x690
+  UUID: 6B21FFBE-C3FB-37CB-9594-7B035F01D3E4
+  Functions: 510
+  Symbols:   1573
+  CStrings:  855
 
Symbols:
+ _cat_makealias
+ _hfs_getquota
+ _hfs_quotaon
+ _hfs_quotastat
+ _hfs_setquota
+ _hfs_setuse
+ abort_transaction.kalloc_type_view_4565
+ abort_transaction.kalloc_type_view_4588
+ finish_end_transaction.kalloc_type_view_4145
+ finish_end_transaction.kalloc_type_view_4269
+ hfs_ext_replace.kalloc_type_view_380
+ hfs_ext_replace.kalloc_type_view_764
+ journal_allocate_transaction.kalloc_type_view_2538
+ journal_allocate_transaction.kalloc_type_view_2542
+ journal_close.kalloc_type_view_2355
+ journal_create.kalloc_type_view_1759
+ journal_create.kalloc_type_view_1866
+ journal_modify_block_end.kalloc_type_view_2893
+ journal_open.kalloc_type_view_1924
+ journal_open.kalloc_type_view_2134
+ replay_journal.kalloc_type_view_1527
+ replay_journal.kalloc_type_view_1538
- abort_transaction.kalloc_type_view_4566
- abort_transaction.kalloc_type_view_4589
- finish_end_transaction.kalloc_type_view_4146
- finish_end_transaction.kalloc_type_view_4270
- journal_allocate_transaction.kalloc_type_view_2539
- journal_allocate_transaction.kalloc_type_view_2543
- journal_close.kalloc_type_view_2356
- journal_create.kalloc_type_view_1760
- journal_create.kalloc_type_view_1867
- journal_modify_block_end.kalloc_type_view_2894
- journal_open.kalloc_type_view_1925
- journal_open.kalloc_type_view_2135
- replay_journal.kalloc_type_view_1528
- replay_journal.kalloc_type_view_1539
CStrings:
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/hfs/core/VolumeAllocation.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_attrlist.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_btreeio.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_cnode.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_hotfiles.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_journal.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_readwrite.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_search.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_vfsops.c"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_vfsutils.c"
+ "12222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "site.hfs_ext_iter_t"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/hfs/core/VolumeAllocation.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_attrlist.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_btreeio.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_cnode.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_hotfiles.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_journal.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_readwrite.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_search.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_vfsops.c"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/hfs/core/hfs_vfsutils.c"

```
