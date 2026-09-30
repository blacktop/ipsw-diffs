## apfs_checkseal

> `/System/Library/Filesystems/apfs.fs/apfs_checkseal`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-  __TEXT.__text: 0x4ece8
+  __TEXT.__text: 0x4eeac
   __TEXT.__auth_stubs: 0x760
   __TEXT.__const: 0x4c0
-  __TEXT.__cstring: 0xff10
+  __TEXT.__cstring: 0xffeb
   __TEXT.__unwind_info: 0x8c0
   __DATA_CONST.__auth_got: 0x3b0
   __DATA_CONST.__got: 0x50

   - /usr/lib/libutil.dylib
   Functions: 729
   Symbols:   133
-  CStrings:  1285
+  CStrings:  1288
 
Functions:
~ sub_10002a058 : 1192 -> 1632
~ sub_10002c6f4 -> sub_10002c8ac : 12056 -> 12064
~ sub_10003e49c -> sub_10003e65c : 632 -> 636
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
