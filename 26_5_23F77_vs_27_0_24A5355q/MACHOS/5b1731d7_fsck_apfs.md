## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

-2811.120.14.0.1
-  __TEXT.__text: 0x53d5c sha256:1b01f996626ec68730dc8878c9998473d84d73997b5c649af825bea61850edc6
-  __TEXT.__auth_stubs: 0xbd0 sha256:8d97253528437884c4a45d18a8f16393a249a4690e87617c792374bfc3414ba2
-  __TEXT.__cstring: 0x19e3f sha256:5e0fd2e8072bc675519aecf1c298b229876122d92dac0a61502c83a1f265530b
-  __TEXT.__const: 0x8710 sha256:1b0c534fecad3c075483a1f6a4873b38238d97a97784903a094889174cf419c6
-  __TEXT.__unwind_info: 0xb50 sha256:a390fd1342c8d9acd7594f7696a6586de4a822140027c648c88be7e8d2affee5
-  __DATA_CONST.__auth_got: 0x5e8 sha256:2ed79eed21ca339359024aa7f3fb96a21f58de0aa2d05c4d96a86f62f2eaf01d
-  __DATA_CONST.__got: 0x68 sha256:c8f18105d477612b30d7a3fdaac1e21cc820b9692ce247a0223115f1b7e738e5
-  __DATA_CONST.__auth_ptr: 0x68 sha256:48ae9683148e2445151d364bfcdc490961e5d27f8b50627591a3f92628796691
-  __DATA_CONST.__const: 0x610 sha256:60606739a3999cff96ae8f448619fbbf3c766ec83312930b665025a00fe5d0b9
-  __DATA_CONST.__cfstring: 0x200 sha256:573d1eadbf6289acc675f7a191c0da229f71621e522086ab91e3a17bb6b4a9e7
-  __DATA.__data: 0xee8 sha256:814bb53ea2f35fc5f37e4ba3aa87210f328407f2925c85e51edb319e2c9c0866
-  __DATA.__bss: 0x1e1f1 sha256:9a0f4b5db51d503b06e1793cacc8e7bcc50c2b0456177ccfd5b01ee171da1a4a
-  __DATA.__common: 0xac9
+3277.0.0.0.1
+  __TEXT.__text: 0x56660 sha256:d312406aa2add70bc27caf527af152261651d609987199878e70ddf32a50f51f
+  __TEXT.__auth_stubs: 0xc00 sha256:7b6c1b989ce9dc128af1ce4b88d37cdbe0d542c12efa73b8325f480183b8bdc8
+  __TEXT.__cstring: 0x1a588 sha256:4da5117acb5a2f57c7a8d0d6f2d0aba102348a8d07f9042d73ae751945026e09
+  __TEXT.__const: 0x8730 sha256:c072792e93dde14a752053afd224e00eac289f9f77c1752d7bad3a1a1d4b66f7
+  __TEXT.__unwind_info: 0xba0 sha256:00b329ee0b782ce6a2d30367cd889eaab6d6b6c7eacc1c013b84512d4b76bea0
+  __DATA_CONST.__const: 0x620 sha256:706b7e88f65baa501c40425a580dbfb286658d4c0cb9bd83376607030cb50a8b
+  __DATA_CONST.__cfstring: 0x200 sha256:2f5fffdf32ff8c208e659b9ee8c31a426848ffc46ede5fa4cfe50464005e4534
+  __DATA_CONST.__auth_got: 0x600 sha256:71de186fd3001e00a6a87cbeb967ed35179671f36ca4dfb961d6a4241c9ec308
+  __DATA_CONST.__got: 0x68 sha256:8d4c47626bda1426d9b142ebb8fd6ed95c9e33c7aa75f3b8ff3206817d1a1b0b
+  __DATA_CONST.__auth_ptr: 0x68 sha256:ed08bdac5f303b42e366d471a833fe34ca28f0656d38affbd2d55b79ac578ba7
+  __DATA.__data: 0xf30 sha256:60a20e587acb1b7e01d7c899103614505267d57e186b428b974dd26346936b8c
+  __DATA.__bss: 0x1e249 sha256:c93c87b6a955791781ea1dc64e6a78405b0a3b68555134718831c5b0a3b05d1a
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
