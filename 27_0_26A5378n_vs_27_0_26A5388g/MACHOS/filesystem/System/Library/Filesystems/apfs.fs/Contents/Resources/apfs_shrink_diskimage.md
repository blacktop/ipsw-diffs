## apfs_shrink_diskimage

> `/System/Library/Filesystems/apfs.fs/Contents/Resources/apfs_shrink_diskimage`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-3283.0.9.501.1
-  __TEXT.__text: 0x59668
+3283.0.13.501.1
+  __TEXT.__text: 0x59884
   __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__cstring: 0x12e4e
+  __TEXT.__cstring: 0x12f3c
   __TEXT.__const: 0x230
   __TEXT.__unwind_info: 0x938
   __DATA_CONST.__const: 0x728

   - /usr/lib/libutil.dylib
   Functions: 772
   Symbols:   140
-  CStrings:  1499
+  CStrings:  1503
 
Functions:
~ sub_100001d18 : 596 -> 640
~ sub_100019d50 -> sub_100019d7c : 512 -> 516
~ sub_100028854 -> sub_100028884 : 484 -> 488
~ sub_10002a870 -> sub_10002a8a4 : 1204 -> 1640
~ sub_100033260 -> sub_100033448 : 10496 -> 10504
~ sub_1000450c8 -> sub_1000452b8 : 632 -> 636
~ sub_10004cb30 -> sub_10004cd24 : 4160 -> 4172
~ sub_10004dee4 -> sub_10004e0e4 : 3476 -> 3504
CStrings:
+ "%s:%d: %s Invalid reap list free entry %d\n"
+ "%s:%d: %s reap list object 0x%llx first index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx free index %u larger than max index %u\n"
+ "%s:%d: %s reap list object 0x%llx last index %u larger than max index %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u\n"
+ "%s:%d: %s reap list object expected %u entries, max %u, but we walked %u + %u = %u\n"
+ "%s:%d: obj is NULL or not apfs object!\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XQJT3Z/Sources/apfs_executables/nx/jobj.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XQJT3Z/Sources/apfs_executables/nx/nx.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.XQJT3Z/Sources/apfs_executables/nx/obj.c"
+ "apfs_sanity_check"
- "%s:%d: %s reap list object 0x%llx first index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx free index %u larger than max %u\n"
- "%s:%d: %s reap list object 0x%llx last index %u larger than max %u\n"
- "%s:%d: obj is NULL or not apfs object!"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/jobj.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/nx.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.qgu8Kl/Sources/apfs_executables/nx/obj.c"
```
