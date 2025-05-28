## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

-2235.0.13.0.0
-  __TEXT.__text: 0x49824
+2235.40.9.0.1
+  __TEXT.__text: 0x49f34
   __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__cstring: 0x1755e
+  __TEXT.__cstring: 0x17879
   __TEXT.__const: 0x8104
-  __TEXT.__unwind_info: 0x9b8
+  __TEXT.__unwind_info: 0x9c4
   __DATA_CONST.__auth_got: 0x458
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x40

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 803
+  Functions: 805
   Symbols:   156
-  CStrings:  1778
+  CStrings:  1788
 
CStrings:
+ "%s (id %llu): failed to register file info (hash %llu): %d\n"
+ "%s (id %llu): unknown flags (0x%x / valid-flags: 0x%x)\n"
+ "2235.40.9.0.1"
+ "chained key of dir-stats object (id %llu) does not match expected value (%llu)\n"
+ "failed to allocate memory to mark dir-stats chain as inconsistent\n"
+ "failed to init fsroot tree to mark dir-stats chain as inconsistent\n"
+ "failed to init fsroot tree to repair dir-stats chained key\n"
+ "file info: attribution tag (hash %llu) skipping clone size repair because the clone mapping repairs were aborted\n"
+ "file info: attribution tag (hash %llu) skipping clone size repair because the computed clone size is negative\n"
+ "file info: attribution tag (hash %llu) skipping clone size repair: full clone size %llu > %llu\n"
+ "file info: attribution tag (hash %llu) with invalid jobj_id (%llu)\n"
+ "file info: attribution tag (hash %llu): full clone size (%llu) does not match computed size (%llu)\n"
+ "file info: attribution tag (hash %llu): full clone size does not match expected value (%llu)\n"
+ "file info: attribution tag (hash %llu): physical size (%llu) does not match computed size (%llu)\n"
+ "file info: attribution tag (hash %llu): physical size does not match expected value (%llu)\n"
+ "file info: attribution tag (hash %llu): total count (%llu) does not match computed count (%llu)\n"
+ "file info: attribution tag (hash %llu): total count does not match expected value (%llu)\n"
+ "file info: found more than one attribution tag with matching computed hash, invalid entry (hash %llu)\n"
+ "found dir-stats object (id %llu; flags 0x%x) with bad chained key (%llu)\n"
+ "need to mark dir-stats %llu as needing reconciliation, due to an issue with dir-stats %llu\n"
+ "performed too many chained-key iterations (current id %llu); can't mark the entire chain as needing reconciliation\n"
+ "unable to allocate memory to repair dir-stats chained key\n"
+ "unable to get dir-stats key of inode (id %llu) to repair dir-stats chained key: %s\n"
+ "unable to load inode (id %llu) to repair dir-stats chained key: %s\n"
- "%s (id %llu): failed to register file info: %d\n"
- "2235.0.13"
- "file info: attribution tag (hash 0x%llx) with invalid jobj_id (%llu)\n"
- "file info: attribution tag (hash 0x%llx): full clone size (%llu) does not match computed size (%llu)\n"
- "file info: attribution tag (hash 0x%llx): full clone size does not match expected value (%llu)\n"
- "file info: attribution tag (hash 0x%llx): physical size (%llu) does not match computed size (%llu)\n"
- "file info: attribution tag (hash 0x%llx): physical size does not match expected value (%llu)\n"
- "file info: attribution tag (hash 0x%llx): total count (%llu) does not match computed count (%llu)\n"
- "file info: attribution tag (hash 0x%llx): total count does not match expected value (%llu)\n"
- "file info: found more than one attribution tag with matching computed hash, invalid entry (hash 0x%llx)\n"
- "found dir-stats object (id %llu; flags 0x%x) with bad chained-key; aborting dir-stats repairs\n"
- "skipping attribution tag clone sizes repair because the clone mapping repairs were aborted\n"
- "skipping attribution tag clone sizes repair because the computed clone size is negative\n"
- "skipping attribution tag clone sizes repair: full clone size %llu > %llu\n"

```
