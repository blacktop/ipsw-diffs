## livefiles_apfs.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_apfs.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-  __TEXT.__text: 0xb4c4c
+  __TEXT.__text: 0xb4f48
   __TEXT.__auth_stubs: 0x8f0
   __TEXT.__const: 0x8690
-  __TEXT.__oslogstring: 0x15dd3
-  __TEXT.__cstring: 0x59bf
+  __TEXT.__oslogstring: 0x15eae
+  __TEXT.__cstring: 0x59c3
   __TEXT.__unwind_info: 0x1020
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__const: 0x3c8

   - /usr/lib/libutil.dylib
   Functions: 2541
   Symbols:   1499
-  CStrings:  2207
+  CStrings:  2210
 
Functions:
~ _nx_check : 23756 -> 23764
~ _omap_get : 632 -> 636
~ _nx_reaper_checkpoint_traverse : 1628 -> 2404
~ _omap_revert_to_snapshot.cold.1 : 96 -> 84
~ _omap_revert_to_snapshot.cold.2 : 100 -> 88
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "2811.160.7.0.4"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "2811.160.7"
```
