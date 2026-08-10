## com.apple.filesystems.hfs.kext

> `com.apple.filesystems.hfs.kext`

### Sections with Same Size but Changed Content

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

 715.160.9.0.0
   __TEXT.__const: 0x1ab8
-  __TEXT.__cstring: 0xa8bd
-  __TEXT_EXEC.__text: 0x4e760
+  __TEXT.__cstring: 0xa909
+  __TEXT_EXEC.__text: 0x4e778
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x4d0
   __DATA.__common: 0x10

   __DATA_CONST.__kalloc_var: 0x5f0
   Functions: 511
   Symbols:   1572
-  CStrings:  856
+  CStrings:  857
 
Functions:
~ _hfs_vnop_getxattr : 924 -> 920
~ _HeadTruncateFile : 864 -> 892
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hJ5eQ0/Sources/hfs/core/VolumeAllocation.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hJ5eQ0/Sources/hfs/core/hfs_attrlist.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hJ5eQ0/Sources/hfs/core/hfs_btreeio.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hJ5eQ0/Sources/hfs/core/hfs_cnode.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hJ5eQ0/Sources/hfs/core/hfs_hotfiles.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hJ5eQ0/Sources/hfs/core/hfs_journal.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hJ5eQ0/Sources/hfs/core/hfs_readwrite.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hJ5eQ0/Sources/hfs/core/hfs_vfsops.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.hJ5eQ0/Sources/hfs/core/hfs_vfsutils.c"
+ "hfs: HeadTruncateFile: too many tail extents, marking volume inconsistent.\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NLm9XZ/Sources/hfs/core/VolumeAllocation.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NLm9XZ/Sources/hfs/core/hfs_attrlist.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NLm9XZ/Sources/hfs/core/hfs_btreeio.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NLm9XZ/Sources/hfs/core/hfs_cnode.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NLm9XZ/Sources/hfs/core/hfs_hotfiles.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NLm9XZ/Sources/hfs/core/hfs_journal.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NLm9XZ/Sources/hfs/core/hfs_readwrite.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NLm9XZ/Sources/hfs/core/hfs_vfsops.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.NLm9XZ/Sources/hfs/core/hfs_vfsutils.c"
```
