## sm_stats

> `/System/Library/Filesystems/apfs.fs/sm_stats`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-  __TEXT.__text: 0x43290
+  __TEXT.__text: 0x4344c
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__cstring: 0xcc2a
+  __TEXT.__cstring: 0xcd05
   __TEXT.__const: 0x1b8
   __TEXT.__unwind_info: 0x6e0
   __DATA_CONST.__auth_got: 0x390

   - /usr/lib/libutil.dylib
   Functions: 577
   Symbols:   129
-  CStrings:  1043
+  CStrings:  1046
 
Functions:
~ sub_100005254 : 1192 -> 1632
~ sub_100026764 -> sub_10002691c : 508 -> 500
~ sub_10002c324 -> sub_10002c4d4 : 12056 -> 12064
~ sub_10003df60 -> sub_10003e118 : 632 -> 636
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
```
