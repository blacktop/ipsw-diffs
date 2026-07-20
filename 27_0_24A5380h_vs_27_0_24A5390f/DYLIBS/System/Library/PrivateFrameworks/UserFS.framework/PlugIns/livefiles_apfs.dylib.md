## livefiles_apfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-3283.0.9.502.1
-  __TEXT.__text: 0xb1678
+3283.0.13.0.0
+  __TEXT.__text: 0xb19ec
   __TEXT.__const: 0x86b0
-  __TEXT.__oslogstring: 0x1635c
-  __TEXT.__cstring: 0x5c26
+  __TEXT.__oslogstring: 0x16438
+  __TEXT.__cstring: 0x5c33
   __TEXT.__unwind_info: 0x1090
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x3c8

   - /usr/lib/libutil.dylib
   Functions: 2581
   Symbols:   1505
-  CStrings:  2239
+  CStrings:  2243
 
Functions:
~ _nx_check : 22440 -> 22448
~ _apfs_init : 560 -> 604
~ _omap_get : 632 -> 636
~ _spaceman_alloc : 4888 -> 4900
~ _spaceman_alloc_iterate_chunks : 3748 -> 3772
~ _nx_reaper_checkpoint_traverse : 1580 -> 2372
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "%s:%d: obj is NULL or not apfs object!\n"
+ "3283.0.13"
+ "apfs_sanity_check"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "%s:%d: obj is NULL or not apfs object!"
- "3283.0.9.502.1"
```
