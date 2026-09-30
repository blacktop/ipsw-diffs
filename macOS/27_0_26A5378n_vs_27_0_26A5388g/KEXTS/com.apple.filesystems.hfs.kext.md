## com.apple.filesystems.hfs.kext

> `com.apple.filesystems.hfs.kext`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__const`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-749.0.0.0.0
+750.0.0.0.0
   __TEXT.__const: 0x1ab0
   __TEXT.__cstring: 0xab88
   __TEXT_EXEC.__text: 0x4e8c4
Symbols:
+ UpdateExtentRecord.kalloc_type_view_1868
+ UpdateExtentRecord.kalloc_type_view_1903
+ file_attribute_exist.kalloc_type_view_1688
+ file_attribute_exist.kalloc_type_view_1714
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
- file_attribute_exist.kalloc_type_view_1679
- file_attribute_exist.kalloc_type_view_1705
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
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yspUrY/Sources/hfs/core/VolumeAllocation.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yspUrY/Sources/hfs/core/hfs_attrlist.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yspUrY/Sources/hfs/core/hfs_btreeio.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yspUrY/Sources/hfs/core/hfs_cnode.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yspUrY/Sources/hfs/core/hfs_hotfiles.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yspUrY/Sources/hfs/core/hfs_journal.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yspUrY/Sources/hfs/core/hfs_readwrite.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yspUrY/Sources/hfs/core/hfs_vfsops.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.yspUrY/Sources/hfs/core/hfs_vfsutils.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3zDDD5/Sources/hfs/core/VolumeAllocation.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3zDDD5/Sources/hfs/core/hfs_attrlist.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3zDDD5/Sources/hfs/core/hfs_btreeio.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3zDDD5/Sources/hfs/core/hfs_cnode.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3zDDD5/Sources/hfs/core/hfs_hotfiles.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3zDDD5/Sources/hfs/core/hfs_journal.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3zDDD5/Sources/hfs/core/hfs_readwrite.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3zDDD5/Sources/hfs/core/hfs_vfsops.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.3zDDD5/Sources/hfs/core/hfs_vfsutils.c"
```
