## livefiles_apfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib`

```diff

-2632.0.68.0.3
-  __TEXT.__text: 0xbe258
+2632.0.77.0.1
+  __TEXT.__text: 0xbe970
   __TEXT.__auth_stubs: 0x8f0
   __TEXT.__const: 0x85c0
-  __TEXT.__oslogstring: 0x15b39
+  __TEXT.__oslogstring: 0x15afa
   __TEXT.__cstring: 0x54c5
-  __TEXT.__unwind_info: 0xfd8
+  __TEXT.__unwind_info: 0xfe0
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x3c8
   __AUTH_CONST.__auth_got: 0x478

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libutil.dylib
-  UUID: C290729E-04BF-39E8-A0DD-551BD8B55074
-  Functions: 2428
-  Symbols:   5466
-  CStrings:  2191
+  UUID: F91E9278-8D9F-3A39-AD98-44AFA6CB9182
+  Functions: 2433
+  Symbols:   5476
+  CStrings:  2190
 
Symbols:
+ _obj_cache_remove.cold.5
+ _obj_cache_remove.cold.6
+ _obj_cache_remove.cold.7
+ _obj_cache_remove.cold.8
+ _obj_cache_remove_new_fs_objects.cold.3
+ _obj_cache_remove_new_fs_objects.cold.4
+ _obj_cache_remove_reverted_fs_objects.cold.6
+ _spaceman_entitled_reserve_active
+ _update_purgeable_clone_tracking
+ _update_purgeable_clone_tracking.cold.1
- _spaceman_unreserve.cold.5
- _spaceman_unreserve.cold.6
- _update_clone_mapping_if_present
- _update_clone_mapping_if_present.cold.1
CStrings:
+ "%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d er %d\n"
+ "2632.0.77.0.1"
+ "update_purgeable_clone_tracking"
- "%s:%d: %s %s: ENOSPC: ttype %s (r %lld d %lld tx %d) blocks %lld free %lld txn %lld # %d th %lld rr %lld sh %lld fq %lld lim %d %d freeup %d wait %d\n"
- "%s:%d: %s unentitled reserve: reserved space underflow: %lld (%lld)\n"
- "2632.0.68.0.3"
- "update_clone_mapping_if_present"

```
