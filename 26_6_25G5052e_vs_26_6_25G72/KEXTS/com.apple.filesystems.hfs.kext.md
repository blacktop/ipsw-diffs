## com.apple.filesystems.hfs.kext

> `com.apple.filesystems.hfs.kext`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__DATA.__data`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`

```diff

-715.160.7.0.0
+715.160.9.0.0
   __TEXT.__const: 0x1ab8
   __TEXT.__cstring: 0xa8bd
-  __TEXT_EXEC.__text: 0x4e754
+  __TEXT_EXEC.__text: 0x4e760
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4d0
   __DATA.__common: 0x10

   __DATA_CONST.__const: 0x1340
   __DATA_CONST.__kalloc_type: 0x2cc0
   __DATA_CONST.__kalloc_var: 0x5f0
-  Functions: 510
-  Symbols:   1571
+  Functions: 511
+  Symbols:   1572
   CStrings:  856
 
Symbols:
+ UpdateExtentRecord.kalloc_type_view_1868
+ UpdateExtentRecord.kalloc_type_view_1903
+ _hfs_set_summary
+ cat_check_link_ancestry.kalloc_type_view_1883
+ cat_check_link_ancestry.kalloc_type_view_1910
+ cat_create.kalloc_type_view_1043
+ cat_create.kalloc_type_view_1110
+ cat_createlink.kalloc_type_view_2215
+ cat_createlink.kalloc_type_view_2290
+ cat_getentriesattr.kalloc_type_view_2636
+ cat_getentriesattr.kalloc_type_view_2757
+ cat_lookup_dirlink.kalloc_type_view_4099
+ cat_lookup_dirlink.kalloc_type_view_4102
+ cat_lookup_dirlink.kalloc_type_view_4140
+ cat_lookup_dirlink.kalloc_type_view_4142
+ cat_lookup_lastlink.kalloc_type_view_2094
+ cat_lookup_lastlink.kalloc_type_view_2173
+ cat_lookup_siblinglinks.kalloc_type_view_2039
+ cat_lookup_siblinglinks.kalloc_type_view_2070
+ cat_lookupbykey.kalloc_type_view_1007
+ cat_lookuplink.kalloc_type_view_1995
+ cat_lookuplink.kalloc_type_view_2019
+ cat_rename.kalloc_type_view_1160
+ cat_rename.kalloc_type_view_1164
+ cat_rename.kalloc_type_view_1169
+ cat_rename.kalloc_type_view_1189
+ cat_rename.kalloc_type_view_1200
+ cat_rename.kalloc_type_view_1206
+ cat_rename.kalloc_type_view_1210
+ cat_rename.kalloc_type_view_1407
+ cat_rename.kalloc_type_view_1409
+ cat_rename.kalloc_type_view_1411
+ cat_resolvelink.kalloc_type_view_3574
+ cat_resolvelink.kalloc_type_view_3596
+ cat_update_siblinglinks.kalloc_type_view_1966
+ cat_update_siblinglinks.kalloc_type_view_1976
+ file_attribute_exist.kalloc_type_view_1688
+ file_attribute_exist.kalloc_type_view_1714
+ getkey.kalloc_type_view_3639
+ getkey.kalloc_type_view_3642
+ getkey.kalloc_type_view_3677
+ hfs_getxattr_internal.kalloc_type_view_566
+ hfs_getxattr_internal.kalloc_type_view_762
+ hfs_removeallattr.kalloc_type_view_2072
+ hfs_removeallattr.kalloc_type_view_2113
+ hfs_set_volxattr.kalloc_type_view_2172
+ hfs_set_volxattr.kalloc_type_view_2233
+ hfs_setxattr_internal.kalloc_type_view_1151
+ hfs_setxattr_internal.kalloc_type_view_1363
+ hfs_vnop_listxattr.kalloc_type_view_1919
+ hfs_vnop_listxattr.kalloc_type_view_1973
+ hfs_vnop_removexattr.kalloc_type_view_1552
+ hfs_vnop_removexattr.kalloc_type_view_1602
- UpdateExtentRecord.kalloc_type_view_1830
- UpdateExtentRecord.kalloc_type_view_1865
- cat_check_link_ancestry.kalloc_type_view_1882
- cat_check_link_ancestry.kalloc_type_view_1909
- cat_create.kalloc_type_view_1042
- cat_create.kalloc_type_view_1109
- cat_createlink.kalloc_type_view_2214
- cat_createlink.kalloc_type_view_2289
- cat_getentriesattr.kalloc_type_view_2635
- cat_getentriesattr.kalloc_type_view_2756
- cat_lookup_dirlink.kalloc_type_view_4098
- cat_lookup_dirlink.kalloc_type_view_4101
- cat_lookup_dirlink.kalloc_type_view_4139
- cat_lookup_dirlink.kalloc_type_view_4141
- cat_lookup_lastlink.kalloc_type_view_2093
- cat_lookup_lastlink.kalloc_type_view_2172
- cat_lookup_siblinglinks.kalloc_type_view_2038
- cat_lookup_siblinglinks.kalloc_type_view_2069
- cat_lookupbykey.kalloc_type_view_1005
- cat_lookuplink.kalloc_type_view_1994
- cat_lookuplink.kalloc_type_view_2018
- cat_rename.kalloc_type_view_1159
- cat_rename.kalloc_type_view_1163
- cat_rename.kalloc_type_view_1168
- cat_rename.kalloc_type_view_1188
- cat_rename.kalloc_type_view_1199
- cat_rename.kalloc_type_view_1205
- cat_rename.kalloc_type_view_1209
- cat_rename.kalloc_type_view_1406
- cat_rename.kalloc_type_view_1408
- cat_rename.kalloc_type_view_1410
- cat_resolvelink.kalloc_type_view_3573
- cat_resolvelink.kalloc_type_view_3595
- cat_update_siblinglinks.kalloc_type_view_1965
- cat_update_siblinglinks.kalloc_type_view_1975
- file_attribute_exist.kalloc_type_view_1679
- file_attribute_exist.kalloc_type_view_1705
- getkey.kalloc_type_view_3638
- getkey.kalloc_type_view_3641
- getkey.kalloc_type_view_3675
- hfs_getxattr_internal.kalloc_type_view_557
- hfs_getxattr_internal.kalloc_type_view_753
- hfs_removeallattr.kalloc_type_view_2063
- hfs_removeallattr.kalloc_type_view_2104
- hfs_set_volxattr.kalloc_type_view_2163
- hfs_set_volxattr.kalloc_type_view_2224
- hfs_setxattr_internal.kalloc_type_view_1142
- hfs_setxattr_internal.kalloc_type_view_1354
- hfs_vnop_listxattr.kalloc_type_view_1910
- hfs_vnop_listxattr.kalloc_type_view_1964
- hfs_vnop_removexattr.kalloc_type_view_1543
- hfs_vnop_removexattr.kalloc_type_view_1593
Functions:
~ _InsertKeyRecord : 476 -> 484
~ _cat_lookupbykey : 1580 -> 1588
~ _ScanUnmapBlocks : 1200 -> 1132
+ _hfs_set_summary
~ _hfs_release_summary : 136 -> 140
~ _BlockFindContiguous : 1960 -> 1932
~ _BlockFindAny : 1280 -> 1252
~ _hfs_find_summary_free : 164 -> 176
~ _hfs_init_summary : 200 -> 212
~ _UpdateAllocLimit : 280 -> 292
~ _update_summary_table : 208 -> 204
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NLm9XZ/Sources/hfs/core/VolumeAllocation.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NLm9XZ/Sources/hfs/core/hfs_attrlist.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NLm9XZ/Sources/hfs/core/hfs_btreeio.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NLm9XZ/Sources/hfs/core/hfs_cnode.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NLm9XZ/Sources/hfs/core/hfs_hotfiles.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NLm9XZ/Sources/hfs/core/hfs_journal.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NLm9XZ/Sources/hfs/core/hfs_readwrite.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NLm9XZ/Sources/hfs/core/hfs_vfsops.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NLm9XZ/Sources/hfs/core/hfs_vfsutils.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1Joxqj/Sources/hfs/core/VolumeAllocation.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1Joxqj/Sources/hfs/core/hfs_attrlist.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1Joxqj/Sources/hfs/core/hfs_btreeio.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1Joxqj/Sources/hfs/core/hfs_cnode.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1Joxqj/Sources/hfs/core/hfs_hotfiles.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1Joxqj/Sources/hfs/core/hfs_journal.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1Joxqj/Sources/hfs/core/hfs_readwrite.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1Joxqj/Sources/hfs/core/hfs_vfsops.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1Joxqj/Sources/hfs/core/hfs_vfsutils.c"
```
