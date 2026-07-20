## newfs_apfs

> `/System/Library/Filesystems/apfs.fs/newfs_apfs`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3283.0.9.502.1
-  __TEXT.__text: 0x516fc
+3283.0.13.0.0
+  __TEXT.__text: 0x51914
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__cstring: 0xf937
+  __TEXT.__cstring: 0xfa1f
   __TEXT.__const: 0x8480
   __TEXT.__unwind_info: 0x848
   __DATA_CONST.__const: 0x570

   - /usr/lib/libutil.dylib
   Functions: 715
   Symbols:   156
-  CStrings:  1314
+  CStrings:  1318
 
Functions:
~ sub_100005948 : 10472 -> 10480
~ sub_10000e740 -> sub_10000e748 : 1204 -> 1640
~ sub_10002d1ec -> sub_10002d3a8 : 596 -> 640
~ sub_100035bf0 -> sub_100035dd8 : 304 -> 312
~ sub_100041d90 -> sub_100041f80 : 632 -> 636
~ sub_100047b80 -> sub_100047d74 : 4156 -> 4168
~ sub_100048f30 -> sub_100049130 : 3496 -> 3520
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "3283.0.13"
+ "apfs_sanity_check"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "3283.0.9.502.1"
```
