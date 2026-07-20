## apfs_diskimage_map

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_diskimage_map`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3283.0.9.501.1
-  __TEXT.__text: 0x4be40
+3283.0.13.501.1
+  __TEXT.__text: 0x4c058
   __TEXT.__auth_stubs: 0x7c0
-  __TEXT.__cstring: 0xefec
+  __TEXT.__cstring: 0xf0da
   __TEXT.__const: 0x210
   __TEXT.__unwind_info: 0x888
   __DATA_CONST.__const: 0x798

   - /usr/lib/libutil.dylib
   Functions: 696
   Symbols:   138
-  CStrings:  1227
+  CStrings:  1231
 
Functions:
~ sub_100002754 : 596 -> 640
~ sub_100019efc -> sub_100019f28 : 516 -> 520
~ sub_1000268c4 -> sub_1000268f4 : 1204 -> 1640
~ sub_100028fa0 -> sub_100029184 : 10496 -> 10504
~ sub_10003acb8 -> sub_10003aea4 : 632 -> 636
~ sub_1000402e0 -> sub_1000404d0 : 4160 -> 4172
~ sub_100041694 -> sub_100041890 : 3476 -> 3504
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "%s:%d: obj is NULL or not apfs object!\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XQJT3Z/Sources/apfs_executables/nx/jobj_snap.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XQJT3Z/Sources/apfs_executables/nx/obj.c"
+ "apfs_sanity_check"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "%s:%d: obj is NULL or not apfs object!"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/jobj_snap.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/obj.c"
```
