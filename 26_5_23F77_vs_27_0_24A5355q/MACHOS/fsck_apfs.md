## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

-2811.120.14.0.1
-  __TEXT.__text: 0x53d5c
-  __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__cstring: 0x19e3f
-  __TEXT.__const: 0x8710
-  __TEXT.__unwind_info: 0xb50
-  __DATA_CONST.__auth_got: 0x5e8
+3277.0.0.0.1
+  __TEXT.__text: 0x56660
+  __TEXT.__auth_stubs: 0xc00
+  __TEXT.__cstring: 0x1a588
+  __TEXT.__const: 0x8730
+  __TEXT.__unwind_info: 0xba0
+  __DATA_CONST.__const: 0x620
+  __DATA_CONST.__cfstring: 0x200
+  __DATA_CONST.__auth_got: 0x600
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0x610
-  __DATA_CONST.__cfstring: 0x200
-  __DATA.__data: 0xee8
-  __DATA.__bss: 0x1e1f1
-  __DATA.__common: 0xac9
+  __DATA.__data: 0xf30
+  __DATA.__bss: 0x1e249
+  __DATA.__common: 0x9a8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/FSKit.framework/FSKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: 853EBF04-256F-3F64-9E08-BE1B3C350CAA
-  Functions: 962
-  Symbols:   206
-  CStrings:  1975
+  UUID: 66D196B3-5E9D-3DE4-B16E-6BB9C51C095C
+  Functions: 987
+  Symbols:   209
+  CStrings:  2014
 
Symbols:
+ _pthread_cond_destroy
+ _pthread_mutex_destroy
+ _pthread_mutex_init
CStrings:
+ "\tactual hash:   %s\n"
+ "\texpected hash: %s\n"
+ " ("
+ "%03llu"
+ "%s (id %llu): unknown flags: (0x%x / known flags are: 0x%x)\n"
+ "%s (id %llu): xf %u/%u: %s: found on a non class F file\n"
+ "%s xfield of inode object (id %llu) does not match expected value (%llu)\n"
+ "%s%llu %cB%s"
+ "%s%llu%-*.*s %cB%s"
+ "%s%llu.%.*s %cB%s"
+ "%s:%spid:%d,%s:%s%s%s%s%s%u:%s invalid implicit stash%s\n"
+ ")"
+ "."
+ "3277.0.0.0.1"
+ "INO_EXT_TYPE_STRICT_CLASS_F"
+ "Requested cache size: %s (%uk blocks * %ukB)\n"
+ "Round %s ov_size (oid 0x%llx) to block size? "
+ "Set ov_size (oid 0x%llx) to the block size? "
+ "_cmd_stash_kek"
+ "apfs superblock at index %u: APFS_FEATURE_EXTENDED_VEK_CLASSES set on non-HCP volume (apfs_features: 0x%llx)\n"
+ "btn: oid (%llu), xid (%llu), type (0x%x), subtype (0x%x), flags (0x%x) level (%u)\nerror: btn: invalid node hash\n"
+ "can't find new dir-stats key for inode (id %llu): error %d\n"
+ "can't repair inode (id %llu) with dir stats (id %llu)\n"
+ "clonegroup-cookie"
+ "failed to add PFKUR entry for inode (%llu): %s\n"
+ "failed to construct drec key (dir_id %llu, file_name %s)\n"
+ "failed to enqueue clonegroup mapping (group_id %llu, private_id %llu, file_id %llu) flags: 0x%x repair: %s\n"
+ "failed to look up resource fork for inode (%llu): %s\n"
+ "failed to register the clonegroup trees in the fsck memory storage\n"
+ "failed to remove INODE_PROT_CLASS_UPGRADE_ROLLIP flag for inode (%llu): %s\n"
+ "failed to sparse VEK extents for inode (%llu): %s\n"
+ "failed to sparse VEK extents for resource fork of inode (%llu): %s\n"
+ "found invalid object (type %u, id %llu)\n"
+ "found solo clonegroup inode: (group_id %llu, private_id %llu, file_id %llu)\n"
+ "hash validation: invalid node hash for node %llu (hash type: %u, hash size: %u, root oid: %llu, seal xid: %llu, broken xid: %llu)\n"
+ "inode (id %llu) has a stale dir_stats (id %llu)\n"
+ "inode (id %llu) needs to untrack from dir-stats\n"
+ "inode (id %llu): found unexpected security xattr\n"
+ "insert missing directory record object (parent_id %llu, file_id %llu)\n"
+ "missing upgrade-rolling entry for inode (%llu), version (%d)\n"
+ "obsolete spaceman tier2 fields should be empty but they aren't\n"
+ "omap entry (oid 0x%llx): invalid ov_paddr + ov_size (%llu + %u)\n"
+ "sm: sm_free_count (%llu) is not valid (%llu)\n"
+ "too many parent chain lookups during missing dir-stats repairs\n"
+ "uid/gid/mode: %d/%d/0x%x bsd_flags: 0x%x internal_flags: 0x%llx name: %.*s\n"
+ "unable to allocate space to walk dir-stats parent chain\n"
+ "unable to init fsroot tree to enqueue dir-stats repairs\n"
+ "xattr record too small (%u)\n"
+ "xattr size (%u) does not match expected size (%lu)\n"
+ "xattr value length (%u) does not match record size (%u)\n"
+ "zero type"
+ "zero type/id"
- "2811.120.14.0.1"
- "NO-NAME"
- "Requested cache size: %lluMB (%uk blocks * %ukB)\n"
- "any"
- "failed to enqueue clonegroup mapping (group_id %llu, private_id %llu, file_id %llu) repair: %s\n"
- "failed to register the clonegroup tree in the fsck memory storage\n"
- "hash validation: invalid node hash for node %llu (root oid: %llu, seal xid: %lld, broken xid: %lld)\n"
- "missing upgrade-rolling entry for inode (%llu)\n"
- "omap entry (oid 0x%llx): invalid ov_paddr (%llu)\n"
- "purgeable inode (id %llu) was unexpectedly registered twice\n"
- "sm: sm_free_count (%llu) is not valid (%llu) (sm_dev %d)\n"
- "spaceman tier2 fields should be empty but they aren't\n"
- "uid/gid/mode: %d/%d/0x%x bsd_flags: 0x%x internal_flags: 0x%llx name: %s\n"

```
