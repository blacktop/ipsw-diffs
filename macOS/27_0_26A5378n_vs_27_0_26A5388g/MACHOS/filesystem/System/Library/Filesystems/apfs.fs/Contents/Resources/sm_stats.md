## sm_stats

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/sm_stats`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3283.0.9.501.1
-  __TEXT.__text: 0x43b4c
+3283.0.13.501.1
+  __TEXT.__text: 0x43d58
   __TEXT.__auth_stubs: 0x720
-  __TEXT.__cstring: 0xcd9d
+  __TEXT.__cstring: 0xce8a
   __TEXT.__const: 0x1c8
   __TEXT.__unwind_info: 0x728
   __DATA_CONST.__const: 0x6f8

   - /usr/lib/libutil.dylib
   Functions: 595
   Symbols:   129
-  CStrings:  1049
+  CStrings:  1053
 
Functions:
~ sub_1000050d8 : 1204 -> 1640
~ sub_10000d230 -> sub_10000d3e4 : 4160 -> 4172
~ sub_10000e5e4 -> sub_10000e7a4 : 3476 -> 3504
~ sub_100012680 -> sub_10001285c : 596 -> 640
~ sub_100024e48 -> sub_100025050 : 520 -> 512
~ sub_10002a8e8 -> sub_10002aae8 : 10496 -> 10504
~ sub_10003c4a0 -> sub_10003c6a8 : 632 -> 636
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XQJT3Z/Sources/apfs_executables/nx/obj.c"
+ "apfs_sanity_check"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/obj.c"
```
