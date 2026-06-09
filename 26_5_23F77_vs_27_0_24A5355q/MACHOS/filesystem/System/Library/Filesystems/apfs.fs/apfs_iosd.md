## apfs_iosd

> `/System/Library/Filesystems/apfs.fs/apfs_iosd`

```diff

-2811.120.14.0.1
-  __TEXT.__text: 0x32e18 sha256:e73deb0342df454a794b98a3a8b2780731e47711c8d40fe30b7f7653ddc7eae6
-  __TEXT.__auth_stubs: 0xa90 sha256:9f31adf662bf924d9b96d7de0fed3ad8078014dc47dddac2839da44a0f7efbd0
-  __TEXT.__const: 0x350 sha256:9e931b7ec6504291b3aab4cde6746dc6cc3e5c48405406ec55b938776c09ef1f
-  __TEXT.__cstring: 0x6614 sha256:464149e70d3b8261b61f02bf37ba00de385dc19ae5ca67c65fa3b43770700d4f
-  __TEXT.__oslogstring: 0x1333 sha256:71548f1088253473d8c1cfed3478c9e1021e2de12ab47d195ccf2d94f2dd328c
-  __TEXT.__unwind_info: 0x618 sha256:ee1abfea65a6eb5a9f21af0a25dce6626383b7dff4c0eae0d7ae27643fc2ad30
-  __DATA_CONST.__auth_got: 0x548 sha256:981ea52b48bb5e0b770d70f9a1341eef45508bfb2f9450e059a5be19b902e8ac
-  __DATA_CONST.__got: 0xb8 sha256:015ec383c00673fdb5506a37c87ab3c43c592862e52d3a68563b49760bb18c09
-  __DATA_CONST.__auth_ptr: 0x28 sha256:6cb70de4a3b84de0a3d62d464f47b6d3c68c8b489df002d490e7dfea0c8842ed
-  __DATA_CONST.__const: 0x6c8 sha256:7f520d329918e16ba9656431240bd7dad145f93a480d577bb218c088e99daa27
-  __DATA_CONST.__cfstring: 0xc80 sha256:0bf0762be0431512e40c0f92919a0cc760f376008e8809b9bd4c4ca764ed8a6c
-  __DATA.__data: 0x9c sha256:203a7294f2f74397c6a54d0bcbd9e58893e32929a2d86d2a974dab790050bb3e
+3277.0.0.0.1
+  __TEXT.__text: 0x336b4 sha256:8f355422f2ae8d6465dc76737fe7fbf2c36e50cfc8809895ba4b1a71a9310789
+  __TEXT.__auth_stubs: 0xa90 sha256:2e59181820d0c484b1c6bd46509c91c9678ceaf699ac2be843316811f0ddb948
+  __TEXT.__const: 0x350 sha256:a75719e501e87d85b5172faddfea5da3c7fcbec9729fa05f285cb912e9b717f7
+  __TEXT.__cstring: 0x6684 sha256:6b64c3111c34ceb67adec1b7f11c43d9226dc940f2fc58899f6d112a4e0bf742
+  __TEXT.__oslogstring: 0x13e0 sha256:94a94ff10b6cdc40c9d3700eb012a78189b5d899a2a7fd322c4f9779f5c1cb9e
+  __TEXT.__unwind_info: 0x650 sha256:60a87958e51721d49502b9509299e9033db4a75a36651d6c117cd49cb889c63f
+  __DATA_CONST.__const: 0x708 sha256:369e67047732a26203ea010901570d37279c3d8506c8a9242691bdaf8afbff3c
+  __DATA_CONST.__cfstring: 0xc80 sha256:c96d14c8b8807301aa35c79741453642b192989eb4190502b2d02c7a5a19eb41
+  __DATA_CONST.__auth_got: 0x548 sha256:6a613539c3e821d06cb5ea155c173b57ed6f54c8bd48308172f2c4affc68e877
+  __DATA_CONST.__got: 0xb8 sha256:0bbafd4c43199bd2362302b5344b357b51442e012002ce929e8a5c4de96bd57f
+  __DATA_CONST.__auth_ptr: 0x20 sha256:57f9d2cfc47c1bce9ee134fd2e3a802f7d058e497de91ffcd1ae3200b030c947
+  __DATA.__data: 0x9c sha256:c95f3ec375dcee663c52e07c6b68bc63764b635366dde27723d600c255c452bb
   __DATA.__bss: 0x38 sha256:d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb
-  __DATA.__common: 0x5c sha256:62b14867e4e79d50673d2f7474335229f54c478f56d2a910235e1953c6d29206
+  __DATA.__common: 0x64 sha256:cd00e292c5970d3c5e2f0ffa5171e555bc46bfc4faddfb4a418b6840b86e79a3
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/AppleFSCompression.framework/AppleFSCompression

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libutil.dylib
-  UUID: E0979EBB-2A44-3E23-8D3A-4B8BD76217D9
-  Functions: 549
+  UUID: 0696A327-2FB5-3F56-9207-B2241BE41BF8
+  Functions: 562
   Symbols:   197
-  CStrings:  875
+  CStrings:  884
 
CStrings:
+ "%s:%d: %s %s tree: PATH TOO LONG: %d\n"
+ "%s:%d: %s Error %d, reinitializing\n"
+ "%s:%d: %s Error reinitializing free extent cache: %d\n"
+ "%s:%d: %s Error searching free extent cache: %d; Reinitializing.\n"
+ "%s:%d: %s Failed to delete covered node from length tree: %d\n"
+ "%s:%d: %s Failed to find length tree predecessor for node that wasn't the smallest\n"
+ "%s:%d: %s Failed to find next smallest extent in length tree: %d\n"
+ "%s:%d: %s Failed to find smallest extent %d in length tree: %d\n"
+ "%s:%d: %s Failed to find smallest extent in paddr tree: %d\n"
+ "%s:%d: %s Failed to find successor node from length tree while updating smallest: %d\n"
+ "%s:%d: %s Failed to find successor node in length tree: %d\n"
+ "%s:%d: %s Failed to get next extent: %d\n"
+ "%s:%d: %s Failed to update partially-covered node in length tree: %d\n"
+ "%s:%d: %s block range %lld:%lld out of bounds %lld\n"
+ "%s:%d: %s checking CZIC for zone %llu list %d traversal count exceeded table count (%u) - aborting\n"
+ "%s:%d: %s chunk %d NOT added because we somehow couldn't find a place for it\n"
+ "%s:%d: %s chunk %d table %d rz# %d list %d %d %d still seems to be current/recent\n"
+ "%s:%d: %s chunk %lld recent zone count overflow\n"
+ "%s:%d: %s chunk %lld recent zone count underflow\n"
+ "%s:%d: %s chunk %lld recent zone count zero but still marked as current\n"
+ "%s:%d: %s error getting bitmap object for chunk %d @ %lld: %d\n"
+ "%s:%d: %s length tree search for 0x%llx 0x%llx returned node %d instead of %d\n"
+ "%s:%d: %s nx_resize detected while processing cib=%u out of %u cibs\n"
+ "%s:%d: Why are we comparing a chunk to itself?\n"
+ "Attempting to reuse a non-candidate chunk zone info\n"
+ "Reserved space < reserved metadata: %llu < %llu\n"
+ "SYSTEM_GRAFT_4K_OBJS"
+ "cache eviction XPC activity complete"
+ "cache eviction XPC activity complete\n"
+ "cache_eviction"
+ "com.apple.filesystems.apfs_iosd.cache_eviction"
+ "error: failed to open container for cache eviction"
+ "error: failed to open container for cache eviction\n"
+ "failed"
+ "failed to set cache eviction state to DONE"
+ "failed to set cache eviction state to DONE\n"
+ "recent zone chunk should have only ONE reference when being moved to the recent list!\n"
+ "spaceman-dev-lock"
+ "spaceman_chunk_zone_info_add"
+ "spaceman_chunk_zone_info_compare"
+ "spaceman_chunk_zone_info_list_remove"
+ "spaceman_chunk_zone_info_load_recent_chunks"
+ "spaceman_chunk_zone_info_recent_decrement"
+ "spaceman_chunk_zone_info_recent_increment"
+ "succeeded"
+ "triggering eviction for keys cache %s\n"
- "%s, Reserved space < reserved metadata: %llu < %llu\n"
- "%s:%d: %s allocation zone on dev %d for allocations of %llu blocks starting at paddr %llu\n"
- "%s:%d: %s block range %lld:%lld out of %s bounds %lld\n"
- "%s:%d: %s dev %d %s tree: PATH TOO LONG: %d\n"
- "%s:%d: %s dev %d Error %d, reinitializing\n"
- "%s:%d: %s dev %d Error reinitializing %s free extent cache: %d\n"
- "%s:%d: %s dev %d Error searching %s free extent cache: %d; Reinitializing.\n"
- "%s:%d: %s dev %d Failed to delete covered node from length tree: %d\n"
- "%s:%d: %s dev %d Failed to find length tree predecessor for node that wasn't the smallest\n"
- "%s:%d: %s dev %d Failed to find next smallest extent in length tree: %d\n"
- "%s:%d: %s dev %d Failed to find smallest extent %d in length tree: %d\n"
- "%s:%d: %s dev %d Failed to find smallest extent in paddr tree: %d\n"
- "%s:%d: %s dev %d Failed to find successor node from length tree while updating smallest: %d\n"
- "%s:%d: %s dev %d Failed to find successor node in length tree: %d\n"
- "%s:%d: %s dev %d Failed to get next extent: %d\n"
- "%s:%d: %s dev %d Failed to update partially-covered node in length tree: %d\n"
- "%s:%d: %s dev %d free extent %lld:%lld appears to span container metadata and should not be free: %d\n"
- "%s:%d: %s dev %d length tree search for 0x%llx 0x%llx returned node %d instead of %d\n"
- "%s:%d: %s error getting cab %d: %d\n"
- "%s:%d: %s error getting cib %d: %d\n"
- "%s:%d: %s error unreserving tier2 space, %lld blocks: %d\n"
- "%s:%d: %s failed to assign chunk %llu to allocation zone %llu\n"
- "%s:%d: %s failed to evaluate chunk %llu (average free ext len %u) for disabled allocation zones, error %d\n"
- "%s:%d: %s failed to evaluate free chunk %llu for disabled allocation zone, error %d\n"
- "%s:%d: %s failed to move roving pointer for dev %d error %d\n"
- "%s:%d: %s failed to search bitmap hints: %d\n"
- "%s:%d: %s failed to update chunk for alloc zone %d: %d\n"
- "%s:%d: %s nx_resize detected while processing dev=%d cib=%u out of %u cibs\n"
- "Absurd combination of allocation flags for spaceman %llx"
- "GRAFT_4K_OBJS"
- "Main"
- "T2"
- "main"
- "spaceman-dev-lock-main"
- "spaceman-dev-lock-tier2"
- "spaceman_evaluate_chunk_for_disabled_allocation_zones"
- "spaceman_iterate_process_bitmap_block"
- "tier2"

```
