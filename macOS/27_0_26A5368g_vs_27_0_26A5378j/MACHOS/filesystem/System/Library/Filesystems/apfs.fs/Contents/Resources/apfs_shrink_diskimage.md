## apfs_shrink_diskimage

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_shrink_diskimage`

```diff

-  __TEXT.__text: 0x59dd4
+  __TEXT.__text: 0x59668
   __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__cstring: 0x12ef1
+  __TEXT.__cstring: 0x12e4e
   __TEXT.__const: 0x230
-  __TEXT.__unwind_info: 0x958
+  __TEXT.__unwind_info: 0x938
   __DATA_CONST.__const: 0x728
   __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__auth_got: 0x3f0

   - /System/Library/PrivateFrameworks/DiskImages.framework/Versions/A/DiskImages
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 779
+  Functions: 772
   Symbols:   140
-  CStrings:  1523
+  CStrings:  1518
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA.__data : content changed
CStrings:
+ "%s:%d: %s oid %lld xid %lld error freeing stale deletion record %d\n"
+ "%s:%d: %s oid %lld xid %lld paddr 0x%llx ov_flags 0x%x error freeing stale entry location %d\n"
+ "%s:%d: %s oid 0x%llx flags 0x%llx type 0x%x/0x%x error freeing new location %d\n"
+ "%s:%d: %s op %d error getting cab %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d @ %lld: %d\n"
+ "%s:%d: %s op %d error getting cib %d bitmap %d @ %lld: %d\n"
+ "%s:%d: %s op %d failed to allocate block from internal pool: %d\n"
+ "%s:%d: %s op %d failed to create bitmap object %lld: %d\n"
+ "%s:%d: %s op %d failed to free internal pool block %lld: %d\n"
+ "%s:%d: %s remove stale mapping oid %lld xid %lld\n"
+ "%s:%d: %s remove stale mapping oid %lld xid %lld failed: %d\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/jobj.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/nx.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/obj.c"
+ "nx-tree-node-compact-lock"
- "%s:%d: %s Bad overlap %lld, %lld to range %lld, %lld\n"
- "%s:%d: %s Bootcache inodes tree is NULL, cannot ignore boot files\n"
- "%s:%d: %s No defrag state for dstream in dstreams tree %lld\n"
- "%s:%d: %s Not a pure overlap %lld, %lld to range %lld, %lld, in newer xid (%lld > %lld) \n"
- "%s:%d: %s bad ranges returned from extent_update_range_to_evict %lld %lld\n"
- "%s:%d: %s could not locate snap meta of snapshot xid %llu\n"
- "%s:%d: %s dstream %lld pext tree is NULL\n"
- "%s:%d: %s dstream Ids do not match %lld != %lld\n"
- "%s:%d: %s dstream_pext_tree_create failed with error %d\n"
- "%s:%d: %s extent_update_range_to_evict failed: %d - %s\n"
- "%s:%d: %s failed to create bitmap object %lld: %d\n"
- "%s:%d: %s failed to delete dstream pext tree, error: %d\n"
- "%s:%d: %s failed to free internal pool block %lld: %d\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/jobj.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/nx.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DuFDA3/Sources/apfs_executables/nx/obj.c"
- "dstream_pext_tree_create"
- "dstream_pext_tree_lookup_overlap"
- "dstream_should_ignore"
- "extent_update_range_to_evict"

```
