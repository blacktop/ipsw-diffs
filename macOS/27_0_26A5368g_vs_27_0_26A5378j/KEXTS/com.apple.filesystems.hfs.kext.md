## com.apple.filesystems.hfs.kext

> `com.apple.filesystems.hfs.kext`

```diff

   __TEXT.__const: 0x1ab0
   __TEXT.__cstring: 0xab88
-  __TEXT_EXEC.__text: 0x4e8c0
-  __TEXT_EXEC.__auth_stubs: 0x1840
+  __TEXT_EXEC.__text: 0x4e8c4
+  __TEXT_EXEC.__auth_stubs: 0x1850
   __DATA.__data: 0x4d0
   __DATA.__common: 0x10
   __DATA.__bss: 0x1a4

   __DATA_CONST.__const: 0x1340
   __DATA_CONST.__kalloc_type: 0x2cc0
   __DATA_CONST.__kalloc_var: 0x5f0
-  __DATA_CONST.__auth_got: 0xc20
+  __DATA_CONST.__auth_got: 0xc28
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x8
-  Functions: 509
-  Symbols:   1567
+  Functions: 510
+  Symbols:   1569
   CStrings:  866
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __DATA.__data : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ _IOMallocZeroDataShareable
+ _hfs_set_summary
+ abort_transaction.kalloc_type_view_4619
+ abort_transaction.kalloc_type_view_4642
+ cat_check_link_ancestry.kalloc_type_view_1907
+ cat_check_link_ancestry.kalloc_type_view_1934
+ cat_create.kalloc_type_view_1066
+ cat_create.kalloc_type_view_1133
+ cat_createlink.kalloc_type_view_2239
+ cat_createlink.kalloc_type_view_2314
+ cat_getentriesattr.kalloc_type_view_2660
+ cat_getentriesattr.kalloc_type_view_2781
+ cat_lookup_dirlink.kalloc_type_view_4123
+ cat_lookup_dirlink.kalloc_type_view_4126
+ cat_lookup_dirlink.kalloc_type_view_4164
+ cat_lookup_dirlink.kalloc_type_view_4166
+ cat_lookup_lastlink.kalloc_type_view_2118
+ cat_lookup_lastlink.kalloc_type_view_2197
+ cat_lookup_siblinglinks.kalloc_type_view_2063
+ cat_lookup_siblinglinks.kalloc_type_view_2094
+ cat_lookupbykey.kalloc_type_view_1030
+ cat_lookuplink.kalloc_type_view_2019
+ cat_lookuplink.kalloc_type_view_2043
+ cat_rename.kalloc_type_view_1183
+ cat_rename.kalloc_type_view_1187
+ cat_rename.kalloc_type_view_1192
+ cat_rename.kalloc_type_view_1212
+ cat_rename.kalloc_type_view_1223
+ cat_rename.kalloc_type_view_1229
+ cat_rename.kalloc_type_view_1233
+ cat_rename.kalloc_type_view_1431
+ cat_rename.kalloc_type_view_1433
+ cat_rename.kalloc_type_view_1435
+ cat_resolvelink.kalloc_type_view_3598
+ cat_resolvelink.kalloc_type_view_3620
+ cat_update_siblinglinks.kalloc_type_view_1990
+ cat_update_siblinglinks.kalloc_type_view_2000
+ finish_end_transaction.kalloc_type_view_4199
+ finish_end_transaction.kalloc_type_view_4323
+ getkey.kalloc_type_view_3663
+ getkey.kalloc_type_view_3666
+ getkey.kalloc_type_view_3701
+ journal_allocate_transaction.kalloc_type_view_2592
+ journal_allocate_transaction.kalloc_type_view_2596
+ journal_close.kalloc_type_view_2409
+ journal_create.kalloc_type_view_1888
+ journal_modify_block_end.kalloc_type_view_2947
+ journal_open.kalloc_type_view_1946
+ journal_open.kalloc_type_view_2188
- abort_transaction.kalloc_type_view_4612
- abort_transaction.kalloc_type_view_4635
- cat_check_link_ancestry.kalloc_type_view_1906
- cat_check_link_ancestry.kalloc_type_view_1933
- cat_create.kalloc_type_view_1065
- cat_create.kalloc_type_view_1132
- cat_createlink.kalloc_type_view_2238
- cat_createlink.kalloc_type_view_2313
- cat_getentriesattr.kalloc_type_view_2659
- cat_getentriesattr.kalloc_type_view_2780
- cat_lookup_dirlink.kalloc_type_view_4122
- cat_lookup_dirlink.kalloc_type_view_4125
- cat_lookup_dirlink.kalloc_type_view_4163
- cat_lookup_dirlink.kalloc_type_view_4165
- cat_lookup_lastlink.kalloc_type_view_2117
- cat_lookup_lastlink.kalloc_type_view_2196
- cat_lookup_siblinglinks.kalloc_type_view_2062
- cat_lookup_siblinglinks.kalloc_type_view_2093
- cat_lookupbykey.kalloc_type_view_1028
- cat_lookuplink.kalloc_type_view_2018
- cat_lookuplink.kalloc_type_view_2042
- cat_rename.kalloc_type_view_1182
- cat_rename.kalloc_type_view_1186
- cat_rename.kalloc_type_view_1191
- cat_rename.kalloc_type_view_1211
- cat_rename.kalloc_type_view_1222
- cat_rename.kalloc_type_view_1228
- cat_rename.kalloc_type_view_1232
- cat_rename.kalloc_type_view_1430
- cat_rename.kalloc_type_view_1432
- cat_rename.kalloc_type_view_1434
- cat_resolvelink.kalloc_type_view_3597
- cat_resolvelink.kalloc_type_view_3619
- cat_update_siblinglinks.kalloc_type_view_1989
- cat_update_siblinglinks.kalloc_type_view_1999
- finish_end_transaction.kalloc_type_view_4192
- finish_end_transaction.kalloc_type_view_4316
- getkey.kalloc_type_view_3662
- getkey.kalloc_type_view_3665
- getkey.kalloc_type_view_3699
- journal_allocate_transaction.kalloc_type_view_2585
- journal_allocate_transaction.kalloc_type_view_2589
- journal_close.kalloc_type_view_2402
- journal_create.kalloc_type_view_1889
- journal_modify_block_end.kalloc_type_view_2940
- journal_open.kalloc_type_view_1947
- journal_open.kalloc_type_view_2181
Functions:
~ _InsertKeyRecord : 476 -> 484
~ _journal_create : 948 -> 924
~ _write_journal_header : 496 -> 492
~ _journal_open : 1828 -> 1920
~ _replay_journal : 5016 -> 5008
~ _journal_is_clean : 816 -> 808
~ _finish_end_transaction : 2468 -> 2464
~ _journal_modify_block_start : 1628 -> 1616
~ _hfs_clonesysfile : 604 -> 648
~ _cat_lookupbykey : 1584 -> 1592
~ _CheckCriteria : 1472 -> 1456
~ _AllocateNode : 652 -> 640
~ _ScanUnmapBlocks : 1200 -> 1132
+ _hfs_set_summary
~ _BlockFindContiguous : 1960 -> 1932
~ _BlockFindAny : 1264 -> 1236
~ _hfs_find_summary_free : 164 -> 176
~ _BlockMarkFreeInternal : 3056 -> 2980
~ _hfs_init_summary : 200 -> 212
~ _UpdateAllocLimit : 280 -> 292
~ _update_summary_table : 208 -> 204
~ _TruncateFileC : 740 -> 800
~ _mountpointname : 140 -> 128
~ _FastUnicodeCompare : 228 -> 204
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3zDDD5/Sources/hfs/core/VolumeAllocation.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3zDDD5/Sources/hfs/core/hfs_attrlist.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3zDDD5/Sources/hfs/core/hfs_btreeio.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3zDDD5/Sources/hfs/core/hfs_cnode.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3zDDD5/Sources/hfs/core/hfs_hotfiles.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3zDDD5/Sources/hfs/core/hfs_journal.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3zDDD5/Sources/hfs/core/hfs_readwrite.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3zDDD5/Sources/hfs/core/hfs_vfsops.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3zDDD5/Sources/hfs/core/hfs_vfsutils.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FZf5wh/Sources/hfs/core/VolumeAllocation.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FZf5wh/Sources/hfs/core/hfs_attrlist.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FZf5wh/Sources/hfs/core/hfs_btreeio.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FZf5wh/Sources/hfs/core/hfs_cnode.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FZf5wh/Sources/hfs/core/hfs_hotfiles.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FZf5wh/Sources/hfs/core/hfs_journal.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FZf5wh/Sources/hfs/core/hfs_readwrite.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FZf5wh/Sources/hfs/core/hfs_vfsops.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FZf5wh/Sources/hfs/core/hfs_vfsutils.c"

```
