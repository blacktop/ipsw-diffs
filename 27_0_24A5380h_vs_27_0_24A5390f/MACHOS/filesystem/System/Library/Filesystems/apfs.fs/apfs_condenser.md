## apfs_condenser

> `/System/Library/Filesystems/apfs.fs/apfs_condenser`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3283.0.9.502.1
-  __TEXT.__text: 0x4cd30
+3283.0.13.0.0
+  __TEXT.__text: 0x4cf48
   __TEXT.__auth_stubs: 0x780
-  __TEXT.__cstring: 0xf6c8
+  __TEXT.__cstring: 0xf7b1
   __TEXT.__const: 0x220
   __TEXT.__unwind_info: 0x828
   __DATA_CONST.__const: 0x8f8

   - /usr/lib/libutil.dylib
   Functions: 681
   Symbols:   134
-  CStrings:  1261
+  CStrings:  1265
 
Functions:
~ sub_100009c28 : 10472 -> 10480
~ sub_10000dc40 -> sub_10000dc48 : 596 -> 640
~ sub_10001100c -> sub_100011040 : 1204 -> 1640
~ sub_1000305cc -> sub_1000307b4 : 276 -> 284
~ sub_10003f758 -> sub_10003f948 : 632 -> 636
~ sub_1000447e4 -> sub_1000449d8 : 4156 -> 4168
~ sub_100045b94 -> sub_100045d94 : 3496 -> 3520
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
