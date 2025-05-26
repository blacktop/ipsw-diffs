## fsck_apfs

> `/System/Library/Filesystems/apfs.fs/fsck_apfs`

```diff

-2235.80.4.0.1
-  __TEXT.__text: 0x49f34
-  __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__cstring: 0x17879
-  __TEXT.__const: 0x8104
-  __TEXT.__unwind_info: 0x9c4
-  __DATA_CONST.__auth_got: 0x458
+2236.102.1.0.0
+  __TEXT.__text: 0x4b3a8
+  __TEXT.__auth_stubs: 0x8d0
+  __TEXT.__cstring: 0x17bcc
+  __TEXT.__const: 0x812c
+  __TEXT.__unwind_info: 0x9e8
+  __DATA_CONST.__auth_got: 0x468
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x40
   __DATA_CONST.__const: 0x4d8
   __DATA_CONST.__cfstring: 0x200
   __DATA.__data: 0xec4
-  __DATA.__bss: 0x1c754
+  __DATA.__bss: 0x1c7a4
   __DATA.__common: 0xab1
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  Functions: 805
-  Symbols:   156
-  CStrings:  1788
+  Functions: 815
+  Symbols:   158
+  CStrings:  1805
 
Symbols:
+ _random
+ _srandomdev
CStrings:
+ "\ndir-stats %llu (has dir-stats? %d)%s:\nflags: 0x%x\nchained-key: %llu (computed: %llu)\norigin-id: %llu (computed: %llu)\nshadow-key: %llu (exists? %d)\ndescendants: %llu (computed: %llu)\nSAF descendants: %llu\ndir-stats descendants: %llu\nphysical size: %llu (computed: %llu)\nresource fork size: %llu (computed: %llu)\nclone size: %llu (exists? %d; computed: %llu)\npurgeable size: %llu (exists? %d; computed: %llu)\nhas calculating dir-stats? %d\norigin is SAF? %d (parent is SAF? %d)\norigin is purgeable? %d\n\n"
+ " [reconstructed]"
+ "%s (id %llu): found dir-stats object (chained-key %llu) that is unexpectedly being moved\n"
+ "%s (id %llu): sparse bytes mismatch for a file in the purgatory\n"
+ "%s (id %llu): unknown flags (0x%hx)\n"
+ "%s (id %llu): unknown flags (0x%x)\n"
+ "%s xfield of dir-stats object (id %llu) does not match expected value (%llu)\n"
+ "2236.102.1"
+ "Checking snapshot %ld of %ld (%s, transaction ID %ld)"
+ "SAF descendants (%llu) of dir-stats object (id %llu) is greater than expected (0)\n"
+ "Unset invalid flags? (0x%llx) "
+ "can't add clone size for dir-stats: %s (%d)\n"
+ "can't add purgeable size for dir-stats: %s (%d)\n"
+ "com.apple.system.fs.speculative_telemetry"
+ "detected chained-key loop involving dir-stats %llu\n"
+ "dir stats repairs"
+ "dir-stats (id %llu) is missing\n"
+ "dir-stats descendants"
+ "failed to allocate memory for insertion of dir-stats\n"
+ "failed to allocate memory to find dir-stats %llu\n"
+ "failed to get fsroot tree for jobj type %d: %s\n"
+ "failed to get fsroot tree to find expanded dir-stats %llu: %s\n"
+ "failed to init the dir stats repair tree\n"
+ "failed to insert dir-stats entry %llu into the repair tree\n"
+ "failed to register the dir stats repair tree in the fsck memory storage\n"
+ "found dir-stats object (id %llu; flags 0x%x) with bad chained key (%llu/%llu)\n"
+ "found unexpected %s xfield associated with inode (object-id %llu)\n"
+ "unable to load dir-stats %llu to retrieve attributes: %s\n"
- "\ndir-stats %llu: (has dir-stats? %d)\nflags: 0x%x\nchained-key: %llu\norigin-id: %llu (computed: %llu)\nshadow-key: %llu (exists? %d)\ndescendants: %llu (computed: %llu)\nSAF descendants: %llu\nphysical size: %llu (computed: %llu)\nresource fork size: %llu (computed: %llu)\nclone size: %llu (exists? %d; computed: %llu)\npurgeable size: %llu (exists? %d; computed: %llu)\nhas calculating dir-stats? %d\norigin is SAF? %d\norigin is purgeable? %d\n\n"
- "%s (id %llu): invalid flags (0x%hx)\n"
- "%s (id %llu): not registering descendant to dir-stats %llu due to sparse bytes mismatch\n"
- "%s (id %llu): unknown flags (0x%x / known-flags are: 0x%x)\n"
- "%s (id %llu): unsupported flags (%u)\n"
- "2235.80.4.0.1"
- "Checking snapshot %ld of %ld (%s)"
- "clone size of dir-stats object (id %llu) does not match expected value (%llu)\n"
- "found dir-stats object (id %llu; flags 0x%x) with bad chained key (%llu)\n"
- "found unexpected xfield associated with inode (object-id %llu)\n"
- "purgeable size of dir-stats object (id %llu) does not match expected value (%llu)\n"

```
