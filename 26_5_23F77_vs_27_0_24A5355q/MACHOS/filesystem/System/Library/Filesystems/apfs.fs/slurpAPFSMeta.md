## slurpAPFSMeta

> `/System/Library/Filesystems/apfs.fs/slurpAPFSMeta`

```diff

-2811.120.14.0.1
-  __TEXT.__text: 0x36b24 sha256:8814d1b0adc6e61ada808a9c323312b780e71050b143e7bb855e4e53055f1576
-  __TEXT.__auth_stubs: 0x830 sha256:65232b582df0485dcee147f9365cc1126977edae4c898b8ca2099da0f7d08a55
-  __TEXT.__cstring: 0x8f52 sha256:347b3aeece3d067b5af5f3c0b557c811db2ddb564344cb6af3400e7be5823dd0
-  __TEXT.__const: 0x1b0 sha256:f64e192855e188fad88b1b8bbabec319e42ae640412d6e00f28abf8c663ab46d
-  __TEXT.__unwind_info: 0x680 sha256:4a620afbf8686ed757d83c71e552673146b5400ac6398986a6650fe4ae75d3fb
-  __DATA_CONST.__auth_got: 0x418 sha256:e4b4dbd41b19da7e8738695fbb91a3142e85503c96c6aac8fe246295c92331cc
-  __DATA_CONST.__got: 0x48 sha256:6649335c9e7691eac3638833560b840aa87aa3af60df32dad3e02cebcb7db73b
-  __DATA_CONST.__auth_ptr: 0x20 sha256:fef588531521f55d5d39a576127c6cfb29bab6a4dd1da95f9df36231beafd8d3
-  __DATA_CONST.__const: 0x470 sha256:02ff0e5de0c86566ad37e1b1d113b1046568e5433a0555dc5ba09b6abb73e233
-  __DATA_CONST.__cfstring: 0x140 sha256:e7fb0bf56320632d237a2f60be04579aea41a7025eb1dabf91e36f0182fb44de
-  __DATA.__data: 0x160 sha256:896fab3d7c8d7dc9fb75ecd223db2172c2269e382b2269e40677e72140122052
+3277.0.0.0.1
+  __TEXT.__text: 0x37574 sha256:829752b01c04f9f214f110c066ab8980ed6b7f98110a95e188b6a02cabdc881b
+  __TEXT.__auth_stubs: 0x830 sha256:3de792e4bd784422cd829c3a96e10f48e02ed436f74f067b61f551f8ddfac173
+  __TEXT.__cstring: 0x8f26 sha256:6d1c1ae6e4a5543157563425282184cd6a0b00745f5aa4748405304630072f70
+  __TEXT.__const: 0x1b0 sha256:09476db93420c2d83f024fb23b0c2241990634c519d6db1627816af08530f061
+  __TEXT.__unwind_info: 0x6a8 sha256:238a7b0569afe7cecbaf487aca96ea25db20e803e601ab3eaa0d94ae892caff7
+  __DATA_CONST.__const: 0x470 sha256:a5e8ebf033d4c4af52c22485e2688086a93c04e8e84fba7bdf9311bab9f60629
+  __DATA_CONST.__cfstring: 0x140 sha256:248d99ec419ccaa5059d1ad4449ae491d04f0d32c45b2c7962031d34c078a1de
+  __DATA_CONST.__auth_got: 0x418 sha256:b0117bcbf8a4e9c667f98fa8b8310adfe980fb881463ef0375f5044f73094cff
+  __DATA_CONST.__got: 0x48 sha256:1d1b652ea0877e590d9b889706df36aa2ce0c0e35159523d1f575f00eabb640d
+  __DATA_CONST.__auth_ptr: 0x20 sha256:a4f7255361a9ea034b82e85a844623c3f1960239a715d9de62c946c049ba08b8
+  __DATA.__data: 0x160 sha256:5de69531eeafd2d0732e2e0fadc8eb177c22a0af3631e1858f5feb50f84e48f3
   __DATA.__bss: 0x4c sha256:f2c0d5456a983ecd12e314fcfa19879179fc8424343baeb1325457472ae85601
   __DATA.__common: 0x38 sha256:d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
-  UUID: 67ED7523-7672-34EA-8EED-20E73D843422
-  Functions: 521
+  UUID: 7A23E0B0-1783-38C2-9D12-BB333561B0AE
+  Functions: 534
   Symbols:   144
-  CStrings:  782
+  CStrings:  779
 
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
+ "%s:%d: %s free queue tree is too large: %lld nodes (limit %d) xid %lld\n"
+ "%s:%d: %s length tree search for 0x%llx 0x%llx returned node %d instead of %d\n"
+ "%s:%d: %s nx_resize detected while processing cib=%u out of %u cibs\n"
+ "%s:%d: Why are we comparing a chunk to itself?\n"
+ "%s:%d: checkpoint superblock has a lower XID %lld than the container superblock %lld\n"
+ "%s:%d: checkpoint<->container superblock mismatch on block count: %lld %lld\n"
+ "%s:%d: checkpoint<->container superblock mismatch on block size: %d %d\n"
+ "%s:%d: checkpoint<->container superblock mismatch on checkpoint data base address: %lld %lld\n"
+ "%s:%d: checkpoint<->container superblock mismatch on checkpoint data block count: %d %d\n"
+ "%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor base address: %lld %lld\n"
+ "%s:%d: checkpoint<->container superblock mismatch on checkpoint descriptor block count: %d %d\n"
+ "%s:%d: checkpoint<->container superblock mismatch on fusion uuid\n"
+ "%s:%d: checkpoint<->container superblock mismatch on uuid\n"
+ "Attempting to reuse a non-candidate chunk zone info\n"
+ "Reserved space < reserved metadata: %llu < %llu\n"
+ "SYSTEM_GRAFT_4K_OBJS"
+ "nx_superblock_agrees_with_container_superblock"
+ "object-cache-reset-lock"
+ "recent zone chunk should have only ONE reference when being moved to the recent list!\n"
+ "spaceman-dev-lock"
+ "spaceman_chunk_zone_info_add"
+ "spaceman_chunk_zone_info_compare"
+ "spaceman_chunk_zone_info_list_remove"
+ "spaceman_chunk_zone_info_load_recent_chunks"
+ "spaceman_chunk_zone_info_recent_decrement"
+ "spaceman_chunk_zone_info_recent_increment"
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
- "%s:%d: %s main free queue tree is too large: %lld nodes (limit %d) xid %lld\n"
- "%s:%d: %s nx_resize detected while processing dev=%d cib=%u out of %u cibs\n"
- "%s:%d: %s tier2 free queue tree is too large: %lld nodes (limit %d) xid %lld\n"
- "%s:%d: %s<->superblock mismatch on block count: %lld %lld\n"
- "%s:%d: %s<->superblock mismatch on block size: %d %d\n"
- "%s:%d: %s<->superblock mismatch on checkpoint data base address: %lld %lld\n"
- "%s:%d: %s<->superblock mismatch on checkpoint data block count: %d %d\n"
- "%s:%d: %s<->superblock mismatch on checkpoint descriptor base address: %lld %lld\n"
- "%s:%d: %s<->superblock mismatch on checkpoint descriptor block count: %d %d\n"
- "%s:%d: %s<->superblock mismatch on fusion uuid\n"
- "%s:%d: %s<->superblock mismatch on uuid\n"
- "%s:%d: the %s superblock has a lower XID %lld than the main superblock %lld\n"
- "Absurd combination of allocation flags for spaceman %llx"
- "GRAFT_4K_OBJS"
- "Main"
- "T2"
- "checkpoint"
- "nx_superblock_agrees_with_main_superblock"
- "spaceman-dev-lock-main"
- "spaceman-dev-lock-tier2"
- "spaceman_evaluate_chunk_for_disabled_allocation_zones"
- "spaceman_iterate_process_bitmap_block"
- "tier2"

```
